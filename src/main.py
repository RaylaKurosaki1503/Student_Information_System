"""
Author: Rayla Kurosaki

File: main.py

Description: This file runs the entire program.
"""

import sys
import logging
import rayla.excel
from algorithm import phase1_add_data
from algorithm import phase2_modify_data
from algorithm import phase3_print_transcript
from constructors.student import Student


def main():
    """
    This program will ask the user to input the following
        1. Their name
        2. The absolute path to the Microsoft Excel Workbook/Spreadsheet
    Once the user finished the tasks above, it will create a student from the
    name, and it will get access to the Microsoft Excel Workbook/Spreadsheet.
    After creating a student and getting access to the Microsoft Excel
    Workbook/Spreadsheet, it will call one function to add all the relevant
    data into the student, one function to perform all the calculations, and one
    function to print the results in the form of a Transcript.
    """
    # # Comment the following lines of code out
    # level = logging.INFO
    # fmt = '%(message)s'
    # logging.basicConfig(level=level, format=fmt)

    # Ask the user for their name.
    name = "Rayla Kurosaki"
    # name = input("Enter your name: ")

    # Creating/Initializing a student.
    student = Student(name)

    # Ask the user to input the absolute path to the Excel workbook.
    # path = sys.argv[1]
    path = input("Enter the absolute path to the Excel workbook: ")

    # Get the Excel Spreadsheet.
    workbook = rayla.excel.get_workbook(path)

    # Add data to the student's database.
    phase1_add_data.main(student, workbook)

    # Manipulate the student's database.
    phase2_modify_data.main(student, workbook)

    # Print the student's transcript.
    phase3_print_transcript.main(student)
    pass


if __name__ == '__main__':
    main()
    pass
