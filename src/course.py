################################################################################
"""
Author: Rayla Kurosaki

File: Course.py

Description:
"""
################################################################################


class Course:
    """

    """

    def __init__(self, term, id, name, credit, prof):
        """

        :param term:
        :param id:
        :param name:
        :param credit:
        :param prof:
        """
        self.term = term
        self.id = id
        self.name = name
        self.credit = credit
        self.prof = prof
        self.grading_scale = {}
        self.assignments = {}
        self.extra_credit = 0
        self.raw_grade = -1
        self.letter_grade = "n/a"
        self.final_grade = "n/a"
        self.gpa = -1
        self.points = -1
        pass

    def get_term(self):
        """

        :return:
        """
        return self.term

    def get_id(self):
        """

        :return:
        """
        return self.id

    def get_name(self):
        """

        :return:
        """
        return self.name

    def get_credit(self):
        """

        :return:
        """
        return self.credit

    def get_prof(self):
        """

        :return:
        """
        return self.prof

    def get_grading_scale(self):
        """

        :return:
        """
        return self.grading_scale

    def set_grading_scale(self, grading_scale):
        """

        :param letter:
        :param num:
        :return:
        """
        self.grading_scale = grading_scale
        pass

    def get_assignments(self):
        """

        :return:
        """
        return self.assignments

    def add_assignment(self, type, assignment):
        self.assignments[type] = assignment
        pass

    def get_extra_credit(self):
        """

        :return:
        """
        return self.extra_credit

    def add_extra_credit(self, extra_credit):
        """

        :param extra_credit:
        :return:
        """
        self.extra_credit += extra_credit
        pass

    def set_extra_credit(self, extra_credit):
        """

        :param extra_credit:
        :return:
        """
        self.extra_credit = extra_credit
        pass

    def get_raw_grade(self):
        """

        :return:
        """
        return self.raw_grade

    def set_raw_grade(self, grade):
        """

        :param grade:
        :return:
        """
        self.raw_grade = grade
        pass

    def get_letter_grade(self):
        """

        :return:
        """
        return self.letter_grade

    def set_letter_grade(self, letter):
        """

        :param letter:
        :return:
        """
        self.letter_grade = letter
        pass

    def get_final_grade(self):
        """

        :return:
        """
        return self.final_grade

    def set_final_grade(self, letter):
        """

        :param letter:
        :return:
        """
        self.final_grade = letter
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

    def get_points(self):
        """

        :return:
        """
        return self.points

    def set_points(self, points):
        """

        :param points:
        :return:
        """
        self.points = points

    pass
