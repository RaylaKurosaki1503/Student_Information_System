"""
Author: Rayla Kurosaki

File: Student.py

Description:
"""


class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.gpa = 0.0
        self.gpa_history = {}
        pass

    def get_name(self):
        return self.name

    def get_courses(self):
        return self.courses

    def add_course(self, course):
        self.courses.append(course)
        pass

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        self.gpa = gpa
        pass

    def get_gpa_history(self):
        return self.gpa_history

    def add_to_gpa_history(self, term, gpa):
        self.gpa_history[term] = gpa
        pass

    pass
