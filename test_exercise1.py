#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__authors__ = 'Paniz Pakravan', 'Shu Yun Susan Shen'
__emails__ = 'p.pakravan@mail.utoronto.ca', 'shuyun.shen@mail.utoronto.ca'
__date__ = '06 November 2015'


from exercise1 import pig_latinify

WORDS = ["dog", "is", "apple", "scratch"]

def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"

def test_basic_exception():
    try:
        item = "ogday" or "atchscray" or "isyay" or "appleyay"
    except AttributeError:
        print ("oops")