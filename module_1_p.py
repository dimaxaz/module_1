grades = [
    [5, 3, 3, 5, 4],
    [2, 2, 2, 3],
    [4, 5, 5, 2],
    [4, 4, 3],
    [5, 5, 5, 4, 5]
]
students_tuple_ = (
    'Johnny',
    'Bilbo',
    'Steve',
    'Khendrik',
    'Aaron'
)

students = list(students_tuple_)

if len(students) != len(grades):
    print("Количество студентов и оценок не совпадает.")
else:
    average_grades = {}

    for i in range(len(students)):
        student = students[i]
        student_grades = grades[i]
        average = sum(student_grades) / len(student_grades)
        average_grades[student] = average

    for student, avg_grade in average_grades.items():
        print(f"{student}: {avg_grade:.2f}")