import os
import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

screen = Tk()
width = screen.winfo_screenwidth()
height = screen.winfo_screenheight()
# setting tkinter window size
screen.geometry("%dx%d" % (width, height))
screen.title('Forget Password')

image2 = Image.open("backfinal (3).png")
test = ImageTk.PhotoImage(image2)

label2 = Label(image=test)
label2.image = test

label2.place(x=0, y=0)


def ResetPass():
    screen.name = username.get()
    screen.password = password.get()
    screen.confirmpassword = Confirmpassword.get()

    if (screen.name == "") | (str(screen.name).isalpha() == False):
        messagebox.showerror("error", "please enter valid name")
    elif (screen.password == ""):
        messagebox.showerror("error", "please enter password")
    elif (screen.confirmpassword == ""):
        messagebox.showerror("error", "please enter confirm password")
    elif screen.password != screen.confirmpassword:
        messagebox.showerror("error", "password and confirm password should match")
    else:
        conn = mysql.connector.connect(host='localhost', user='root', passwd='anuja1234', database='emojify')
        curr = conn.cursor()

        query = "select * from user where name='username'"
        query = query.replace('username', screen.name)
        #curr.execute("select * from emojify where name=(%s)",(screen.name))
        curr.execute(query)
        row=curr.fetchone()
        print(query, row)
        conn.close()

        if row==None:
            messagebox.showerror('error', 'Incorrect Username')
            return
        elif row[3] == screen.password:
            messagebox.showerror('error', 'New Password should be different from old Password')
        elif len(screen.password) < 8:
            messagebox.showerror('Error', 'Password Should be minimum 8 characters long')
        elif screen.password.isdigit()==True:
            messagebox.showerror('error', 'Password should be alphanumeric')
        elif screen.password.isalpha()==True:
            messagebox.showerror('error', 'Password should be alphanumeric')
        elif screen.password.islower()==True|screen.password.isupper()==True:
            messagebox.showerror('error', 'Password should be mix of upper and lower characters')
        elif screen.password.__contains__('*')==False|screen.password.__contains__('%')==False|screen.password.__contains__('#')==False| \
            screen.password.__contains__('@')==False|screen.password.__contains__('&')==False|screen.password.__contains__('$')==False:
            messagebox.showerror('error', 'Password should contain either of these special character only - *, %, &, $, #, @')
        else:
            conn = mysql.connector.connect(host='localhost', user='root', passwd='anuja1234', database='emojify')
            curr = conn.cursor()
            query="update user set password='psw' where name='usr'"
            query = query.replace('psw', screen.password)
            query= query.replace('usr', screen.name)
            print(query)
            curr.execute(query)
            conn.commit()
            conn.close()
            messagebox.showinfo('success', 'Password is reset, Please login with new password')
            screen.destroy()



Label(screen, text="Reset Password", font="Verdana 28 bold", bd=0).place(x=200, y=80)

# username label and text entry box
usernameLabel = Label(screen, text="User Name", font="Verdana 20").place(x=200, y=160)
username = StringVar()
usernameEntry = Entry(screen, textvariable=username, font="Verdana 20").place(x=200, y=210)

# password label and password entry box
passwordLabel = Label(screen, text="New Password", font="Verdana 20").place(x=200, y=250)
password = StringVar()
passwordEntry = Entry(screen, textvariable=password, show='*', font="Verdana 20").place(x=200, y=300)

# confirm password label and password entry box
ConfirmpasswordLabel = Label(screen, text="Confirm Password", font="Verdana 20").place(x=200, y=340)
Confirmpassword = StringVar()
ConfirmpasswordEntry = Entry(screen, textvariable=Confirmpassword, show='*', font="Verdana 20").place(x=200, y=390)

SubmitButton = Button(screen, text="SUBMIT", font="Georgia 15 bold", height=1, width=15, bd=5,bg="slate blue", command=ResetPass).place(x=200, y=500)

screen.mainloop()