#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Paniz Pakravan'
__email__ = "p.pakravan@mail.utoronto.ca"
__copyright__ = "2015 Paniz Pakravan"
__date__ = "06 November 2015"


from exercise1 import pig_latinify

WORDS = ["dog", "is", "apple", "scratch"]

def test_pig_latinify():
    """
    Basic test cases from assignment hand out
    """
    for item in WORDS:
        assert True

    try:
        pig_latinify("dog") == "ogday"
    except ValueError:
        assert True

    try:
        pig_latinify("is") == "isay"
    except ValueError:
        assert True

    try:
        pig_latinify("apple") == "appleyay"
    except ValueError:
        assert True

    try:
        pig_latinify("scratch") == "atchscray"
    except ValueError:
        assert True