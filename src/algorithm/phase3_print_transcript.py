"""
Author: Rayla Kurosaki

File: phase3_print_transcript.py

Description: This file contains all the functionality of printing the student's
             transcript.
"""

import numpy as np

import copy

import __utils__ as utils


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


def print_to_file(student, data_to_print):
    """
    Creates a text file to print the student's transcript on.

    :param student: The student to manipulate.
    :param data_to_print: The data to print.
    """
    # Get the column spacing.
    max_len = utils.get_max_len(data_to_print)
    # Write onto a file.
    with open("../data/transcript.txt", "w") as f:
        # Print the student's basic info.
        student.print_student(f)
        # Initialize the current term.
        curr_term = ""
        # Print the upper boundary.
        utils.print_boundary(f, max_len)
        # iterate through each row to print.
        for row in data_to_print:
            # If this is a new term.
            if not (curr_term == row[0]):
                # If the row is not the header.
                if not (curr_term == ""):
                    # Print a line to separate the courses by term.
                    utils.print_separator(f, max_len)
                    pass
                # Set the current term as the row's term.
                curr_term = row[0]
                pass
            # Print the details of the row.
            utils.print_row(f, row, max_len)
            pass
        # Print the lower boundary.
        utils.print_boundary(f, max_len)
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
    # Print the transcript.
    print_to_file(student, data_to_print)
    pass
