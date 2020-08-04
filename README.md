# students-presence-tracking
Simple API that tracks students' presence in particular classes by performing some calculations and adding them to a database (SQLite).

There are 3 files. 

context-manager.py deals with database's connection, commits and closes the database automatically. 
database.py deals with the whole database and some calculations. adds a new student, lists the students in particular subjects, deletes students.
app.py is the main file, mainly dealing with the user inputs and putting them as an argument to the functions of database.py. 
Also, displays options and calls the needed functions.

PS: It's my first project since I started learning programming.
