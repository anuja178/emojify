import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

screen = Tk()
screen.title("Home page")
width = screen.winfo_screenwidth()
height = screen.winfo_screenheight()
#setting tkinter window size
screen.geometry("%dx%d" % (width, height))
#screen.configure(bg="plum")

image2 = Image.open("HomePage.png")
test = ImageTk.PhotoImage(image2)

label2 = Label(image=test)
label2.image = test

label2.place(x=0, y=0)

#backgroundImg
#img= PhotoImage(file='', master= screen)
#img_label= Label(screen,image=img)

#define the position of the image
# img_label.place(x=0, y=90)
#draw line
#canvas = Canvas(screen, width=1347, height=80)
#canvas.pack()

#canvas.create_line(5, 60, 1345, 60, width=3)
heading = Label(screen, text="EMOJIFY", font="Georgia 40 bold", fg="red").place(x=20, y=15)



#logo
'''logoImg = PhotoImage(file="emojify-logos.png")
Label(screen, image=logoImg, height=100, width=100).place(x=600, y=10)'''

def PermissionCam():
    cam=messagebox.askyesno("permission", "Use your camera...?")

    if(cam==1):
        os.system("emoji.py")
    else:
        messagebox.showerror("NoUse", "Sorry Try Again....")
        exit()

def ChangPass():
    os.system('ForgetPassword.py')

def LogOut():
    os.system('mainPage.py')

#Camera image
camImage = PhotoImage(file="device-camera-icon.png")

#camera button
camButton = Button(screen, image=camImage, height=100, width=150, bd=0, command=PermissionCam).place(x=585, y=500)

#profilelogo
image1 = Image.open("ProfileLogo1.jpg")
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

# Position image
label1.place(x=15, y=100)


#profileDetails

image2 = Image.open("ProfileDetails1.png")
test = ImageTk.PhotoImage(image2)

label2 = Label(image=test)
label2.image = test

# Position image
label2.place(x=230, y=100)

#QuotesImg
image5 = Image.open("emoji.png")
test = ImageTk.PhotoImage(image5)

label2 = Label(image=test)
label2.image = test

# Position image
label2.place(x=970, y=290)


#change Passimage
image3 = Image.open("CPass.png")
test = ImageTk.PhotoImage(image3)

#CHangePassword button
ChangePassButton = Button(screen, image=test, bd=0, command=ChangPass)
ChangePassButton.image = test
ChangePassButton.place(x=300, y=490)

#LogOut image
image4 = Image.open("LogPas.png")
test = ImageTk.PhotoImage(image4)

#Logout button
LogoutButton = Button(screen, image=test, bd=0, command=LogOut)
LogoutButton.image = test
LogoutButton.place(x=900, y=500)

UserName = Label(screen, text="UserName", font="Georgia 15 bold").place(x=280, y=160)
Age = Label(screen, text="Age", font="Georgia 15 bold").place(x=280, y=235)
PhoneNo = Label(screen, text="PhoneNo", font="Georgia 15 bold").place(x=280, y=310)

Quotes = Label(screen, text="Emojis are not Only", font="Georgia 26 bold").place(x=680, y=160)
Quotes1 = Label(screen, text="the Stickers,", font="Georgia 26 bold").place(x=680, y=230)
Quotes2 = Label(screen, text="it's a EMotion..", font="Georgia 26 bold").place(x=680, y=300)

mainloop()


