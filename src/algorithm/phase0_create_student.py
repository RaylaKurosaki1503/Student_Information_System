"""
Author: Rayla Kurosaki

File: phase0_create_student.py

Description: This file creates a student given the information the student has
             added on the first page of the Microsoft Excel
             Workbook/Spreadsheet.
"""

import __utils__ as utils
import constructors as struct
import minors as minor
import degrees as major


def create_new_student(workbook):
    """
    Creates an instance of a student based on the spreadsheet that contains
    the student's basic info.

    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse
                     through.
    :return: A student with their basic info.
    """
    ws = utils.get_worksheet(workbook, "basic_info")
    name, majors, minors = "", {}, {}
    for row in ws.iter_rows():
        type, data, degree = row[0].value, row[1].value, row[2].value
        match type:
            case "Name":
                name = data
                pass
            case "Major":
                match data:
                    case "Computational Mathematics":
                        majors[data] = major.Cmth2017()
                        pass
                    case "Applied and Computational Mathematics":
                        pass
                pass
            case "Minor":
                match data:
                    case "Physics":
                        minors[data] = minor.Phys()
                        pass
                    case "Computer Science":
                        minors[data] = minor.Compsci()
                        pass
                pass
        pass
    return struct.Student(name, majors, minors)


def phase0_main(workbook):
    """
    The main function to call the functions above to create a new student.

    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse
                     through.
    """
    return create_new_student(workbook)
