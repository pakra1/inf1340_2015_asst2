#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Paniz Pakravan and Shu Yun Susan Shen'
__email__ = "p.pakravan@mail.utoronto.ca"
__copyright__ = "2015 Paniz Pakravan"
__date__ = "06 November 2015"

table1 = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]
table2 = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

def check_stat(table1, table2):

# first thing check row 0, looking at the number of columns

    if len(table1[0])==len(table2[0]):
        #counter to keep track of similar column titles and numbers
        count = 0
        for index in range(len(table1[0])):
            table1_column = table1[0][index]
            table2_column = table2[0][index]
            if table1_column == table2_column:
                count += 1
        if count == len(table1[0]):
            return 0
        else:
            return "MismatchedAttributesException"
    else:
        return "MismatchedAttributesException"

check_stat(table1, table2)

def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

#returns new table with all unique rows that appear in either table
    x = check_stat(table1, table2)
    new_table = []
    new_table.append(table1)
    if x == 0:
        for i in range(len(table2)):
            item = table2[i]
            if item not in table1:
                new_table.append(item)
            else:
                continue
    print new_table

union(table1,table2)


def intersection(table1, table2):
    """
    Describe your function

    """
#returns new table with unique rows that appear in both tables
    x = check_stat(table1, table2)
    new_table = []
    if x == 0:
        for i in range(len(table1)):
            item = table1[i]
            if item in table2:
                new_table.append(item)
            else:
                continue
    print new_table

intersection(table1,table2)


def difference(table1, table2):
    """
    Describe your function

    """

#returns new table with unique rows in the first table
    x = check_stat(table1, table2)
    new_table = []
    new_table.append(table1[0])
    if x == 0:
        for i in range(len(table1)):
            item = table1[i]
            if item not in table2:
                new_table.append(item)
            else:
                continue
    print new_table

difference (table1,table2)

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

