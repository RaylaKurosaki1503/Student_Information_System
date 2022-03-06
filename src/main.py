"""
Author: Rayla Kurosaki

File: main.py

Description: This program will print the student's transcript given the input
             file "sis.xlsx".
"""
import sys
from os.path import exists as file_exists

import rayla.excel
from algorithm import phase0_create_student
from algorithm import phase1_add_data
from algorithm import phase2_modify_data
from algorithm import phase3_print_transcript

if __name__ == '__main__':
    # # Lines of code to print the transcript in the console
    # import logging
    # logging.basicConfig(level=logging.INFO, format="%(message)s")

    # Hard code the path from source root.
    path = "data/sis.xlsx"
    # Check if the file exists
    if not file_exists(path):
        # Exits the program if the file does not exist.
        print("Place your excel file in the data directory.\n"
              "Make sure it is called \"sis.xlsx\"")
        sys.exit(0)
        pass

    # Get the Excel Spreadsheet.
    workbook = rayla.excel.get_workbook(path)

    # Create a new student.
    student = phase0_create_student.main(workbook)

    # Add data to the student's database.
    phase1_add_data.main(student, workbook)

    # Manipulate the student's database.
    phase2_modify_data.main(student, workbook)

    # Print the student's transcript.
    phase3_print_transcript.main(student)

    print("The transcript has been printed. "
          "Look for \"transcript.txt\" in the data directory.")
    pass
