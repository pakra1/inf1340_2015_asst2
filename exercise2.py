#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Paniz Pakravan and Shu Yun Susan Shen'
__email__ = "p.pakravan@mail.utoronto.ca"
__copyright__ = "2015 Paniz Pakravan"
__date__ = "06 November 2015"


def find(input_string, substring, start, end):
    """
    Return the lowest index where the substring is found without using find

    :param :
    :return:
    :raises:

    """

    first_letter_match = substring[0]
    #to ensure that search is kept within the index length that matches the length of the input_substring
    while len(input_string) < end:
        end = len(input_string)
   
    for index in range(start, end):
        #counter ensures perfect match between input_string and substring
        found_count = 0
        #compare_first = input_string[index]
        if input_string[index] == first_letter_match:
            #if the first letter of substring matches a letter in the string, check to see if remaining letters match
            for indiv_index in range(len(substring)):
                #Saves current index in the input_string for matching letter between substring and input_string
                if input_string[index+indiv_index] == substring[indiv_index]:
                    found_count = found_count + 1

        #returns the location where it found the first matching letter of substring if all letters in substring found
        while found_count == len(substring):
            return index
    # if there is no match or only a couple of letters in substring found
    if found_count < len(substring):
        return -1

def multi_find(input_string, substring, start, end):
    """
    Function returns string with 0 or more indexes
    If no substring is found, empty string is returned

    :param :
    :return:
    :raises:

    """
    locations_found = []
    while start < end or start < len(substring):
        find_word = find(input_string, substring, start, end)
        if find_word == -1:
            break   #no word found, stop
        else: #find index for remaining substring if in the string
            #save the index of the first appearance of substring
            locations_found.append(str(find_word))
            # shift the starting position of find, to make sure you can find any remaining substrings in input_string
            start = find_word + 1
    return ",".join(locations_found)


