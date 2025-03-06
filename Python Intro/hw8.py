'''
COMP 4401
Homework 8 - Dictionaries & JSON Files

General Homework Guidelines: 
- Homework must be submitted in a .py file. Please do not submit .ipynb files.
- Homework should not use packages or functions that have not yet been discussed in class.
- Use comments to explain what your code is doing. 
- Use a consistent coding style. 
- Use descriptive variable names.
- Test your code regularly using a variety of different inputs. 
- Every function must include a docstring for documentation (see: 
   https://realpython.com/documenting-python-code/). This docstring should include:
     - 1 or 2 lines describing what the function does
     - input parameters, their types and what they are for
     - return data type and what it is
- All tests of your functions should be commented out in your final submission or
  encolosed with an if __name__ == '__main__' codeblock.
- All functions should use return statements to return a value, rather than
  printing some value, unless the instructions specifically say to print.


# Table with type equivalence between JSON and Python
# Python	            JSON
#--------------------------------
# dict	                object
# list, tuple	        array
# str	                string
# int, long, float	    number
# True	                true
# False	                false
# None	                null

'''
# --------------------------------------------------------------------------#


### ----------------------###
### -----Dictionaries-----###
### ----------------------###

# 1. Write a function, called listToDict, that takes a list as an argument
# and returns a dictionary containing the keys 1 through n, where n is the
# size of the list, and the values correspond to the values in the list.
# For example, if the list is [2, 6, 6, 1, 7, 9] then the dictionary maps:
# 1 —> 2, 2 —> 6, 3 —>6, 4 —> 1, 5 —> 7 and 6 —> 9.
# In Python this would be: {1:2, 2:6, 3:6, 4:1, 5:7, 6:9}
# (10 points)

import json


def listToDict(listA):
    """
    Converts a list to a dictionary with keys 1 through n, where n is the size of the list,
    and the values correspond to the values in the list.

    Args:
        list: A list of any type.

    Returns:
        Dict_result: A dictionary with keys 1 through n, where n is the size of the list,
        and the values correspond to the values in the list.
    """
    # Create an empty dictionary to store the result.
    dict_result = {}
    for i in range(len(listA)):
        dict_result[i + 1] = listA[i]
    return dict_result


if __name__ == '__main__':
    listA = [2, 6, 6, 1, 7, 9]
    result = listToDict(listA)
    print(result)

# Output:
# {1: 2, 2: 6, 3: 6, 4: 1, 5: 7, 6: 9}


# 2. Write a function, called newDict, that takes a dictionary as an argument
# and returns a new dictionary with the keys and values inverted (keys become
# values and values become keys).
# What happens if there are duplicate values?
# (10 points)

def newDict(dict):
    """
    Invert the keys and values of a dictionary.
    Args:
        dict (dict): A dictionary.

    Returns:
        dict: A new dictionary with keys and values inverted.
    """
    inverted_dict = {}

    for key, value in dict.items():
        # Invert the key and value in the new dictionary.
        inverted_dict[value] = key

    return inverted_dict


if __name__ == '__main__':
    dict = {1: 'apple', 2: 'banana', 3: 'apple'}
    inverted_result = newDict(dict)
    print(inverted_result)

# Output:
# {'apple': 3, 'banana': 2}
# If there are duplicate values in the original dictionary, the last occurrence of a
# value will overwrite previous occurrences in the inverted dictionary as shown in the example.


# 3. Write a function, called uniqueElems, that takes a list of values as a
# parameter and determines if all elements are unique (no repeated values).
# Return True if all values are unique, False otherwise. Think of a way to use
# dictionary to perform this task.
# (10 points)

def uniqueElems(listB):
    """
    Checks if all elements in a list are unique (no repeated values).

    Args:
        list (list): The list to be checked.

    Returns:
        bool: True if all values are unique, False otherwise.
    """
    list_dict = {}  # empty dictionary to count the occurrences of elements.

    for element in listB:
        # If the element is already in the dictionary, it's not unique.
        if element in list_dict:
            return False
        list_dict[element] = 1  # Add the element to the dictionary.

    # If the loop completes without returning False, all elements are unique.
    return True


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 2, 3, 4]

    list_dict1 = uniqueElems(list1)
    list_dict2 = uniqueElems(list2)

    print("List 1 is unique:", list_dict1)  # Output True
    print("List 2 is unique:", list_dict2)  # Output False


# 4. Write a function, called valFrequency, that given a list of values as a
# parameter, counts the frequencies for each value in the list. You can do this
# by returning a dictionary (think about what the key should be and what value
# should be associated with it).
# For example, if the list is [1, 3, 5, 2, 1, 2, 5, 8, 4, 5] then we have:
# 2 x 1's, 1 x 3's, 3 x 5's, 2 x 2's, 1 x 4's, 1 x 8’s
# In Python this would be: {1: 2, 3: 1, 5: 3, 2: 2, 8: 1, 4: 1}
# (10 points)

def valFrequency(listC):
    """
    Counts the frequencies of each value in a list.

    Args:
        list (list): The list to count frequencies for.

    Returns:
        dict:A dictionary containing the frequencies of each value in the list.
    """
    frequency_dict = {}  # An empty dictionary to store the frequencies.

    for value in listC:
        if value in frequency_dict:
            # Increment the count for existing values.
            frequency_dict[value] += 1
        else:
            frequency_dict[value] = 1  # Initialize count to 1 for new values.

    return frequency_dict


if __name__ == '__main__':
    listC = [1, 3, 5, 2, 1, 2, 5, 8, 4, 5]
    frequency_result = valFrequency(listC)
    print(frequency_result)
# Output
# {1: 2, 3: 1, 5: 3, 2: 2, 8: 1, 4: 1}

# 5. Write a function, called addsToK, that given an integer k and a list of n
# unordered integers A, determines if there is a pair of distinct integers in A
# that add up to k. Returns True if there are, False otherwise.
# For example : given [1, 6, 7, 3, 7, 10, 3] if k=13 then there is a pair of
# integers that add up to 13 : 10 and 3. If k=14 then there isn’t a pair of distinct
# integers that add up to 14 (can’t use 7 twice even if it appears twice in the list)
# (10 points)


def addsToK(k, A):
    """
    Determines if there is a pair of distinct integers in a list that add up to a given integer.


    Args:
        k (int): The target sum.
        A (list): The list of unordered integers.

    Returns:
        bool: True if there is a pair of distinct integers that add up to k, False otherwise.
    """
    seen_values = set()  # A set to store values we have seen so far.

    for num in A:
        complement = k - num
        if complement in seen_values and num != complement:
            return True  # If a pair of distinct integers is found.
        seen_values.add(num)

    return False  # If no pair of distinct integers is found.


if __name__ == '__main__':
    list1 = [1, 6, 7, 3, 7, 10, 3]
    k1 = 13
    k2 = 14

    result1 = addsToK(k1, list1)
    result2 = addsToK(k2, list1)

    print(f"There is a pair that adds up to {k1}: {result1}")  # Output True
    print(f"There is a pair that adds up to {k2}: {result2}")  # Output False


### -------------------###
### -----JSON FIle-----###
### -------------------###

# 6. Write a function, called senatorsInfo, that takes a filename string
# as an argument. It should load the json file and extract the Senator's
# following information:
# First name
# Last name
# State
# Party
# Start date (since when they've been Senators)
# Congress number (which sessions of Congress they were Senators for)
# Contact form
# Phone number
# Twitter handle
# Birthday
# Nickname
# The function should write the senators information to a json file
# called senatorsInfo.json. Use an indent of 2 to make the data more
# readable. The function should also return the data, this should
# be a list of dictionaries.
# Hint: You may want to use the get() method when getting the data
# (20 points)


def senatorsInfo(filename):
    """
   Extracts information from the senators.json file:  
   Writes the senators information to a json file called senatorsInfo.json.
   Also returns the data as a list of dictionaries.

   Args:
       filename: The path to the senators.json file.

   Returns:
       A list of dictionaries containing the senators information.
   """
    # Load the senators.json file
    with open(filename, 'r', encoding='utf-8') as file:
        senators_data = json.load(file)

    senator_info_list = []  # An empty list to store senator information

    # Ensures that senators_data is a list of dictionaries
    if isinstance(senators_data, list) and all(isinstance(senator, dict) for senator in senators_data):
        # Extract the required senators information
        for senator in senators_data:
            senator_info = {
                'First name': senator.get('first_name', ''),
                'Last name': senator.get('last_name', ''),
                'State': senator.get('state', ''),
                'Party': senator.get('party', ''),
                'Start date': senator.get('start_date', ''),
                'Congress number': senator.get('congress_number', ''),
                'Contact form': senator.get('contact_form', ''),
                'Phone number': senator.get('phone_number', ''),
                'Twitter handle': senator.get('twitter_handle', ''),
                'Birthday': senator.get('birthday', ''),
                'Nickname': senator.get('nickname', ''),
            }
            # Add the senator's information to the list
            senator_info_list.append(senator_info)

    # Write the senator information to a new .json file
    with open('senatorsInfo.json', 'w') as output_file:
        json.dump(senator_info_list, output_file, indent=2)

    return senator_info_list


if __name__ == '__main__':
    filename = 'senators.json'
    senators_info = senatorsInfo(filename)
    print(senators_info)


# 7. Write a function, called noContactForm, that takes in a filename string,
# loads the data in from a json file and returns a list containing the first
# and last name of the senators that do
# not have a contact form.
# (15 points)

def noContactForm(filename):
    """
    Returns a list containing the first and last name of the senators that do not have a contact form.

    Args:
        filename: The path to the senators.json file.

    Returns:
        A list of strings containing the first and last name of the senators that do not have a contact form.
    """
    # An empty list to store the names of senators without a contact form
    senators_no_contact_form = []

    # Ensure that senators_data is a list of dictionaries
    if isinstance(filename, str):
        with open(filename, 'r', encoding='utf-8') as file:
            senators_data = json.load(file)

            if isinstance(senators_data, list) and all(isinstance(senator, dict) for senator in senators_data):
                # Check data for the absence of a contact form
                for senator in senators_data:
                    if 'contact_form' not in senator or senator['contact_form'] == '':
                        first_name = senator.get('first_name', '')
                        last_name = senator.get('last_name', '')
                        senators_no_contact_form.append(
                            (first_name, last_name))

    return senators_no_contact_form


if __name__ == '__main__':
    filename = 'senators.json'
    senators_no_contact_form = noContactForm(filename)
    for senator in senators_no_contact_form:
        print(f"Senator without a contact form: {senator[0]} {senator[1]}")

# 8. Write a function, called congressSessionMembers, that takes a congress session
# sessionNumber (int) and a filename (str). It should load the data created in question 6
# and search for all the senators that were part of that particular session of congress.
# The function should write the resulting senators to a file called
# congressSession{sessionNumber}.json and returns a list of every senator that was
# part of the Senate for the given sessionNumber. It should return an empty
# list if none of the senators were members for that congress.
# (Congress session 1 should have nobody in it (except maybe Chuck Grassley
# and Mitch McConnell)).
# The numbers of senators for each Congress session available.
# sessionNumber 116 = 33
# sessionNumber 117 = 64
# sessionNumber 118 = 100
# sessionNumber 119 = 66
# sessionNumber 120 = 34
# all other session numbers should be empty
# (15 points)


def congressSessionMembers(sessionNumber, filename):
    """
    Returns a list of every senator that was part of the Senate for the given sessionNumber.

    Args:
        sessionNumber: The congress session number.
        filename: The path to the senatorsInfo.json file.

    Returns:
        A list of dictionaries containing the senators' information.
    """
    # Define the number of senators for each Congress session
    session_senator_counts = {
        116: 33,
        117: 64,
        118: 100,
        119: 66,
        120: 34
    }

    # Check if the provided sessionNumber is in the dictionary
    if sessionNumber not in session_senator_counts:
        # If not in the dictionary, return an empty list
        return []

    # Load the data from the senatorsInfo.json file
    with open(filename, 'r', encoding='utf-8') as file:
        senators_data = json.load(file)

    # An empty list to store senators part of the specified session
    senators_in_session = []

    # Add senators to the list for the specified session
    for senator in senators_data:
        congress_number = senator.get('congress_number', 0)
        if congress_number == sessionNumber:
            senators_in_session.append(senator)

    # Introduce a new .json file congressSession{sessionNumber}.json
    output_filename = f'congressSession{sessionNumber}.json'
    with open(output_filename, 'w') as output_file:
        json.dump(senators_in_session, output_file, indent=2)

    return senators_in_session


if __name__ == '__main':
    session_number = 116  # Replace with the desired session number
    filename = 'senatorsInfo.json'
    senators_in_session = congressSessionMembers(session_number, filename)
    print(f"Senators for Congress session {session_number}:")
    for senator in senators_in_session:
        print(f"{senator['first_name']} {senator['last_name']}")
