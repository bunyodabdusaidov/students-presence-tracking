from .database_connection import DatabaseConnection

database = 'data.db'


def create_student_table():
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Students(name text primary key, surname text,'
                       'subject text, present integer)')


def add_student(name, surname, subject):
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Students VALUES(?, ?, ?, 0)', (name, surname, subject))


def mark_as_present(name, surname, subject):
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE Students SET present=1 WHERE name=? and surname=? and subject=?', (name, surname, subject))


def total():
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Students')

        students = [{
            'name': row[0],
            'surname': row[1],
            'subject': row[2],
            'present': row[3]
            }
            for row in cursor.fetchall()]
        return students


def indexed():
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE INDEX ON Students')


def present_students_names():
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT name, surname, subject FROM Students WHERE present=1')

        students = [{'name': row[0], 'surname': row[1], 'subject': row[2]} for row in cursor.fetchall()]
        return students


def absent_students_names():
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT name, surname, subject FROM Students WHERE present=0')

        students = [{'name': row[0], 'surname': row[1], 'subject': row[2]} for row in cursor.fetchall()]
        return students


def delete_student(name, surname, subject):
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Students WHERE name=? and surname=? and subject=?', (name, surname, subject))

