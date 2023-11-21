# Anna Vrbaski
# 101182246 A4

import psycopg2
import sys

# connection params
dbname = 'A4Q1'
user = 'postgres'
password = 'arFvYo01'
host = 'localhost'

# connect to db
def connect():
    conn = psycopg2.connect(dbname = dbname, user=user, password=password, host = host)
    return conn

# FUNCTIONS

# retrieves and displays all records from the students table
def getAllStudents():
    conn = connect()
    
    try:
        with conn.cursor() as cur:
            # call SQL commad to show all students
            cur.execute("SELECT * FROM students")
            students = cur.fetchall()
            # print each student
            for student in students:
                print(student)
    except Exception as exc:
        print("Error occured: ", exc)
    finally:
        conn.close()
        
# inserts a new student record into the students table
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect()
    
    try:
        with conn.cursor() as cur:
            # call SQL commad to add student
            cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", 
            (first_name, last_name, email, enrollment_date))
            conn.commit()
            print("Student added successfully")
    except psycopg2.IntegrityError: # if email is not unique
        print("Error: Student with this email already exsists")
    except Exception as exc:
        print("Error occurded: ", exc)
    finally:
        conn.close()
        
# updates the email address for a student with the specific student_id
def updateStudentEmail(student_id, new_email):
    conn = connect()
    
    try: 
        with conn.cursor() as cur:
            # call SQL commad to update selected student
            cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
            conn.commit()
            if cur.rowcount == 0:
                print("Student with studentID %s could not be found", student_id)
            else:
                print("Student email changed successfully")
    except Exception as exc:
        print("Error occured: ", exc)
    finally:
        conn.close()
        
# deletes the record of the student with the specifiec student_id
def deleteStudent(student_id):
    conn = connect()
    
    try:
        with conn.cursor() as cur:
            # call SQL commad to delete student
            cur.execute("DELETE FROM students WHERE student_id = %s", (student_id))
            conn.commit()
            if cur.rowcount == 0:
                print("Student with studentID %s could not be found", student_id)
            else:
                print("Student deleted successfully")
    except Exception as exc:
        print("Error occured: ", exc)
    finally:
        conn.close()
        
# PYTHON SCRIPT
# for command line argurments

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "getAllStudents":
            getAllStudents()
        elif command == "addStudent" and len(sys.argv) == 6:
            _, _, first_name, last_name, email, enrollment_date = sys.argv
            addStudent(first_name, last_name, email, enrollment_date)
        elif command == "updateStudentEmail" and len(sys.argv) == 4:
            _, _, student_id, new_email = sys.argv
            updateStudentEmail(student_id, new_email)
        elif command == "deleteStudent" and len(sys.argv) == 3:
            _, _, student_id = sys.argv
            deleteStudent(student_id)
        else:
            print("Invalid arguments.")
    else:
        print("No command provided.")
