from utils import json_database

"""App with the help of which someone exactly teachers can track their students' presence in the lessons.

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
    date = input('Enter a current date in "DD-MM-YYYY" format: ')
    subject = input('Enter a new student\'s subject: ')
    name = input('Enter a new student\'s name: ')
    surname = input('Enter a new student\'s surname: ')

    json_database.add_student(date, subject, name, surname)


def mark_as_present():
    name = input('Enter the student\'s name: ')
    surname = input('Enter a new student\'s surname: ')
    subject = input('Enter the student\'s subject: ')

    json_database.mark_as_present(name, surname, subject)


def total():
    students = json_database.total()
    if any(students):
        for student in students:
            present = 'YES' if student['present'] else 'NO'
            print(f"{student['name']} {student['surname']} studies in {student['subject']}, present: {present}")
    else:
        print("There aren't any students yet! Enter 'a' to add a new student.")


def present_students_names():
    students = json_database.present_students_names()
    if any(students):
        for student in students:
            print(f"The present students is/are "
                  f"{student['name']} {student['surname']}")
    else:
        print("There aren't any students yet! Enter 'a' to add a new student.")


def absent_students_names():
    students = json_database.absent_students_names()
    if any(students):
        for student in students:
            print(f"The absent students is/are "
                  f"{student['name']} {student['surname']}")
    else:
        print("There aren't any students yet! Enter 'a' to add a new student.")


def delete_student():
    name = input('Enter the student\'s name: ')
    surname = input('Enter a new student\'s surname: ')
    subject = input('Enter the student\'s subject: ')

    json_database.delete_student(name, surname, subject)


inputs = {
    'a': add_student,
    'm': mark_as_present,
    't': total,
    'n': present_students_names,
    's': absent_students_names,
    'd': delete_student
}


def user():
    json_database.create_student_table()
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



























