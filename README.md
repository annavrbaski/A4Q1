Anna Vrbaski 101182246 A4 Q1

SetUp:
    - need to first create a new database
    - change the params of the databse connection where
        dbname is the name of the database you created
        user is the PostgreSQL username 
        password is the PostgreSQL password 
        host is the hostname; use "localhost" if your database is on your local machine

How to run:
    python3 "file name" "function" "params"
    i.e python3 A4Q1.py deleteStudent 4

Functions:
    - connect() uses psycopg2 and the parameters from the setup, to establish a connection to the databse
    - getAllStudents() uses connect() to connect to the db, and then uses cursor() (a method of the connection object)
        to execute the SQL commands, which in this case is SELECT. Then, it gets all the students and prints them.
    - addStudent() uses connect() and cursor() in the same way, except the SQL command is INSERT
    - updateStudentEmail() uses connect() and cursor() in the same way, except the SQL command is UPDATE
    - deleteStudent() uses connect() and cursor() in the same way, except the SQL command is DELETE

    - at the end of the file there is a simple python script to call the functions from the command line# A4Q1
 
