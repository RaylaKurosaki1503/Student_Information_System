"""
Author: Rayla Kurosaki

File: student.py

Description: This file contains all the functionality of a student.
"""


class Student:
    def __init__(self, name):
        """
        Creates an instance of a student.

        :param name: Name of the student.
        """
        self.name = name
        self.courses = []
        self.gpa = 0.0
        self.gpa_history = {}
        pass

    def get_name(self):
        """
        Gets the name of the student.

        :return: The name of the student.
        """
        return self.name

    def get_courses(self):
        """
        Gets the list of courses the student has taken.

        :return: A list of courses the student has taken
        """
        return self.courses

    def add_course(self, course):
        """
        Adds a new course to the list of courses the student has taken.

        :param course: A new course the student has taken
        """
        self.courses.append(course)
        pass

    def get_gpa(self):
        """
        Gets the student's current GPA.

        :return: The student's current GPA.
        """
        return self.gpa

    def set_gpa(self, gpa):
        """
        Sets the student's current GPA.

        :param gpa: The student's current GPA.
        """
        self.gpa = gpa
        pass

    def get_gpa_history(self):
        """
        Get a dictionary which contains the student's GPA for each term/semester.

        :return: A dictionary which contains the student's GPA for each
                 term/semester.
        """
        return self.gpa_history

    def add_to_gpa_history(self, term, gpa):
        """
        Adds a term-GPA pair to the student's database.

        :param term: The term the student earn their GPA in.
        :param gpa: The GPA the student earned in a specific semester.
        """
        self.gpa_history[term] = gpa
        pass

    def print_student(self):
        """
        Pretty prints the student's basic info.
        """
        print(f"Name: {self.name}")
        pass

    pass
