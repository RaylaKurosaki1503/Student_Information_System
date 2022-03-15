"""
Author: Rayla Kurosaki

File: student.py

Description: This file contains all the functionality of a student.
"""


class Student:
    def __init__(self, name, majors, minors):
        """
        Creates an instance of a student.

        :param name: Name of the student.
        :param majors: A list of majors/degrees the student wants to earn or
                       has earned.
        :param minors: A list of minors the student wants to earn or has
                       earned.
        """
        self.name = name
        self.majors = majors
        self.minors = minors
        self.courses = []
        self.gpa = 0.0
        self.gpa_history = {}

    def get_name(self):
        """
        Gets the name of the student.

        :return: The name of the student.
        """
        return self.name

    def get_majors(self):
        """
        Gets the student's major(s).

        :return: The student's major(s).
        """
        return self.majors

    def get_minors(self):
        """
        Gets the student's minor(s).

        :return: The student's minor(s).
        """
        return self.minors

    def get_courses(self):
        """
        Gets the list of courses the student has taken.

        :return: A list of courses the student has taken.
        """
        return self.courses

    def add_course(self, course):
        """
        Adds a new course to the list of courses the student has taken.

        :param course: A new course the student has taken.
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
        Get a dictionary which contains the student's GPA for each
        term/semester.

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

    def print_student(self, file):
        """
        Pretty prints the student's basic info.

        :param file: A file to write on.
        """
        file.write(f"Name: {self.name}\n")
        for major in self.majors:
            file.write(f"Major: name (degree_level) [GPA]\n")
            # file.write(f"\tSatisfied: True/False\n")
            pass
        for minor in self.minors.values():
            file.write(f"Minor: {minor.get_name()} [{minor.get_gpa()}]\n")
            file.write(f"\tSatisfied: {minor.is_satisfied()}\n")
            pass
        file.write("\n")
        pass

    pass
