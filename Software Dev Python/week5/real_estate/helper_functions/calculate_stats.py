
def cheapest(property_dict, location):
    """
    Finds the cheapest property for a given State/Territory.

    Parameters:
        property_dict (dict): The dictionary containing property data.
        location (str): The State or Territory.

    Returns:
        namedtuple: The cheapest property in the specified location.
    """
    cheapest_property = None
    min_price = float('inf')
    for property in property_dict.get(location, {}).values():
        for prop in property:
            try:
                price = float(prop.price)
                if price < min_price:
                    min_price = price
                    cheapest_property = prop
            except ValueError:
                continue  # Ignore poorly formatted rows
    return cheapest_property


def priciest(property_dict, location):
    """
    Finds the priciest property for a given State/Territory.

    Parameters:
        property_dict (dict): The dictionary containing property data.
        location (str): The State or Territory.

    Returns:
        namedtuple: The priciest property in the specified location.
    """
    priciest_property = None
    max_price = float('-inf')
    for property in property_dict.get(location, {}).values():
        for prop in property:
            try:
                price = float(prop.price)
                if price > max_price:
                    max_price = price
                    priciest_property = prop
            except ValueError:
                continue  # Ignore poorly formatted rows
    return priciest_property


def dirt_cheap(property_dict):
    """
    Finds the absolute cheapest property in all of the US States and Territories.

    Parameters:
        property_dict (dict): The dictionary containing property data.

    Returns:
        namedtuple: The absolute cheapest property.
    """
    # Leverage the cheapest function
    all_locations = property_dict.keys()
    cheapest_properties = [cheapest(property_dict, loc)
                           for loc in all_locations]
    # Filter out None values which might occur if a location has no valid properties
    cheapest_properties = [prop for prop in cheapest_properties if prop]
    # Find the absolute cheapest
    absolute_cheapest = min(cheapest_properties,
                            key=lambda x: float(x.price), default=None)
    return absolute_cheapest


def best_deal(property_dict, location, bedrooms, bathrooms):
    """
    Finds the property with the best price per square foot in a given State/Territory,
    with a specific number of bedrooms and bathrooms.

    Parameters:
        property_dict (dict): The dictionary containing property data.
        location (str): The State or Territory.
        bedrooms (int): Number of bedrooms.
        bathrooms (float): Number of bathrooms.

    Returns:
        namedtuple: The property with the best price per square foot.
    """
    best_property = None
    best_value = float('inf')
    for property in property_dict.get(location, {}).values():
        for prop in property:
            try:
                if int(prop.bedrooms) == bedrooms and float(prop.bathrooms) == bathrooms:
                    price_per_sqft = float(prop.price) / float(prop.house_size)
                    if price_per_sqft < best_value:
                        best_value = price_per_sqft
                        best_property = prop
            except ValueError:
                continue  # Ignore poorly formatted rows
    return best_property


def budget_friendly(property_dict, bedrooms, bathrooms, max_budget):
    """
    Finds the property that offers the best value (price per square foot) within a maximum budget,
    regardless of the State/Territory, with a specific number of bedrooms and bathrooms.

    Parameters:
        property_dict (dict): The dictionary containing property data.
        bedrooms (int): Number of bedrooms.
        bathrooms (float): Number of bathrooms.
        max_budget (float): Maximum budget.

    Returns:
        namedtuple: The property that offers the best value within the budget.
    """
    all_locations = property_dict.keys()
    best_properties = []
    for location in all_locations:
        best_properties.append(
            best_deal(property_dict, location, bedrooms, bathrooms))
    # Filter out None values and properties over the budget
    best_properties = [prop for prop in best_properties if prop and float(
        prop.price) <= max_budget]
    # Find the property with the best price per square foot within the budget
    best_value_property = min(best_properties, key=lambda x: float(
        x.price) / float(x.house_size), default=None)
    return best_value_property
