"""
Author: Rayla Kurosaki

File: minor.py

Description: This file contains the functionality to represent a minor.
"""

import __utils__ as utils


class Minor:
    def __init__(self, name):
        """
        Create an instance of a minor.
        """
        self.name = name
        self.prereq = {}
        self.req = {}
        self.electives = {}
        self.gpa = -1
        pass

    def get_name(self):
        """
        Gets the name of the minor.

        :return: The name of the minor.
        """
        return self.name

    def get_prereq(self):
        """
        Gets the prerequisite courses for this minor.

        :return: The prerequisite courses for this minor.
        """
        return self.prereq

    def get_req(self):
        """
        Gets the required courses for this minor.

        :return: The required courses for this minor.
        """
        return self.req

    def get_electives(self):
        """
        Get the electives for this minor.

        :return: The electives for this minor.
        """
        return self.electives

    def get_gpa(self):
        """
        Get the GPA for this minor.

        :return: The GPA for this minor.
        """
        return self.gpa

    def filter(self):
        """
        Removes all electives the student did not take to fulfill the minor.
        """
        temp_dict = {}
        for id, course in self.electives.items():
            if course is not None:
                temp_dict[id] = course
                pass
            pass
        self.electives.clear()
        self.electives.update(temp_dict)
        pass

    def compute_gpa(self):
        """
        Computes the GPA for this minor.
        """
        total_earned_credits, total_points = 0.0, 0.0
        for course in self.req.values():
            total_earned_credits += course.get_earned_credit()
            total_points += course.get_points()
            pass
        for course in self.electives.values():
            total_earned_credits += course.get_earned_credit()
            total_points += course.get_points()
            pass
        self.gpa = utils.format_num_3(total_points / total_earned_credits)
        pass

    pass
