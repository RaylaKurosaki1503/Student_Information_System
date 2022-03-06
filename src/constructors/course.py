"""
Author: Rayla Kurosaki

File: course.py

Description: This file contains all the functionality of a course.
"""


class Course:
    def __init__(self, term, id, sxn, name, credit, prof):
        """
        Creates an instance of a course.

        :param term: The semester/term that this course was taken.
        :param id: The course ID.
        :param sxn: The course section.
        :param name: THe course name.
        :param credit: The number of credits a student can earn for this course.
        :param prof: The name of the professor that taught this course.
        """
        self.term = term
        self.id = id
        self.sxn = sxn
        self.name = name
        self.credit = credit
        self.earned_credit = 0
        self.prof = prof
        self.grading_scale = {}
        self.assignments = {}
        self.extra_credit = 0
        self.raw_grade = -1
        self.letter_grade = "n/a"
        self.final_grade = "n/a"
        self.points = -1

    def get_term(self):
        """
        Gets the semester/term the course was taken.

        :return: The semester/term the course was taken.
        """
        return self.term

    def get_id(self):
        """
        Gets the course ID of this course.

        :return: The course ID of this course.
        """
        return self.id

    def get_section(self):
        """
        Gets the course section of this course.

        :return: The course section of this course.
        """
        return self.sxn

    def get_name(self):
        """
        Gets the name of this course.

        :return: The name of this course.
        """
        return self.name

    def get_credit(self):
        """
        Gets the number of credits a student can earn for this course.

        :return: The number of credits a student can earn for this course.
        """
        return self.credit

    def get_earned_credit(self):
        """
        Gets the number of credits the student has earned for this course.

        :return: The number of credits the student has earned for this course.
        """
        return self.earned_credit

    def set_earned_credit(self, earned_credit):
        """
        Sets the number of credits the student has earned for this course.
        """
        self.earned_credit = earned_credit
        pass

    def get_prof(self):
        """
        Gets the name of the professor that taught this course.

        :return: The name of the professor that taught this course.
        """
        return self.prof

    def get_grading_scale(self):
        """
        Gets the professor's grading scale for this course.

        :return: The professor's grading scale for this course.
        """
        return self.grading_scale

    def set_grading_scale(self, grading_scale):
        """
        Sets the professor's grading scale for this course.

        :param grading_scale: The professor's grading scale for this course.
        """
        self.grading_scale = grading_scale
        pass

    def get_assignments(self):
        """
        Gets all the assignments the student did for this course.

        :return: The assignments the student did for this course.
        """
        return self.assignments

    def add_assignment(self, type, assignment):
        """
        Add a new type of assignment for the course.

        :param type: The type of assignment.
        :param assignment: A new assignment.
        """
        self.assignments[type] = assignment
        pass

    def get_extra_credit(self):
        """
        Get the extra credit the student has earned for this course.

        :return: The extra credit the student has earned for this course.
        """
        return self.extra_credit

    def add_extra_credit(self, extra_credit):
        """
        Adds extra credit the student has earned for this course.

        :param extra_credit: Extra credit the student has earned.
        """
        self.extra_credit += extra_credit
        pass

    def get_raw_grade(self):
        """
        Gets the raw grade the student has earned for this course.

        :return: The raw grade the student has earned for this course.
        """
        return self.raw_grade

    def set_raw_grade(self, grade):
        """
        Sets the raw grade the student has earned for this course.

        :param grade: The raw grade the student has earned for this course.
        """
        self.raw_grade = grade
        pass

    def get_letter_grade(self):
        """
        Get the letter grade the student has earned for this course.

        :return: The letter grade the student has earned for this course.
        """
        return self.letter_grade

    def set_letter_grade(self, letter):
        """
        Sets the letter grade the student has earned for this course.

        :param letter: The letter grade the student has earned for this course.
        """
        self.letter_grade = letter
        pass

    def get_final_grade(self):
        """
        Get the final grade the student has earned for this course.

        :return: The final grade the student has earned for this course.
        """
        return self.final_grade

    def set_final_grade(self, letter):
        """
        Sets the final grade the student has earned for this course.

        :param letter: The final grade the student has earned for this course.
        """
        self.final_grade = letter
        pass

    def get_points(self):
        """
        Gets the points the student has earned for this course.

        :return: The points the student has earned for this course.
        """
        return self.points

    def set_points(self, points):
        """
        Sets the points the student has earned for this course.

        :param points: The points the student has earned for this course.
        """
        self.points = points

    pass
