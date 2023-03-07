import os
from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

screen = Tk()
def clear():
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        phoneNo_entry.delete(0, END)
        password_entry.delete(0, END)
        confirmpassword_entry.delete(0, END)

def back():
    os.system('mainPage.py')

def register():
    screen.name = name_entry.get()
    screen.age = age_entry.get()
    screen.phoneNo = phoneNo_entry.get()
    screen.password = password_entry.get()
    screen.confirmpassword = confirmpassword_entry.get()
    # file_name='registration_record'
    conn = mysql.connector.connect(host='localhost', user='root', passwd='anuja1234', database='emojify')
    curr = conn.cursor()
    query = "select name from user"
    curr.execute(query)
    row = curr.fetchall()
    print(row)
    conn.close()

    if (screen.name == "") | (str(screen.name).isalpha() == False):
        messagebox.showerror("error", "please enter valid name")
    elif (screen.age == "") | (str(screen.age).isdigit() == False):
        messagebox.showerror("error", "please enter age in numeric")
    elif (int(screen.age) > 100):
        messagebox.showerror("error", "please enter age below 100")
    elif (screen.phoneNo == "") | (str(screen.phoneNo).isdigit() == False) | (len(str(screen.phoneNo)) != 10):
        messagebox.showerror("error", "please enter 10 digit phone number in numeric")
    elif (screen.password == ""):
        messagebox.showerror("error", "please enter password")
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
    elif (screen.confirmpassword == ""):
        messagebox.showerror("error", "please enter confirm password")
    elif screen.password != screen.confirmpassword:
        messagebox.showerror("error", "password and confirm password should match")
    # elif row != None:
    #     while i in row:
    #         if i == screen.name:
    #             messagebox.showerror('error', 'This username is not available. Please try another one ')
    # #           break
    # #     print('for loop ended')
    # #     #messagebox.showinfo('success', 'user name in available')
    else:
        mydb = mysql.connector.connect(host='localhost', user='root', passwd='anuja1234', database='emojify')
        mycursor = mydb.cursor()
        mycursor.execute("insert into user values (%s,%s,%s,%s)",
                         (screen.name, screen.age, screen.phoneNo, screen.password))
        mydb.commit()
        messagebox.showinfo("Success", 'Registration Successful')
        #  Label(screen,text="Registration successful", font="30").place(x=230, y=255)
        #  write to file only when all valid details entered in form as per validations above
        # '''with open(file_name + ".csv", "a") as f:
        #     # permission a is for append
        #     f.write(self.name + ",")
        #     f.write(self.age + ",")
        #     f.write(self.phoneNo + ",")
        #     f.write(self.password + ",")
        #     f.write(self.confirmpassword + "\n")'''


#
screen.title("REGISTRATION FORM")
width = screen.winfo_screenwidth()
height = screen.winfo_screenheight()
#setting tkinter window size
screen.geometry("%dx%d" % (width, height))

'''image2 = Image.open("backSmile.png")
test = ImageTk.PhotoImage(image2)

label2 = Label(image=test)
label2.image = test

label2.place(x=0, y=0)
'''
# label(heading)
Label(screen, text="REGISTRATION FORM", font="Georgia 35 bold", bg="red", fg="white").pack(fill="both")

# name, age, phoneNo, username, password, confirmpassword
Label(screen, text="UserName", font="Verdana 25").place(x=330, y=120)
Label(screen, text="Age", font="Verdana 25").place(x=330, y=190)
Label(screen, text="Phone No", font="Verdana 25").place(x=330, y=260)
Label(screen, text="Password", font="Verdana 25").place(x=330, y=330)
Label(screen, text="Confirm Password", font="Verdana 25").place(x=330, y=400)


# entry
name_info = StringVar()
age_info = StringVar()
phoneNo_info = StringVar()
password_info = StringVar()
confirmpassword_info = StringVar()

name_entry = Entry(screen, font="Verdana 15", bd=5, textvariable="name_info")
name_entry.place(x=800, y=120)
age_entry = Entry(screen, font="Verdana 15", bd=5, textvariable="age_info")
age_entry.place(x=800, y=190)
phoneNo_entry = Entry(screen, font="Verdana 15", bd=5, textvariable="phoneNo_info")
phoneNo_entry.place(x=800, y=260)
password_entry = Entry(screen, font="Verdana 15", bd=5, textvariable="password_info", show="*")
password_entry.place(x=800, y=330)
confirmpassword_entry = Entry(screen, font="Verdana 15", bd=5, textvariable="confirmpassword_info", show="*")
confirmpassword_entry.place(x=800, y=400)


# button
register_btn = Button(screen, text="Register", font="Georgia 23 bold", height=1, width=10, fg='blue')
register_btn.place(x=600, y=500)
clear_btn = Button(screen, text="Clear", font="Georgia 18 bold underline", height=1, width=10, bd=0)
clear_btn.place(x=1100, y=600)
back_btn = Button(screen, text="Back", font="Georgia 18 bold underline", height=1, width=10, bd=0)
back_btn.place(x=100, y=600)

register_btn.configure(command=register)
clear_btn.configure(command=clear)
back_btn.configure(command=back)


mainloop()
