"""
Author: Rayla Kurosaki

File: Course.py

Description:
"""


class Course:
    def __init__(self, term, id, name, credit, prof):
        self.term = term
        self.id = id
        self.name = name
        self.credit = credit
        self.prof = prof
        self.assignments = {}
        self.extra_credit = 0
        self.raw_grade = -1
        self.letter_grade = "n/a"
        self.final_grade = "n/a"
        self.gpa = -1
        self.points = -1
        pass

    def get_term(self):
        return self.term

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_credit(self):
        return self.credit

    def get_prof(self):
        return self.prof

    def get_assignments(self):
        return self.assignments

    def add_assignment(self, type, assignment):
        self.assignments[type] = assignment
        pass

    def get_extra_credit(self):
        return self.extra_credit

    def set_extra_credit(self, extra_credit):
        self.extra_credit = extra_credit
        pass

    def get_raw_grade(self):
        return self.raw_grade

    def set_raw_grade(self, grade):
        self.raw_grade = grade
        pass

    def get_letter_grade(self):
        return self.letter_grade

    def set_letter_grade(self, letter):
        self.letter_grade = letter
        pass

    def get_final_grade(self):
        return self.final_grade

    def set_final_grade(self, letter):
        self.final_grade = letter
        pass

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        self.gpa = gpa
        pass

    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points

    pass


def pp_print(course):
    print([course.get_term(), course.get_id(), course.get_name(),
           course.get_credit(), course.get_assignments()])
    pass
