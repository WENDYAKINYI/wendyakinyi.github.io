
def calculate_payments(amount, int_rate, duration):
    """
    Calculates the monthly payment for a loan based on the loan amount, annual interest rate, and loan term.

    Parameters:
    - amount (float): The total amount of the loan.
    - int_rate (float): The annual interest rate as a percentage
    - duration (int): The loan term in months.

    Returns:
    - float: The monthly payment amount.
    """
    monthly_interest_rate = (int_rate / 100) / 12
    number_of_payments = duration
    monthly_payment = amount * (monthly_interest_rate * (1 + monthly_interest_rate)
                                ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    return monthly_payment


def calculate_total_paid(amount, int_rate, duration):
    """
    Calculates the total payment over the life of the loan.

    Parameters:
    - amount (float): The total amount of the loan.
    - int_rate (float): The annual interest rate as a percentage.
    - duration (int): The loan termin months.

    Returns:
    - float: The total payment amount.
    """
    monthly_payment = calculate_payments(amount, int_rate, duration)
    total_payment = monthly_payment * duration
    return total_payment


def calculate_total_interest(amount, int_rate, duration):
    """
    Calculates the total amount of interest paid over the life of the loan.

    Parameters:
    - amount (float): The original loan amount.
    - int_rate (float): The annual interest rate as a percentage.
    - duration (int): The loan term in months.

    Returns:
    - float: The total interest paid.
    """
    total_payment = calculate_total_paid(amount, int_rate, duration)
    total_interest = total_payment - amount
    return total_interest


# if __name__ == "__main__":
#     amount = 10000  # loan amount
#     int_rate = 6.8  # annual interest rate
#     duration = 120  # loan term in months

#     monthly_payment = calculate_payments(amount, int_rate, duration)
#     print(f"Monthly Payment: {monthly_payment:.2f}")

#     total_payment = calculate_total_paid(amount, int_rate, duration)
#     print(f"Total Payment: {total_payment:.2f}")

#     total_interest = calculate_total_interest(amount, int_rate, duration)
#     print(f"Total Interest Paid: {total_interest:.2f}")
