from tkinter import *
from Follower import *
from Unfollower import *
from functools import partial

tkWindow=Tk()
def followstart():
    get_credential(username.get(),password.get(),Tags.get(),Follow_.get(),tkWindow)

def unfollowstart():
    unfollow_it(username.get(),password.get(),tkWindow)

def on_click(event):
    TagsEntry.configure(state=NORMAL)
    TagsEntry.delete(0, END)
tkWindow.geometry=("250x1300")
tkWindow.title('Insta Bot')
tkWindow.maxsize(250,250)
tkWindow.minsize(250,250)
usernameLabel=Label(tkWindow,text="Username", height="3").grid(row=0,column=0)
username=StringVar()
usernameEntry=Entry(tkWindow,textvariable=username).grid(row=0,column=1)

passwordLabel=Label(tkWindow,text="Password",height="3").grid(row=2,column=0)
password=StringVar()
passwordEntry=Entry(tkWindow,textvariable=password,show='*').grid(row=2,column=1)

TagsLabel=Label(tkWindow,text="Tags (sep ,)", height="3", width="10").grid(row=3,column=0)  
Tags=StringVar()
TagsEntry=Entry(tkWindow,textvariable=Tags)
TagsEntry.grid(row=3,column=1)
TagsEntry.insert(0,"Required: Follow only")
on_click_id = TagsEntry.bind('<Button-1>', on_click)

Follow_Label=Label(tkWindow,text="Total Follow", height="3", width="10").grid(row=4,column=0)  
Follow_=IntVar()
Follow_Entry=Entry(tkWindow,textvariable=Follow_).grid(row=4,column=1)


FollowerStart=Button(tkWindow,text="Follow",width="15",command=followstart).grid(row=6,column=0)
UnfollowerStart=Button(tkWindow,text="Unfollow",width="15",command=unfollowstart).grid(row=6,column=1)

tkWindow.mainloop()

