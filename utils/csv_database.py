students_file = 'data.txt'


def create_student_table():
    with open(students_file, 'w'):
        pass


def add_student(date, subject, name, surname):
    with open(students_file, 'a') as file:
        file.write(f"{date},{subject},{name},{surname},0\n")


def total():
    with open(students_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'date': line[0], 'subject': line[1], 'name': line[2], 'surname': line[3], 'present': line[4]}
        for line in lines
    ]


def mark_as_present(name, surname, subject):
    students = total()
    for student in students:
        if student['name'] and student['surname'] and student['subject'] == name and surname and subject:
            student['present'] = '1'
    _save_students(students)


def _save_students(students):
    with open(students_file, 'w') as file:
        for student in students:
            file.write(f"{student['date']}, {student['subject']}, {student['name']}, {student['surname']}, {student['present']}\n")


def present_students_names():
    students = total()
    students = filter(lambda present: present == '1', students)
    return students


def absent_students_names():
    students = total()
    students = filter(lambda present: present != '1', students)
    return students


def delete_student(name, surname, subject):
    students = total()
    students = [student for student in students if student['name'] and student['surname'] and student['subject'] != name and surname and subject]
    _save_students(students)






































