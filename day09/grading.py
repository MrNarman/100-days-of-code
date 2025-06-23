student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

grade = ''
student_grades = {}
for student in student_scores:
    if student_scores[student] > 90:
        grade = 'Outstanding'
    elif student_scores[student] > 80:
        grade = 'Exceeds Expectations'
    elif student_scores[student] > 70:
        grade = 'Acceptable'
    else:
        grade = 'Fail'

    student_grades[student] = grade
print(student_grades)