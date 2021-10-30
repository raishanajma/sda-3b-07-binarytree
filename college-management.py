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
        else:
            print("")
            print("-- INVALID OPTION! --")

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

#23:21