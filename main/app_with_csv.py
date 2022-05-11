from utils import csv_database

"""App with the help of which instructors can track their students' presence in the lessons.

inputs: add a new student(name, surname, subject) , mark as present or absent, the total number of students, 
the total number of present and absent students, delete a student"""

INPUT = """
Welcome! What do you want to do?
Options:
- 'a' to add a new student (name, surname, subject)
- 'm' to mark a student as present
- 't' to see the total number of students in a particular subject
- 'n' to see who is present in a particular class
- 's' to see who is absent in a particular class
- 'd' to delete a student from a particular class
- 'q' to quit the app
Enter a letter: """


def user():
    csv_database.create_student_table()
    user_input = input(INPUT)

    while user_input != 'q':
        if user_input == 'a':
            add_student()
        elif user_input == 'm':
            mark_as_present()
        elif user_input == 't':
            total()
        elif user_input == 'n':
            present_students_names()
        elif user_input == 's':
            absent_students_names()
        elif user_input == 'd':
            delete_student()
        else:
            print('Unknown command! Please try again.')

        user_input = input(INPUT)


def add_student():
    date = input('Enter a current date in "DD-MM-YYYY" format: ')
    subject = input('Enter a new student\'s subject: ')
    name = input('Enter a new student\'s name: ')
    surname = input('Enter a new student\'s surname: ')

    csv_database.add_student(date, subject, name, surname)


def mark_as_present():
    name = input('Enter the student\'s name: ')
    surname = input('Enter a new student\'s surname: ')
    subject = input('Enter the student\'s subject: ')

    csv_database.mark_as_present(name, surname, subject)


def total():
    students = csv_database.total()
    for student in students:
        present = 'YES' if student['present'] == '1' else 'NO'
        print(f"{student['name']} {student['surname']} studies in {student['subject']}, present: {present}")


def present_students_names():
    students = csv_database.present_students_names()
    for student in students:
        if any(student):
            print(f"The present students is/are "
                  f"{student['name']} {student['surname']}")
        else:
            print("There aren't any present students.")


def absent_students_names():
    students = csv_database.absent_students_names()
    for student in students:
        print(f"The absent students is/are "
              f"{student['name']} {student['surname']}")


def delete_student():
    name = input('Enter the student\'s name: ')
    surname = input('Enter a new student\'s surname: ')
    subject = input('Enter the student\'s subject: ')

    csv_database.delete_student(name, surname, subject)


user()



























