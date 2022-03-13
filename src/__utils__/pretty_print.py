"""
Author: Rayla Kurosaki

File: pretty_print.py

Description: This file contains the functionality of pretty printing data in
             the form of a table.
"""

import numpy as np

import copy
import logging
import math


# def get_data_to_print(header, data):
#     """
#     Gets all the necessary data to print.
#
#     :param header: The first row to print.
#     :param data:
#     :return: The necessary data to print.
#     """
#     # Initialize the data to print.
#     data_to_print = copy.deepcopy(np.array([header]))
#     for e in data:
#         lst = np.array([
#             [
#                 # Enter the data here
#             ]
#         ])
#         data_to_print = np.vstack((data_to_print, lst))
#     return data_to_print


def get_max_len(data_to_print):
    """
    Computes the spacing for each column.

    :param data_to_print: The data needed to be printed.
    :return: Get the column spacing.
    """
    max_len = []
    # Get the shape of the 2-d array.
    rows, cols = np.shape(data_to_print)
    # Get the length of the longest string in each column.
    for i in range(cols):
        max_len.append(len(max(data_to_print[:, i], key=len)))
        pass
    return max_len


def get_spacing(max_len, header):
    """
    Get the spacing for the main header.

    :param max_len: The column spacing.
    :param header: Name of the main header.
    :return: The spacing for the main header.
    """
    boundary_length = sum(max_len) + 3 * (len(max_len)) + 1
    return math.ceil((boundary_length - len(header)) / 2) - 1


def print_boundary(f, lst):
    """
    Prints the top and/or bottom most borders of the table.

    :param f: File reader.
    :param lst: A list of numbers to determine the size of a column.
    """
    string = f"|"
    for i, v in enumerate(lst):
        string += f"{'-' * (2 + v)}"
        if i + 1 == len(lst):
            string += f"|"
            pass
        else:
            string += f"-"
            pass
        pass
    f.write(f"{string} \n")
    logging.info(string)
    pass


def print_separator(f, lst):
    """
    This prints out a line that separate terms.

    :param f: File reader.
    :param lst: A list of numbers to determine the size of a column.
    """
    string = f"|"
    for i, v in enumerate(lst):
        string += f"{'-' * (2 + v)}"
        if i + 1 == len(lst):
            string += f"|"
            pass
        else:
            string += f"+"
            pass
        pass
    f.write(f"{string} \n")
    logging.info(string)
    pass


def print_row(f, data, lst):
    """
    Prints out the data.

    :param f: File reader.
    :param data: Data to print out.
    :param lst: A list of numbers to determine the size of a column.
    """
    string = f"|"
    for e1, e2 in zip(data, lst):
        string += f" {e1}{' ' * (e2 - len(e1))} |"
    f.write(f"{string} \n")
    logging.info(string)
    pass
