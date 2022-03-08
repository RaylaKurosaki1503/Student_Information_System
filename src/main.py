"""
Author: Rayla Kurosaki

File: main.py

Description: This program will print the student's transcript given the input
             file "sis.xlsx".
"""

import sys
from os.path import exists as file_exists

import rayla.excel
import algorithm as alg


def main():
    # Hardcode the path from source root.
    path = "../data/sis.xlsx"
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
    student = alg.phase0_main(workbook)
    # Add data to the student's database.
    alg.phase1_main(student, workbook)
    # Manipulate the student's database.
    alg.phase2_main(student, workbook)
    # Print the student's transcript.
    alg.phase3_main(student)
    print("The transcript has been printed. "
          "Look for \"transcript.txt\" in the data directory.")
    pass


if __name__ == '__main__':
    main()
    pass
