################################################################################
"""
Author: Rayla Kurosaki

File: helper_functions.py

Description:
"""
################################################################################


def is_correct_course(term, course_id, name, course):
    """

    :param term:
    :param course_id:
    :param name:
    :param course:
    :return:
    """
    c1 = term == course.get_term()
    c2 = course_id == course.get_id()
    c3 = name == course.get_name()
    return c1 and c2 and c3


def format_num(num):
    """

    :param num:
    :return:
    """
    return float("{:.2f}".format(num))


def is_numeric(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
