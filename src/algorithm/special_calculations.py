"""
Author: Rayla Kurosaki

File: special_calculations.py

Description: This file contains functions to compute the raw grade of certain
             courses. This is required since the courses here either do not
             compute the raw grade of the course in the standard way, or the
             grades themselves need some modification before computing the
             raw grade.
"""

import algorithm as alg


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
    # Get the raw grade.
    course_grade = course.get_raw_grade()
    # Initialize the assignment and exam averages.
    sum_assignments, sum_exams = 0.0, 0.0
    # For each assignment.
    for type, assignment in course.get_assignments().items():
        # Initialize the weighted average.
        weighted_average = 0.0
        # If there are grades.
        if len(assignment.get_grades()) > 0:
            # Get the weight and average for this type of assignment.
            weight = assignment.get_weight()
            type_grade = assignment.get_average()
            # Compute the weighted average for this type of assignment.
            weighted_average = weight * type_grade / 100
            pass
        # If this type of assignment is not an exam.
        if type in lst:
            # Increase the assignment weighted average.
            sum_assignments += weighted_average
            pass
        # Otherwise, increase the exam weighted average.
        else:
            sum_exams += weighted_average
            pass
        pass
    # Multiply both weighted averages by 2.
    sum_assignments *= 2
    sum_exams *= 2
    # If the difference in the weighted averages is more than 20.
    if abs(sum_assignments - sum_exams) > 20:
        # Compute the maximum weighted averages.
        max_assignment, max_exam = sum_assignments + 10, sum_exams + 10
        # If the minimum weighted average is the exam weighted average.
        if sum_exams < sum_assignments:
            # If the raw grade is larger than the maximum exam average.
            if course_grade > max_exam:
                # Set the raw grade to the maximum exam grade.
                course.set_raw_grade(alg.format_num_3(max_exam))
                pass
            pass
        # If the minimum weighted average is the assignment weighted average.
        else:
            # If the raw grade is larger than the maximum assignment average.
            if course_grade > max_assignment:
                # Set the raw grade to the maximum assignment grade.
                course.set_raw_grade(alg.format_num_3(max_assignment))
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
    # Initializing the numerator and denominator.
    num, denom = 0, 0
    # For each assignment type.
    for assignment in course.get_assignments().values():
        # For each grade in this assignment type.
        for grade in assignment.get_grades():
            # Split the string
            num_str, denom_str = grade[1].split(" / ")
            # Cumulatively add the numerator and denominator.
            num += float(num_str)
            denom += float(denom_str)
            pass
        pass
    # If the denominator is not 0 (if there are no grades).
    if not (denom == 0):
        # Divide the numerator by the denominator and then multiply by 100.
        # Then set this value as the raw grade for the course.
        course.set_raw_grade(alg.format_num_3(100 * num / denom))
    pass


def calc_UP2(course):
    """
    Special calculations to compute the raw grade for University Physics II
    taught by Tracy A. Davis. For this class, all quiz grades have their grades
    raised by a set amount.

    :param course: University Physics II taught by Tracy A. Davis.
    """
    # Set the new raw grade.
    new_raw_grade = 0.0
    # For each typeof assignment.
    for type, assignment in course.get_assignments().items():
        # Get the weight of the type of assignment.
        assignment_weight = assignment.get_weight()
        # If the type of assignment is a Quiz.
        if type == "Quiz":
            # Initialize the quiz average.
            quiz_sum = 0.0
            # Get the list of quiz grades.
            grades = assignment.get_grades()
            # If there are quiz grades.
            if not (len(grades) == 0):
                # For each quiz grade.
                for grade in grades:
                    # Compute the new quiz grade. This is done by computing the
                    # difference between 10 and the denominator of the quiz
                    # grade. Then adding that difference to the numerator of
                    # the quiz grade. Finally, divide this number by 10.
                    num, denom = grade[1].split(" / ")
                    quiz_sum += (float(num) + 10 - float(denom)) / 10
                    pass
                # Compute the quiz average.
                assignment_average = 100 * quiz_sum / len(grades)
                pass
            # If there are no quiz grades.
            else:
                # Set the quiz average to 0.
                assignment_average = 0
                pass
            # Set the quiz average for the Quiz assignment.
            assignment.set_average(assignment_average)
            pass
        # if the type of assignment is not a Quiz.
        else:
            # Get the pre-calculated average of the assignment.
            assignment_average = assignment.get_average()
            pass
        # Add the assignment weighted average to the new raw grade.
        new_raw_grade += assignment_average * assignment_weight / 100
        pass
    # If the new raw grade is not 0.
    if not (new_raw_grade == 0):
        # Set the new raw grade for this course.
        course.set_raw_grade(alg.format_num_2(new_raw_grade))
        pass
    # Otherwise, set the raw grade as "n/a"
    else:
        course.set_raw_grade("n/a")
        pass
    pass


def calc_VnW(course):
    """
    Special calculations to compute the raw grade for Vibrations and Waves
    taught by Michael Richmond. For this class, the average homework grade is
    calculated differently.

    :param course: Vibrations and Waves course taught by Michael Richmond
    """
    # Get the homework assignments
    homework = course.get_assignments()["Homework"]
    # Get the homework grades
    hw_grades = homework.get_grades()
    if not (len(hw_grades) == 0):
        num, denom = 0, 0
        # Iterate through each hw grade
        for grade in hw_grades:
            # Add the numerators and denominators of each grade
            num_str, denom_str = grade[1].split(" / ")
            num += float(num_str)
            denom += float(denom_str)
            pass
        # Re-compute the homework average grade
        homework.set_average(alg.format_num_3(100 * num / denom))
        course_grade, total_weight = 0, 0
        # Re-compute the course raw grade
        for assignment in course.get_assignments().values():
            total_weight += assignment.get_weight()
            course_grade += assignment.get_weight() * assignment.get_average()
            pass
        # Re-set the course raw grade
        course.set_raw_grade(alg.format_num_3(course_grade / total_weight))
    pass
