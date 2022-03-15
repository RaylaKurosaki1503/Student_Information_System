"""
Author: Rayla Kurosaki

File: special_calculations.py

Description: This file contains functions to compute the raw grade of certain
             courses. This is required since the courses here either do not
             compute the raw grade of the course in the standard way, or the
             grades themselves need some modification before computing the
             raw grade.
"""

import __utils__ as utils


def calc_CS(course, lst):
    """
    For some courses, they have a course grade limit rule. This rule comes into
    play when the difference between your Assignments and Tests averages is
    more than about 20%. Also, the raw grade may only be at most 10% more than
    the average grade of the elements of your worse Assignments Component or
    Tests Component. Courses that would use this rule include but are not
    limited to:
        - Computer Science I
        - Computer Science II
        - The Mechanics of Programming

    :param course: A course that can apply the course grade limit rule.
    :param lst: A list of types of assignments that are not exams.
    """
    course_grade = course.get_raw_grade()
    sum_assignments, sum_exams = 0.0, 0.0
    for type, assignment in course.get_assignments().items():
        weighted_average = 0.0
        if len(assignment.get_grades()) > 0:
            weight = assignment.get_weight()
            type_grade = assignment.get_average()
            weighted_average = weight * type_grade / 100
            pass
        if type in lst:
            sum_assignments += weighted_average
            pass
        else:
            sum_exams += weighted_average
            pass
        pass
    sum_assignments *= 2
    sum_exams *= 2
    if abs(sum_assignments - sum_exams) > 20:
        max_assignment, max_exam = sum_assignments + 10, sum_exams + 10
        if sum_exams < sum_assignments:
            if course_grade > max_exam:
                course.set_raw_grade(utils.format_num_3(max_exam))
                pass
            pass
        else:
            if course_grade > max_assignment:
                course.set_raw_grade(utils.format_num_3(max_assignment))
                pass
            pass
        pass
    pass


def calc_basic(course):
    """
    For some courses, the raw grade is calculated simply by computing the sum
    of the numerators of the grades and the sum of the numerators of the
    grades. Then dividing the two values.

    :param course: A course the student has taken.
    """
    num, denom = 0, 0
    for assignment in course.get_assignments().values():
        for grade in assignment.get_grades():
            num_str, denom_str = grade[1].split(" / ")
            num += float(num_str)
            denom += float(denom_str)
            pass
        pass
    if not (denom == 0):
        course.set_raw_grade(utils.format_num_3(100 * num / denom))
    pass


def calc_UP2(course):
    """
    Special calculations to compute the raw grade for University Physics II
    taught by Dr. Davis. For this class, all quiz grades have their grades
    raised by a set amount.

    :param course: University Physics II taught by Dr. Davis.
    """
    new_raw_grade = 0.0
    for type, assignment in course.get_assignments().items():
        assignment_weight = assignment.get_weight()
        if type == "Quiz":
            quiz_sum = 0.0
            grades = assignment.get_grades()
            if not (len(grades) == 0):
                for grade in grades:
                    num, denom = grade[1].split(" / ")
                    quiz_sum += (float(num) + 10 - float(denom)) / 10
                    pass
                assignment_average = 100 * quiz_sum / len(grades)
                pass
            else:
                assignment_average = 0
                pass
            assignment.set_average(assignment_average)
            pass
        else:
            assignment_average = assignment.get_average()
            pass
        new_raw_grade += assignment_average * assignment_weight / 100
        pass
    if not (new_raw_grade == 0):
        course.set_raw_grade(utils.format_num_2(new_raw_grade))
        pass
    else:
        course.set_raw_grade("n/a")
        pass
    pass


def calc_VnW(course):
    """
    Special calculations to compute the raw grade for Vibrations and Waves
    taught by Dr. Richmond. For this class, the average homework grade is
    calculated differently.

    :param course: Vibrations and Waves course taught by Dr. Richmond.
    """
    homework = course.get_assignments()["Homework"]
    hw_grades = homework.get_grades()
    if not (len(hw_grades) == 0):
        num, denom = 0, 0
        for grade in hw_grades:
            num_str, denom_str = grade[1].split(" / ")
            num += float(num_str)
            denom += float(denom_str)
            pass
        homework.set_average(utils.format_num_3(100 * num / denom))
        course_grade, total_weight = 0, 0
        for assignment in course.get_assignments().values():
            total_weight += assignment.get_weight()
            course_grade += assignment.get_weight() * assignment.get_average()
            pass
        course.set_raw_grade(utils.format_num_3(course_grade / total_weight))
    pass
