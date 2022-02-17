"""
Author: Rayla Kurosaki

File: Course.py

Description:
"""


class Assignment:
    def __init__(self, type, weight):
        self.type = type
        self.weight = weight
        self.lst_grades = []
        self.average = -1
        self.drop_count = 0
        pass

    def get_type(self):
        return self.type

    def get_weight(self):
        return self.weight

    def get_grades(self):
        return self.lst_grades

    def add_grade(self, grade):
        self.lst_grades.append(grade)
        pass

    def get_average(self):
        return self.average

    def set_average(self, average):
        self.average = average
        pass

    def get_drop_count(self):
        return self.drop_count

    def add_drop_count(self):
        self.drop_count += 1
        pass

    def set_drop_count(self, d):
        self.drop_count = d
        pass

    pass


def pp_print(assignment):
    print([assignment.get_type(), assignment.get_weight(),
           assignment.get_grades(), assignment.get_average(),
           assignment.get_drop_count()])
    pass
