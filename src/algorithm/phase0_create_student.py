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


def create_new_student(workbook):
    """
    Creates an instance of a student based on the spreadsheet that contains
    the student's basic info.

    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse
                     through.
    :return: A student with their basic info.
    """
    # Get the worksheet that contains the student's basic info.
    ws = utils.get_worksheet(workbook, "basic_info")
    # Initialize some variables.
    name, majors, minors = "", {}, {}
    # For each row in the spreadsheet.
    for row in ws.iter_rows():
        # Unpack the row.
        type, data, degree = row[0].value, row[1].value, row[2].value
        match type:
            # If the type of data is the student's name.
            case "Name":
                # Set the student's name.
                name = data
                pass
            # If the type of data is the student's major.
            case "Major":
                # Set the student's major.
                majors[data] = degree
                # Filter through which major to set.
                pass
            # If the type of data is the student's minor.
            case "Minor":
                # Set the student's minor.
                match data:
                    # Filter through which minor to set.
                    case "Physics":
                        # Create a Physics minor to set.
                        minors[data] = minor.Phys()
                        pass
                    case "Computer Science":
                        # Create a Computer Science minor to set.
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
