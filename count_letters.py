# Author: Ashton Lee
# Github User: ashton01L
# Date: 8/8/2024
# Description: Define a function named 'count_letters' that takes as a parameter
# a string and returns a dictionary that tabulates how many of
# each letter is in that string.
def count_letters(string_in):
    """
    Counts the occurrence of each letter of a string input and tallies the number of occurrences to deliver an output
    dictionary showing uppercase keys of the individual letters used within that particular string and the respective
    count of occurrence of each letter

    :param string_in: (str): The input string of which we are counting occurrences of letters.

    :return: (dict): A dictionary (list) with uppercase letters as keys and their respective occurrence count.
    """
    # Initialize and empty dictionary to store counts of letters
    letter_count = {}

    # Iterate through each character in the string input
    for letter in string_in:
        # Convert each letter to upper case
        upper_char = letter.upper()

        # Check if the character is in alphabet
        if 'A' <= upper_char <= 'Z':
            # Increment the count if the letter is already in the dictionary
            if upper_char in letter_count:
                letter_count[upper_char] += 1
            else:
                # Otherwise, add letter to dictionary
                letter_count[upper_char] = 1

    return letter_count

# # test output - output should be {'A': 2, 'B': 2, 'C': 2, 'D': 1, 'E': 3}
# print(count_letters("AaBbCcDeee"))
