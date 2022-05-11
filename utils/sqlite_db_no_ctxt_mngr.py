import sqlite3

database = 'data.db'


def create_student_table():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Students(name text primary key, surname text,'
                   'subject text, present integer)')
    connection.commit()
    connection.close()


def add_student(name, surname, subject):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Students VALUES(?, ?, ?, 0)', (name, surname, subject))
    connection.commit()
    connection.close()


def mark_as_present(name, surname, subject):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('UPDATE Students SET present=1 WHERE name=? and surname=? and subject=?', (name, surname, subject))
    connection.commit()
    connection.close()


def total():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Students')

    students = [{'name': row[0],
                 'surname': row[1],
                 'subject': row[2],
                 'present': row[3]
                 }
                for row in cursor.fetchall()]
    connection.close()
    return students


def indexed():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('CREATE INDEX ON students')
    connection.commit()
    connection.close()


def present_students_names():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('SELECT name, surname, subject FROM Students WHERE present=1')

    students = [{'name': row[0], 'surname': row[1], 'subject': row[2]} for row in cursor.fetchall()]
    connection.close()
    return students


def absent_students_names():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('SELECT name, surname, subject FROM Students WHERE present=0')

    students = [{'name': row[0], 'surname': row[1], 'subject': row[2]} for row in cursor.fetchall()]
    connection.close()
    return students


def delete_student(name, surname, subject):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Students WHERE name=? surname=? subject=?', (name, surname, subject))
    connection.commit()
    connection.close()





































