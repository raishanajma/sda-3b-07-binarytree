import mysql.connector as mysql
import hashlib
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter import ttk

host = "localhost"
user = "root"
password = ""
database = "College"

db = mysql.connect(host = host, user = user, password = password, database = database)
command_handler = db.cursor(buffered = True)

root = Tk()
root.geometry("650x500")
root.title("ATTENDANCE MANAGER")
style = ttk.Style()

style.theme_use("default")
style.configure("Treeview", background = "#D3D3D3", foreground = "black", fieldbackground = "#D3D3D3")

def auth_admin():
    authadmin = Frame(root)
    authadmin.pack()
    labeladmin = tk.Label(authadmin, text = "\nATTENDANCE MANAGEMENT SYSTEM FOR ADMIN\n", fg = "#283618", font = ("calibri", 12, "bold")).pack(side = "top")
    lusername = tk.Label(authadmin, text = "USERNAME", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    username = tk.Entry(authadmin, width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    username.pack(padx = 5, pady = 5)
    lpassword = tk.Label(authadmin, text = "PASSWORD", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    password = tk.Entry(authadmin, show = "*", width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    password.pack(padx = 5, pady = 5)
    whitespace = tk.Label(authadmin, text = "\n \n").pack()
    loginbtn = tk.Button(authadmin, text = "Login  🡪", command = lambda: (validateadmin(username, password, authadmin), username, password), width = 10, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "right", padx = 10, pady = 15)
    mainbtn = tk.Button(authadmin, text = "🡨  Back", command = lambda: (authadmin.destroy(), main()), width = 10, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "left", padx = 10, pady = 15)

def validateadmin(username, password, authadmin):
    usernamePassed = username.get()
    passwordPassed = password.get()
    if usernamePassed == "admin" :
        if passwordPassed == "password":
            authadmin.destroy()
            admin_session()
        else:
            tkinter.messagebox.showwarning("WARNING", "Password you entered is incorrect!")
    else:
        tkinter.messagebox.showwarning("WARNING", "Username you entered is incorrect!")

def admin_session():
    adminsession = Frame(root)
    adminsession.pack()
    welcome = tk.Label(adminsession, text = "\nWELCOME\nYOU SIGNED IN AS ADMIN\n", fg = "#283618", font = ("calibri", 12, "bold")).pack(side = "top")
    registerstudent = tk.Button(adminsession, text = "Register new student", command = lambda: (registeringstudent(adminsession)), width = 18, font = ("Calibri"), bg = "#606C38", fg = "#FEFAE0", activebackground = "#7f5539")
    registerstudent.pack(padx = 10, pady = 10)
    registerteacher = tk.Button(adminsession, text = "Register new teacher", command = lambda: (registeringteacher(adminsession)), width = 18, font = ("Calibri"), bg = "#606C38", fg = "#FEFAE0", activebackground = "#7f5539")
    registerteacher.pack(padx = 10, pady = 10)
    deletestudent = tk.Button(adminsession, text = "Delete student", command = lambda: (deletingstudent(adminsession)), width = 18, font = ("Calibri"), bg = "#606C38", fg = "#FEFAE0", activebackground = "#7f5539")
    deletestudent.pack(padx = 10, pady = 10)
    deleteteacher = tk.Button(adminsession, text = "Delete teacher", command = lambda: (deletingteacher(adminsession)), width = 18, font = ("Calibri"), bg = "#606C38", fg = "#FEFAE0", activebackground = "#7f5539")
    deleteteacher.pack(padx = 10, pady = 10)
    whitespace = tk.Label(adminsession, text = "\n \n").pack()
    logoutbtn = tk.Button(adminsession, text = "Logout", command = lambda: (adminsession.destroy(), auth_admin()), width = 13, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "right", padx = 10, pady = 10)
    mainbtn = tk.Button(adminsession, text = "Back to main", command = lambda: (adminsession.destroy(), main()), width = 13, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "left", padx = 10, pady = 10)

def registeringstudent(adminsession):
    adminsession.destroy()
    registstudent = Frame(root)
    registstudent.pack()
    welcome = tk.Label(registstudent, text = "\nREGISTER NEW STUDENT\n ", fg = "#283618", font = ("calibri", 12, "bold")).pack(side = "top")
    lfullname = tk.Label(registstudent, text = "Insert student's name", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    fullname = tk.Entry(registstudent, width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    fullname.pack(padx = 5, pady = 5)
    lusername = tk.Label(registstudent, text = "Insert student's username", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    username = tk.Entry(registstudent, width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    username.pack(padx = 5, pady = 5)
    lpassword = tk.Label(registstudent, text = "Insert student's password", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    password = tk.Entry(registstudent, width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    password.pack(padx = 5, pady = 5)
    whitespace = tk.Label(registstudent, text = "\n \n \n").pack()
    savebtn = tk.Button(registstudent, text = "Save  🡪", command = lambda: (savestudent(fullname, username, password), fullname, username, password), width = 13, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "right", padx = 10, pady = 10)
    backbtn = tk.Button(registstudent, text = "🡨  Back", command = lambda: (registstudent.destroy(), admin_session()), width = 13, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "left", padx = 10, pady = 10)

def savestudent(fullname, username, password):
    fullnamePassed = fullname.get()
    usernamePassed = username.get()
    passwordPassed = password.get()
    securepassword = hashlib.sha256(passwordPassed.encode()).hexdigest()
    query_vals = (fullnamePassed, usernamePassed, securepassword)
    command_handler .execute("INSERT INTO users (fullname, username, password, privilege) VALUES (%s, %s, %s, 'STUDENT')", query_vals)
    db.commit()
    tkinter.messagebox.showinfo("SUCCESS", "Student successfully added!")

def registeringteacher(adminsession):
    adminsession.destroy()
    registteacher = Frame(root)
    registteacher.pack()
    welcome = tk.Label(registteacher, text = "\nREGISTER NEW STUDENT\n ", fg = "#283618", font = ("calibri", 12, "bold")).pack(side = "top")
    lfullname = tk.Label(registteacher, text = "Insert teacher's name", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    fullname = tk.Entry(registteacher, width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    fullname.pack(padx = 5, pady = 5)
    lusername = tk.Label(registteacher, text = "Insert teacher's username", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    username = tk.Entry(registteacher, width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    username.pack(padx = 5, pady = 5)
    lpassword = tk.Label(registteacher, text = "Insert teacher's password", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    password = tk.Entry(registteacher, width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    password.pack(padx = 5, pady = 5)
    whitespace = tk.Label(registteacher, text = "\n \n \n").pack()
    savebtn = tk.Button(registteacher, text = "Save  🡪", command = lambda: (saveteacher(fullname, username, password), fullname, username, password), width = 13, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "right", padx = 10, pady = 10)
    backbtn = tk.Button(registteacher, text = "🡨  Back", command = lambda: (registteacher.destroy(), admin_session()), width = 13, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "left", padx = 10, pady = 10)

def saveteacher(fullname, username, password):
    fullnameget = fullname.get()
    usernameget = username.get()
    passwordget = password.get()
    securepassword = hashlib.sha256(passwordget.encode()).hexdigest()
    query_vals = (fullnameget, usernameget, securepassword)
    command_handler.execute("INSERT INTO users (fullname, username, password, privilege) VALUES (%s, %s, %s, 'TEACHER')", query_vals)
    db.commit()
    tkinter.messagebox.showinfo("SUCCESS", "Teacher successfully added!")

def deletingstudent(adminsession):
    adminsession.destroy()
    delstudent = Frame(root)
    delstudent.pack()
    welcome = tk.Label(delstudent, text = "\nDELETE EXISTING STUDENT\n ", fg = "#283618", font = ("calibri", 12, "bold")).pack(side = "top")
    lusername = tk.Label(delstudent, text = "Insert student's username", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    username = tk.Entry(delstudent, width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    username.pack(padx = 5, pady = 5)
    whitespace = tk.Label(delstudent, text = "\n ").pack()
    deltbtn = tk.Button(delstudent, text = "Delete  🡪", width = 13, command = lambda: (dstudent(username), username), font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "right", padx = 5, pady = 5)
    backbtn = tk.Button(delstudent, text = "🡨  Back", width = 13, command = lambda: (delstudent.destroy(), admin_session()), font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "left", padx = 5, pady = 5)

def dstudent(username):
    username = username.get()
    query_vals = (username, "STUDENT")
    command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
    db.commit()
    if command_handler.rowcount < 1:
        tkinter.messagebox.showwarning("NOT FOUND", "Student's username not found!")
    else:
        tkinter.messagebox.showinfo("SUCCESS", "Student has been deleted!")

def deletingteacher(adminsession):
    adminsession.destroy()
    delteacher = Frame(root)
    delteacher.pack()
    welcome = tk.Label(delteacher, text = "\nDELETE EXISTING TEACHER\n ", fg = "#283618", font = ("calibri", 12, "bold")).pack(side = "top")
    lusername = tk.Label(delteacher, text = "Insert teacher's username", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    username = tk.Entry(delteacher, width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    username.pack(padx = 5, pady = 5)
    whitespace = tk.Label(delteacher, text = "\n ").pack()
    deltbtn = tk.Button(delteacher, text = "Delete  🡪", command = lambda: (dteacher(username), username), width = 13, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "right", padx = 10, pady = 10)
    backbtn = tk.Button(delteacher, text = "🡨  Back", command = lambda: (delteacher.destroy(), admin_session()), width = 13, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "left", padx = 10, pady = 10)

def dteacher(username):
    username = username.get()
    query_vals = (username, "TEACHER")
    command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
    db.commit()
    if command_handler.rowcount < 1:
        tkinter.messagebox.showwarning("NOT FOUND", "Teacher's username not found!")
    else:
        tkinter.messagebox.showinfo("SUCCESS", "Teacher has been deleted!")

def auth_student():
    authstudent = Frame(root)
    authstudent.pack()
    labelstudent = tk.Label(authstudent, text = "\nATTENDANCE MANAGEMENT SYSTEM FOR STUDENT\n", fg = "#283618", font = ("calibri", 12, "bold")).pack()
    lusername = tk.Label(authstudent, text = "USERNAME", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    username = tk.Entry(authstudent, width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    username.pack(padx = 5, pady = 5)
    lpassword = tk.Label(authstudent, text = "PASSWORD", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    password = tk.Entry(authstudent, show = "*", width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    password.pack(padx = 5, pady = 5)
    whitespace = tk.Label(authstudent, text = "\n ").pack()
    loginbtn = tk.Button(authstudent, text = "Login  🡪", command = lambda: (validatestudent(username, password, authstudent), username, password), width = 10, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "right", padx = 10, pady = 15)
    mainbtn = tk.Button(authstudent, text = "🡨  Back", command = lambda: (authstudent.destroy(), main()), width = 10, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "left", padx = 10, pady = 15)

def validatestudent(username, password, authstudent):
    passwordPassed = password.get()
    securepassword = hashlib.sha256(passwordPassed.encode()).hexdigest()
    username = username.get()
    query_vals = (username, securepassword)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'STUDENT'", query_vals)
    if command_handler.rowcount <= 0:
        tkinter.messagebox.showwarning("WARNING", "Login details you entered is incorrect!")
    else:
        command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'STUDENT'", query_vals)
        datas = command_handler.fetchall()
        for data in datas:
            idstudent = data[0]
            fullname = data[1]
        authstudent.destroy()
        student_session(idstudent, fullname, username)

def student_session(idstudent, fullname, username):
    studentsession = Frame(root)
    studentsession.pack()
    welcome = tk.Label(studentsession, text = "\nWELCOME\nYOU SIGNED IN AS STUDENT\n ", fg = "#283618", font = ("calibri", 12, "bold")).pack(side = "top")
    attendancebtn = tk.Button(studentsession, text = "View attendance report", command = lambda: attendancereport(idstudent, fullname, username, studentsession), width = 20, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(padx = 10, pady = 15)
    logout = tk.Button(studentsession, text = "Logout", command = lambda: (studentsession.destroy(), auth_student()), width = 10, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "bottom", padx = 10, pady = 15)

def attendancereport(idstudent, fullname, username, studentsession):
    studentsession.destroy()
    attendreport = Frame(root)
    attendreport.pack()
    idstudent = str(idstudent)
    fullname = str(fullname)
    username = str(username)
    labelreport = tk.Label(attendreport, text = ("\n\nStudent's ID : " + idstudent + "\nStudent's name : " + fullname + "\nStudent's username : " + username), font = ("calibri", 12,), justify = "left").pack()
    whitespace = tk.Label(attendreport, text = "\n ").pack()
    scrolltabley = Scrollbar(attendreport)
    scrolltabley.pack(side = "right", fill = "y")
    scrolltablex = Scrollbar(attendreport, orient = "horizontal")
    scrolltablex.pack(side = "bottom", fill = "x")
    tablereport = ttk.Treeview(attendreport, columns = (1, 2), show = "headings", height = 10, yscrollcommand = scrolltabley.set, xscrollcommand = scrolltablex.set)
    tablereport.pack(pady = 20)
    scrolltabley.config(command = tablereport.yview)
    scrolltablex.config(command = tablereport.xview)
    tablereport.heading(1, text = "DATE")
    tablereport.heading(2, text = "STATUS")
    command_handler.execute("SELECT date, status FROM attendance ORDER BY date ASC")
    records = command_handler.fetchall()
    for data in records:
        tablereport.insert('', 'end', values = data)

def auth_teacher():
    authteacher = Frame(root)
    authteacher.pack()
    labelteacher = tk.Label(authteacher, text = "\nATTENDANCE MANAGEMENT SYSTEM FOR TEACHER\n", fg = "#283618", font = ("calibri", 12, "bold")).pack()
    lusername = tk.Label(authteacher, text = "USERNAME", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    username = tk.Entry(authteacher, width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    username.pack(padx = 5, pady = 5)
    lpassword = tk.Label(authteacher, text = "PASSWORD", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    password = tk.Entry(authteacher, show = "*", width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    password.pack(padx = 5, pady = 5)
    whitespace = tk.Label(authteacher, text = "\n ").pack()
    loginbtn = tk.Button(authteacher, text = "Login  🡪", command = lambda: (validateteacher(username, password, authteacher), username, password), width = 10, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "right", padx = 10, pady = 15)
    mainbtn = tk.Button(authteacher, text = "🡨  Back", command = lambda: (authteacher.destroy(), main()), width = 10, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "left", padx = 10, pady = 15)

def validateteacher(username, password, authteacher):
    passwordPassed = password.get()
    securepassword = hashlib.sha256(passwordPassed.encode()).hexdigest()
    usernamePassed = username.get()
    query_vals = (usernamePassed, securepassword)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'TEACHER'", query_vals)
    if command_handler.rowcount <= 0:
        tkinter.messagebox.showwarning("WARNING", "Login details you entered is incorrect!")
    else:
        authteacher.destroy()
        teacher_session()

def teacher_session():
    teachersession = Frame(root)
    teachersession.pack()
    welcome = tk.Label(teachersession, text = "\nWELCOME\nYOU SIGNED IN AS TEACHER\n ", fg = "#283618", font = ("calibri", 12, "bold")).pack(side = "top")
    markstudent = tk.Button(teachersession, text = "Mark student attendance", command = lambda: markstudents(teachersession), width = 25, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(padx = 10, pady = 10)
    viewstudent = tk.Button(teachersession, text = "View student attendance", command = lambda: viewstudentreport(teachersession), width = 25, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(padx = 10, pady = 10)
    whitespace = tk.Label(teachersession, text = "\n \n").pack()
    logoutbtn = tk.Button(teachersession, text = "Logout", command = lambda: (teachersession.destroy(), auth_teacher()), width = 10, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "bottom", padx = 10, pady = 15)
    

def viewstudentreport(teachersession):
    teachersession.destroy()
    viewattend = Frame(root)
    viewattend.pack()
    labelview = tk.Label(viewattend, text = "\nSTUDENT ATTENDANCE\n", fg = "#283618", font = ("calibri", 12, "bold")).pack(side = "top")
    scrolltabley = Scrollbar(viewattend)
    scrolltabley.pack(side = "right", fill = "y")
    scrolltablex = Scrollbar(viewattend, orient = "horizontal")
    scrolltablex.pack(side = "bottom", fill = "x")
    tablereport = ttk.Treeview(viewattend, columns = (1, 2, 3, 4, 5), show = "headings", height = 10, yscrollcommand = scrolltabley.set, xscrollcommand = scrolltablex.set)
    tablereport.pack(pady = 20)
    scrolltabley.config(command = tablereport.yview)
    scrolltablex.config(command = tablereport.xview)
    tablereport.heading(1, text = "DATE")
    tablereport.heading(2, text = "STUDENT ID")
    tablereport.heading(3, text = "NAME")
    tablereport.heading(4, text = "USERNAME")
    tablereport.heading(5, text = "STATUS")
    command_handler.execute("SELECT date, studentid, fullname, username, status FROM attendance ORDER BY date ASC")
    records = command_handler.fetchall()
    for data in records:
        tablereport.insert('', 'end', values = data)
    whitespace = tk.Label(viewattend, text = "\n ").pack()
    mainbtn = tk.Button(viewattend, text = "🡨  Back", command = lambda: (viewattend.destroy(), teacher_session()), width = 10, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(padx = 10, pady = 15)


def markstudents(teachersession):
    teachersession.destroy()
    markstd = Frame(root)
    markstd.pack()
    welcome = tk.Label(markstd, text = "\nMARK STUDENT'S ATTENDANCE\n\n", fg = "#283618", font = ("Calibri", 12, "bold")).pack()
    ldate = tk.Label(markstd, text = "DATE (DD)", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    date = tk.Entry(markstd, width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    date.pack(padx = 5, pady = 5)
    lmonth = tk.Label(markstd, text = "MONTH (MM)", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    month = tk.Entry(markstd, width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    month.pack(padx = 5, pady = 5)
    lyear = tk.Label(markstd, text = "YEAR (YYYY)", fg = "#283618", font = ("calibri", 11, "bold")).pack(padx = 10, pady = 5)
    year = tk.Entry(markstd, width = 15, fg = "#283618", font = ("roboto", 10, "normal"))
    year.pack(padx = 5, pady = 5)
    whitespace = tk.Label(markstd, text = "\n \n").pack()
    nextbtn = tk.Button(markstd, text = "Next  🡪", command = lambda: (check(date, month, year, markstd), date, month, year), width = 10, font = ("Calibri"), bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "right", padx = 10, pady = 15)
    mainbtn = tk.Button(markstd, text = "🡨  Back", command = lambda: (markstd.destroy(), teacher_session()), width = 10, font = ("Calibri"), bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "left", padx = 10, pady = 15)

def check(date, month, year, markstd):
    markstud2 = Frame(root)
    markstud2.pack()
    datePassed = date.get()
    datePassed = str(datePassed)
    monthPassed = month.get()
    monthPassed = str(monthPassed)
    yearPassed = year.get()
    yearPassed = str(yearPassed)
    markstd.destroy()
    fulltime = datePassed + " / " + monthPassed + " / " + yearPassed
    option = ["ABSENT", "LATE", "PRESENT"]
    welcome = tk.Label(markstud2, text = "\nMARK STUDENT'S ATTENDANCE\n", fg = "#283618", font = ("Calibri", 12, "bold")).pack()
    tanggal = tk.Label(markstud2, text = ("Date : " + fulltime + "\n "), fg = "#283618", font = ("Calibri", 11, "bold")).pack(anchor = "w")
    command_handler.execute("SELECT * FROM users WHERE privilege = 'STUDENT'")
    records = command_handler.fetchall()
    for data in records:
        tk.Label(markstud2, text = ("Student's name     : " + data[1]), fg = "#283618", font = ("Calibri", 11, "bold"), justify = "left").pack(anchor = "w")
        tk.Label(markstud2, text = ("Student's username : " + data[2]), fg = "#283618", font = ("Calibri", 11, "bold"), justify = "left").pack(anchor = "w")
        statustoday = ttk.Combobox(markstud2, values = option, width = 15)
        statustoday.pack()
        studentid = data[0]
        fullname = data[1]
        username = data[2]
        whitespace = tk.Label(markstud2, text = "\n ---------------------------------------- \n").pack()
    nextbtn = tk.Button(markstud2, text = "Next  🡪", command = lambda: (getSelection(fulltime, studentid, fullname, username, statustoday), fulltime, studentid, fullname, username, statustoday), width = 10, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "right", padx = 10, pady = 15)
    mainbtn = tk.Button(markstud2, text = "🡨  Back", command = lambda: (markstud2.destroy(), teacher_session()), width = 10, font = "Calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(side = "left", padx = 10, pady = 15)

def getSelection(fulltime, studentid, fullname, username, statustoday):
    val = statustoday.get()
    query_vals = (fulltime, studentid, fullname, username, val) 
    command_handler.execute("INSERT INTO attendance (date, studentid, fullname, username, status) VALUES (%s, %s, %s, %s, %s)", query_vals)
    db.commit()
    tkinter.messagebox.showinfo("SUCCESS", "Student has been marked!")

def main():
    frame = Frame(root)
    frame.pack()
    opening = tk.Label(frame, text = "\nWELCOME TO ATTENDANCE MANAGEMENT SYSTEM\n", fg = "#283618", font = ("calibri", 12, "bold")).pack()
    btnadmin = tk.Button(frame, text = "Login as Admin", command = lambda: (frame.destroy(), auth_admin()), width = 15, font = "calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(padx = 10, pady = 5)
    btnstudent = tk.Button(frame, text = "Login as Student", command = lambda: (frame.destroy(), auth_student()), width = 15, font = "calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(padx = 10, pady = 5)
    btnteacher = tk.Button(frame, text = "Login as Teacher", command = lambda: (frame.destroy(), auth_teacher()), width = 15, font = "calibri", bg = "#606C38", fg = "#FEFAE0", activebackground = "#7F5539").pack(padx = 10, pady = 5)
    root.mainloop()

main()
