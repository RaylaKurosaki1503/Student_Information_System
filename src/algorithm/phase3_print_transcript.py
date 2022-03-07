"""
Author: Rayla Kurosaki

File: phase3_print_transcript.py

Description: This file contains all the functionality of printing the student's
             transcript.
"""

import numpy as np

import logging
import copy


def get_data_to_print(student):
    """
    Gets all the necessary data to print.

    :param student: The student to manipulate.
    :return: The necessary data to print.
    """
    # Set the header of the table.
    header = np.array([
        ["Term", "Course ID", "Course Name", "Raw Grade",
         "Final Grade"]
    ])
    # Initialize the data to print.
    data_to_print = copy.deepcopy(header)
    # Iterate through each course.
    for course in student.get_courses():
        # Add course data to the list of data to print.
        lst = np.array([
            [course.get_term(), course.get_id() + "." + course.get_section(),
             course.get_name(), course.get_raw_grade(),
             course.get_final_grade()]
        ])
        data_to_print = np.vstack((data_to_print, lst))
        pass
    return data_to_print


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


def print_boundary(f, lst):
    """
    Prints the top and/or bottom most borders of the transcript.

    :param f: File reader.
    :param lst: A list of numbers to determine the size of a column.
    """
    string = "|"
    for i, v in enumerate(lst):
        string += "-" * (2 + v)
        if i + 1 == len(lst):
            string += "|"
            pass
        else:
            string += "-"
            pass
        pass
    f.write(string + "\n")
    logging.info(string)
    pass


def print_separator(f, lst):
    """
    This prints out a line that separate terms.

    :param f: File reader.
    :param lst: A list of numbers to determine the size of a column.
    """
    string = "|"
    for i, v in enumerate(lst):
        string += "-" * (2 + v)
        if i + 1 == len(lst):
            string += "|"
            pass
        else:
            string += "+"
            pass
        pass
    f.write(string + "\n")
    logging.info(string)
    pass


def print_row(f, data, lst):
    """
    Prints out the data.

    :param f: File reader.
    :param data: Data to print out.
    :param lst: A list of numbers to determine the size of a column.
    """
    string = "|"
    for e1, e2 in zip(data, lst):
        string += " " + e1 + " " * (e2 - len(e1)) + " |"
    f.write(string + "\n")
    logging.info(string)
    pass


def print_to_file(student, data_to_print, max_len):
    """
    Creates a text file to print the student's transcript on.

    :param student: The student to manipulate.
    :param data_to_print: The data to print.
    :param max_len: The length of each column.
    """
    # Write onto a file.
    with open("data/transcript.txt", "w") as f:
        # Print the student's basic info.
        student.print_student(f)
        # Initialize the current term.
        curr_term = ""
        # Print the upper boundary.
        print_boundary(f, max_len)
        # iterate through each row to print.
        for i, row in enumerate(data_to_print):
            # If this is a new term.
            if not (curr_term == row[0]):
                # If the row is not the header.
                if not (curr_term == ""):
                    # Print a line to separate the courses by term.
                    print_separator(f, max_len)
                    pass
                # Set the current term as the row's term.
                curr_term = row[0]
                pass
            # Print the details of the row.
            print_row(f, row, max_len)
            pass
        # Print the lower boundary.
        print_boundary(f, max_len)
        pass
    pass


def phase3_main(student):
    """
    The main function to call the functions above to print the student's
    transcript.

    :param student: The student to manipulate.
    """
    # Get the data to print.
    data_to_print = get_data_to_print(student)
    # Get the column spacing.
    max_len = get_max_len(data_to_print)
    # Print the transcript.
    print_to_file(student, data_to_print, max_len)
    pass
