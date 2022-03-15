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
    ws = utils.get_worksheet(workbook, "courses")
    for i, row in enumerate(ws.values):
        if not (i == 0):
            term, id, sxn, name, ch, prof = row
            new_course = struct.Course(term, id, sxn, name, int(ch), prof)
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
    ws = utils.get_worksheet(workbook, "assignments")
    for i, row in enumerate(ws.values):
        if not (i == 0):
            term, id, sxn, name, type, weight = row
            for course in student.get_courses():
                if utils.is_correct_course(term, id, sxn, name, course):
                    assignment = struct.Assignment(type, float(weight))
                    course.add_assignment(type, assignment)
                    c4 = course.get_prof() == "Dawn Hollenbeck"
                    c5 = course.get_id() == "PHYS-320"
                    c6 = course.get_id() == "PHYS-321"
                    c7 = type == "Homework and Quiz"
                    if c4 and (c5 or c6) and c7:
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
    ws = utils.get_worksheet(workbook, "grades")
    for i, row in enumerate(ws.values):
        if not (i == 0):
            term, id, sxn, name, type, raw, curved, notes = row
            if not ((raw is None) and (curved is None)):
                for course in student.get_courses():
                    if utils.is_correct_course(term, id, sxn, name, course):
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
    pass


def add_extra_credit(student, workbook):
    """
    Adds all the extra credit the student has earned to the corresponding
    courses from the Microsoft Excel Workbook/Spreadsheet.

    :param student: The student to manipulate.
    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse
                     through.
    """
    ws = utils.get_worksheet(workbook, "extra_credit")
    for i, row in enumerate(ws.values):
        if not (i == 0):
            term, id, sxn, name, extra_credit = row
            for course in student.get_courses():
                if utils.is_correct_course(term, id, sxn, name, course):
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
    letters = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-"]
    ws = utils.get_worksheet(workbook, "grading_scales")
    for i, row in enumerate(ws.values):
        if not (i == 0):
            term = row[0]
            id = row[1]
            sxn = row[2]
            name = row[3]
            grading_scale = {}
            for j in range(len(letters)):
                num = row[j + 4]
                if not (num is None):
                    grading_scale[letters[j]] = float(num)
                    pass
                pass
            for course in student.get_courses():
                if utils.is_correct_course(term, id, sxn, name, course):
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
    ws = utils.get_worksheet(workbook, "drop_grades")
    for i, row in enumerate(ws.values):
        if not (i == 0):
            term, id, sxn, name, type, count = row
            for course in student.get_courses():
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
    add_courses(student, workbook)
    add_assignments(student, workbook)
    add_grades(student, workbook)
    add_extra_credit(student, workbook)
    add_grading_scale(student, workbook)
    add_drop_count(student, workbook)
    pass
