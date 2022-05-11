from utils import sqlite_db_yes_ctxt_mngr

"""App with the help of which instructors can track their students' presence in the lessons.

inputs: add a new student(name, surname, subject) , mark as present or absent, the total number of students, 
the total number of present and absent students, delete a student"""

INPUT = """
Options:
- 'a' to add a new student (name, surname, subject)
- 'm' to mark a student as present
- 't' to see the total number of students in a particular subject
- 'n' to see who is present in a particular class
- 's' to see who is absent in a particular class
- 'd' to delete a student from a particular class
- 'q' to quit the app
Enter a letter: """


def add_student():
    name = input('Enter a new student\'s name: ')
    surname = input('Enter a new student\'s surname: ')
    subject = input('Enter a new student\'s subject: ')

    sqlite_db_yes_ctxt_mngr.add_student(name, surname, subject)


def mark_as_present():
    name = input('Enter the student\'s name: ')
    surname = input('Enter the student\'s surname: ')
    subject = input('Enter the student\'s subject: ')

    sqlite_db_yes_ctxt_mngr.mark_as_present(name, surname, subject)


def total():
    students = sqlite_db_yes_ctxt_mngr.total()
    for student in students:
        present = 'YES' if student['present'] else 'NO'
        print(f"{student['name']} {student['surname']} studies in {student['subject']}, present: {present}")


def present_students_names():
    students = sqlite_db_yes_ctxt_mngr.present_students_names()
    if any(students):
        for student in students:
            print(f"{student['name']} {student['surname']}, subject: {student['subject']}")
    else:
        print("It seems there aren't any students or present students! "
              "Please add a new student ('a') or mark a student as present.")


def absent_students_names():
    students = sqlite_db_yes_ctxt_mngr.absent_students_names()
    if any(students):
        for student in students:
            print(f"{student['name']} {student['surname']}, subject: {student['subject']}")
    else:
        print("It seems all the students are present or there aren't any students at all! "
              "Please first add a new student.")


def delete_student():
    name = input('Enter the student\'s name: ')
    surname = input('Enter the student\'s surname: ')
    subject = input('Enter the student\'s subject: ')

    sqlite_db_yes_ctxt_mngr.delete_student(name, surname, subject)


inputs = {
    'a': add_student,
    'm': mark_as_present,
    't': total,
    'n': present_students_names,
    's': absent_students_names,
    'd': delete_student
}


def user():
    sqlite_db_yes_ctxt_mngr.create_student_table()
    print('Welcome! What do you want to do?')
    user_input = input(INPUT)

    while user_input != 'q':
        if user_input in inputs:
            selected_input = inputs[user_input]
            selected_input()
        else:
            print('Unknown command! Please try again.')

        user_input = input(INPUT)


user()



























