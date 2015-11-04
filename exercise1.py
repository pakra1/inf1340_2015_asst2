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
    Convert English word input and convert into Pig Latin word.
    :param :
    :return: output_word
    :raises:
    """
    first_letter = word[0]

    if first_letter in VOWELS:
        output_word = word + "yay"
    else:
    #scan for vowel if word starts with a consonant
        for i in range(len(word)):
            individual_letter = word[i]
            if individual_letter in VOWELS:
                output_word = word[i:] + word[:i] + "ay"
                break
            else:
                continue

    print output_word

pig_latinify("dog")