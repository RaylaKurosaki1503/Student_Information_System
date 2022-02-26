"""
Author: Rayla Kurosaki

File: phase2_modify_data.py

Description: This file contains all the functionality of modifying data from
             the Microsoft Excel Workbook/Spreadsheet to the student's database.
"""

import rayla.excel
from algorithm import helper_functions as hf
from algorithm import special_calculations as sc
import copy


def modify_other(student):
    """
    Performs some extra data manipulation for a specific professor teaching
    specific courses.

    :param student: The student to manipulate.
    """
    # Iterate through the courses.
    for course in student.get_courses():
        # If a specific professor is teaching specific courses.
        c1 = course.get_prof() == "Dawn Hollenbeck"
        c2 = course.get_id() == "PHYS-320.01"
        c3 = course.get_id() == "PHYS-321.01"
        if c1 and (c2 or c3):
            # Create a new assignment type that combines homeworks and quizzes.
            assignments = course.get_assignments()
            lst = copy.deepcopy(assignments["Homework"].get_grades())
            temp = copy.deepcopy(assignments["Quiz"].get_grades())
            for e in temp:
                lst.append(e)
                pass
            # Add this new type of assignment.
            assignment = assignments["Homework and Quiz"]
            assignment.set_grades(lst)
            pass
        pass
    pass


def overwrite_final_exam(student, workbook):
    """
    Overwrites exam grades under certain conditions and for certain courses.

    :param student: The student to manipulate.
    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse through.
    """
    # Get the worksheet that contains all the types of assignments.
    ws = rayla.excel.get_worksheet(workbook, "overwrite_final_exam")
    # Iterate through each row of the worksheet.
    for i, row in enumerate(ws.values):
        # If it is not the first row.
        if not (i == 0):
            # Unpack the row.
            term, id, sxn, name = row
            # Iterate through the courses the student has taken.
            for course in student.get_courses():
                # If this assignment belongs to this course.
                if hf.is_correct_course(term, id + "." + sxn, name, course):
                    # If the course was University Physics 1.
                    if course.get_id() == "PHYS-211.04":
                        # Get the exams.
                        exams = course.get_assignments()["Exam"]
                        # Get all the exam grades but the final exam and sort
                        # the list in ascending order.
                        exam_grades = exams.get_grades()[:-1]
                        exam_grades = sorted(exam_grades, key=lambda x: x[0])
                        # Get the final exam grade.
                        final_exam_grade = exams.get_grades()[-1]
                        # If the final exam grade is higher than the lowest exam
                        # grade.
                        if final_exam_grade[0] > exam_grades[0][0]:
                            # Replace the lowest exam grade with the final exam
                            # grade.
                            exam_grades.pop(0)
                            exam_grades.append(final_exam_grade)
                            pass
                        # Add the final exam to the list of exams.
                        exam_grades.append(final_exam_grade)
                        exams.set_grades(exam_grades)
                        pass
                    # If the class was Vibrations and Waves.
                    elif course.get_id() == "PHYS-283.01":
                        # Get each exam.
                        exam1 = course.get_assignments()["Exam 1"]
                        exam2 = course.get_assignments()["Exam 2"]
                        final_exam = course.get_assignments()["Final Exam"]
                        # Get each exam's grade.
                        exam1_grades = exam1.get_grades()
                        exam2_grades = exam2.get_grades()
                        final_exam_grade = final_exam.get_grades()
                        # Replace the lowest exam grade with the final exam
                        # grade.
                        if exam1_grades[0][0] < exam2_grades[0][0]:
                            if final_exam_grade[0][0] > exam1_grades[0][0]:
                                exam1.set_grades(final_exam_grade)
                                pass
                        else:
                            if final_exam_grade[0][0] > exam2_grades[0][0]:
                                exam2.set_grades(final_exam_grade)
                                pass
                            pass
                        pass
                    else:
                        # Get the exams.
                        exams = course.get_assignments()["Exam"]
                        # Get the exam grades and sort it in ascending order.
                        exam_grades = exams.get_grades()
                        exam_grades = sorted(exam_grades, key=lambda x: x[0])
                        # Get the final exam.
                        final_exam = course.get_assignments()["Final Exam"]
                        # Get the final exam grade.
                        final_exam_grade = final_exam.get_grades()
                        # Replace the lowest exam grade with the final exam
                        # grade.
                        if final_exam_grade[0][0] > exam_grades[0][0]:
                            exam_grades.pop(0)
                            exam_grades.append(final_exam_grade[0])
                            exams.set_grades(exam_grades)
                        pass
                    pass
                pass
            pass
        pass
    pass


def drop_grades(student):
    """
    Drop the lowest X grades for certain courses. The number of grades to drop
    also depend on the course.

    :param student: The student to manipulate.
    """
    # Iterate through each course.
    for course in student.get_courses():
        # Iterate through the dictionary of (type, assignment) pairs.
        for type, assignment in course.get_assignments().items():
            # If there are grades to drop for this assignment type.
            drop = assignment.get_drop_count()
            if not (drop == 0):
                # Drop the lowest n grades.
                lst_grades = sorted(assignment.get_grades(), key=lambda x: x[0])
                course.get_assignments()[type].set_grades(lst_grades[drop:])
                pass
            pass
        pass
    pass


def calc_raw_grade(student):
    """
    Computes the raw grade for each course.

    :param student: The student to manipulate.
    """
    # Iterate through each course.
    for course in student.get_courses():
        # If there is only one assignment type (Final Grade).
        if len(course.get_assignments()) == 1:
            # Set the raw course grade as the Final Grade.
            grade = course.get_assignments()["Final Grade"].get_grades()[0]
            course.set_raw_grade(grade)
            pass
        else:
            # Initialize some floating numbers.
            course_grade, total_weight = 0.0, 0.0
            # Iterate through each (type, assignment) pair in the dictionary.
            for type, assignment in course.get_assignments().items():
                # Get the list of grades.
                grades = assignment.get_grades()
                # If there are grades.
                if not (len(grades) == 0):
                    # Compute the average grade of this assignment type.
                    num_lst_grades = [e[0] for e in assignment.get_grades()]
                    grade = sum(num_lst_grades) / len(num_lst_grades)
                    # Set the grade for this assignment type.
                    assignment.set_average(grade)
                    # Increase the total weight for raw course grade
                    # computation.
                    total_weight += assignment.get_weight()
                    # Increase the raw course grade by the weighted assignment
                    # grade.
                    course_grade += grade * assignment.get_weight()
                    pass
                # If there are no grades.
                else:
                    # Set the average grade as "n/a".
                    assignment.set_average("n/a")
                    pass
                pass
            # If there is no weight.
            if total_weight == 0:
                # Then there is no grade.
                grade = "n/a"
                pass
            else:
                # Otherwise, compute the raw grade.
                grade = hf.format_num_2(course_grade / total_weight)
                pass
            # Set the raw course grade.
            course.set_raw_grade(grade)
            pass
        # If the student has earned extra credit.
        extra_credit = course.get_extra_credit()
        if not (extra_credit == 0):
            # Add that amount to the raw grade.
            raw_grade = course.get_raw_grade() + extra_credit
            # If the grade goes above 100.
            if raw_grade > 100:
                # limit the raw grade to 100.
                raw_grade = 100
                pass
            # Set the raw grade.
            course.set_raw_grade(raw_grade)
            pass
        pass
    pass


def special_calc(student):
    """
    Some courses/professors choose to have different method/algorithm to
    determine how to calculate the student's raw grade.

    :param student: The student to manipulate.
    """
    # Initialize some lists.
    CS1 = ["Lab", "Homework", "Project", "Miscellaneous"]
    CS2 = ["Lab", "Homework", "Project"]
    CS3 = ["Homework", "Project"]
    # Iterate through each course.
    for course in student.get_courses():
        # Match the course ID and compute the new raw grade for that course.
        match course.get_id():
            case "CSCI-141.02":
                sc.calc_CS(course, CS1)
            case "CSCI-142.01":
                sc.calc_CS(course, CS2)
            case "ENGL-314.01":
                sc.calc_basic(course)
            case "MATH-399.01":
                sc.calc_basic(course)
            case "PHYS-212.06":
                sc.calc_UP2(course)
            case "CSCI-243.01":
                sc.calc_CS(course, CS3)
            case "PHYS-283.01":
                sc.calc_VnW(course)
        pass
    pass


def raw_letter_grade(student):
    """
    Compute the letter grade for each course based on the professors' grading
    scale for that course.

    :param student: The student to manipulate.
    """
    # Iterate through each course.
    for course in student.get_courses():
        # Get the raw grade for this course.
        raw_grade = course.get_raw_grade()
        # If the raw grade is numeric.
        if hf.is_numeric(raw_grade):
            # For the special case with Math Job Seminar.
            if course.get_id == "MATH-399.01":
                # If the numeric grade is above 70.
                if raw_grade >= 70:
                    # The student passes.
                    course.set_letter_grade("S (Pass)")
                    course.set_final_grade("S (Pass)")
                    pass
                else:
                    # Otherwise, the student fails.
                    course.set_letter_grade("F")
                    course.set_final_grade("F")
                    pass
                pass
            # For all other courses with a numeric raw grade.
            else:
                # Get the grading scale for this course.
                grading_scale = course.get_grading_scale()
                # Set the letter grade for this course.
                for letter, num in grading_scale.items():
                    if raw_grade >= num:
                        course.set_letter_grade(letter)
                        course.set_final_grade(letter)
                        break
                    pass
                    course.set_letter_grade("F")
                    course.set_final_grade("F")
                pass
            pass
        else:
            # For non-numeric raw grades, set the letter and final grades as the
            # raw grade.
            course.set_letter_grade(raw_grade)
            course.set_final_grade(raw_grade)
            pass
        pass
    pass


def overwrite_final_grade(student, workbook):
    """
    Overwrites the final grade that best reflects the data from SIS.

    :param student: The student to manipulate.
    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse through.
    """
    # Get the worksheet that contains all the types of assignments.
    ws = rayla.excel.get_worksheet(workbook, "overwrite_final_grade")
    # Iterate through each row of the worksheet.
    for i, row in enumerate(ws.values):
        # If it is not the first row.
        if not (i == 0):
            # Unpack the row.
            term, id, sxn, name, grade, condition = row
            # Iterate through the courses the student has taken.
            for course in student.get_courses():
                # If this assignment belongs to this course.
                if hf.is_correct_course(term, id + "." + sxn, name, course):
                    # If there is no special condition.
                    if condition is None:
                        # Set the grade as the final grade.
                        course.set_final_grade(grade)
                        pass
                    else:
                        # Set the special condition as the final grade.
                        course.set_final_grade(condition)
                        pass
                    pass
                pass
            pass
        pass
    pass


def credit_earned(student):
    """
    Compute the amount of credit the student has earned for each course.

    :param student: The student to manipulate.
    """
    # Iterate through each course.
    for course in student.get_courses():
        # If the student did not fail the course.
        if not (course.get_final_grade() in ["F", "NE"]):
            # Set the number of earned credits for that course.
            course.set_earned_credit(course.get_credit())
            pass
        pass
    pass


def course_gpa_points(student):
    """
    Computes the points for each course the student has taken.

    :param student: The student to manipulate.
    """
    # Initialize a dictionary of (letter grade, gpa) pairs.
    gpa_points = {
        "A": hf.format_num_3(12 / 3),
        "A-": hf.format_num_3(11 / 3),
        "B+": hf.format_num_3(10 / 3),
        "B": hf.format_num_3(9 / 3),
        "B-": hf.format_num_3(8 / 3),
        "C+": hf.format_num_3(7 / 3),
        "C": hf.format_num_3(6 / 3),
        "C-": hf.format_num_3(5 / 3),
        "D+": hf.format_num_3(4 / 3),
        "D": hf.format_num_3(3 / 3),
        "D-": hf.format_num_3(3 / 3),
        "F": hf.format_num_3(0 / 3)
    }
    # Iterate through each course.
    for course in student.get_courses():
        # If there is no grade for this course.
        if course.get_final_grade() == "n/a":
            # Then there is no GPA for this course.
            course.set_points("n/a")
            pass
        else:
            # Get the final grade and the number of credits earned.
            final_grade = course.get_final_grade()
            earned_credit = course.get_earned_credit()
            # If the number of credits earned is 0 or if the final grade is
            # SE/NE.
            if (earned_credit == 0) or (final_grade in ["SE", "NE"]):
                # Set the points earned for that course to be 0.
                course.set_points(hf.format_num_3(0 / 3))
                pass
            else:
                # Otherwise, compute the number of points the student has
                # earned for this course.
                num = gpa_points[final_grade] * course.get_credit()
                course.set_points(hf.format_num_3(num))
                pass
            pass
        pass
    pass


def student_gpa_points(student):
    """
    Compute the student's current GPA and record the student's semester/term
    GPA.

    :param student: The student to manipulate.
    """
    # Initialize cumulative variables.
    sum_credits, sum_points = 0.0, 0.0
    # Initialize semester variables.
    term_credits, term_points = 0.0, 0.0
    # Initialize the current semester.
    current_term = ""
    # Iterate through the courses.
    for course in student.get_courses():
        # If there is a grade.
        if not (course.get_final_grade() == "n/a"):
            # If the grade is SE/PE/UE.
            if course.get_final_grade() in ["SE", "PE", "UE"]:
                # Set the credit and points to 0.
                course_credit = 0
                course_points = 0
                pass
            else:
                # Get the course points.
                course_points = course.get_points()
                # Get the course earned credits.
                course_credit = course.get_earned_credit()
                pass
            # Get the semester.
            term = course.get_term()
            # If this is a new semester, and it is the first semester.
            if current_term == "":
                # Set the current semester as the semester.
                current_term = term
            # If this is a new semester, and it is not the first semester.
            if not (term == current_term):
                # Compute the semester GPA.
                term_gpa = hf.format_num_2(term_points / term_credits)
                # Add this record to the history of GPAs.
                student.add_to_gpa_history(current_term, term_gpa)
                # Set the current semester as the semester.
                current_term = term
                # Re-initialize the semester credits and semester points.
                term_credits = course_credit
                term_points = course_points
                pass
            else:
                # Cumulatively add the semester credits and semester points.
                term_credits += course_credit
                term_points += course_points
                pass
            # Cumulatively add the cumulative credits and cumulative points.
            sum_credits += course_credit
            sum_points += course_points
            pass
        pass
    # Compute the current semester GPA.
    term_gpa = hf.format_num_2(term_points / term_credits)
    # Add the current semester GPA to the history of GPAs.
    student.add_to_gpa_history(current_term, term_gpa)
    # Set the student's cumulative GPA.
    student.set_gpa(hf.format_num_2(sum_points / sum_credits))
    pass


def main(student, workbook):
    """
    The main function to call the functions above to perform computations and
    modify the student's database.

    :param student: The student to manipulate.
    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse through.
    """
    # Performs some extra data manipulation.
    modify_other(student)

    # Overwrite the exam grades for some classes.
    overwrite_final_exam(student, workbook)

    # Drop grades for some classes.
    drop_grades(student)

    # Compute the raw grade for all courses.
    calc_raw_grade(student)

    # Perform special calculations to calculate the raw grade for specific
    # courses.
    special_calc(student)

    # Determine the letter grade based ont eh raw grade and the grading scale.
    raw_letter_grade(student)

    # Overwrite the final grade for each class.
    overwrite_final_grade(student, workbook)

    # Compute the number of credits earned.
    credit_earned(student)

    # Compute course points.
    course_gpa_points(student)

    # Compute student's GPAs.
    student_gpa_points(student)
    pass
