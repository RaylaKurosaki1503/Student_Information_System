"""
Author: Rayla Kurosaki

File: assignment.py

Description: This file contains all the functionality of an assignment.
"""

import algorithm as alg


class Assignment:
    def __init__(self, type, weight):
        """
        Creates an instance of an assignment type.

        :param type: The type of assignment.
        :param weight: The weight of this assignment.
        """
        self.type = type
        self.weight = weight
        self.lst_grades = []
        self.average = -1
        self.drop_count = 0
        pass

    def get_type(self):
        """
        Get the type of assignment.

        :return: The type of assignment.
        """
        return self.type

    def get_weight(self):
        """
        Get the weight of the assignment type.

        :return: The weight of the assignment type.
        """
        return self.weight

    def get_grades(self):
        """
        Get the list of grades for this type of assignment.

        :return: The list of grades for this type of assignment.
        """
        return self.lst_grades

    def set_grades(self, grades):
        """
        Set the list of grades for this type of assignment.

        :param grades: The list of grades the student earned for this type of
                       assignment.
        """
        self.lst_grades = grades
        pass

    def add_grade(self, grade_str):
        """
        Adds the grade to the list of grades for this assignment. Also
        computes the numerical value of the grade if the grade is in the form
        "p / q" where p and q are real numbers.

        :param grade_str: The grade as a string.
        """
        if "/" in grade_str:
            num, denom = grade_str.split(" / ")
            grade_num = alg.format_num_2(100 * float(num) / float(denom))
            self.lst_grades.append([grade_num, grade_str])
            pass
        else:
            self.lst_grades.append(grade_str)
            pass
        pass

    def get_average(self):
        """
        Gets the average grade for this type of assignment.

        :return: The average grade for this type of assignment.
        """
        return self.average

    def set_average(self, average):
        """
        Sets the average grade for this type of assignment.

        :param average: The average grade for this type of assignment.
        """
        self.average = average
        pass

    def get_drop_count(self):
        """
        Get the number of grades to drop for this type of assignment.

        :return: The number of grades to drop for this type of assignment.
        """
        return self.drop_count

    def set_drop_count(self, drop_count):
        """
        Sets the number of grades to drop for this type of assignment.

        :param drop_count: The number of grades to drop for this type of
                           assignment.
        """
        self.drop_count = drop_count
        pass

    pass
