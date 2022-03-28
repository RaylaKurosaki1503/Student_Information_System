"""
Author: Rayla Kurosaki

File: example.py

Description: This program will print the student's transcript given the input
             file "sis.xlsx".
"""

import sys
from os.path import exists as file_exists

import __utils__ as utils
import algorithm as alg


def main():
    """
    The driver function to run the program.
    """
    filename = "sis"
    path = f"../data/{filename}.xlsx"
    if not file_exists(path):
        print(f"Place your excel file in the data directory.\n"
              f"Make sure it is called \"{filename}.xlsx\"")
        sys.exit(0)
        pass
    workbook = utils.get_workbook(path)
    student = alg.phase0_main(workbook)
    alg.phase1_main(student, workbook)
    alg.phase2_main(student, workbook)
    alg.phase3_main(student, "grades")
    alg.phase4_main(student, "transcript")
    pass


if __name__ == '__main__':
    main()
    pass
