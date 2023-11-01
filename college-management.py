import mysql.connector as mysql
from os import system
import hashlib

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
    print("===================================")
    print("  WELCOME, YOU SIGNED IN AS ADMIN")
    print("===================================")
    print("")
    print("MENU : ")
    print("1. REGISTER NEW STUDENT")
    print("2. REGISTER NEW TEACHER")
    print("3. DELETE EXISTING STUDENT")
    print("4. DELETE EXISTING TEACHER")
    print("5. LOGOUT")

    while 1:
        print("")
        user_option = input(str("PLEASE CHOOSE VALID OPTION : "))

        if user_option == "1":
            system('cls')
            print("")
            print("-- REGISTER NEW STUDENT --")
            fullname = input(str("STUDENT NAME : "))
            username = input(str("STUDENT USERNAME : "))
            password = input(str("STUDENT PASSWORD : "))
            securepassword = hashlib.sha256(password.encode()).hexdigest()
            query_vals = (fullname, username, securepassword)
            command_handler.execute("INSERT INTO users (fullname, username, password, privilege) VALUES (%s, %s, %s, 'STUDENT')", query_vals)
            db.commit()
            print("")
            print("NAME     : " + fullname)
            print("USERNAME : " + username)
            print("ROLE     : STUDENT")
            print("")
            print("-- STUDENT SUCCESSFULLY REGISTERED --")
            print("*****")
            print("")
            print("ADMIN SESSION (A) / MAIN (M)")
            while 1:
                selesai = input("PLEASE INSERT VALID OPTION => ")
                if selesai == "A" or selesai == "a":
                    admin_session()
                elif selesai == "M" or selesai == "m":
                    main()
                else:
                    print("INVALID OPTION!")
                    print("")
        elif user_option == "2":
            system('cls')
            print("")
            print("-- REGISTER NEW TEACHER --")
            fullname = input(str("TEACHER NAME : "))
            username = input(str("TEACHER USERNAME : "))
            password = input(str("TEACHER PASSWORD : "))
            securepassword = hashlib.sha256(password.encode()).hexdigest()
            query_vals = (fullname, username, securepassword)
            command_handler.execute("INSERT INTO users (fullname, username, password, privilege) VALUES (%s, %s, %s, 'TEACHER')", query_vals)
            db.commit()
            print("")
            print("NAME     : " + fullname)
            print("USERNAME : " + username)
            print("ROLE     : TEACHER")
            print("")
            print("-- TEACHER SUCCESSFULLY REGISTERED --")
            print("*****")
            print("")
            print("ADMIN SESSION (A) / MAIN (M)")
            while 1:
                selesai = input("PLEASE INSERT VALID OPTION => ")
                if selesai == "A" or selesai == "a":
                    admin_session()
                elif selesai == "M" or selesai == "m":
                    main()
                else:
                    print("INVALID OPTION!")
                    print("")
        elif user_option == "3":
            system('cls')
            print("")
            print("-- DELETE EXISTING STUDENT--")
            username = input(str("INPUT STUDENT USERNAME : "))
            query_vals = (username, "STUDENT")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("STUDENT USERNAME NOT FOUND")
            else:
                print("STUDENT USERNAME " + username +  " HAS BEEN DELETED")
            print("")
            print("ADMIN SESSION (A) / MAIN (M)")
            while 1:
                selesai = input("PLEASE INSERT VALID OPTION => ")
                if selesai == "A" or selesai == "a":
                    admin_session()
                elif selesai == "M" or selesai == "m":
                    main()
                else:
                    print("INVALID OPTION!")
                    print("")
        elif user_option == "4":
            system('cls')
            print("")
            print("-- DELETE EXISTING TEACHER--")
            username = input(str("INPUT TEACHER USERNAME : "))
            query_vals = (username, "TEACHER")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("TEACHER USERNAME NOT FOUND")
            else:
                print("TEACHER USERNAME " + username + " HAS BEEN DELETED")
            print("")
            print("ADMIN SESSION (A) / MAIN (M)")
            while 1:
                selesai = input("PLEASE INSERT VALID OPTION => ")
                if selesai == "A" or selesai == "a":
                    admin_session()
                elif selesai == "M" or selesai == "m":
                    main()
                else:
                    print("INVALID OPTION!")
                    print("")
        elif user_option == "5":
            main()
        else:
            print("")
            print("-- INVALID OPTION! --")

def auth_student():
    system('cls')
    print("=== COLLEGE MANAGEMENT SYSTEM FOR STUDENT ===")
    print("")
    while 1:
        username = input("USERNAME : ")
        password = input("PASSWORD : ")
        print("")
        securepassword = hashlib.sha256(password.encode()).hexdigest()
        query_vals = (username, securepassword)
        command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'STUDENT'", query_vals)
        if command_handler.rowcount <= 0:
            print("")
            print("-- INVALID LOGIN DETAIL --")
        else:
            student_session(username)

def student_session(username):
    system('cls')
    print("====================================")
    print("  WELCOME, YOU SIGNED IN AS STUDENT")
    print("====================================")
    print("")
    print("MENU : ")
    print("1. VIEW ATTENDANCE REPORT")
    print("2. LOGOUT / MAIN")
    print("")
    while 1:
        user_option = input("PLEASE INSERT VALID OPTION : ")
        if user_option == "1":
            system('cls')
            username = (str(username), )
            command_handler.execute("SELECT date, studentid, fullname, username, status FROM attendance WHERE username = %s ORDER BY date ASC", username)
            records = command_handler.fetchall()
            print("-- ATTENDANCE REPORT --")
            print("")
            if command_handler.rowcount == 0:
                print("")
                print("REPORT EMPTY. PLEASE ASK YOUR TEACHER TO FILL YOUR REPORT!")
            else:
                for data in records:
                    print("======================================")
                    print("STUDENT INFORMATION")
                    print("STUDENT ID : ", data[1])
                    print("NAME       : ", data[2])
                    print("USERNAME   : ", data[3])
                    print("======================================")
                    break
            print("")
            print("--------------------------------------")
            for record in records:
                print("DATE   : ", record[0])
                print("STATUS : ", record[4])
                print("--------------------------------------")
            print("")
            print("STUDENT SESSION (S) / MAIN (M)")
            while 1:
                selesai = input("PLEASE INSERT VALID OPTION => ")
                if selesai == "S" or selesai == "s":
                    student_session(username)
                elif selesai == "M" or selesai == "m":
                    main()
                else:
                    print("INVALID OPTION!")
                    print("")
        elif user_option == "2":
            main()
        else:
            print("-- INVALID OPTION! --")

def auth_teacher():
    system('cls')
    print("")
    print("=== COLLEGE MANAGEMENT SYSTEM FOR TEACHER ===")
    print("")
    while 1:
        username = input(str("USERNAME : "))
        password = input(str("PASSWORD : "))
        print("")
        securepassword = hashlib.sha256(password.encode()).hexdigest()
        query_vals = (username, securepassword)
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
    print("3. VIEW ALL STUDENTS LIST")
    print("4. LOGOUT")
    while 1:
        print("")
        user_option = input(str("PLEASE CHOOSE VALID OPTION : "))
        if user_option == "1":
            system('cls')
            print("")
            print("-- MARK STUDENT ATTENDANCE --")
            command_handler.execute("SELECT * FROM users WHERE privilege = 'STUDENT'")
            records = command_handler.fetchall()
            date = input("INSERT DATE (DD / MM / YYYY) : ")
            print("")
            print("LIST OF STUDENTS")
            print("============================================")
            for data in records:
                nomor = str(data[0])
                print("ID       : " + nomor)
                print("NAME     : " + data[1])
                print("USERNAME : " + data[2])
                print("----------------------------------------")
            print("ABSENT (A) / LATE (L) / PRESENT (P) / QUIT MARK ATTENDANCE (Q)")
            for record in records:
                nomor = str(record[0])
                while 1:
                    status = input("STATUS FOR " + record[1] + " (ID : " + nomor + ") => ")
                    if status == "P" or status == "p" :    
                        query_vals = (date, record[0], record[1], record[2])
                        command_handler.execute("INSERT INTO attendance (date, studentid, fullname, username, status) VALUES (%s, %s, %s, %s, 'PRESENT')", query_vals)
                        db.commit()
                        break
                    elif status == "A" or status == "a" :
                        query_vals = (date, record[0], record[1], record[2])
                        command_handler.execute("INSERT INTO attendance (date, studentid, fullname, username, status) VALUES (%s, %s, %s, %s, 'ABSENT')", query_vals)
                        db.commit()
                        break
                    elif status == "L" or status == "l" :
                        query_vals = (date, record[0], record[1], record[2])
                        command_handler.execute("INSERT INTO attendance (date, studentid, fullname, username, status) VALUES (%s, %s, %s, %s, 'LATE')", query_vals)
                        db.commit()
                        break
                    elif status == "q" or status == "Q":
                        teacher_session()
                    else:
                        print("INVALID OPTION!")
                        print("")
            print("ALL STUDENTS MARKED")
            print("")
            print("BACK TO MAIN (M) / LOGOUT (Q)")
            while 1:
                selesai = input("INSERT VALID CHOICE => ")
                if selesai == "M" or selesai == "m":
                    teacher_session()
                elif selesai == "Q" or selesai == "q":
                    main()
                else:
                    print("INVALID OPTION!")
        elif user_option == "2":
            system('cls')
            print("")
            print("-- STUDENT ATTENDANCE --")
            print("")
            print("==========================================")
            command_handler.execute("SELECT date, studentid, fullname, status FROM attendance ORDER BY date ASC")
            records = command_handler.fetchall()
            for record in records:
                print("DATE         : ", record[0])
                print("STUDENT ID   : ", record[1])
                print("NAME         : ", record[2])
                print("STATUS       : ", record[3])
                print("==========================================")
            print("")
            print("BACK TO MAIN (M) / LOGOUT (Q)")
            while 1:
                selesai = input("INSERT VALID CHOICE => ")
                if selesai == "M" or selesai == "m":
                    teacher_session()
                elif selesai == "Q" or selesai == "q":
                    main()
                else:
                    print("INVALID OPTION!")
        elif user_option == "3":
            system('cls')
            print("LIST OF STUDENT")
            print("")
            for data in records:
                print("STUDENT ID   : ", data[0])
                print("NAME         : ", data[1])
                print("USERNAME     : ", data[2])
                print("==========================================")
            print("")
            print("BACK TO MAIN (M) / LOGOUT (Q)")
            while 1:
                selesai = input("INSERT VALID CHOICE => ")
                if selesai == "M" or selesai == "m":
                    teacher_session()
                elif selesai == "Q" or selesai == "q":
                    main()
                else:
                    print("INVALID OPTION!")
        elif user_option == "4":
            main()
        else:
            print("")
            print("-- INVALID OPTION! --")
                        
def main():
        system('cls')
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
                auth_student()
            elif option == "3":
                auth_teacher()
            else:
                print("INVALID OPTION!")

main()
