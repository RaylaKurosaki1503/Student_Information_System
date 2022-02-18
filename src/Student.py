################################################################################
"""
Author: Rayla Kurosaki

File: student.py

Description:
"""
################################################################################


class Student:
    """

    """

    def __init__(self, name):
        """

        :param name:
        """
        self.name = name
        self.courses = []
        self.gpa = 0.0
        self.gpa_history = {}
        pass

    def get_name(self):
        """

        :return:
        """
        return self.name

    def get_courses(self):
        """

        :return:
        """
        return self.courses

    def add_course(self, course):
        """

        :param course:
        :return:
        """
        self.courses.append(course)
        pass

    def get_gpa(self):
        """

        :return:
        """
        return self.gpa

    def set_gpa(self, gpa):
        """

        :param gpa:
        :return:
        """
        self.gpa = gpa
        pass

    def get_gpa_history(self):
        """

        :return:
        """
        return self.gpa_history

    def add_to_gpa_history(self, term, gpa):
        """

        :param term:
        :param gpa:
        :return:
        """
        self.gpa_history[term] = gpa
        pass

    pass
