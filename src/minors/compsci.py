"""
Author: Rayla Kurosaki

File: compsci.py

Description: This file contains the functionality to represent the Computer
             Science minor. The requirements have been updated on 2022/03/09.
"""

from minors.minor import Minor

dict_prereq = {
    "CSCI-141": "Computer Science I",
    "CSCI-142": "Computer Science II",
    "MATH-181": "Project-Based Calculus I",
    "MATH-182": "Project-Based Calculus II",
    "MATH-200": "Discrete Mathematics with Introduction to Proofs",
}
dict_req = {
    "CSCI-243": "The Mechanics of Programming"
}
dict_electives = {
    "CSCI-250": "Concepts of Computer Systems",
    "CSCI-251": "Concepts of Parallel and Distributed Systems",
    "CSCI-261": "Analysis of Algorithms",
    "CSCI-262": "Introduction to Computer Science Theory",
    "CSCI-263": "Honors Introduction to Computer Science Theory",
    "CSCI-264": "Honors Analysis of Algorithms",
    "CSCI-320": "Principles of Data Management",
    "CSCI-331": "Introduction to Artificial Intelligence",
    "CSCI-344": "Programming Language Concepts",
    "CSCI-351": "Data Communications and Networks",
    "CSCI-352": "Operating Systems",
    "CSCI-420": "Principles of Data Mining",
    "CSCI-421": "Principles of Database System Implementation",
    "CSCI-431": "Introduction to Computer Vision",
    "CSCI-452": "Systems Programming",
    "CSCI-453": "Computer Architecture",
    "CSCI-455": "Principles of Cybersecurity",
    "CSCI-462": "Introduction to Cryptography",
    "CSCI-464": "Xtreme Theory",
    "CSCI-510": "Introduction to Computer Graphics",
    "CSCI-518": "Collaborative Seminar in Computer Graphics",
    "CSCI-519": "Seminar in Computer Graphics",
    "CSCI-521": "Principles of Data Cleaning and Preparation",
    "CSCI-529": "Seminar in Data Management",
    "CSCI-531": "Introduction to Security Measurement",
    "CSCI-532": "Introduction to Intelligent Security Systems",
    "CSCI-539": "Seminar in Artificial Intelligence",
    "CSCI-541": "Programming Skills",
    "CSCI-549": "Seminar in Languages and Tools",
    "CSCI-559": "Seminar in Systems",
    "CSCI-569": "Seminar in Theory",
    "CSCI-599": "Computer Science Undergraduate Independent Study",
    "CSCI-610": "Foundations of Computer Graphics",
    "CSCI-620": "Introduction to Big Data",
    "CSCI-621": "Foundations of Database System Implementation",
    "CSCI-622": "Data Security and Privacy",
    "CSCI-630": "Foundations of Artificial Intelligence",
    "CSCI-631": "Foundations of Computer Vision",
    "CSCI-632": "Mobile Robot Programming",
    "CSCI-633": "Biologically Inspired Intelligent Systems",
    "CSCI-635": "Introduction to Machine Learning",
    "CSCI-641": "Advanced Programming Skills",
    "CSCI-642": "Secure Coding",
    "CSCI-651": "Foundations of Computer Networks",
    "CSCI-652": "Distributed Systems",
    "CSCI-654": "Foundations of Parallel Computing",
    "CSCI-655": "Foundations of Cybersecurity",
    "CSCI-661": "Foundations of Computer Science Theory",
    "CSCI-662": "Foundations of Cryptography",
    "CSCI-664": "Computational Complexity",
    "CSCI-665": "Foundations of Algorithms",
    "CSCI-711": "Global Illumination",
    "CSCI-712": "Computer Animation: Algorithms and Techniques",
    "CSCI-713": "Applied Perception in Graphics and Visualization",
    "CSCI-714": "Scientific Visualization",
    "CSCI-715": "Applications in Virtual Reality",
    "CSCI-716": "Computational Geometry",
    "CSCI-719": "Topics in Computer Graphics",
    "CSCI-720": "Big Data Analytics",
    "CSCI-721": "Foundations of Data Cleaning and Preparation",
    "CSCI-722": "Data Analytics Cognitive Comp",
    "CSCI-723": "Advanced Database Skills: Graph Databases",
    "CSCI-724": "Web Services and Service Oriented Computing",
    "CSCI-729": "Topics in Data Management",
    "CSCI-731": "Advanced Computer Vision",
    "CSCI-732": "Image Understanding",
    "CSCI-734": "Foundations of Security Measurement and Evaluation",
    "CSCI-735": "Foundations of Intelligent Security Systems",
    "CSCI-736": "Neural Networks and Machine Learning",
    "CSCI-737": "Pattern Recognition",
    "CSCI-739": "Topics in Intelligent Systems",
    "CSCI-740": "Programming Language Theory",
    "CSCI-742": "Compiler Construction",
    "CSCI-746": "Software Development Tools",
    "CSCI-749": "Topics in Languages and Tools",
    "CSCI-759": "Topics in Systems",
    "CSCI-761": "Topics in Advanced Algorithms",
    "CSCI-762": "Advanced Cryptography",
    "CSCI-769": "Topics in Theory"
}


class Compsci(Minor):
    def __init__(self):
        """
        Create an instance of a Computer Science minor.
        """
        # Call the super class
        super().__init__("Computer Science")
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
        the Computer Science minor.

        :return: True if the student has passed all the prerequisite courses
                 for the Computer Science minor. False otherwise.
        """
        # List of grades that would not satisfy fulfilling the prerequisite
        lst1 = ["D+", "D", "D-", "F", "NE"]
        lst2 = ["F", "NE"]
        # For each prerequisite course
        for course in self.prereq.values():
            # If the student did not get a C- or better in this course
            if course.get_id() in ["CSCI-141", "CSCI-142", "MATH-181"]:
                if course.get_final_grade() in lst1:
                    # Return False
                    # print(f"Prerequisites are not satisfied for the "
                    #       f"{self.name} minor.")
                    return False
                pass
            # If the student did not get an F or better in this course
            else:
                if course.get_final_grade() in lst2:
                    # print(f"Prerequisites are not satisfied for the "
                    #       f"{self.name} minor.")
                    return False
                pass
            pass
        return True

    def is_satisfied_required(self):
        """
        Determines if the student has passed all the required courses for the
        Computer Science minor.

        :return: True if the student has passed all the required courses for
                 the Computer Science minor. False otherwise.
        """
        # List of grades that would not satisfy fulfilling the required course
        lst = ["F", "NE"]
        # For each prerequisite course
        for course in self.req.values():
            # If the student did not pass this course
            if course.get_final_grade() in lst:
                # print(f"Required courses are not satisfied for the "
                #       f"{self.name} minor.")
                return False
            pass
        return True

    def is_satisfied_electives(self):
        """
        Determines if the student has passed 3 electives for the Computer
        Science minor.

        :return: True if the student has passed 3 electives for the Computer
                 Science minor. False otherwise.
        """
        # List of grades that would not satisfy fulfilling the required
        # course.
        lst = ["F", "NE"]
        # For each elective the student took.
        for course in self.electives.values():
            # If the student failed the class.
            if course.get_final_grade() in lst:
                return False
            pass
        return True

    def is_satisfied(self):
        """
        Determines if the student has completed the Computer Science minor.

        :return: True if the student has completed the Computer Science minor.
                 False otherwise.
        """
        cond1 = self.is_satisfied_prereq()
        cond2 = self.is_satisfied_required()
        cond3 = self.is_satisfied_electives()
        return cond1 and cond2 and cond3

    pass
