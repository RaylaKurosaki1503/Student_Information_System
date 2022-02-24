################################################################################
"""
Author: Rayla Kurosaki

File: main.py

Description:
"""
################################################################################


import sys
import rayla.excel
from algorithm import phase1_add_data
from algorithm import phase2_modify_data
from algorithm import phase3_print_transcript
from constructors.student import Student


def main():
    """

    :return:
    """
    # Creating/Initializing a student
    name = "Rayla Kurosaki"
    stu = Student(name)
    # Ask the user to input the absolute path to the Excel workbook
    # path = input("Enter the absolute path to the excel workbook: ")
    path = sys.argv[1]
    # Get the Excel Spreadsheet
    wb = rayla.excel.get_workbook(path)
    # Add data to the student's database
    phase1_add_data.main(stu, wb)
    # Manipulate the student database
    phase2_modify_data.main(stu, wb)
    # Print the student's transcript
    phase3_print_transcript.main(stu)

    for k, v in stu.get_gpa_history().items():
        print(k, v)

    for course in stu.get_courses():
        print([course.get_term(), course.get_id(), course.get_name(),
               course.get_raw_grade(), course.get_letter_grade(),
               course.get_final_grade()])
    return


if __name__ == '__main__':
    main()
