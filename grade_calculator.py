def mark_to_grade(sml, n):
    mak_grad = {90: "A+", 80: "A", 70: "B+", 60: "B", 50: "C+", 40: "C", 30: "P", 0: "F"}
    sub_grad_list, total_marks = {}, 0
    for x, y in sml.items():
        total_marks += y
        sub_grad_list[x] = mak_grad[y - (y % 10) if y > 30 else 0]
    total_grade = mak_grad[total_marks/n - (total_marks/n % 10) if total_marks > 30 else 0]
    return sub_grad_list, total_grade

try:
    subj_list = {}
    num = int(input("Enter the number of subjects: "))
    for i in range(0, num):
        subj = input("Enter the subject: ")
        mark = int(input("Enter percentage got: "))
        subj_list[subj] = mark

    subj_grades, grade = mark_to_grade(subj_list, num)
    print("Grade in subject:\n")
    for i, j in subj_grades.items():
        print(f"{i} = {j}")
    print(f"Total grade: {grade}")
except ValueError:
    print("Enter a valid response.")
