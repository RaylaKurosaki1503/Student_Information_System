################################################################################
"""
Author: Rayla Kurosaki

File: phase1_add_data.py

Description:
"""
################################################################################


import rayla.excel
from algorithm import helper_functions as hf
from constructors.course import Course
from constructors.assignment import Assignment


def add_courses(student, workbook):
    """

    :param student:
    :param workbook:
    :return:
    """
    # Get the worksheet that contains all the courses the student has taken
    ws = rayla.excel.get_worksheet(workbook, "courses")
    # Set an index counter
    i = 0
    # Iterate through each row of the worksheet
    for row in ws.values:
        # If the row is not the first row
        if not (i == 0):
            # Unpack the row
            term, id, sxn, name, ch, prof = row
            course_id = id + "." + sxn
            # Create a new course from that row
            new_course = Course(term, course_id, name, int(ch), prof)
            # Add that course to the student's database
            student.add_course(new_course)
            pass
        # Increment the index counter by 1
        i += 1
        pass
    pass


def add_assignments(student, workbook):
    """

    :param student:
    :param workbook:
    :return:
    """
    # Get the worksheet that contains all the types of assignments
    ws = rayla.excel.get_worksheet(workbook, "assignments")
    # Set the index counter
    i = 0
    # Iterate through each row of the worksheet
    for row in ws.values:
        # If it is not the first row
        if not (i == 0):
            # Unpack the row
            term, id, sxn, name, type, weight = row
            # Iterate through the courses the student has taken
            for course in student.get_courses():
                # If this assignment belongs to this course
                if hf.is_correct_course(term, id + "." + sxn, name, course):
                    # Create a new assignment type and add it to this course.
                    assignment = Assignment(type, float(weight))
                    course.add_assignment(type, assignment)
                    # Course.add_assignment(course, type, assignment)
                    # Special case
                    c4 = id + "." + sxn == "PHYS-320.01"
                    c5 = id + "." + sxn == "PHYS-321.01"
                    c6 = type == "Homework and Quiz"
                    if (c4 or c5) and c6:
                        assignment = Assignment("Homework", float(weight))
                        course.add_assignment("Homework", assignment)
                        assignment = Assignment("Quiz", float(weight))
                        course.add_assignment("Quiz", assignment)
                        pass
                    break
                    pass
                pass
            pass
        # Increment the index counter
        i += 1
        pass
    pass


def add_grades(student, workbook):
    """

    :param student:
    :param workbook:
    :return:
    """
    # Get the worksheet that contains all the courses the student has taken
    ws = rayla.excel.get_worksheet(workbook, "grades")
    # Set an index counter
    i = 0
    # Iterate through each row of the worksheet
    for row in ws.values:
        # If the row is not the first row
        if not (i == 0):
            # Unpack the row
            term, id, sxn, name, type, raw, curved, notes = row
            # Exit the loop if there is no grade for the assignment
            if not ((raw is None) and (curved is None)):
                # Iterate through the courses the student has taken
                for course in student.get_courses():
                    # If this assignment belongs to this course
                    if hf.is_correct_course(term, id + "." + sxn, name, course):
                        # Add the grade to the correct assignment type
                        assignment = course.get_assignments()[type]
                        if curved is not None:
                            assignment.add_grade(curved)
                            pass
                        else:
                            assignment.add_grade(raw)
                            pass
                        break
                        pass
                    pass
                pass
            pass
        # Increment the index counter by 1
        i += 1
        pass
    pass


def add_extra_credit(student, workbook):
    """

    :param student:
    :param workbook:
    :return:
    """
    # Get the worksheet that contains all the courses the student has taken
    ws = rayla.excel.get_worksheet(workbook, "extra_credit")
    # Set an index counter
    i = 0
    # Iterate through each row of the worksheet
    for row in ws.values:
        # If the row is not the first row
        if not (i == 0):
            # Unpack the row
            term, id, sxn, name, extra_credit = row
            # Iterate through the courses the student has taken
            for course in student.get_courses():
                # If this assignment belongs to this course
                if hf.is_correct_course(term, id + "." + sxn, name, course):
                    # Set the extra credit the student has earned for that class
                    course.set_extra_credit(extra_credit)
                    break
                    pass
                pass
            pass
        # Increment the index counter by 1
        i += 1
        pass
    pass


def add_grading_scale(student, workbook):
    """

    :param student:
    :param workbook:
    :return:
    """
    letters = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-"]
    # Get the worksheet that contains all the courses the student has taken
    ws = rayla.excel.get_worksheet(workbook, "grading_scales")
    # Set an index counter
    i = 0
    # Iterate through each row of the worksheet
    for row in ws.values:
        # If the row is not the first row
        if not (i == 0):
            # Unpack the row
            term = row[0]
            course_id = row[1] + "." + row[2]
            name = row[3]
            # Create the grading scale
            grading_scale = {}
            for i in range(len(letters)):
                num = row[i + 4]
                if not (num is None):
                    grading_scale[letters[i]] = float(num)
            # Iterate through the courses the student has taken
            for course in student.get_courses():
                # If this assignment belongs to this course
                if hf.is_correct_course(term, course_id, name, course):
                    # Set the grading scale for that class
                    course.set_grading_scale(grading_scale)
                    break
                    pass
                pass
            pass
        # Increment the index counter by 1
        i += 1
        pass
    pass


def add_drop_count(student, workbook):
    """

    :param student:
    :param workbook:
    :return:
    """
    # Get the worksheet that contains all the types of assignments
    ws = rayla.excel.get_worksheet(workbook, "drop_grades")
    # Set the index counter
    i = 0
    # Iterate through each row of the worksheet
    for row in ws.values:
        # If it is not the first row
        if not (i == 0):
            # Unpack the row
            term, id, sxn, name, type, count = row
            # Iterate through the courses the student has taken
            for course in student.get_courses():
                # If this assignment belongs to this course
                if hf.is_correct_course(term, id + "." + sxn, name, course):
                    assignments = course.get_assignments()
                    assignment = assignments[type]
                    assignment.set_drop_count(count)
                    break
                    pass
                pass
            pass
        # Increment the index counter
        i += 1
        pass
    pass


def add_other(student):
    """

    :param student:
    :return:
    """
    for course in student.get_courses():
        if course.get_id() in ["PHYS-320.01", "PHYS-321.01"]:
            assignments = course.get_assignments()
            hw_n_quiz = []
            for grade in assignments["Homework"].get_grades():
                hw_n_quiz.append(grade)
                pass
            for grade in assignments["Quiz"].get_grades():
                hw_n_quiz.append(grade)
                pass
            assignment = assignments["Homework and Quiz"]
            assignment.set_grades(hw_n_quiz)
    pass


def main(student, workbook):
    """

    :param student:
    :param workbook:
    :return:
    """
    add_courses(student, workbook)
    add_assignments(student, workbook)
    add_grades(student, workbook)
    add_extra_credit(student, workbook)
    add_grading_scale(student, workbook)
    add_drop_count(student, workbook)
    add_other(student)
    pass
