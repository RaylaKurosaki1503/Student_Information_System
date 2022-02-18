################################################################################
"""
Author: Rayla Kurosaki

File: main.py

Description:
"""
################################################################################


import rayla.excel
from student import Student
import add_data
import modify_data


def main():
    """

    :return:
    """
    # Creating/Initializing a student
    name = "Rayla Kurosaki"
    stu = Student(name)
    # Ask the user to input the absolute path to the Excel workbook
    path = input("Enter the absolute path to the excel workbook: ")
    wb = rayla.excel.get_workbook(path)

    add_data.main(stu, wb)
    modify_data.main(stu, wb)
    # for course in stu.get_courses():
    #     print(course.get_raw_grade(), course.get_letter_grade())
    #     print(course.get_name(), ",", course.get_gpa())
    #     for assignment in course.get_assignments().values():
    #         print("\t" + str(assignment.get_type()) + ":" + str(assignment.get_average()))
    #     print("")
    for k,v in stu.get_gpa_history().items():
        print(k, v)
    return


if __name__ == '__main__':
    main()
