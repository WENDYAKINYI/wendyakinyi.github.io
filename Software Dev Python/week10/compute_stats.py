import sys


def my_stats(values):
    """
    Computes basic statistics (minimum, maximum, average, and median) for a list of numerical values.

    Parameters:
        values (list of str): A list of strings representing the numerical values to be processed.

    Returns:
        tuple of (float, float, float, float) or None: A tuple containing the minimum, maximum, average,
        and median of the valid numerical values. Returns None if no valid data is provided.
    """
    # Initialize variables for computing statistics
    total = 0
    count = 0
    min_value = float('inf')
    max_value = float('-inf')
    filtered_values = []

    # Filter and process each value
    for value in values:
        try:
            value = float(value.strip())  # Convert input to float
            if value == -9999.0:  # Exclude missing data values
                continue

            # Update statistics with valid values
            total += value
            count += 1
            min_value = min(min_value, value)
            max_value = max(max_value, value)
            filtered_values.append(value)
        except ValueError:
            # Skip lines that cannot be converted to float
            continue

    # To ensure there are valid values to calculate statistics
    if count == 0:
        return None

    # Calculate average value
    average = total / count

    # Calculate median value
    filtered_values.sort()
    n = len(filtered_values)
    median = (filtered_values[n // 2] if n % 2 !=
              0 else (filtered_values[n // 2 - 1] + filtered_values[n // 2]) / 2)

    return min_value, max_value, average, median


def main():
    """
    This function reads numerical data from standard input, computes basic statistics, and prints them.

    If no valid data is provided, it prints a message indicating that.
    """
    # Read data from standard input (stdin)
    values = sys.stdin.readlines()
    stats = my_stats(values)

    if stats:
        min_value, max_value, average, median = stats
        # Print computed values
        print(f"min: {min_value}, max: {max_value}, average: {
              average}, median: {median}")
    else:
        print("No valid data provided.")


if __name__ == "__main__":
    main()
