from tkinter import *
from tkinter import messagebox
import os
from PIL import Image, ImageTk
class FirstPage(Tk) :
    def __init__(self):
        super(FirstPage,self).__init__()

        self.title("First page")
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))

        image2 = Image.open("Back1.png")
        test = ImageTk.PhotoImage(image2)

        label2 = Label(image=test)
        label2.image = test

        label2.place(x=0, y=0)

        '''bg = PhotoImage(file="backfinal.jpg")
        self.label1 = Label(image=bg)
        self.label1.place(x=0, y=0)'''


        self.lbl1= Label(self, text="EMOJIFY", font="Georgia 90 bold", fg="red").place(x=420, y=450)

        # button
        self.bt1 = Button(self, text="Register", font="RockwellExtraBold 20 bold underline", command=self.clickme_register, bd=0)
        self.bt1.place(x=1100, y=30)

        self.bt2 = Button(self, text="Login", font="RockwellExtraBold 20 bold underline", command=self.clickme_login, bd=0)
        self.bt2.place(x=1250, y=30)



    def clickme_register(self):
        os.system('registrationpage.py')


    def clickme_login(self):
        os.system('loginPage.py')


root=FirstPage()
root.mainloop()

# screen = Tk()
# screen.title("First page")
# screen.geometry("500x500")
# # nameOfApp
# Label(screen,text="EMOJIFY", font="RockwellExtraBold 50 bold", fg="red").place(x=100, y=150)
#
# # button
# bt1=Button(screen,text="Register", font="RockwellExtraBold 30 bold",command=clickme)
# bt1.place(x=150, y=250)
#
#
# bt2=Button(screen,text="Login", font="RockwellExtraBold 30 bold",command=clickme)
# bt2.place(x=150, y=350)
