"""
Author: Rayla Kurosaki

File: main.py

Description: This file runs the entire program.
"""
import sys

import rayla.excel
from algorithm import phase1_add_data
from algorithm import phase2_modify_data
from algorithm import phase3_print_transcript
from constructors.student import Student


def main():
    """
    This function will ask the user to input the following
        1. Their name
        2. The absolute path to the Microsoft Excel Workbook/Spreadsheet
    Once the user finished the tasks above, it will create a student from the
    name, and it will get access to the Microsoft Excel Workbook/Spreadsheet.
    After creating a student and getting access to the Microsoft Excel
    Workbook/Spreadsheet, it will call one function to add all the relevant
    data into the student, one function to perform all the calculations, and one
    function to print the results in the form of a Transcript.
    """
    # Creating/Initializing a student
    # name = input("Enter your name: ")
    name = "Rayla Kurosaki"
    student = Student(name)
    # Ask the user to input the absolute path to the Excel workbook
    # path = input("Enter the absolute path to the excel workbook: ")
    path = sys.argv[1]
    # Get the Excel Spreadsheet
    workbook = rayla.excel.get_workbook(path)
    # Add data to the student's database
    phase1_add_data.main(student, workbook)
    # Manipulate the student's database
    phase2_modify_data.main(student, workbook)
    # Print the student's transcript
    phase3_print_transcript.main(student)
    return


if __name__ == '__main__':
    main()
    # print(sys.argv)
    pass
