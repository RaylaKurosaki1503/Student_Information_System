"""
Author: Rayla Kurosaki

File: phase0_create_student.py

Description: This file creates a student given the information the student has
             added on the first page of the Microsoft Excel
             Workbook/Spreadsheet.
"""

import rayla.excel
from constructors.student import Student


def create_new_student(workbook):
    ws = rayla.excel.get_worksheet(workbook, "basic_info")
    name, majors, minors = "", {}, {}
    for row in ws.iter_rows():
        type, data, degree = row[0].value, row[1].value, row[2].value
        match type:
            case "Name":
                name = data
            case "Major":
                majors[data] = degree
            case "Minor":
                minors[data] = ""
    return Student(name, majors, minors)


def main(workbook):
    return create_new_student(workbook)
