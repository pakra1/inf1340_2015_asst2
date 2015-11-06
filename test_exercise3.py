#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__authors__ = 'Paniz Pakravan', 'Shu Yun Susan Shen'
__emails__ = 'p.pakravan@mail.utoronto.ca', 'shuyun.shen@mail.utoronto.ca'
__date__ = '06 November 2015'

from exercise3 import union, intersection, difference

###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

FRIENDS1 = [["Number", "Name", "Age"],
             [1111, "Rachel", 37],
             [2222, "Joey", 39],
             [3333, "Ross", 38]]

FRIENDS2 = [["Number", "Name", "Age"],
            [4444, "Monica", 56],
            [2222, "Joey", 39],
            [3333, "Ross", 38]]


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    return set(map(tuple, t1)) == set(map(tuple, t2))


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """
    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))

def test_union():
    """
    Test union operation.
    """
    result = [["Number", "Name", "Age"],
             [1111, "Rachel", 37],
             [4444, "Monica", 56],
             [2222, "Joey", 39],
             [3333, "Ross", 38]]

    assert is_equal(result, union(FRIENDS1, FRIENDS2))

def negative_test_union():
    """
    Test error union operation.
    """
    if not is_equal(result, union(table1, table2)):
        assert True
    else:
        assert False


def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))

def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Name", "Age"],
              [2222, "Joey", 39],
             [3333, "Ross", 38]]

    assert is_equal(result, intersection(FRIENDS1, FRIENDS2))

def negative_test_intersection():
    """
    Test error intersection operation.
    """
    if not is_equal(result, intersection(GRADUATES, MANAGERS)):
        assert True
    else:
        assert False


def test_difference():
    """
    Test difference operation.
    """
    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))

def test_difference():
    """
    Test difference operation.
    """
    result = [["Number", "Name", "Age"],
              [1111, "Rachel", 37]]

    assert is_equal(result, difference(FRIENDS1, FRIENDS2))

def negative_test_difference():
    """
    Test error intersection operation.
    """
    if not is_equal(result, difference(GRADUATES, MANAGERS)):
        assert True
    else:
        assert False