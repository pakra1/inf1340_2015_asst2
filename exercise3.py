#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__authors__ = 'Paniz Pakravan', 'Shu Yun Susan Shen'
__emails__ = 'p.pakravan@mail.utoronto.ca', 'shuyun.shen@mail.utoronto.ca'
__date__ = '06 November 2015'

GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]
MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

def check_stat(GRADUATES, MANAGERS):

# first thing check row 0, looking at the number of columns

    if len(GRADUATES[0])==len(MANAGERS[0]):
        #counter to keep track of similar column titles and numbers
        count = 0
        for index in range(len(GRADUATES[0])):
            GRADUATES_column = GRADUATES[0][index]
            MANAGERS_column = MANAGERS[0][index]
            if GRADUATES_column == MANAGERS_column:
                count += 1
        if count == len(GRADUATES[0]):
            return 0
        else:
            return "MismatchedAttributesException"
    else:
        return "MismatchedAttributesException"

check_stat(GRADUATES, MANAGERS)

def union(GRADUATES, MANAGERS):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
#returns new table with all unique rows that appear in either table
    x = check_stat(GRADUATES, MANAGERS)
    new_table = []
    new_table.append(GRADUATES)
    if x == 0:
        for i in range(len(MANAGERS)):
            item = MANAGERS[i]
            if item not in GRADUATES:
                new_table.append(item)
            else:
                continue
    return new_table

union(GRADUATES,MANAGERS)

def intersection(GRADUATES, MANAGERS):
    """
    Describe your function

    """
#returns new table with unique rows that appear in both tables
    x = check_stat(GRADUATES, MANAGERS)
    new_table = []
    if x == 0:
        for i in range(len(GRADUATES)):
            item = GRADUATES[i]
            if item in MANAGERS:
                new_table.append(item)
            else:
                continue
    return new_table

intersection(GRADUATES,MANAGERS)

def difference(GRADUATES, MANAGERS):
    """
    Describe your function

    """
#returns new table with unique rows in the first table
    x = check_stat(GRADUATES, MANAGERS)
    new_table = []
    new_table.append(GRADUATES[0])
    if x == 0:
        for i in range(len(GRADUATES)):
            item = GRADUATES[i]
            if item not in MANAGERS:
                new_table.append(item)
            else:
                continue
    return new_table

difference (GRADUATES,MANAGERS)

#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass


