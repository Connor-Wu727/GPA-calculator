# def calculating_GPA_not_weighted():
#     num_classes = int(input("Enter the number of classes: "))
#     if num_classes > 9:
#         print("Enter proper number of classes")
#         return num_classes
#     total_score = 0
#     for i in range(1, num_classes + 1):
#         score = int(input(f"Enter the score of class {i}: "))
#
#         if score >= 93 and score <= 100:
#             total_score += 4
#         elif score >= 90 and score < 93:
#             total_score += 3.67
#         elif score > 87 and score < 90:
#             total_score += 3.33
#         elif score >= 84 and score <= 87:
#             total_score += 3
#         elif score >= 80 and score < 83:
#             total_score += 2.67
#         elif score >= 77 and score < 80:
#             total_score += 2.33
#         elif score >= 74 and score < 77:
#             total_score += 2
#         elif score >= 70 and score < 73:
#             total_score += 1.67
#         elif score >= 67 and score < 70:
#             total_score += 1.33
#         elif score >= 64 and score < 67:
#             total_score += 1
#         elif score >= 60 and score <= 63:
#             total_score += 0.67
#         elif score < 60:
#             total_score += 0.33
#         else:
#             print("Enter proper score")
#             return score
#
#
#     gpa = total_score / num_classes
#     print("Your GPA is:", gpa)
#
#
# def calculating_GPA_weighted():
#     num_classes = int(input("Enter the number of classes: "))
#     num_of_AP_classes = int(input("Enter the number of AP classes: "))
#     num_of_normal_classes = int(input("Enter the number of normal classes: "))
#     if num_classes> 9:
#         print("Enter proper number of classes")
#     total_score = 0
#
#     for i in range(1, num_of_AP_classes + 1):
#         score = int(input(f"Enter the score of AP class {i}: "))
#
#         if score >= 93 and score <= 100:
#             total_score += 5
#         elif score >= 90 and score < 93:
#             total_score += 4.67
#         elif score > 87 and score < 90:
#             total_score += 4.33
#         elif score >= 84 and score <= 87:
#             total_score += 4
#         elif score >= 80 and score < 83:
#             total_score += 3.67
#         elif score >= 77 and score < 80:
#             total_score += 3.33
#         elif score >= 74 and score < 77:
#             total_score += 2
#         elif score >= 70 and score < 73:
#             total_score += 3.67
#         elif score >= 67 and score < 70:
#             total_score += 2.33
#         elif score >= 64 and score < 67:
#             total_score += 2
#         elif score >= 60 and score <= 63:
#             total_score += 1.67
#         elif score < 60:
#             total_score += 1.33
#         else:
#             print("Enter proper score")
#             return score
#
#     for i in range(1, num_of_normal_classes + 1):
#         score = int(input(f"Enter the score of normal class {i}: "))
#
#         if score >= 93 and score <= 100:
#             total_score += 4
#         elif score >= 90 and score < 93:
#             total_score += 3.67
#         elif score > 87 and score < 90:
#             total_score += 3.33
#         elif score >= 84 and score <= 87:
#             total_score += 3
#         elif score >= 80 and score < 83:
#             total_score += 2.67
#         elif score >= 77 and score < 80:
#             total_score += 2.33
#         elif score >= 74 and score < 77:
#             total_score += 2
#         elif score >= 70 and score < 73:
#             total_score += 1.67
#         elif score >= 67 and score < 70:
#             total_score += 1.33
#         elif score >= 64 and score < 67:
#             total_score += 1
#         elif score >= 60 and score <= 63:
#             total_score += 0.67
#         elif score < 60:
#             total_score += 0.33
#         else:
#             print("Enter proper score")
#             return score
#
#     gpa = total_score / num_classes
#     print("Your GPA is:", gpa)
#
#
# def determine_grade():
#     Grade = int(input("Enter your grade number: "))
#     if 8 < Grade <=12:
#         print("Do you want to calculate weighted GPA?(Yes or no)")
#         x = input()
#         if x == "Yes" or x == "yes":
#             calculating_GPA_weighted()
#         elif x == "No" or x == "no":
#             calculating_GPA_not_weighted()
#         else:
#             print("Enter proper grade")
#     elif Grade < 8:
#         print("You don't need to calculate GPA")
#     elif Grade == 8:
#         calculating_GPA_weighted()
#     else:
#         print("Enter proper grade")
#
#
# determine_grade()
#
# import streamlit as st
#
# def score_to_gpa(score):
#     if 93 <= score <= 100:
#         return 4.0
#     elif 90 <= score < 93:
#         return 3.67
#     elif 87 <= score < 90:
#         return 3.33
#     elif 84 <= score < 87:
#         return 3.0
#     elif 80 <= score < 84:
#         return 2.67
#     elif 77 <= score < 80:
#         return 2.33
#     elif 74 <= score < 77:
#         return 2.0
#     elif 70 <= score < 74:
#         return 1.67
#     elif 67 <= score < 70:
#         return 1.33
#     elif 64 <= score < 67:
#         return 1.0
#     elif 60 <= score < 64:
#         return 0.67
#     elif score < 60:
#         return 0.33
#     else:
#         return None
#
# def calculating_GPA_not_weighted(scores):
#     total_score = 0
#     num_classes = len(scores)
#     for score in scores:
#         g = score_to_gpa(score)
#         if g is None:
#             return None
#         total_score += g
#     if num_classes == 0:
#         return 0
#     return total_score / num_classes
#
# def calculating_GPA_weighted(ap_scores, normal_scores):
#     total_score = 0
#     num_classes = len(ap_scores) + len(normal_scores)
#     for score in ap_scores:
#         if 93 <= score <= 100:
#             total_score += 5
#         elif 90 <= score < 93:
#             total_score += 4.67
#         elif 87 <= score < 90:
#             total_score += 4.33
#         elif 84 <= score < 87:
#             total_score += 4
#         elif 80 <= score < 84:
#             total_score += 3.67
#         elif 77 <= score < 80:
#             total_score += 3.33
#         elif 74 <= score < 77:
#             total_score += 3
#         elif 70 <= score < 74:
#             total_score += 2.67
#         elif 67 <= score < 70:
#             total_score += 2.33
#         elif 64 <= score < 67:
#             total_score += 2
#         elif 60 <= score < 64:
#             total_score += 1.67
#         else:
#             total_score += 1.33
#     for score in normal_scores:
#         if 93 <= score <= 100:
#             total_score += 4
#         elif 90 <= score < 93:
#             total_score += 3.67
#         elif 87 <= score < 90:
#             total_score += 3.33
#         elif 84 <= score < 87:
#             total_score += 3
#         elif 80 <= score < 84:
#             total_score += 2.67
#         elif 77 <= score < 80:
#             total_score += 2.33
#         elif 74 <= score < 77:
#             total_score += 2
#         elif 70 <= score < 74:
#             total_score += 1.67
#         elif 67 <= score < 70:
#             total_score += 1.33
#         elif 64 <= score < 67:
#             total_score += 1
#         elif 60 <= score < 64:
#             total_score += 0.67
#         else:
#             total_score += 0.33
#     if num_classes == 0:
#         return 0
#     return total_score / num_classes
#
# st.title("GPA Calculator")
#
# grade = st.number_input("Enter your grade number:", min_value=0, max_value=12, step=1, value=9)
#
# if grade < 8:
#     st.write("You don't need to calculate GPA")
# elif grade == 8:
#     st.write("Calculating unweighted GPA automatically (Grade 8)")
#     num_normal = st.number_input("Enter the number of normal classes:", min_value=0, max_value=9, value=0, step=1)
#     ap_scores = []
#     normal_scores = []
#     for i in range(num_normal):
#         s = st.number_input(f"Enter the score of normal class {i+1}:", min_value=0, max_value=100, value=80, step=1)
#         normal_scores.append(s)
#     if st.button("Calculate GPA"):
#         gpa = calculating_GPA_weighted(ap_scores, normal_scores)
#         if gpa is None:
#             st.error("Invalid score entered")
#         else:
#             st.success(f"Your GPA is: {gpa:.2f}")
# elif 8 < grade <= 12:
#     weighted = st.radio("Do you want to calculate weighted GPA?", ("Yes", "No"))
#     if weighted == "Yes":
#         num_ap = st.number_input("Enter the number of AP classes:", min_value=0, max_value=9, value=0, step=1)
#         num_normal = st.number_input("Enter the number of normal classes:", min_value=0, max_value=9, value=0, step=1)
#         ap_scores = []
#         normal_scores = []
#         for i in range(num_ap):
#             s = st.number_input(f"Enter the score of AP class {i+1}:", min_value=0, max_value=100, value=80, step=1)
#             ap_scores.append(s)
#         for i in range(num_normal):
#             s = st.number_input(f"Enter the score of normal class {i+1}:", min_value=0, max_value=100, value=80, step=1)
#             normal_scores.append(s)
#         if st.button("Calculate GPA"):
#             gpa = calculating_GPA_weighted(ap_scores, normal_scores)
#             if gpa is None:
#                 st.error("Invalid score entered")
#             else:
#                 st.success(f"Your GPA is: {gpa:.2f}")
#     else:
#         num_classes = st.number_input("Enter the number of classes:", min_value=0, max_value=9, value=0, step=1)
#         scores = []
#         for i in range(num_classes):
#             s = st.number_input(f"Enter the score of class {i+1}:", min_value=0, max_value=100, value=80, step=1)
#             scores.append(s)
#         if st.button("Calculate GPA"):
#             gpa = calculating_GPA_not_weighted(scores)
#             if gpa is None:
#                 st.error("Invalid score entered")
#             else:
#                 st.success(f"Your GPA is: {gpa:.2f}")
# else:
#     st.write("Please enter a grade between 0 and 12")

import streamlit as st

# Page name
st.set_page_config(page_title="GPA Calculator", layout="centered")

# The formula of transporting score to GPA
def points(score):
    score = int(score)
    if score < 0 or score > 100:
        return None

    if 93 <= score <= 100:
        return 4
    elif 90 <= score < 93:
        return 3.67
    elif 87 <= score < 90:
        return 3.33
    elif 84 <= score < 87:
        return 3
    elif 80 <= score < 84:
        return 2.67
    elif 77 <= score < 80:
        return 2.33
    elif 74 <= score < 77:
        return 2
    elif 70 <= score < 74:
        return 1.67
    elif 67 <= score < 70:
        return 1.33
    elif 64 <= score < 67:
        return 1
    elif 60 <= score < 64:
        return 0.67
    elif score < 60:
        return 0.33


def electives():
    elective_number = st.radio("Enter your elective number:", [1, 2], index=0, key="elec_num")

    if elective_number == 2:
        elective_one = st.text_input("Your first elective name: ", key="elec1_name")
        elective_two = st.text_input("Your second elective name: ", key="elec2_name")

        score1 = st.number_input(
            f"Score for {elective_one}: ",
            min_value=0, max_value=100, value=0, step=1, key="elec1_score"
        )
        score2 = st.number_input(
            f"Score for {elective_two}: ",
            min_value=0, max_value=100, value=0, step=1, key="elec2_score"
        )

        return points(int(score1)) + points(int(score2)), 2

    elif elective_number == 1:
        only_elective = st.text_input("Your elective: ", key="elec_only_name")
        score = st.number_input(
            "Score for elective: ",
            min_value=0, max_value=100, value=0, step=1, key="elec_only_score"
        )
        return points(int(score)), 1

    else:
        st.write("Not a grade 9")
        return 0, 0


def math():
    level = st.radio("Is your mathematics level at:",
                     ["A. Pre - calculus A", "B. Pre - calculus AB", "C. AP - calculus AB"], key="math_level")
    if level == "A. Pre - calculus A":
        score = st.number_input("Enter your Pre - calculus A score: ", min_value=0, max_value=100, value=0, step=1, key="math_score_a")
        return points(int(score))
    elif level == "B. Pre - calculus AB":
        score = st.number_input("Enter your Pre - calculus AB score: ", min_value=0, max_value=100, value=0, step=1,
                                key="math_score_b")
        return points(int(score))
    elif level == "C. AP - calculus AB":
        score = st.number_input("Enter your AP calculus AB score: ", min_value=0, max_value=100, value=0, step=1, key="math_score_c")
        return points(int(score))
    else:
        st.write("Not a grade 9")
        return 0


def science():
    subject = st.radio("Is your science subject:",
                       ["A. AP physics 1", "B. Honors physics", "C. Honors chemistry", "D. Honors biology"],
                       key="sci_subject")
    if subject == "A. AP physics 1":
        score = st.number_input("Enter your AP physics 1 score: ", min_value=0, max_value=100, value=0, step=1, key="sci_score_a")
        return points(int(score))
    elif subject == "B. Honors physics":
        score = st.number_input("Enter your Honors physics score: ", min_value=0, max_value=100, value=0, step=1, key="sci_score_b")
        return points(int(score))
    elif subject == "C. Honors chemistry":
        score = st.number_input("Enter your Honors chemisrty score: ", min_value=0, max_value=100, value=0, step=1, key="sci_score_c")
        return points(int(score))
    elif subject == "D. Honors biology":
        score = st.number_input("Enter your Honors biology score: ", min_value=0, max_value=100, value=0, step=1, key="sci_score_d")
        return points(int(score))
    else:
        st.write("Not a grade 9")
        return 0


def chinese():
    chinese = st.number_input("Score for your Chinese 9: ", min_value=0, max_value=100, value=0, step=1, key="chinese_score")
    return points(int(chinese))


def literature():
    literature = st.number_input("Score for your honors English literature: ", min_value=0, max_value=100, value=0, step=1,
                                 key="lit_score")
    return points(int(literature))


def language():
    language = st.number_input("Score for your honors English language: ", min_value=0, max_value=100, value=0, step=1,
                               key="lang_score")
    return points(int(language))


def history():
    history = st.number_input("Score for your AP world history: ", min_value=0, max_value=100, value=0, step=1, key="hist_score")
    return points(int(history))


def calculating_GPA_not_weighted():
    num_classes = st.number_input("Enter the number of classes: ", min_value=1, max_value=8, value=1, step=1,
                                  key="nw_num_classes")
    num_classes = int(num_classes)
    total_score = 0
    for i in range(1, num_classes + 1):
        score = st.number_input(f"Enter the score of class {i}: ", min_value=0, max_value=100, value=0, step=1, key=f"nw_score_{i}")
        score = int(score)
        if score >= 93 and score <= 100:
            total_score += 4
        elif score >= 90 and score < 93:
            total_score += 3.67
        elif score >= 87 and score < 90:
            total_score += 3.33
        elif score >= 84 and score < 87:
            total_score += 3
        elif score >= 80 and score <= 83:
            total_score += 2.67
        elif score >= 77 and score < 80:
            total_score += 2.33
        elif score >= 74 and score < 77:
            total_score += 2
        elif score >= 70 and score <= 73:
            total_score += 1.67
        elif score >= 67 and score < 70:
            total_score += 1.33
        elif score >= 64 and score < 67:
            total_score += 1
        elif score >= 60 and score <= 63:
            total_score += 0.67
        elif score < 60:
            total_score += 0.33
        else:
            st.write("Enter proper score")
            return None

    gpa = total_score / num_classes
    return gpa


def calculating_GPA_weighted():
    num_of_AP_classes = st.number_input("Enter the number of AP classes: ", min_value=0, max_value=8, value=1, step=1,
                                        key="w_num_ap")
    num_of_AP_classes = int(num_of_AP_classes)
    num_of_normal_classes = st.number_input("Enter the number of normal classes: ", min_value=0,
                                            max_value=8 - num_of_AP_classes, value=0, step=1,
                                            key="w_num_normal")
    num_of_normal_classes = int(num_of_normal_classes)
    num_classes = num_of_AP_classes + num_of_normal_classes

    if num_classes == 0:
        return

    total_score = 0

    for i in range(1, num_of_AP_classes + 1):
        score = st.number_input(f"Enter the score of AP class {i}: ", min_value=0, max_value=100, value=0, step=1,
                                key=f"w_ap_score_{i}")
        score = int(score)
        if score >= 93 and score <= 100:
            total_score += 5
        elif score >= 90 and score < 93:
            total_score += 4.67
        elif score >= 87 and score < 90:
            total_score += 4.33
        elif score >= 84 and score < 87:
            total_score += 4
        elif score >= 80 and score <= 83:
            total_score += 3.67
        elif score >= 77 and score < 80:
            total_score += 3.33
        elif score >= 74 and score < 77:
            total_score += 3
        elif score >= 70 and score <= 73:
            total_score += 2.67
        elif score >= 67 and score < 70:
            total_score += 2.33
        elif score >= 64 and score < 67:
            total_score += 2
        elif score >= 60 and score <= 63:
            total_score += 1.67
        elif score < 60:
            total_score += 1.33
        else:
            st.write("Enter proper score")
            return None

    for i in range(1, num_of_normal_classes + 1):
        score = st.number_input(f"Enter the score of normal class {i}: ", min_value=0, max_value=100, value=0, step=1,
                                key=f"w_normal_score_{i}")
        score = int(score)
        if score >= 93 and score <= 100:
            total_score += 4
        elif score >= 90 and score < 93:
            total_score += 3.67
        elif score >= 87 and score < 90:
            total_score += 3.33
        elif score >= 84 and score < 87:
            total_score += 3
        elif score >= 80 and score <= 83:
            total_score += 2.67
        elif score >= 77 and score < 80:
            total_score += 2.33
        elif score >= 74 and score < 77:
            total_score += 2
        elif score >= 70 and score <= 73:
            total_score += 1.67
        elif score >= 67 and score < 70:
            total_score += 1.33
        elif score >= 64 and score < 67:
            total_score += 1
        elif score >= 60 and score <= 63:
            total_score += 0.67
        elif score < 60:
            total_score += 0.33
        else:
            st.write("Enter proper score")
            return None

    gpa = total_score / num_classes
    return gpa


def grade_9_calculator():
    total_score = 0
    course_count = 0

    elective_score, elective_count = electives()
    total_score += elective_score
    course_count += elective_count

    total_score += math()
    course_count += 1

    total_score += science()
    course_count += 1

    total_score += history()
    course_count += 1

    total_score += literature()
    course_count += 1

    total_score += language()
    course_count += 1

    total_score += chinese()
    course_count += 1

    gpa = total_score / course_count
    return gpa


def subject_score_calculator():
    subject = st.text_input("What is your subject: ", key="sub_name_tab")
    major_worth = st.number_input("How much percent the major worth: ", min_value=0, max_value=100, value=50, step=1,
                                  key="sub_maj_w_tab")
    minor_worth = st.number_input("How much percent the minor worth: ", min_value=0, max_value=100, value=50, step=1,
                                  key="sub_min_w_tab")

    major = major_worth / 100
    minor = minor_worth / 100

    major_full_marks = st.number_input("How much major points does the subject have? ", min_value=1, value=100, step=1,
                                       key="sub_maj_f_tab")
    major_get_marks = st.number_input("How much major points did you get? ", min_value=0, value=80, step=1,
                                      key="sub_maj_g_tab")
    major_points = (major_get_marks / major_full_marks) * 100

    minor_full_marks = st.number_input("How much minor points does the subject have? ", min_value=1, value=100, step=1,
                                       key="sub_min_f_tab")
    minor_get_marks = st.number_input("How much minor points did you get? ", min_value=0, value=80, step=1,
                                      key="sub_min_g_tab")
    minor_points = (minor_get_marks / minor_full_marks) * 100

    if st.button("Calculate Subject Score", key="btn_sub_tab"):
        if major_worth + minor_worth != 100:
            st.error("Major and minor worth must add up to 100")
        elif major_get_marks > major_full_marks:
            st.error("Major marks cannot exceed full marks")
        elif minor_get_marks > minor_full_marks:
            st.error("Minor marks cannot exceed full marks")
        else:
            score = major * major_points + minor * minor_points
            st.success(f"Your {subject} score is: {score:.2f}")


st.title("GPA Calculator")

tab1, tab2 = st.tabs(["GPA Calculator", "Subject Score Calculator"])

with tab1:
    Grade = st.number_input("Enter your grade number (number not words please):", min_value=0, max_value=12, step=1,
                            value=9, key="grade_tab1")
    Grade = int(Grade)

    if 8 < Grade <= 12:
        if Grade == 9:
            gpa = grade_9_calculator()
            if st.button("Calculate GPA", key="calc_g9_tab1"):
                if gpa is not None:
                    st.success(f"{gpa:.2f}")
        else:
            x = st.radio("Do you want to calculate weighted GPA?(Yes or no)", ["Yes", "No"], key="weighted_tab1")
            if x == "Yes":
                gpa = calculating_GPA_weighted()
                if st.button("Calculate GPA", key="calc_w_tab1"):
                    if gpa is not None:
                        st.success(f"{gpa:.2f}")
            elif x == "No":
                gpa = calculating_GPA_not_weighted()
                if st.button("Calculate GPA", key="calc_nw_tab1"):
                    if gpa is not None:
                        st.success(f"{gpa:.2f}")
            else:
                st.write("Enter proper grade")
    elif Grade < 8:
        st.write("You don't need to calculate GPA")
    elif Grade == 8:
        gpa = calculating_GPA_not_weighted()
        if st.button("Calculate GPA", key="calc_8_tab1"):
            if gpa is not None:
                st.success(f"{gpa:.2f}")
    else:
        st.write("Enter proper grade")
with tab2:
    subject_score_calculator()

# streamlit run "GPA calculator.py"
# python3 -m pip install streamlit