###############################################################################
"""
Author: Rayla Kurosaki

File: phase3_print_transcript.py

Description:
"""
###############################################################################
import numpy as np
import copy


def print_boundary(f, lst):
    string = "|"
    for i in range(len(lst)):
        string += "-" * (2 + lst[i])
        if i + 1 == len(lst):
            string += "|"
            pass
        else:
            string += "-"
            pass
        pass
    f.write(string + "\n")
    pass


def print_separator(f, lst):
    string = "|"
    for i in range(len(lst)):
        string += "-" * (2 + lst[i])
        if i + 1 == len(lst):
            string += "|"
            pass
        else:
            string += "+"
            pass
        pass
    f.write(string + "\n")
    pass


def print_row(f, data, lst):
    string = "|"
    for i in range(len(data)):
        e = data[i]
        string += " " + e + " " * (lst[i] - len(e)) + " |"
    f.write(string + "\n")
    pass


def main(student):
    with open("transcript.txt", "w") as f:
        # Set the header of the table
        header = np.array([
            ["Term/Semester", "Course ID", "Course Name", "Raw Grade", "Final Grade"]
        ])
        # Initialize the data to print
        data_to_print = copy.deepcopy(header)

        # iterate through each course
        for course in student.get_courses():
            # Add course data to the list of data to print
            lst = np.array([
                [course.get_term(), course.get_id(), course.get_name(),
                 course.get_raw_grade(), course.get_final_grade()]
            ])
            data_to_print = np.vstack((data_to_print, lst))
            pass
        # Get the shape of the 2-d array
        rows, cols = np.shape(data_to_print)
        curr_term = ""
        max_len = []
        # Get the length of the longest string in each column
        for i in range(cols):
            max_len.append(len(max(data_to_print[:, i], key=len)))
            pass
        # Pretty print the transcript
        print_boundary(f, max_len)
        for i in range(rows):
            row = data_to_print[i]
            if not (curr_term == row[0]):
                if not (curr_term == ""):
                    print_separator(f, max_len)
                    pass
                curr_term = row[0]
                pass
            print_row(f, row, max_len)
            pass
        print_boundary(f, max_len)
        pass
    pass
