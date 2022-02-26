"""
Author: Rayla Kurosaki

File: helper_functions.py

Description: This file contains easy-to-read functions for other built-in
             functions and functions as blocks of code that appear in multiple
             places within this project.
"""


def is_correct_course(term, course_id, name, course):
    """
    Determine if the selected course is the one to manipulate.

    :param term: The term/semester of the course to match.
    :param course_id: The course ID number to match.
    :param name: The name of the course to match.
    :param course: Course to test.
    :return: True if this course is the course we want to manipulate. False
             otherwise.
    """
    c1 = term == course.get_term()
    c2 = course_id == course.get_id()
    c3 = name == course.get_name()
    return c1 and c2 and c3\


def format_num_2(num):
    """
    Format the number to 2 decimal places.

    :param num: The number to format.
    :return: The number formatted to 2 decimal places.
    """
    return float("{:.2f}".format(num))


def format_num_3(num):
    """
    Format the number to 3 decimal places.

    :param num: The number to format.
    :return: The number formatted to 3 decimal places.
    """
    return float("{:.3f}".format(num))


def is_numeric(string):
    """
    Determine whether the string is a number.

    :param string: String to test.
    :return: True if the string is a number. False otherwise.
    """
    try:
        float(string)
        return True
    except ValueError:
        return False
