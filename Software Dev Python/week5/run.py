from real_estate.load_data.load import RealEstate
from real_estate.helper_functions import calculate_stats


def main():
    # Instantiate the RealEstate class
    real_estate = RealEstate("realtor-data-1.csv",
                             "real_estate/load_data/data/")

    # Print the first 5 Property containers for every State and Territory
    for category, properties in real_estate.properties_dict.items():
        print(f"'{category}':")
        for state, state_properties in properties.items():
            print(f"    '{state}': {state_properties[:5]}")

    # call for all functions in the calculate_stats module
    functions = [func for func in dir(calculate_stats) if callable(
        getattr(calculate_stats, func)) and not func.startswith("__")]

    # specific arguments
    specific_args = {
        'best_deal': (real_estate.properties_dict, 'Connecticut', 3, 2),
        'cheapest': (real_estate.properties_dict, 'Tennessee'),
        'dirt_cheap': (real_estate.properties_dict,),
        'priciest': (real_estate.properties_dict, 'Delaware'),
        'budget_friendly': (real_estate.properties_dict, 2, 1, 100000),
    }
    for func_name in functions:
        if func_name in specific_args:
            args = specific_args[func_name]
            result = real_estate.compute_stats(func_name, *args)
        else:
            result = real_estate.compute_stats(func_name)
        print(f"Result of {func_name}: {result}")


if __name__ == "__main__":
    main()
