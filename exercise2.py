#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__authors__ = 'Paniz Pakravan', 'Shu Yun Susan Shen'
__emails__ = 'p.pakravan@mail.utoronto.ca', 'shuyun.shen@mail.utoronto.ca'
__date__ = '06 November 2015'


def find(input_string, substring, start, end):
    """
    Return the lowest index where the substring is found without using find

    :param : input_string, substring, start, end
    :return:
    :raises:

    """

    first_letter_match = substring[0]
    # ensure that search is kept within the index length that matches the length of the input_substring
    while len(input_string) < end:
        end = len(input_string)

    for index in range(start, end):
        #counter ensures perfect match between input_string and substring
        found_count = 0
        if input_string[index] == first_letter_match:
            #check to see if remaining letters match
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

    :param : input_string, substring, start, end
    :return:
    :raises:

    """
    locations_found = []
    while start < end or start < len(substring):
        find_word = find(input_string, substring, start, end)
        if find_word == -1:
            break   #no word found, stop
        #find index for remaining substring if in the string
        else:
            #save the index of the first appearance of substring
            locations_found.append(str(find_word))
            start = find_word + 1

    return ",".join(locations_found)
