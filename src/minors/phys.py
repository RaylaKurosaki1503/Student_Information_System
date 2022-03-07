"""
Author: Rayla Kurosaki

File: phys.py

Description:
"""
from minors.minor import Minor

dict_prereq = {
    "MATH-181": "Project-Based Calculus I",
    "MATH-182": "Project-Based Calculus II",
    "PHYS-211": "University Physics I",
    "PHYS-212": "University Physics II"
}
dict_req = {
    "PHYS-213": "Modern Physics I",
    "PHYS-283": "Vibrations and Waves"
}
dict_electives = {
    "PHYS-315": "Modern Physics I",
    "PHYS-316": "Advanced Laboratory in Physics",
    "PHYS-365": "Physical Optics",
    "PHYS-377": "Advanced Computational Physics",
    "PHYS-214": "Modern Physics II",
    "PHYS-320": "Mathematical Methods in Physics",
    "PHYS-330": "Classical Mechanics",
    "PHYS-360": "Introduction to Chaotic Dynamics Waves",
    "PHYS-408": "Laser Physics",
    "PHYS-411": "Electricity and Magnetism",
    "PHYS-414": "Quantum Mechanics",
    "PHYS-440": "Thermal and Statistical Physics"
}


class Phys(Minor):
    def __init__(self):
        """
        Create an instance of a Physics minor.
        """
        # Call the super class
        super().__init__("Physics")
        # Initialize the courses that are prerequisites for this minor.
        for id in dict_prereq:
            self.prereq[id] = None
            pass
        # Initialize the courses that are required for this minor.
        for id in dict_req:
            self.req[id] = None
            pass
        # Initialize the courses that are electives for this minor.
        for id in dict_electives:
            self.electives[id] = None
            pass
        pass

    def is_satisfied_prereq(self):
        """
        Determines if the student has passed all the prerequisite courses for
        the Physics minor.

        :return: True if the student has passed all the prerequisite courses
                 for the Physics minor. False otherwise.
        """
        # List of grades that would not satisfy fulfilling the prerequisite
        lst1 = ["D+", "D", "D-", "F", "NE"]
        lst2 = ["F", "NE"]
        # For each prerequisite course
        for course in self.prereq.values():
            # If the student did not get a C- or better in this course
            if course.get_id() in ["MATH-181", "MATH-182", "PHYS-211"]:
                if course.get_final_grade() in lst1:
                    print(f"Prerequisites are not satisfied for the "
                          f"{self.name} minor.")
                    return False
                pass
            # If the student did not get an F or better in this course
            else:
                if course.get_final_grade() in lst2:
                    print(f"Prerequisites are not satisfied for the "
                          f"{self.name} minor.")
                    return False
                pass
            pass
        return True

    def is_satisfied_required(self):
        """
        Determines if the student has passed all the required courses for the
        Physics minor.

        :return: True if the student has passed all the required courses for
                 the Physics minor. False otherwise.
        """
        # List of grades that would not satisfy fulfilling the required course
        lst = ["F", "NE"]
        # For each prerequisite course
        for course in self.req.values():
            # If the student did not pass this course
            if course.get_final_grade() in lst:
                print(f"Required courses are not satisfied for the "
                      f"{self.name} minor.")
                return False
            pass
        return True

    def is_satisfied_electives(self):
        """
        Determines if the student has passed 3 electives for the Physics
        minor with at least one elective from group A and at least one
        elective from group B.

        :return: True if the condition is satisfied. False otherwise.
        """
        # List of grades that would not satisfy fulfilling the required
        # course.
        lst = ["F", "NE"]
        # Courses from group A.
        lst_a = ["PHYS-315", "PHYS-316", "PHYS-365", "PHYS-377"]
        # Courses from group B.
        lst_b = ["PHYS-214", "PHYS-320", "PHYS-330", "PHYS-360", "PHYS-408",
                 "PHYS-411", "PHYS-414", "PHYS-440"]
        # Count the number of courses the student took in each group.
        count_a, count_b = 0, 0
        # For each elective the student took.
        for id, course in self.electives.items():
            # If the student passed the class.
            if course.get_final_grade() not in lst:
                # If the class is in group A.
                if id in lst_a:
                    # Increment the counter by 1 for this group.
                    count_a += 1
                # If the class is in group B.
                else:
                    # Increment the counter by 1 for this group.
                    count_b += 1
        # If the student has taken 3 electives with one of them in group A
        # and at least one in group B.
        if (count_a + count_b >= 3) and ((count_a >= 1) or (count_b >= 1)):
            return True
        # Otherwise, the student has not fulfilled the requirements to earn
        # the Physics minor.
        else:
            return False

    def is_satisfied(self):
        """
        Determines if the student has completed the Physics minor.

        :return: True if the student has completed the Physics minor. False
                 otherwise.
        """
        cond1 = self.is_satisfied_prereq()
        cond2 = self.is_satisfied_required()
        cond3 = self.is_satisfied_electives()
        return cond1 and cond2 and cond3

    pass
