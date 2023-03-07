import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os
import numpy as np
import cv2
from tensorflow.keras.models import Sequential
from keras.layers import Dense, Dropout,Flatten
from keras.layers import Conv2D
from keras.optimizers import Adam
from keras.layers import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
import threading

emotion_model = Sequential()
emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(7, activation='softmax'))
emotion_model.load_weights('model.h5')
cv2.ocl.setUseOpenCL(False)

emotion_dict = {0: " Angry ", 1: " Disgusted ", 2: " Fearful ", 3: " Happy ", 4: " Neutral ", 5: " Sad ", 6: " Surprise " }

cur_path = os.path.dirname(os.path.abspath(__file__))

emoji_dist = {0:cur_path+"/emoji/angry_f.png", 1:cur_path+"/emoji/disgust_f.png", 2:cur_path+"/emoji/fear_f.png", 3:cur_path+"/emoji/happy_f.png", 4:cur_path+"/emoji/netural_f.png", 5:cur_path+"/emoji/sad_f.png", 6:cur_path+"/emoji/surprise_f.png"}

global last_frame1
last_frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
global cap1
show_text=[0]
global frame_number

def show_subject():
    cap1 = cv2.VideoCapture(0)
    if not cap1.isOpened():
        print("can't open the camera")
    global frame_number
    # length = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_number += 1
    # if frame_number>= length:
    #     exit()
    cap1.set(1, frame_number)
    flag1, frame1 = cap1.read()
    frame1 = cv2.resize(frame1,(600, 500))
    bounding_box = cv2.CascadeClassifier('C:/Users/Anuja/PycharmProjects/recognition/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    gray_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    num_faces= bounding_box.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)
    for(x, y, w, h) in num_faces:
        cv2.rectangle(frame1, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
        roi_gray_frame = gray_frame[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)
        predication = emotion_model.predict(cropped_img)
        maxindex = int(np.argmax(predication))
        cv2.putText(frame1, emotion_dict[maxindex], (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        show_text[0]=maxindex
    if flag1 is None:
        print("Major error!")
    elif flag1:
        global last_frame1
        last_frame1 = frame1.copy()
        pic = cv2.cvtColor(last_frame1, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(pic)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imagtk = imgtk
        lmain.configure(image=imgtk)
        root.update()
        lmain.after(10, show_subject)
        show_avatar()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit()
#
def show_avatar():
    frame2 = cv2.imread(emoji_dist[show_text[0]])
    pic2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
    img2 = Image.fromarray(pic2)
    imgtk2 = ImageTk.PhotoImage(image=img2)
    lmain2.imgtk2 = imgtk2
    lmain3.configure(text=emotion_dict[show_text[0]], font=('arial', 45, 'bold'))
    lmain2.configure(image=imgtk2)
    root.update()
    lmain2.after(10, show_avatar)

def Back():
    os.system("HomePage.py")

if __name__ == "__main__":
    frame_number = 0
    root = tk.Tk()
    root.title("photo to emoji")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    # setting tkinter window size
    root.geometry("%dx%d" % (width, height))
    root['bg']='gold'
    # image2 = Image.open("cam.png")
    # test = ImageTk.PhotoImage(image2)
    #
    # label2 = Label(image=test)
    # label2.image = test
    #
    # label2.place(x=0, y=0)

    lmain = tk.Label(master=root, padx=50, bd=10,  fg="#CDCDCD", bg="black")
    lmain2 = tk.Label(master=root, bd=10, fg="#CDCDCD", bg="black")
    lmain3 = tk.Label(master=root, bd=10, fg="#CDCDCD", bg="black")
    lmain.pack(side=LEFT)
    lmain.place(x=100, y=50)
    lmain3.pack()
    lmain3.place(x=1000, y=100)
    lmain2.pack(side=RIGHT)
    lmain2.place(x=1000, y=200)


    # LogOut image
    # image4 = Image.open("LogPas.png")
    # test = ImageTk.PhotoImage(image4)
    #
    # # Logout button
    # LogoutButton = Button(root, image=test, bd=0, command=root.destroy)
    # LogoutButton.image = test
    # LogoutButton.place(x=700, y=600)

    BackButton = Button(root, text='Back', fg="Black", command=Back,
                        font=('arial', 25, 'bold', 'underline')).place(x=550, y=600)
    exitButton = Button(root, text='Quit', fg="Black", command=root.destroy, font=('arial',25,'bold','underline')).place(x=750, y=600)
    # show_subject()
    # show_avatar()
    #flag = 0
    #if flag == 0:
    threading.Thread(target=show_subject).start()
    threading.Thread(target=show_avatar).start()
    #flag = 1
    root.mainloop()