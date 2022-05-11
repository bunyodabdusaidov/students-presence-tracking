import json

students_file = 'data.json'


def create_student_table():
    with open(students_file, 'w') as file:
        json.dump([], file)


def add_student(date, subject, name, surname):
    students = total()
    students.append({'date': date, 'subject': subject, 'name': name, 'surname': surname, 'present': False})
    _save_students(students)


def total():
    with open(students_file, 'r') as file:
        return json.load(file)


def mark_as_present(name, surname, subject):
    students = total()
    if any(students):
        for student in students:
            if student['name'] == name or student['surname'] == surname or student['subject'] == subject:
                student['present'] = True
                print('Ok, this student is marked as present.')
    else:
        print("It seems there aren't any students! Please, first add a new student by entering 'a'.")
    _save_students(students)


def _save_students(students):
    with open(students_file, 'w') as file:
        json.dump(students, file)


def present_students_names():
    students = total()
    students = [student for student in students if student['present']]
    return students


def absent_students_names():
    students = total()
    students = [student for student in students if student['present'] is not True]
    return students


def delete_student(name, surname, subject):
    students = total()
    students = [student for student in students if student['name'] != name or student['surname'] != surname or student['subject'] != subject]
    _save_students(students)






































