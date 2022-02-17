"""
Author: Rayla Kurosaki

File: add_data.py

Description:
"""

from Assignment import Assignment
from Course import Course
import rayla.excel


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
                c1 = term == course.get_term()
                c2 = id + "." + sxn == course.get_id()
                c3 = name == course.get_name()
                # If this assignment belongs to this course
                if c1 and c2 and c3:
                    # Create a new assignment type and add it to this course.
                    assignment = Assignment(type, float(weight))
                    Course.add_assignment(course, type, assignment)
                    # Special case where
                    c4 = id + "." + sxn == "PHYS-320.01"
                    c5 = id + "." + sxn == "PHYS-321.01"
                    c6 = type == "Homework and Quiz"
                    if (c4 or c5) and c6:
                        assignment = Assignment("Homework", float(weight))
                        Course.add_assignment(course, "Homework", assignment)
                        assignment = Assignment("Quiz", float(weight))
                        Course.add_assignment(course, "Quiz", assignment)
                        pass
                    # To save time, break out of this loop.
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
            # Iterate through the courses the student has taken
            for course in student.get_courses():
                c1 = term == course.get_term()
                c2 = id + "." + sxn == course.get_id()
                c3 = name == course.get_name()
                # If this assignment belongs to this course
                if c1 and c2 and c3:
                    # Add teh grade to the correct assignment type
                    assignment = Course.get_assignments(course)[type]
                    Assignment.add_grade(assignment, raw)
                    break
                    pass
                pass
            pass
        # Increment the index counter by 1
        i += 1
        pass
    pass


def add_data_main(student, workbook):
    add_courses(student, workbook)
    add_assignments(student, workbook)
    add_grades(student, workbook)
