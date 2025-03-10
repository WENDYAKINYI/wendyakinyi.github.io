'''
COMP 4401
Homework 7 - Strings & Sets

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
'''
#--------------------------------------------------------------------------#

###-----------------###
###-----Strings-----###
###-----------------###

# All functions must be able to handle edge cases like an empty string or list and 
# strings and lists with a single character.


# 1. Write a function, called checkPalindrome, that takes a string as an argument and 
# determines if the string is a palindrome. The function should return True if it is
# a palindrome, False otherwise.
# A palindrome is a string that is the same forward and backward like: level or noon.
# Make sure your function works on the string "rats live on no evil star"
# (10 points)

def checkPalindrome(string):
    """
    Checks if a string is a palindrome. Returns True if the given string is a palindrome, False otherwise.

    Parameters:
        string (str): A string to check if it is a palindrome.

    Returns:
        True if the given string is a palindrome, False otherwise.
    """
    # Remove spaces and convert the input string to lowercase
    string = string.replace(" ", "").lower()

    # Compare the original string to its reverse
    return string == string[::-1]

if __name__ == '__main__':
    input_string = "rats live on no evil star"
    is_palindrome = checkPalindrome(input_string)
    if is_palindrome:
        print(f'"{input_string}" is a palindrome.')
    else:
        print(f'"{input_string}" is not a palindrome.')
        # output "rats live on no evil star" is a palindrome.



# 2. Create a function, called sortStrings, that takes a list of strings and sorts the list 
# based on the length of string from lower to higher. Cannot use built-in sorting functions
# (10 points)

def sortStrings(list_strings):
    """
    Sort a list of strings based on string length from lower to higher without using built-in sorting functions.
.

    Parameters:
        list_strings (list of str): The list of strings to be sorted.

    Returns:
        sorted list of str: The sorted list of strings.
    """
    # Create a dictionary to store strings by their lengths
    string_length_dict = {}

    # Iterate through the input list and populate the dictionary
    for string in list_strings:
        string_length = len(string)
        if string_length not in string_length_dict:
            string_length_dict[string_length] = []
        string_length_dict[string_length].append(string)

    # Sort the dictionary keys (string lengths)
    sorted_lengths = sorted(string_length_dict.keys())

    # Create a list of strings sorted in ascending order.
    sorted_list_strings = []
    for length in sorted_lengths:
        sorted_list_strings.extend(string_length_dict[length])

    return sorted_list_strings


if __name__ == '__main__':
    list_of_strings = ["hi", "petero", "come", "here", "please"]
    sorted_list_strings = sortStrings(list_of_strings)
    print(sorted_list_strings)
    # output ['hi', 'come', 'here', 'petero', 'please']




# 3. Write a function, called mixedString, that takes a word string and computes a list of 
# all words generated by a single swap of letters in the word. 
# For example ‘swap’ should return [‘pwas’, ‘wsap’, ‘sawp’, swpa’] (notice that letters are 
# only swapped with their immediate neighbors only, i.e. you don’t have ‘waps’)
# (10 points)

def mixedString(word):
    """
    Computes a list of all words generated by a single swap of letters in the word, only swapping with immediate neighbors.

    Parameters:
        word (str): The input word.

    Returns:
        list of str: A list of all words generated by a single swap of adjacent letters.
    """
    # create an empty list to store the swapped words
    swapped_words = []

    # Iterate over all pairs of adjacent letters in the word.
    for i in range(len(word) - 1):
        # Swap neighbouring letters
        swapped_word = list(word)
        swapped_word[i], swapped_word[i +
                                      1] = swapped_word[i + 1], swapped_word[i]
        swapped_words.append(''.join(swapped_word))

    return swapped_words


if __name__ == '__main__':
    example_word = "swap"
    swapped_words = mixedString(example_word)
    print(swapped_words)
    # output ['wsap', 'sawp', 'swpa']

# 4. Write a function, called reversePhrase, that takes a string of words and returns the 
# string with the words in reverse order. You cannot use any library methods or functions 
# like .split(). 
# For example if the sentence is: “I love python”, then the function returns: “python love 
# I”
# (10 points)

def reversePhrase(phrase):
    """
    Reverses the order of words in a string.

    Parameters:
        phrase (str): The string of words.

    Returns:
        str: The string with words in reverse order.
    """
    # Create an empty list to store reversed words
    reversed_words = []
    word = ''

    # Iterate over the words in the input string
    for char in phrase:
        if char != ' ':
            word += char
        else:
            if word:
                reversed_words.append(word)
                word = ''

    # Add the Add the word to the list of reversed words
    if word:
        reversed_words.append(word)

    # Reverse the list of words and join them into a single string
    reversed_phrase = ' '.join(reversed(reversed_words))

    return reversed_phrase


if __name__ == '__main__':
    phrase = "I love python"
    reversed_phrase = reversePhrase(phrase)
    print(reversed_phrase)
    #output 'python love I'

# 5. Write a function, called uniqueLetters, that takes a string as an argument and returns 
# a new string with no duplicated letters. 
# For example if the word is: “application” then the function returns “aplicton”
# (10 points)

def uniqueLetters(string):
    """
    Returns a new string with no duplicated letters.

    Parameters:
        string (str): The input string.

    Returns:
        str: A new string with no duplicated letters.
    """
    # create an empty string to store unique letters
    unique_string = ''

    # Iterate through the characters of the string
    for character in string:
        if character not in unique_string:
            unique_string += character

    return unique_string


if __name__ == '__main__':
    input_string = "tennesssee"
    result = uniqueLetters(input_string)
    print(result)
    #output 'tens'



###--------------###
###-----Sets-----###
###--------------###

# 6. Create a function, called setComp, that uses Python set comprehension to generate a 
# set of pair tuples consisting of all of the integers between 1 and 10,000 and the square 
# of that number but only if the square is divisible by 3 and return that set. 
# For example (3, 9) would be in the set since 3^2 is 9 and 9 is divisible by 3.
# You should have 3333 tuples in your set.
# (10 points)

def setComp():
    """Generates a set of pair tuples consisting of all of the integers between 1 and 10,000 and the square of that number but only if the square is divisible by 3 and returns that set.

    Returns:
        set: A set of pair tuples consisting of all of the integers between 1 and 10,000 and the square of that number but only if the square is divisible by 3.
    """

    # Create a set to store the pair tuples.
    pair_tuples = set()

    # Iterate over the integers between 1 and 10,000.
    for x in range(1, 10001):
        # Calculate the square of the integer.
        square = x**2

        # Check if the square is divisible by 3.
        if square % 3 == 0:
            # Add the pair tuple to the set.
            pair_tuples.add((x, square))

    return pair_tuples


if __name__ == '__main__':
    pair_tuples = setComp()
    print(len(pair_tuples))  
    #output '3333'



# 7. Write a function, called minMaxSet, that takes a set of numbers and returns the 
# minimum and maximum value in the set as a tuple. Cannot use the built-in functions 
# min()/max(). Hint: You may want to use math.inf and -math.inf
# (10 points)
import math


def minMaxSet(set_of_numbers):
    """
    Returns the minimum and maximum values in a set of numbers.

    Parameters:
        set_of_numbers (set): The set of numbers.

    Returns:
        tuple: A tuple containing the minimum and maximum values.
    """
    # Initialize minimum and maximum values
    min_value = math.inf
    max_value = -math.inf

    # Iterate over the numbers in the set to find the actual minimum and maximum
    for number in set_of_numbers:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number
    
    # Return the minimum and maximum values as a tuple.
    return min_value, max_value


if __name__ == '__main__':
    set_of_numbers = {5, -2, 8, 2, 10, 20}
    minMaxInt = minMaxSet(set_of_numbers)
    print(minMaxInt)
    #output (-2, 20)


# 8. Write a function, uniqueElems, that given a list of values, determines if all elements 
# are unique (no repeated values). If elements are unique return True and False otherwise. 
# You must use a set to perform this task.
# (10 points)

def uniqueElems(list_of_values):
    """
    Returns True if all elements in a list are unique, False otherwise.

    Parameters:
        list_of_values (list): The list of values.

    Returns:
        bool: True if all elements are unique, False otherwise.
    """
    # Create a set from the list of values.
    value_set = set(list_of_values)

    # If the length of the set is equal to the length of the list, then all elements in the list are unique.
    if len(list_of_values) == len(value_set):
        return True
    else:
        return False


if __name__ == '__main__':
    list_of_values1 = [1, 2, 3, 4, 5]
    list_of_values2 = [1, 3, 3, 3, 4]

    result1 = uniqueElems(list_of_values1)
    result2 = uniqueElems(list_of_values2)

    print(result1)  # True
    print(result2)  # False




# 9. Write a function, called distinctElems, that takes two sets, A and B, and returns a new 
# frozen set containing elements that are in either A or B but NOT in the intersection of A 
# and B. 
# (10 points)

def distinctElems(set_A, set_B):
    """
    Return a new frozen set containing elements that are in either A or B but NOT in the intersection of A and B.

    Parameters:
        set_A (set): A set of elements.
        set_B (set): Another set of elements.

    Returns:
        frozenset: A frozen set of distinct elements.
    """
    # Create a new set to store the distinct elements.
    distinct_elements = set()
    
    # Find the intersection of sets A and B
    intersection = set_A & set_B

    # Find elements that are in either A or B but not in the intersection
    distinct_elements = (set_A - intersection) | (set_B - intersection)

    # Convert the result to a frozen set
    return frozenset(distinct_elements)


if __name__ == '__main__':
    set_A = {1, 2, 3, 4, 5}
    set_B = {1, 5, 6, 7, 8}

    distinct_elements = distinctElems(set_A, set_B)
    print(distinct_elements)
    #output frozenset({2, 3, 4, 6, 7, 8})



# 10. Write a function, called addsToK, that given an integer k and a list of n unordered 
# integers A, determines if there is a distinct pair of integers in A that add up to k. 
# Return True if a pair of integers add up to k, return False other.
# You must perform this task using sets. 
# (10 points)

def addsToK(int_k, list_A):
    """
    Returns True if there is a distinct pair of integers in list_of_numbers that add up to k, False otherwise.

    Parameters:
        int_k (int): The target sum.
        list_A (list): The list of unordered integers.

    Returns:
        bool: True if a pair of distinct integers adds up to k, False otherwise.
    """
    # Create a set to store the seen integers
    seen_numbers = set()

    # Iterate over the list of unordered integers
    for number in list_A:
        # Calculate the complement needed to reach k
        complement = int_k - number

        # Check if the complement is in the set of seen integers
        if complement in seen_numbers:
            return True

        # Add the integer to the set
        seen_numbers.add(number)

    return False


if __name__ == '__main__':
    list_A = [3, 4, 8, 3, 2, 9]
    int_k = 15
    result = addsToK(int_k, list_A)
    print(result) 
    #output 'False'























