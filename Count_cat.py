from Tkinter import * 
import os
import sys
import string
import fileinput
import re
import operator
from pytube import YouTube


class Video(object):

    def __init__(self,path):
        self.path = path


    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = "MP4"

global reslist
def get_vid(reslist):
    print "get",reslist
    u=""
    tx=""
    try:
     f = open("count.txt","r")
     lines = f.readlines()
     f.close()
     d ={}
     d2=[]
     cat_list= {}
     name_list={}
     for line in lines:
        searcho= re.search(r'Category..(.*).Name..(.*).mp4.Video_id..(.*).View.(.*)',line,re.M|re.I)
        if searcho:
            category = searcho.group(1)
            name = searcho.group(2)+".mp4"
            Video_id = searcho.group(3)
            view = int(searcho.group(4))
            for val in reslist:
              if val == category:
                 d.update({Video_id:view})
                 name_list.update({Video_id:name})
                 cat_list.update({Video_id:category})
              else:
                 print"nothing found!!"
     d2 = sorted(d.items(), key=lambda x: x[1])
     print d2
     print cat_list
     flag = 0
     for x, y in d2:
        category=cat_list.get(x)
        name = name_list.get(x)
        flag+=1
        if flag ==1:
                    q= y+1
                    u = "Category:-"+category+" "+"Name:-"+name+" "+"Video_id:-"+x+" "+"View:"+str(y)
                    print "u",category, u
                    tx = "Category:-"+category+" "+"Name:-"+name+" "+"Video_id:-"+x+" "+"View:"+str(q)
                    print "tx",tx
                    print "x",x
                    interchange(u,tx)
                    return x+".mp4"
        else:
            break
    
    except IOError:
        print "Error reading file:count.txt"
    
    
def rem_cat():
  try:
    f = open("category.txt","r")
    lines = f.readlines()
    f.close()
    f= open("category.txt","w")
    for line in lines:
        if not line == "\n":
            f.write(line)
    f.close()                
  except IOError:
        print "Error reading file:category.txt"
def rem():
   try: 
    f = open("count.txt","r")
    lines = f.readlines()
    f.close()
    f= open("count.txt","w")
    for line in lines:
        if not line == "\n":
            f.write(line)
    f.close()
   except IOError:
        print "Error reading file:count.txt"
def func(steam,file_handle):
   l.config(text = "Complete!", width = "10")

def clicked():
     x = txt.get()
     global cat
     cat = txt2.get()
     yt = YouTube(x,on_complete_callback = func)
     y = yt.title
     p = yt.video_id
     yt.streams.filter(file_extension = "mp4").first().download('.\python project',filename = p)
     try:
      f = open("count.txt","a")
      s = "Category:-"+cat+" "+"Name:-"+y+".mp4"+" "+"Video_id:-"+p+" "+"View:"+str(0)
      f.write('\n')
      f.write(s)
      f.close
      rem()
      try:
       if not os.path.exists('.\category.txt'):
         f = open("category.txt","w")
       else:
        f = open("category.txt","r")
        lines = f.readlines()
        f.close()
       f= open("category.txt","w")
       for line in lines:
           print "clicked:line",line
           print "clicked:cat",cat
           if cat != line:
              print "old",line
              f.write(line)
      except IOError:
        print "Error reading file:category.txt"   
      print "\n" 
      f.write('\n')   
      print cat
      f.write(cat)
      del cat
      f.close()
      rem_cat()
     except IOError:
        print "Error reading file:count.txt"
        

def interchange(u,tx):
   print "iu",u
   print "itx",tx
   try:
    f = open("count.txt","r")
    lines = f.readlines()
    f.close()
    print "li",lines
    f = open("count.txt","w")
    for line in lines:
        line.rstrip()
        if not u in line:
           print line
           print "f",u
           f.write(line)
    f.write('\n')
    f.write(tx)
    f.close()
    rem()
   except IOError:
        print "Error reading file:count.txt"
    
def remove_all(substr, str):
    index = 0
    length = len(substr)
    while string.find(str, substr) != -1:
        index = string.find(str, substr)
        str = str[0:index] + str[index+length:]
    return str

def play():
    reslist = list()
    seleccion = mylist.curselection()
    for i in seleccion:
        entrada = mylist.get(i)
        reslist.append(entrada)
    for val in reslist:
        txt3.insert(0,val+',')
    print reslist
    p = get_vid(reslist)
    movie = Movie_MP4(r"C:\Users\asus\Desktop\python project\\"+str(p) )
    movie.play()

def refresh():
       window.destroy()
       execfile("Count_cat.py",globals())

def files(path):  
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

window = Tk()
window.title("Youtube Downloader")
l = Label(window,text="   ")
l.grid(column=0,row=2)
l2 = Label(window,text="Enter Category")
l2.grid(column=0,row=1)
lbl = Label(window, text="Enter URL")
button = Button(window, text = "Refresh",command = refresh)
button.grid(column=0,row=6)
scrollbar = Scrollbar(window)
scrollbar.grid(row=4,column=2, rowspan=1, sticky=N+S)
mylist=Listbox(window,selectmode = "multiple", height=5, width=40, yscrollcommand=scrollbar.set)
Button(window, text="Play", command=play).grid(column=1, row=6)
try:
 f = open("category.txt", "r")
 lines = f.readlines()
 lines = [x.strip() for x in lines]
 f.close()
 for line in lines:
       mylist.insert(END,line)
except IOError:
        print "Error reading file:category.txt"
mylist.grid(row=4,column=1,rowspan=1,sticky=E+W)
scrollbar.config( command = mylist.yview )
lbl.grid(column=0, row=0)
txt2 = Entry(window,width=30)
txt2.grid(column=1, row=1)
txt = Entry(window,width=50)
txt.grid(column=1, row=0)
btn = Button(window, text="Download", command=clicked)
btn.grid(column=1, row=2)
lable = Label(window, text="Selected Category")
lable.grid(column=0, row=5)
txt3 = Entry(window,width=50)
txt3.grid(column=1, row=5)
window.mainloop()
