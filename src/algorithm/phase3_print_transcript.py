"""
Author: Rayla Kurosaki

File: phase3_print_transcript.py

Description: This file contains the functionality to print a simplified
             version of the student's transcript onto a text file.
"""

import numpy as np

import copy

import __utils__ as utils


def get_data_to_print(student):
    """
    Gets all the necessary data to print.

    :param student: The student to extract data from.
    :return: The necessary data to print.
    """
    header = np.array([
        ["Term", "Course ID", "Course Name", "Raw Grade",
         "Final Grade"]
    ])
    data_to_print = copy.deepcopy(header)
    for course in student.get_courses():
        lst = np.array([
            [course.get_term(), course.get_id() + "." + course.get_section(),
             course.get_name(), course.get_raw_grade(),
             course.get_final_grade()]
        ])
        data_to_print = np.vstack((data_to_print, lst))
        pass
    return data_to_print


def print_to_file(data_to_print):
    """
    Creates a text file to print the student's transcript on.

    :param data_to_print: The data to print.
    """
    max_len = utils.get_max_len(data_to_print)
    with open("../data/transcript.txt", "w") as f:
        # student.print_student(f)
        curr_term = ""
        utils.print_boundary(f, max_len)
        for row in data_to_print:
            if not (curr_term == row[0]):
                if not (curr_term == ""):
                    utils.print_separator(f, max_len)
                    pass
                curr_term = row[0]
                pass
            utils.print_row(f, row, max_len)
            pass
        utils.print_boundary(f, max_len)
        pass
    pass


def phase3_main(student):
    """
    The driver function to print a simplified version of the student's
    transcript onto a text file.

    :param student: The student to manipulate.
    """
    data_to_print = get_data_to_print(student)
    print_to_file(data_to_print)
    pass
