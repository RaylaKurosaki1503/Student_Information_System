"""
Author: Rayla Kurosaki

File: phase1_add_data.py

Description: This file contains all the functionality of adding data from the
             Microsoft Excel Workbook/Spreadsheet to the student's database.
"""

import __utils__ as utils
import constructors as struct


def add_courses(student, workbook):
    """
    Adds all the courses the student has taken from the Microsoft Excel
    Workbook/Spreadsheet.

    :param student: The student to manipulate.
    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse
                     through.
    """
    # Get the worksheet that contains all the courses the student has taken.
    ws = utils.get_worksheet(workbook, "courses")
    # Iterate through each row of the worksheet.
    for i, row in enumerate(ws.values):
        # If the row is not the first row.
        if not (i == 0):
            # Unpack the row.
            term, id, sxn, name, ch, prof = row
            # Create a new course from that row.
            new_course = struct.Course(term, id, sxn, name, int(ch), prof)
            # Add that course to the student's database.
            student.add_course(new_course)
            pass
        pass
    pass


def add_assignments(student, workbook):
    """
    Adds all the types of assignments to the corresponding courses from the
    Microsoft Excel Workbook/Spreadsheet.

    :param student: The student to manipulate.
    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse
                     through.
    """
    # Get the worksheet that contains all the types of assignments for each
    # course.
    ws = utils.get_worksheet(workbook, "assignments")
    # Iterate through each row of the worksheet.
    for i, row in enumerate(ws.values):
        # If it is not the first row.
        if not (i == 0):
            # Unpack the row.
            term, id, sxn, name, type, weight = row
            # Iterate through the courses the student has taken.
            for course in student.get_courses():
                # Find the correct course.
                if utils.is_correct_course(term, id, sxn, name, course):
                    # Create a new assignment type and add it to this course.
                    assignment = struct.Assignment(type, float(weight))
                    course.add_assignment(type, assignment)
                    # Special case for the courses taught by a specific
                    # professor.
                    c4 = course.get_prof() == "Dawn Hollenbeck"
                    c5 = course.get_id() == "PHYS-320"
                    c6 = course.get_id() == "PHYS-321"
                    c7 = type == "Homework and Quiz"
                    if c4 and (c5 or c6) and c7:
                        # Add Homeworks and Quizzes as separate categories.
                        assignment = struct.Assignment("Homework",
                                                       float(weight)
                                                       )
                        course.add_assignment("Homework", assignment)
                        assignment = struct.Assignment("Quiz", float(weight))
                        course.add_assignment("Quiz", assignment)
                        pass
                    break
                    pass
                pass
            pass
        pass
    pass


def add_grades(student, workbook):
    """
    Adds all the grades the student earned to the corresponding type of
    assignment that corresponds to the corresponding courses from the
    Microsoft Excel Workbook/Spreadsheet.

    :param student: The student to manipulate.
    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse
                     through.
    """
    # Get the worksheet that contains all the grades of the assignments the
    # student has done.
    ws = utils.get_worksheet(workbook, "grades")
    # Iterate through each row of the worksheet.
    for i, row in enumerate(ws.values):
        # If the row is not the first row.
        if not (i == 0):
            # Unpack the row.
            term, id, sxn, name, type, raw, curved, notes = row
            # Exit the loop if there is no grade for the assignment.
            if not ((raw is None) and (curved is None)):
                # Iterate through the courses the student has taken.
                for course in student.get_courses():
                    # Find the correct course.
                    if utils.is_correct_course(term, id, sxn, name, course):
                        # Add the grade to the assignment type.
                        # print(i)
                        assignment = course.get_assignments()[type]
                        # If the grade is curved, add the curved grade.
                        if curved is not None:
                            assignment.add_grade(curved)
                            pass
                        # Otherwise, add the raw grade.
                        else:
                            assignment.add_grade(raw)
                            pass
                        break
                    pass
                pass
            pass
        pass
    pass


def add_extra_credit(student, workbook):
    """
    Adds all the extra credit the student has earned to the corresponding
    courses from the Microsoft Excel Workbook/Spreadsheet.

    :param student: The student to manipulate.
    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse
                     through.
    """
    # Get the worksheet that contains all the courses the student has taken.
    ws = utils.get_worksheet(workbook, "extra_credit")
    # Iterate through each row of the worksheet.
    for i, row in enumerate(ws.values):
        # If the row is not the first row.
        if not (i == 0):
            # Unpack the row.
            term, id, sxn, name, extra_credit = row
            # Iterate through the courses the student has taken.
            for course in student.get_courses():
                # If this assignment belongs to this course.
                if utils.is_correct_course(term, id, sxn, name, course):
                    # Set the extra credit the student has earned for that
                    # class.
                    course.add_extra_credit(extra_credit)
                    break
                pass
            pass
        pass
    pass


def add_grading_scale(student, workbook):
    """
    Adds the grading scale to the corresponding courses from the
    Microsoft Excel Workbook/Spreadsheet.

    :param student: The student to manipulate.
    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse
                     through.
    """
    # Initialize all the letter grades in descend order.
    letters = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-"]
    # Get the worksheet that contains all the courses the student has taken.
    ws = utils.get_worksheet(workbook, "grading_scales")
    # Iterate through each row of the worksheet.
    for i, row in enumerate(ws.values):
        # If the row is not the first row.
        if not (i == 0):
            # Unpack the row.
            term = row[0]
            id = row[1]
            sxn = row[2]
            name = row[3]
            # Create the grading scale.
            grading_scale = {}
            for j in range(len(letters)):
                num = row[j + 4]
                if not (num is None):
                    grading_scale[letters[j]] = float(num)
                    pass
                pass
            # Iterate through the courses the student has taken.
            for course in student.get_courses():
                # If this assignment belongs to this course.
                if utils.is_correct_course(term, id, sxn, name, course):
                    # Set the grading scale for that class.
                    course.set_grading_scale(grading_scale)
                    break
                pass
            pass
        pass
    pass


def add_drop_count(student, workbook):
    """
    Add the number of assignments to drop (if any) to the corresponding
    courses from the Microsoft Excel Workbook/Spreadsheet.

    :param student: The student to manipulate.
    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse
                     through.
    """
    # Get the worksheet that contains all the types of assignments.
    ws = utils.get_worksheet(workbook, "drop_grades")
    # Iterate through each row of the worksheet.
    for i, row in enumerate(ws.values):
        # If it is not the first row.
        if not (i == 0):
            # Unpack the row.
            term, id, sxn, name, type, count = row
            # Iterate through the courses the student has taken.
            for course in student.get_courses():
                # If this assignment belongs to this course.
                if utils.is_correct_course(term, id, sxn, name, course):
                    assignments = course.get_assignments()
                    assignment = assignments[type]
                    assignment.set_drop_count(count)
                    break
                pass
            pass
        pass
    pass


def phase1_main(student, workbook):
    """
    The main function to call the functions above to add data to the student's
    database.

    :param student: The student to manipulate.
    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse
                     through.
    """
    # Add courses.
    add_courses(student, workbook)
    # Add the types of assignments.
    add_assignments(student, workbook)
    # Add the student grades.
    add_grades(student, workbook)
    # Add extra credit.
    add_extra_credit(student, workbook)
    # Add grading scales.
    add_grading_scale(student, workbook)
    # Add the number of grades to drop.
    add_drop_count(student, workbook)
    pass
