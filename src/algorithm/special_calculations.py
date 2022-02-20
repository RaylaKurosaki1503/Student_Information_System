################################################################################
"""
Author: Rayla Kurosaki

File: special_calculations.py

Description:
"""
################################################################################


from algorithm import helper_functions as hf


def calc_CS(course, lst):
    """

    :param course:
    :param lst:
    :return:
    """
    course_grade = course.get_raw_grade()
    sum_assignments, sum_exams = 0.0, 0.0
    for type, assignment in course.get_assignments().items():
        weighted_average = 0.0
        grades = assignment.get_grades()
        if len(grades) > 0:
            weight = assignment.get_weight()
            type_grade = assignment.get_average()
            weighted_average = weight * type_grade / 100
            pass
        if type in lst:
            sum_assignments += weighted_average
            pass
        else:
            sum_exams += weighted_average
            pass
        pass
    sum_assignments *= 2
    sum_exams *= 2
    max_assignment, max_exam = sum_assignments + 10, sum_exams + 10
    if abs(sum_assignments - sum_exams) > 20:
        if sum_exams < sum_assignments:
            if course_grade > max_exam:
                course.set_raw_grade(hf.format_num_3(max_exam))
                pass
            pass
        else:
            if course_grade > max_assignment:
                course.set_raw_grade(hf.format_num_3(max_assignment))
                pass
            pass
        pass
    pass


def calc_basic(course):
    """

    :param course:
    :return:
    """
    num, denom = 0, 0
    for assignment in course.get_assignments().values():
        for grade in assignment.get_grades():
            num_str, denom_str = grade[1].split(" / ")
            num += float(num_str)
            denom += float(denom_str)
            pass
        pass
    if not (denom == 0):
        course.set_raw_grade(hf.format_num_3(100 * num / denom))
    pass


def calc_UP2(course):
    """

    :param course:
    :return:
    """
    course_grade, total_weight = 0.0, 0.0
    for type, assignment in course.get_assignments().items():
        grades = assignment.get_grades()
        if not (len(grades) == 0):
            sum = 0.0
            total_weight += assignment.get_weight()
            for grade in grades:
                num = float(grade[1].split(" / ")[0])
                denom = float(grade[1].split(" / ")[1])
                if type == "Quiz":
                    diff = 10 - float(denom)
                    num += diff
                    denom += diff
                    pass
                sum += num / denom
                pass
            average = sum / len(grades)
            course_grade += average * assignment.get_weight()
            assignment.set_average(100 * average)
            pass
        pass
    if not (total_weight == 0):
        course.set_raw_grade(hf.format_num_3(100 * course_grade / total_weight))
    pass


def calc_VnW(course):
    """

    :param course:
    :return:
    """
    # Get the homework assignments
    homework = course.get_assignments()["Homework"]
    # Get the homework grades
    hw_grades = homework.get_grades()
    if not (len(hw_grades) == 0):
        num, denom = 0, 0
        # Iterate through each hw grade
        for grade in hw_grades:
            # Add the numerators and denominators of each grade
            num_str, denom_str = grade[1].split(" / ")
            num += float(num_str)
            denom += float(denom_str)
            pass
        # Re-compute the homework average grade
        homework.set_average(hf.format_num_3(100 * num / denom))
        course_grade, total_weight = 0, 0
        # Re-compute the course raw grade
        for assignment in course.get_assignments().values():
            total_weight += assignment.get_weight()
            course_grade += assignment.get_weight() * assignment.get_average()
            pass
        # Re-set the course raw grade
        course.set_raw_grade(hf.format_num_3(course_grade / total_weight))
    pass
