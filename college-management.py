import mysql.connector as mysql
from os import system

host = "localhost"
user = "root"
password = ""
database = "College"

db = mysql.connect(host = host, user = user, password = password, database = database)
command_handler = db.cursor(buffered = True)

def auth_admin():
    print("")
    print("=== COLLEGE MANAGEMENT SYSTEM FOR ADMIN ===")
    print("")
    username = input(str("USERNAME : "))
    password = input(str("PASSWORD : "))
    print("")

    if username == "admin" :
        if password == "password":
            admin_session()
        else:
            print("-- WRONG PASSWORD --")
    else:
        print("-- USERNAME DOESN'T RECOGNIZED --")        

def admin_session():
    system('cls')
    print("=======================================")
    print("  WELCOME, YOU ARE SIGNED IN AS ADMIN")
    print("=======================================")
    print("")
    print("MENU : ")
    print("1. REGISTER NEW STUDENT")
    print("2. REGISTER NEW TEACHER")
    print("3. DELETE EXISTING STUDENT")
    print("4. DELETE EXISTING TEACHER")
    print("5. LOGOUT")
    print("")

    while 1:
        user_option = input(str("PLEASE CHOOSE VALID OPTION : "))

        if user_option == "1":
            print("")
            print("-- REGISTER NEW STUDENT --")
            fullname = input(str("STUDENT NAME : "))
            username = input(str("STUDENT USERNAME : "))
            password = input(str("STUDENT PASSWORD : "))
            query_vals = (fullname, username, password)
            command_handler.execute("INSERT INTO users (fullname, username, password, privilege) VALUES (%s, %s, %s, 'STUDENT')", query_vals)
            db.commit()
            print("")
            print("NAME : " + fullname)
            print("ROLE : STUDENT")
            print("")
            print("-- STUDENT SUCCESSFULLY REGISTERED --")
            print("*****")
            print("")
        elif user_option == "2":
            print("")
            print("-- REGISTER NEW TEACHER --")
            fullname = input(str("TEACHER NAME : "))
            username = input(str("TEACHER USERNAME : "))
            password = input(str("TEACHER PASSWORD : "))
            query_vals = (fullname, username, password)
            command_handler.execute("INSERT INTO users (fullname, username, password, privilege) VALUES (%s, %s, %s, 'TEACHER')", query_vals)
            db.commit()
            print("")
            print("NAME : " + fullname)
            print("ROLE : TEACHER")
            print("")
            print("-- TEACHER SUCCESSFULLY REGISTERED --")
            print("*****")
            print("")
        elif user_option == "3":
            print("")
            print("-- DELETE EXISTING STUDENT--")
            username = input(str("INPUT STUDENT USERNAME : "))
            query_vals = (username, "STUDENT")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("STUDENT USERNAME NOT FOUND")
            else:
                print("STUDENT USERNAME %s HAS BEEN DELETED")
        elif user_option == "4":
            print("")
            print("-- DELETE EXISTING STUDENT--")
            username = input(str("INPUT TEACHER USERNAME : "))
            query_vals = (username, "TEACHER")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("TEACHER USERNAME NOT FOUND")
            else:
                print("TEACHER USERNAME %s HAS BEEN DELETED")
        elif user_option == "5":
            main()
        else:
            print("")
            print("-- INVALID OPTION! --")
            
def auth_teacher():
    print("")
    print("=== COLLEGE MANAGEMENT SYSTEM FOR TEACHER ===")
    print("")
    while 1:
        username = input(str("USERNAME : "))
        password = input(str("PASSWORD : "))
        print("")
        query_vals = (username, password)
        command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'TEACHER'", query_vals)
        if command_handler.rowcount <= 0:
            print("")
            print("-- USERNAME NOT FOUND --")
        else:
            teacher_session()

def teacher_session():
    system('cls')
    print("====================================")
    print("  WELCOME, YOU SIGNED IN AS TEACHER")
    print("====================================")
    print("")
    print("MENU : ")
    print("1. MARK STUDENT ATTENDANCE")
    print("2. VIEW STUDENT ATTENDANCE")
    print("3. LOGOUT")
    while 1:
        print("")
        user_option = input(str("PLEASE CHOOSE VALID OPTION : "))
        if user_option == "1":
            print("")
            print("-- MARK STUDENT ATTENDANCE --")
            command_handler.execute("SELECT username FROM users WHERE privilege = 'STUDENT'")
            records = command_handler.fetchall()
            for record in records:
                record = str(record).replace("'", "")
                record = str(record).replace(",", "")
                record = str(record).replace("(", "")
                record = str(record).replace(")", "")
                print("ABSENT (A) / LATE (L) / PRESENT (P)")
                status = input(str("INPUT STATUS FOR " + str(record) + " "))
                query_vals = (str(record), status)

def main():
        print("")
        print("***** WELCOME TO COLLEGE MANAGEMENT SYSTEM *****")
        print("")
        print("1. LOGIN AS ADMIN")
        print("2. LOGIN AS STUDENT")
        print("3. LOGIN AS TEACHER ")
        print("")

        while 1:
            option = input(str("CHOOSE YOUR ROLE : "))

            if option == "1":
                auth_admin()
            elif option == "2":
                print("=== COLLEGE MANAGEMENT SYSTEM FOR STUDENT ===")
            elif option == "3":
                print("== COLLEGE MANAGEMENT SYSTEM FOR TEACHER ==")
            else:
                print("INVALID OPTION!")

main()

#belum selesai
