################################################################################
"""
Author: Rayla Kurosaki

File: Assignment.py

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

    def set_grades(self, grades):
        """

        :return:
        """
        self.lst_grades = grades
        pass

    def add_grade(self, grade_str):
        """

        :param grade_str:
        :return:
        """
        if "/" in grade_str:
            num, denom = grade_str.split(" / ")
            grade_num = 100 * float(num) / float(denom)
            self.lst_grades.append([grade_num, grade_str])
        else:
            self.lst_grades.append(grade_str)
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
