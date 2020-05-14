from tkinter import *
import os
from Follower import *
from Unfollower import *
import sys
from functools import partial

def followstart():
    get_credential(username.get(),password.get(),Tags.get())

def unfollowstart():
    unfollow_it(username.get(),password.get())


tkWindow=Tk()
tkWindow.geometry=('500x600')
tkWindow.title('Insta Follower/Unfollower')

usernameLabel=Label(tkWindow,text="Username", height="3").grid(row=0,column=0)
username=StringVar()
usernameEntry=Entry(tkWindow,textvariable=username).grid(row=0,column=1)

passwordLabel=Label(tkWindow,text="Password",height="3").grid(row=2,column=0)
password=StringVar()
passwordEntry=Entry(tkWindow,textvariable=password,show='*').grid(row=2,column=1)
TagsLabel=Label(tkWindow,text="Tags (sep ,)", height="3", width="10").grid(row=3,column=0)  
Tags=StringVar()
TagsEntry=Entry(tkWindow,textvariable=Tags).grid(row=3,column=1)
# FollowerStart=Button(tkWindow,text="Follow",width="15",command=followstart).grid(row=6,column=0)
FollowerStart=Button(tkWindow,text="Follow",width="15",command=followstart).grid(row=6,column=0)
UnfollowerStart=Button(tkWindow,text="Unfollow",width="15",command=unfollowstart).grid(row=6,column=1)

tkWindow.mainloop()

