################################################################################
"""
Author: Rayla Kurosaki

File: main.py

Description:
"""
################################################################################


from student import Student
import add_data
import rayla.excel


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
    return


if __name__ == '__main__':
    main()
