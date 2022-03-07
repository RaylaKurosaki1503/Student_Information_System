"""
Author: Rayla Kurosaki

File: minor.py

Description:
"""
import algorithm as alg


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
        Removes all electives the student did nto take to fulfill the minor.
        """
        # Initialize a temporary dictionary.
        temp_dict = {}
        # For each elective in the minor.
        for id, course in self.electives.items():
            # If the student took the course.
            if course is not None:
                # Add it to the temporary dictionary.
                temp_dict[id] = course
                pass
            pass
        # Clear the electives' dictionary and then update with only the
        # electives the student took.
        self.electives.clear()
        self.electives.update(temp_dict)
        pass

    def compute_gpa(self):
        """
        Computes the GPA for this minor.
        """
        # Initialize the number of earned points and earned credits.
        total_earned_credits, total_points = 0.0, 0.0
        # For each required course.
        for course in self.req.values():
            # Accumulate the credits earned for this course.
            total_earned_credits += course.get_earned_credit()
            # Accumulate the points earned for this course.
            total_points += course.get_points()
            pass
        # For each elective.
        for course in self.electives.values():
            # Accumulate the credits earned for this course.
            total_earned_credits += course.get_earned_credit()
            # Accumulate the points earned for this course.
            total_points += course.get_points()
            pass
        # Compute the GPA for this minor.
        self.gpa = alg.format_num_3(total_points / total_earned_credits)
        pass

    pass
