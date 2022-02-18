################################################################################
"""
Author: Rayla Kurosaki

File: assignment.py

Description:
"""
################################################################################


class Assignment:
    """

    """
    def __init__(self, type, weight):
        """

        :param type:
        :param weight:
        """
        self.type = type
        self.weight = weight
        self.lst_grades = []
        self.average = -1
        self.drop_count = 0
        pass

    def get_type(self):
        """

        :return:
        """
        return self.type

    def get_weight(self):
        """

        :return:
        """
        return self.weight

    def get_grades(self):
        """

        :return:
        """
        return self.lst_grades

    def add_grade(self, grade):
        """

        :param grade:
        :return:
        """
        self.lst_grades.append(grade)
        pass

    def get_average(self):
        """

        :return:
        """
        return self.average

    def set_average(self, average):
        """

        :param average:
        :return:
        """
        self.average = average
        pass

    def get_drop_count(self):
        """

        :return:
        """
        return self.drop_count

    def add_drop_count(self):
        """

        :return:
        """
        self.drop_count += 1
        pass

    def set_drop_count(self, drop_count):
        """

        :param drop_count:
        :return:
        """
        self.drop_count = drop_count
        pass

    pass


def pp_print(assignment):
    """

    :param assignment:
    :return:
    """
    print([assignment.get_type(), assignment.get_weight(),
           assignment.get_grades(), assignment.get_average(),
           assignment.get_drop_count()])
    pass
