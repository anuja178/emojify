import os
from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

def validateLogin():
    uname = username.get()
    upassword = password.get()

    query = "select count(*) from user where name='" + uname + "' and password='" + upassword + "'"
    # print(query)
    conn = mysql.connector.connect(host='localhost', user='root', passwd='anuja1234', database='emojify')

    curr = conn.cursor()
    curr.execute(query)

    rows = curr.fetchone()
    count = rows[0]

    if (count == 1):
        messagebox.showinfo("Login Successfully", "Login Successfully")
        screen.destroy()

        os.system("HomePage.py")
    else:
        messagebox.showerror("Login Failed", "Invalid username and passoword")
    '''newWindow = Tk()

            newWindow.title("New Window")

            newWindow.geometry("200x200")'''

    # Label(newWindow, text="Welcome " + str(uname)).pack()
    conn.close()

def forgetPass():
    os.system('ForgetPassword.py')

def back():
    os.system('mainPage.py')


# window

screen = Tk()
width = screen.winfo_screenwidth()
height = screen.winfo_screenheight()
#setting tkinter window size
screen.geometry("%dx%d" % (width, height))
screen.title('Login')

image2 = Image.open("backgrd.png")
test = ImageTk.PhotoImage(image2)

label2 = Label(image=test)
label2.image = test

label2.place(x=0, y=0)
#loginName
Label(screen, text="LOGIN", font="Verdana 28 bold").place(x=200, y=100)

# username label and text entry box
usernameLabel = Label(screen, text="UserName", font="Verdana 20").place(x=200, y=180)
username = StringVar()
usernameEntry = Entry(screen, textvariable=username, font="Verdana 20" ).place(x=200, y=220)

# password label and password entry box
passwordLabel = Label(screen, text="Password", font="Verdana 20").place(x=200, y=260)
password = StringVar()
passwordEntry = Entry(screen, textvariable=password, show='*',font="Verdana 20").place(x=200, y=300)

# login button
loginButton = Button(screen, text="LOGIN", font="Georgia 15 bold", height=1, width=15, bd=5,bg="slate blue", command=validateLogin).place(x=200, y=420)

back_btn = Button(screen, text="Back", font="Georgia 18 bold underline", height=1, width=10, bd=0)
back_btn.place(x=0, y=630)

back_btn.configure(command=back)

#forgotPassword
forgotPassword = Button(screen, text="Forget Password?", fg='blue', font="Verdana 15 underline",bd='0', command=forgetPass).place(x=200, y=340)

screen.mainloop()

