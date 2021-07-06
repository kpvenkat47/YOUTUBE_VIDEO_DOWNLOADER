import pytube
from tkinter import *
from tkinter import messagebox
w=Tk()
w.title("YT DOWNLOADER")
w.config(background="cyan3")
w.geometry("670x110+50+50")
w.resizable(False,False)
lab1=Label(w,text="YouTube URL:",font = ('Serifbold',18,'bold'),bg="red2",fg="white")
url=Entry(w,text=" ",borderwidth=1,width=50,)
url.config(highlightthickness=1,highlightbackground="darkgreen")

videourl = url.get()

def DWN():
    """get valid YOUTUBE video ,else show error warning"""
    videourl = url.get()
    if len(videourl)==0 :
        messagebox.showwarning("Empty URL","URL is empty")
    elif "youtube" not in videourl:
        messagebox.showwarning("Warning","URL is wrong")
        url.delete(0,'end')
    else:
        messagebox._show("Loading","Loading...Wait a Few seconds file is started to Download")

        y = pytube.YouTube(videourl)
        video = y.streams.first()

        video.download('D:')
        messagebox.showinfo("Completed","File is ready go and check Local Disk D:")

        w.destroy()

btn=Button(w,text="Download",borderwidth=4,width=8,relief="raised",font = ('Serifbold',18,'bold'),bg="slate blue",fg="white",command=DWN)
btn.grid(row=1,column=2,ipady=2)
url.grid(row=1,column=1,ipady=2,padx=13)
lab1.grid(row=1,column=0)
w.mainloop()
