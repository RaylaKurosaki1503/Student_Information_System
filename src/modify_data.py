################################################################################
"""
Author: Rayla Kurosaki

File: modify_data.py

Description:
"""
################################################################################


import special_calculations
import rayla.excel
import helper_functions as hf


def overwrite_final(student, workbook):
    """

    :param student:
    :param workbook:
    :return:
    """
    # Get the worksheet that contains all the types of assignments
    ws = rayla.excel.get_worksheet(workbook, "overwrite_final_exam")
    # Set the index counter
    i = 0
    # Iterate through each row of the worksheet
    for row in ws.values:
        # If it is not the first row
        if not (i == 0):
            # Unpack the row
            term, id, sxn, name = row
            # Iterate through the courses the student has taken
            for course in student.get_courses():
                # If this assignment belongs to this course
                if hf.is_correct_course(term, id + "." + sxn, name, course):
                    # If the course was University Physics 1
                    if course.get_id() == "PHYS-211.04":
                        # Get the exams
                        exams = course.get_assignments()["Exam"]
                        # Get all the exam grades but the final exam and sort
                        # the list in ascending order
                        exam_grades = exams.get_grades()[:-1]
                        exam_grades = sorted(exam_grades, key=lambda x: x[0])
                        # Get the final exam grade
                        final_exam_grade = exams.get_grades()[-1]
                        # If the final exam grade is higher than the lowest exam
                        # grade
                        if final_exam_grade[0] > exam_grades[0][0]:
                            # Replace the lowest exam grade with the final exam
                            # grade
                            exam_grades.pop(0)
                            exam_grades.append(final_exam_grade)
                            pass
                        # Add the final exam to the list of exams
                        exam_grades.append(final_exam_grade)
                        exams.set_grades(exam_grades)
                        pass
                    # If the class was Vibrations and Waves
                    elif course.get_id() == "PHYS-283.01":
                        # Get each exam
                        exam1 = course.get_assignments()["Exam 1"]
                        exam2 = course.get_assignments()["Exam 2"]
                        final_exam = course.get_assignments()["Final Exam"]
                        # Get each exam's grade
                        exam1_grades = exam1.get_grades()
                        exam2_grades = exam2.get_grades()
                        final_exam_grade = final_exam.get_grades()
                        # Replace the lowest exam grade with the final exam
                        # grade
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
                        # Get the exams
                        exams = course.get_assignments()["Exam"]
                        # Get the exam grades and sort it in ascending order
                        exam_grades = exams.get_grades()
                        exam_grades = sorted(exam_grades, key=lambda x: x[0])
                        # Get the final exam
                        final_exam = course.get_assignments()["Final Exam"]
                        # Get the final exam grade
                        final_exam_grade = final_exam.get_grades()
                        # Replace the lowest exam grade with the final exam
                        # grade
                        if final_exam_grade[0][0] > exam_grades[0][0]:
                            exam_grades.pop(0)
                            exam_grades.append(final_exam_grade[0])
                            exams.set_grades(exam_grades)
                        pass
                    pass
                pass
            pass
        # Increment the index counter
        i += 1
        pass
    pass


def drop_grades(student):
    """

    :param student:
    :return:
    """
    # Iterate through each course
    for course in student.get_courses():
        # Iterate through the dictionary of (type, assignment) pairs
        for type, assignment in course.get_assignments().items():
            # If there are grades to drop for this assignment type
            drop = assignment.get_drop_count()
            if not (drop == 0):
                # Drop the lowest n grades
                lst_grades = sorted(assignment.get_grades(), key=lambda x: x[0])
                course.get_assignments()[type].set_grades(lst_grades[drop:])
                pass
            pass
        pass
    pass


def calc_raw_grade(student):
    """

    :param student:
    :return:
    """
    # Iterate through each course
    for course in student.get_courses():
        # If there is only one assignment type (Final Grade)
        if len(course.get_assignments()) == 1:
            # Set the raw course grade as the Final Grade
            assignment = course.get_assignments()["Final Grade"]
            grade = assignment.get_grades()[0]
            course.set_raw_grade(grade)
            pass
        else:
            # Initialize some floating numbers
            course_grade, total_weight = 0.0, 0.0
            # Iterate through each (type, assignmnet) pair in the dictionary
            for type, assignment in course.get_assignments().items():
                # Get the list of grades
                grades = assignment.get_grades()
                # If there are grades
                if not (len(grades) == 0):
                    # Compute the average grade of this assignment type
                    num_lst_grades = [e[0] for e in assignment.get_grades()]
                    grade = sum(num_lst_grades) / len(num_lst_grades)
                    # Set the grade for this assignment type
                    assignment.set_average(grade)
                    # Increase the total weight for raw course grade
                    # computation
                    total_weight += assignment.get_weight()
                    # Increase the raw course grade by the weighted assignment
                    # grade
                    course_grade += grade * assignment.get_weight()
                    pass
                else:  # If there are no grades
                    # Set the average grade as "n/a"
                    assignment.set_average("n/a")
                    pass
                pass
            # Set the raw course grade
            course.set_raw_grade(hf.format_num(course_grade / total_weight))
            pass
        # If the student has earned extra credit, add that amount to the raw
        # grade
        extra_credit = course.get_extra_credit()
        if not (extra_credit == 0):
            raw_grade = course.get_raw_grade() + extra_credit
            if raw_grade > 100:
                raw_grade = 100
                pass
            course.set_raw_grade(raw_grade)
            pass
        pass
    pass


def special_calc(student):
    """

    :param student:
    :return:
    """
    CS1 = ["Lab", "Homework", "Project", "Miscellaneous"]
    CS2 = ["Lab", "Homework", "Project"]
    CS3 = ["Homework", "Project"]
    for course in student.get_courses():
        if course.get_id() == "CSCI-141.02":
            special_calculations.calc_CS(course, CS1)
            pass
        elif course.get_id() == "CSCI-142.01":
            special_calculations.calc_CS(course, CS2)
            pass
        elif course.get_id() == "ENGL-314.01":
            special_calculations.calc_basic(course)
            pass
        elif course.get_id() == "MATH-399.01":
            special_calculations.calc_basic(course)
            pass
        elif course.get_id() == "PHYS-212.06":
            special_calculations.calc_UP2(course)
            pass
        elif course.get_id() == "CSCI-243.01":
            special_calculations.calc_CS(course, CS3)
            pass
        elif course.get_id() == "PHYS-283.01":
            special_calculations.calc_VnW(course)
            pass
        pass
    pass


def raw_letter_grade(student):
    """

    :param student:
    :return:
    """
    # Iterate through each course
    for course in student.get_courses():
        # Get the raw grade for this course
        raw_grade = course.get_raw_grade()
        if hf.is_numeric(raw_grade):
            if course.get_id == "MATH-399.01":
                if raw_grade >= 70:
                    course.set_letter_grade("S (Pass)")
                    pass
                else:
                    course.set_letter_grade("F")
                    pass
                pass
            else:
                # Get the grading scale for this course
                grading_scale = course.get_grading_scale()
                # Set the letter grade for this course
                for letter, num in grading_scale.items():
                    if raw_grade >= num:
                        course.set_letter_grade(letter)
                        break
                        pass
                    pass
                    course.set_letter_grade("F")
                pass
            pass
        else:
            course.set_letter_grade(raw_grade)
            pass
        pass
    pass


def final_grade(student, workbook):
    """

    :param student:
    :param workbook:
    :return:
    """
    # Get the worksheet that contains all the types of assignments
    ws = rayla.excel.get_worksheet(workbook, "overwrite_final_grade")
    # Set the index counter
    i = 0
    # Iterate through each row of the worksheet
    for row in ws.values:
        # If it is not the first row
        if not (i == 0):
            # Unpack the row
            term, id, sxn, name, grade, condition = row
            # Iterate through the courses the student has taken
            for course in student.get_courses():
                # If this assignment belongs to this course
                if hf.is_correct_course(term, id + "." + sxn, name, course):
                    if condition is None:
                        course.set_final_grade(grade)
                        pass
                    else:
                        course.set_final_grade(condition)
                        pass
                    pass
                pass
            pass
        # Increment the index counter
        i += 1
        pass
    pass


def course_gpa_points(student):
    gpa_points = {"A": 4.000, "A-": 3.667,
                  "B+": 3.333, "B": 3.000, "B-": 2.667,
                  "C+": 2.333, "C": 2.000, "C-": 1.667,
                  "D+": 1.333, "D": 1.000, "D-": 1.000,
                  "F": 0.000}
    for course in student.get_courses():
        final_grade = course.get_final_grade()
        credit = course.get_credit()
        if (credit == 0) or (final_grade in ["SE", "NE"]):
            course.set_gpa(0)
            course.set_points(0)
            pass
        else:
            course.set_gpa(gpa_points[final_grade])
            course.set_points(gpa_points[final_grade] * course.get_credit())
            pass
        pass
    pass


def student_gpa_points(student):
    sum_credits, sum_points = 0.0, 0.0
    term_credits, term_points = 0.0, 0.0
    current_term = ""
    for course in student.get_courses():
        course_credit = course.get_credit()
        course_points = course.get_points()
        term = course.get_term()
        if current_term == "":
            current_term = term
        if not (term == current_term):
            student.add_to_gpa_history(term, term_points / term_credits)
            current_term = term
            term_credits = course_credit
            term_points = course_points
            pass
        else:
            term_credits += course_credit
            term_points += course_points
            pass
        sum_credits += course_credit
        sum_points += course_points
        pass
    student.add_to_gpa_history(current_term, term_points / term_credits)
    student.set_gpa(sum_points / sum_credits)


def main(student, workbook):
    overwrite_final(student, workbook)
    drop_grades(student)
    calc_raw_grade(student)
    special_calc(student)
    raw_letter_grade(student)
    final_grade(student, workbook)
    course_gpa_points(student)
    student_gpa_points(student)
    pass
