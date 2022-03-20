"""
Author: Rayla Kurosaki

File: main.py

Description: This program will print the student's transcript given the input
             file "sis.xlsx".
"""

import sys
from os.path import exists as file_exists

import __utils__ as utils
import algorithm as alg


def main():
    """
    The driver code to run the program.
    """
    path = "../data/sis.xlsx"
    if not file_exists(path):
        print("Place your excel file in the data directory.\n"
              "Make sure it is called \"sis.xlsx\"")
        sys.exit(0)
        pass
    workbook = utils.get_workbook(path)
    student = alg.phase0_main(workbook)
    alg.phase1_main(student, workbook)
    alg.phase2_main(student, workbook)
    alg.phase3_main(student)
    alg.phase4_main(student)
    pass


if __name__ == '__main__':
    # main()
    print("Hello Rayla!")
    pass
