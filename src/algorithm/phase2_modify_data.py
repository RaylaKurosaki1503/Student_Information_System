"""
Author: Rayla Kurosaki

File: phase2_modify_data.py

Description: This file contains all the functionality of modifying data from
             the Microsoft Excel Workbook/Spreadsheet to the student's
             database.
"""

import copy

import __utils__ as utils


def modify_other(student):
    """
    Performs some extra data manipulation for a specific professor teaching
    specific courses.

    :param student: The student to manipulate.
    """
    for course in student.get_courses():
        c1a = course.get_term() == "2019-2020 Fall"
        c1b = course.get_id() == "PHYS-320"
        c1c = course.get_section() == "01"
        c2a = course.get_term() == "2019-2020 Spring"
        c2b = course.get_id() == "PHYS-321"
        c2c = course.get_section() == "01"
        if (c1a and c1b and c1c) or (c2a and c2b and c2c):
            assignments = course.get_assignments()
            lst = copy.deepcopy(assignments["Homework"].get_grades())
            temp = copy.deepcopy(assignments["Quiz"].get_grades())
            for e in temp:
                lst.append(e)
                pass
            assignment = assignments["Homework and Quiz"]
            assignment.set_grades(lst)
            pass
        pass
    pass


def overwrite_final_exam(student, workbook):
    """
    Overwrites exam grades under certain conditions and for certain courses.

    :param student: The student to manipulate.
    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse
                     through.
    """
    ws = utils.get_worksheet(workbook, "overwrite_final_exam")
    for i, row in enumerate(ws.values):
        if not (i == 0):
            term, id, sxn, name = row
            for course in student.get_courses():
                if utils.is_correct_course(term, id, sxn, name, course):
                    if course.get_id() == "PHYS-211":
                        exams = course.get_assignments()["Exam"]
                        exam_grades = exams.get_grades()[:-1]
                        exam_grades = sorted(exam_grades, key=lambda x: x[0])
                        final_exam_grade = exams.get_grades()[-1]
                        if final_exam_grade[0] > exam_grades[0][0]:
                            exam_grades.pop(0)
                            exam_grades.append(final_exam_grade)
                            pass
                        exam_grades.append(final_exam_grade)
                        exams.set_grades(exam_grades)
                        pass
                    elif course.get_id() == "PHYS-283":
                        exam1 = course.get_assignments()["Exam 1"]
                        exam2 = course.get_assignments()["Exam 2"]
                        final_exam = course.get_assignments()["Final Exam"]
                        exam1_grades = exam1.get_grades()
                        exam2_grades = exam2.get_grades()
                        final_exam_grade = final_exam.get_grades()
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
                        exams = course.get_assignments()["Exam"]
                        exam_grades = exams.get_grades()
                        exam_grades = sorted(exam_grades, key=lambda x: x[0])
                        final_exam = course.get_assignments()["Final Exam"]
                        final_exam_grade = final_exam.get_grades()
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
    Drop the lowest X grades for certain courses. The number of grades to
    drop also depend on the course.

    :param student: The student to manipulate.
    """
    for course in student.get_courses():
        for type, assignment in course.get_assignments().items():
            drop = assignment.get_drop_count()
            if not (drop == 0):
                lst_grades = sorted(assignment.get_grades(),
                                    key=lambda x: x[0])
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
    for course in student.get_courses():
        if len(course.get_assignments()) == 1:
            grade = course.get_assignments()["Final Grade"].get_grades()[0]
            course.set_raw_grade(grade)
            pass
        else:
            course_grade, total_weight = 0.0, 0.0
            for type, assignment in course.get_assignments().items():
                grades = assignment.get_grades()
                if not (len(grades) == 0):
                    num_lst_grades = [e[0] for e in assignment.get_grades()]
                    grade = sum(num_lst_grades) / len(num_lst_grades)
                    assignment.set_average(grade)
                    total_weight += assignment.get_weight()
                    course_grade += grade * assignment.get_weight()
                    pass
                else:
                    assignment.set_average("n/a")
                    pass
                pass
            if total_weight == 0:
                grade = "n/a"
                pass
            else:
                grade = utils.format_num_2(course_grade / total_weight)
                pass
            course.set_raw_grade(grade)
            pass
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
    Some courses/professors choose to have different method/algorithm to
    determine how to calculate the student's raw grade.

    :param student: The student to manipulate.
    """
    CS1 = ["Lab", "Homework", "Project", "Miscellaneous"]
    CS2 = ["Lab", "Homework", "Project"]
    CS3 = ["Homework", "Project"]
    for course in student.get_courses():
        match course.get_id():
            case "CSCI-141.02":
                utils.calc_CS(course, CS1)
            case "CSCI-142.01":
                utils.calc_CS(course, CS2)
            case "ENGL-314.01":
                utils.calc_basic(course)
            case "MATH-399.01":
                utils.calc_basic(course)
            case "PHYS-212.06":
                utils.calc_UP2(course)
            case "CSCI-243.01":
                utils.calc_CS(course, CS3)
            case "PHYS-283.01":
                utils.calc_VnW(course)
        pass
    pass


def raw_letter_grade(student):
    """
    Compute the letter grade for each course based on the professors' grading
    scale for that course.

    :param student: The student to manipulate.
    """
    for course in student.get_courses():
        raw_grade = course.get_raw_grade()
        if utils.is_numeric(raw_grade):
            if course.get_id == "MATH-399.01":
                if raw_grade >= 70:
                    course.set_letter_grade("S (Pass)")
                    course.set_final_grade("S (Pass)")
                    pass
                else:
                    course.set_letter_grade("F")
                    course.set_final_grade("F")
                    pass
                pass
            else:
                grading_scale = course.get_grading_scale()
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
            course.set_letter_grade(raw_grade)
            course.set_final_grade(raw_grade)
            pass
        pass
    pass


def overwrite_final_grade(student, workbook):
    """
    Overwrites the final grade that best reflects the data from SIS.

    :param student: The student to manipulate.
    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse
                     through.
    """
    ws = utils.get_worksheet(workbook, "overwrite_final_grade")
    for i, row in enumerate(ws.values):
        if not (i == 0):
            term, id, sxn, name, grade, condition = row
            for course in student.get_courses():
                if utils.is_correct_course(term, id, sxn, name, course):
                    if condition is None:
                        course.set_final_grade(grade)
                        pass
                    else:
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
    for course in student.get_courses():
        if not (course.get_final_grade() in ["F", "NE"]):
            course.set_earned_credit(course.get_credit())
            pass
        pass
    pass


def course_units(student):
    """
    Compute the amount of units the student has earned for each course.

    :param student: The student to manipulate.
    """
    for course in student.get_courses():
        if course.get_final_grade() in ["SE", "PE"]:
            course.set_units(0)
            pass
        else:
            course.set_units(course.get_earned_credit())
            pass
        pass
    pass


def course_gpa_points(student):
    """
    Computes the points for each course the student has taken.

    :param student: The student to manipulate.
    """
    gpa_points = {
        "A": utils.format_num_3(12 / 3),
        "A-": utils.format_num_3(11 / 3),
        "B+": utils.format_num_3(10 / 3),
        "B": utils.format_num_3(9 / 3),
        "B-": utils.format_num_3(8 / 3),
        "C+": utils.format_num_3(7 / 3),
        "C": utils.format_num_3(6 / 3),
        "C-": utils.format_num_3(5 / 3),
        "D+": utils.format_num_3(4 / 3),
        "D": utils.format_num_3(3 / 3),
        "D-": utils.format_num_3(3 / 3),
        "F": utils.format_num_3(0 / 3)
    }
    for course in student.get_courses():
        if course.get_final_grade() == "n/a":
            course.set_points("n/a")
            pass
        else:
            final_grade = course.get_final_grade()
            earned_credit = course.get_earned_credit()
            if (earned_credit == 0) or (final_grade in ["SE", "NE"]):
                course.set_points(utils.format_num_3(0 / 3))
                pass
            else:
                num = gpa_points[final_grade] * course.get_credit()
                course.set_points(utils.format_num_3(num))
                pass
            pass
        pass
    pass


def student_gpa_points(student):
    """
    Compute the student's current GPA and record the student's term GPA.

    :param student: The student to manipulate.
    """
    sum_credits, sum_points = 0.0, 0.0
    term_credits, term_points = 0.0, 0.0
    current_term = ""
    for course in student.get_courses():
        if not (course.get_final_grade() == "n/a"):
            if course.get_final_grade() in ["SE", "PE", "UE"]:
                course_credit = 0
                course_points = 0
                pass
            else:
                course_points = course.get_points()
                course_credit = course.get_earned_credit()
                pass
            term = course.get_term()
            if current_term == "":
                current_term = term
            if not (term == current_term):
                term_gpa = utils.format_num_2(term_points / term_credits)
                student.add_to_gpa_history(current_term, term_gpa)
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
        pass
    term_gpa = utils.format_num_2(term_points / term_credits)
    student.add_to_gpa_history(current_term, term_gpa)
    student.set_gpa(utils.format_num_2(sum_points / sum_credits))
    pass


def modify_student_minors(student):
    """
    Modify the student's minor(s).

    :param student: The student to manipulate.
    """
    for minor in student.get_minors().values():
        prereq = minor.get_prereq()
        req = minor.get_req()
        electives = minor.get_electives()
        for course in student.get_courses():
            if course.get_id() in prereq:
                prereq[course.get_id()] = course
                pass
            elif course.get_id() in req:
                req[course.get_id()] = course
                pass
            elif course.get_id() in electives:
                electives[course.get_id()] = course
                pass
            pass
        minor.filter()
        minor.compute_gpa()
        pass
    pass


def phase2_main(student, workbook):
    """
    The main function to call the functions above to perform computations
    and modify the student's database.

    :param student: The student to manipulate.
    :param workbook: The Microsoft Excel Workbook/Spreadsheet to parse
                     through.
    """
    modify_other(student)
    overwrite_final_exam(student, workbook)
    drop_grades(student)
    calc_raw_grade(student)
    special_calc(student)
    raw_letter_grade(student)
    overwrite_final_grade(student, workbook)
    credit_earned(student)
    course_units(student)
    course_gpa_points(student)
    student_gpa_points(student)
    modify_student_minors(student)
    pass
