"""
Author: Rayla Kurosaki

File: major.py

Description: This file contains the functionality to represent a major.
"""

import __utils__ as utils


class Major:
    def __init__(self, name, degree):
        """
        Create an instance of a major.
        """
        self.name = name
        self.degree = degree
        self.gpa = "n/a"
        self.courses = {}
        pass

    def get_name(self):
        """
        Gets the name of the major.

        :return: The name of the major.
        """
        return self.name

    def get_degree(self):
        """
        Gets the degree of the major.

        :return: The degree of the major.
        """
        return self.degree

    def get_gpa(self):
        """
        Get the GPA for this major.

        :return: The GPA for this major.
        """
        return self.gpa

    pass
