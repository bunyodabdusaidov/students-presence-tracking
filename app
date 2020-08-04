from utils import database
"""
App with the help of which someone exactly teachers can track their students' presence in the lessons.

inputs: add a new student(name, surname, subject) , mark as present or absent, the total number of students, 
the total number of present and absent students, delete a student

"""

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

    database.add_student(name, surname, subject)


def mark_as_present():
    name = input('Enter the student\'s name: ')
    surname = input('Enter the student\'s surname: ')
    subject = input('Enter the student\'s subject: ')

    database.mark_as_present(name, surname, subject)


def total():
    students = database.total()
    for student in students:
        present = 'YES' if student['present'] else 'NO'
        print(f"{student['name']} {student['surname']} studies in {student['subject']}, present: {present}")


def present_students_names():
    students = database.present_students_names()
    if any(students):
        for student in students:
            print(f"{student['name']} {student['surname']}, subject: {student['subject']}")
    else:
        print("It seems there aren't any students or present students! "
              "Please add a new student ('a') or mark a student as present.")


def absent_students_names():
    students = database.absent_students_names()
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

    database.delete_student(name, surname, subject)


inputs = {
    'a': add_student,
    'm': mark_as_present,
    't': total,
    'n': present_students_names,
    's': absent_students_names,
    'd': delete_student
}


def user():
    database.create_student_table()
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

