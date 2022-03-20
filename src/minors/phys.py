"""
Author: Rayla Kurosaki

File: phys.py

Description: This file contains the functionality to represent the Physics
             minor. The requirements have been updated on 2022/03/09.
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
        super().__init__("Physics")
        for id in dict_prereq:
            self.prereq[id] = None
            pass
        for id in dict_req:
            self.req[id] = None
            pass
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
        lst1 = ["D+", "D", "D-", "F", "NE"]
        lst2 = ["F", "NE"]
        for course in self.prereq.values():
            if course.get_id() in ["MATH-181", "MATH-182", "PHYS-211"]:
                if course.get_final_grade() in lst1:
                    return False
                pass
            else:
                if course.get_final_grade() in lst2:
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
        lst = ["F", "NE"]
        for course in self.req.values():
            if course.get_final_grade() in lst:
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
        lst = ["F", "NE"]
        lst_a = ["PHYS-315", "PHYS-316", "PHYS-365", "PHYS-377"]
        lst_b = ["PHYS-214", "PHYS-320", "PHYS-330", "PHYS-360", "PHYS-408",
                 "PHYS-411", "PHYS-414", "PHYS-440"]
        count_a, count_b = 0, 0
        for id, course in self.electives.items():
            if course.get_final_grade() not in lst:
                if id in lst_a:
                    count_a += 1
                    pass
                else:
                    count_b += 1
                    pass
                pass
            pass
        if (count_a + count_b >= 3) and ((count_a >= 1) or (count_b >= 1)):
            return True
        else:
            return False
        pass
    pass

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
