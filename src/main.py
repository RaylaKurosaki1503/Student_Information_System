"""
Author: Rayla Kurosaki

File: main.py

Description:
"""
import Assignment
import Course
from Student import Student
import add_data
import rayla.excel


def main():
    # Creating/Initializing a student given their name, major(s), and minor(s)
    name = "Rayla Kurosaki"
    majors = ["Computational Mathematics",
              "Applied and Computational Mathematics"]
    minors = ["Physics"]

    """
    """
    stu = Student(name)
    path = input("Enter the absolute path to the excel workbook: ")
    wb = rayla.excel.get_workbook(path)

    add_data.add_data_main(stu, wb)

    for course in stu.get_courses():
        Course.pp_print(course)
        for type, assignment in Course.Course.get_assignments(course).items():
            Assignment.pp_print(assignment)
        print("")
    return


if __name__ == '__main__':
    main()
