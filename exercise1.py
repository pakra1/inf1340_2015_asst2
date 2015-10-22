#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Paniz Pakravan'
__email__ = "p.pakravan@mail.utoronto.ca"
__copyright__ = "2015 Paniz Pakravan"
__date__ = "06 November 2015"

VOWELS = ["a", "e", "i", "o", "u"]

def pig_latinify(word):
    """
    Describe your function

    :param :
    :return: output_word
    :raises:

    """
    first_letter = word[0]
    if first_letter in VOWELS:  # case a)
        output_word = word + "yay"

    return output_word

print(pig_latinify("apple"))
