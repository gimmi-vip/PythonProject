'''from tkinter import *


mv=Tk()
canvas=Canvas(mv, bg="black", height=900, width=1400)
canvas.pack()
photo=PhotoImage(file="hotel12.png")
canvas.create_image(690,350, image=photo)

mainloop()'''

'''import tkinter
from tkinter import *
root=Tk()
root.geometry("600x600")

# def enterd(event):
#     btn.config(bg="red")
#
# def left(event):
#     btn.config(bg="white")


f=Frame(root,background='black')
f.pack(expand=True,fill="both")
f1=Frame(root,background='yellow',height=50,width=50)
f1.pack(expand=True,fill="both")

f2=Frame(root,background='red',height=50,width=50)
f2.pack(expand=True)
# btn=Button(f2,text="kkkkkkkkkkkkkkkkkkk")
# btn.pack()
# btn.bind("<Enter>",enterd)
# btn.bind("<Leave>",left)




mainloop()'''


'''try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
root = tk.Tk()
# use opacity alpha values from 0.0 to 1.0
# opacity/tranparency applies to image and frame
root.wm_attributes('-alpha', 0.7)
# use a GIF image you have in the working directory
# or give full path
photo = tk.PhotoImage(file="hotel12.png")
tk.Label(root, image=photo).pack()
root.mainloop()'''

#jpg to png
from PIL import Image

img = Image.open('order.jpg')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("order1.png", "PNG")

# import tkinter as tk
# from tkinter import *
# root=Tk()
# def key_pressed(event):
#     if event.char==" ":
#         print("mjmahi")
#     print(event.char)
# root.bind("<Key>",key_pressed)
# root.mainloop()


'''from tkinter import *

top = Tk()
def list(event):

    Lb = Listbox(top)
    Lb.insert(1, 'Python')
    Lb.insert(2, 'Java')
    Lb.insert(3, 'C++')
    Lb.insert(4, 'Any other')
    Lb.pack()


button = Button(top, text='Stop', width=25, command=list)
button.pack()
button.bind("<Enter>",list)


top.mainloop()'''
#------------------------------------------------menubar_________________________________________________________
'''from tkinter import *
from tkinter import messagebox
import tkinter

top = Tk()
global mb

mb = Menubutton(top, text="condiments", relief=RAISED)
mb.pack()

#mb.bind("<Enter>",list)
#def list(event):

mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label="mayo",
                      variable=mayoVar )
mb.menu.add_checkbutton ( label="ketchup",
                      variable=ketchVar )
mb.menu.add_checkbutton.bin


top.mainloop()'''''
#-----------------------------------------------------------------------------------------------------------------

'''from tkinter import *

root = Tk()

def callback(event):
    print("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()'''
#------------------------------------- print key----------------------
'''from tkinter import *

root = Tk()

def key(event):
    print("pressed", repr(event.char))

def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()'''
#-------------------------------------------------------------------------
'''from tkinter import *

root = Tk()

def callback():
    print("called the callback!")
filename = PhotoImage(file="hotel12.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# create a toolbar
toolbar = Frame(root)
toolbar.config(bg="darkblue")

b = Button(toolbar, text="new", width=6, command=callback,bg="darkblue",relief="flat",fg="white")
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text="open", width=6, command=callback, font=("Hargus-Normal", 17))
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)

toolbar.place(x=100,y=100)

mainloop()'''
#-----------------------------------------------------------------------------------------------------------

'''import tkinter as tk
from tkinter import *

root = Tk()
frame1 = Frame(root)
frame1.config(bg="red")




l1=Label(frame1,text="    Enter Below Details- ",font=("Medusa",20),bg="red")
l1.pack(side=TOP,padx=2,pady=2)
l2=Label(frame1,text="",font=("Medusa",10),bg="red")
l2.pack(side=TOP,padx=2,pady=2)

l4=Label(frame1,text="Coustomer Name:-",font=("Times new roman",10),bg="red")
l4.place(x=20,y=50)

e4=Entry(frame1,bd=3).place(x=180,y=50)

l2=Label(frame1,text="",font=("Medusa",10),bg="red")
l2.pack(side=TOP,padx=2,pady=2)


l5=Label(frame1,text="Aadhar card No:-",font=("Times new roman",10),bg="red")
l5.place(x=20,y=100)
e5=Entry(frame1,bd=3).place(x=180,y=100)

l2=Label(frame1,text="",font=("Medusa",20),bg="red")
l2.pack(side=TOP,padx=2,pady=2)

l6=Label(frame1,text="Address:-",font=("Times new roman",10),bg="red")
l6.place(x=20,y=150)
e6=Entry(frame1,bd=3).place(x=180,y=150)

l2=Label(frame1,text="",font=("Medusa",20),bg="red")
l2.pack(side=TOP,padx=2,pady=2)
l7=Label(frame1,text="Contact:-",font=("Times new roman",10),bg="red")
l7.place(x=20,y=200)
e7=Entry(frame1).place(x=180,y=200)
l2=Label(frame1,text="",font=("Medusa",20),bg="red")
l2.pack(side=TOP,padx=2,pady=2)
Button(frame1,text="SAVE", font=("Medusa", 10), bg="red").place(x=200,y=250)

l2=Label(frame1,text="",font=("Medusa",60),bg="red")
l2.pack(side=TOP,padx=2,pady=2)
frame1.pack()


root.mainloop()'''


#
#


# code written by shubhank
# from tkinter import *
# from tkinter import ttk
# import time
# import datetime
# from PIL import ImageTk, Image
# import os
# import sqlite3
# from tkinter import messagebox
#
# root=Tk()
# root.title("mj")
# root.geometry("1028x780")
#
#
#
# def reserve():
#      b_frame = Frame(root, height=420, width=1080, bg='gray89')
#      path = "newbg6lf.jpg"
#      img = ImageTk.PhotoImage(Image.open(path))
#      label = Label(b_frame, image=img, height=420, width=1080)
#      label.image = img
#      label.place(x=0, y=0)
#      b_frame.config(bg="black")
#
#      hline = Frame(b_frame,height=10,width=960,bg='cyan4')
#      hline.place(x=122,y=27)
#      vline = Frame(b_frame, height=400, width=7, bg='lightsteelblue3')
#      vline.place(x=700, y=0)
#
#      Label(b_frame, text='Personal Information', font='msserif 15', bg='gray93').place(x=225, y=0)
#
#      fnf = Frame(b_frame, height=1, width=1)
#      fn = Entry(fnf)
#
#      mnf = Frame(b_frame, height=1, width=1)
#      mn = Entry(mnf)
#
#      lnf = Frame(b_frame, height=1, width=1)
#      ln = Entry(lnf)
#
#      fn.insert(0, 'First Name *')
#      mn.insert(0, 'Middle Name')
#      ln.insert(0, 'Last Name *')
#
#      def on_entry_click1(event):
#          if fn.get() == 'First Name *':
#              fn.delete(0, END)
#              fn.insert(0, '')
#
#      def on_entry_click2(event):
#          if mn.get() == 'Middle Name':
#              mn.delete(0, END)
#              mn.insert(0, '')
#
#      def on_entry_click3(event):
#          if ln.get() == 'Last Name *':
#              ln.delete(0, END)
#              ln.insert(0, '')
#
#      def on_exit1(event):
#          if fn.get() == '':
#              fn.insert(0, 'First Name *')
#
#      def on_exit2(event):
#          if mn.get() == '':
#              mn.insert(0, 'Middle Name')
#
#      def on_exit3(event):
#          if ln.get() == '':
#              ln.insert(0, 'Last Name *')
#
#      fn.bind('<FocusIn>', on_entry_click1)
#      mn.bind('<FocusIn>', on_entry_click2)
#      ln.bind('<FocusIn>', on_entry_click3)
#      fn.bind('<FocusOut>', on_exit1)
#      mn.bind('<FocusOut>', on_exit2)
#      ln.bind('<FocusOut>', on_exit3)
#
#      fn.pack(ipady=4, ipadx=15)
#      mn.pack(ipady=4, ipadx=15)
#      ln.pack(ipady=4, ipadx=15)
#      fnf.place(x=20, y=42)
#      mnf.place(x=235, y=42)
#      lnf.place(x=450, y=42)
#
#      Label(b_frame, text='Contact Information', font='msserif 15', bg='gray93').place(x=225, y=90)
#
#      cnf = Frame(b_frame, height=1, width=1)
#      cn = Entry(cnf)
#
#      emf = Frame(b_frame, height=1, width=1)
#      em = Entry(emf)
#
#      adf = Frame(b_frame, height=1, width=1)
#      ad = Entry(adf)
#
#      cn.insert(0, 'Contact Number *')
#      em.insert(0, 'Email *')
#      ad.insert(0, "Guest's Address *")
#
#      def on_entry_click4(event):
#          if cn.get() == 'Contact Number *':
#              cn.delete(0, END)
#              cn.insert(0, '')
#
#      def on_entry_click5(event):
#          if em.get() == 'Email *':
#              em.delete(0, END)
#              em.insert(0, '')
#
#      def on_entry_click6(event):
#          if ad.get() == "Guest's Address *":
#              ad.delete(0, END)
#              ad.insert(0, '')
#
#      def on_exit4(event):
#          if cn.get() == '':
#              cn.insert(0, 'Contact Number *')
#
#      def on_exit5(event):
#          if em.get() == '':
#              em.insert(0, 'Email *')
#
#      def on_exit6(event):
#          if ad.get() == '':
#              ad.insert(0, "Guest's Address *")
#
#      cn.bind('<FocusIn>', on_entry_click4)
#      em.bind('<FocusIn>', on_entry_click5)
#      ad.bind('<FocusIn>', on_entry_click6)
#      cn.bind('<FocusOut>', on_exit4)
#      em.bind('<FocusOut>', on_exit5)
#      ad.bind('<FocusOut>', on_exit6)
#
#      cn.pack(ipady=4, ipadx=15)
#      em.pack(ipady=4, ipadx=15)
#      ad.pack(ipady=4, ipadx=15)
#      cnf.place(x=20, y=130)
#      emf.place(x=235, y=130)
#      adf.place(x=450, y=130)
#      # l = Label(b_frame,text='Please Enter The Unique Payment ID',font='msserif 15',bg='cyan4',fg='white')
#      # l.place(x=245,y=0)
#
#      Label(b_frame, text='Reservation Information', font='msserif 15', bg='gray93').place(x=210, y=175)
#
#      nocf = Frame(b_frame, height=1, width=1)
#      noc = Entry(nocf)
#
#      noaf = Frame(b_frame, height=1, width=1)
#      noa = Entry(noaf)
#
#      nodf = Frame(b_frame, height=1, width=1)
#      nod = Entry(nodf)
#
#      noc.insert(0, 'Number of Children *')
#      noa.insert(0, 'Number of Adults *')
#      nod.insert(0, 'Number of Days of Stay *')
#
#      def on_entry_click7(event):
#          if noc.get() == 'Number of Children *':
#              noc.delete(0, END)
#              noc.insert(0, '')
#
#      def on_entry_click8(event):
#          if noa.get() == 'Number of Adults *':
#              noa.delete(0, END)
#              noa.insert(0, '')
#
#      def on_entry_click9(event):
#          if nod.get() == 'Number of Days of Stay *':
#              nod.delete(0, END)
#              nod.insert(0, '')
#
#      def on_exit7(event):
#          if noc.get() == '':
#              noc.insert(0, 'Number of Children *')
#
#      def on_exit8(event):
#          if noa.get() == '':
#              noa.insert(0, 'Number of Adults *')
#
#      def on_exit9(event):
#          if nod.get() == '':
#              nod.insert(0, 'Number of Days of Stay *')
#
#      noc.bind('<FocusIn>', on_entry_click7)
#      noa.bind('<FocusIn>', on_entry_click8)
#      nod.bind('<FocusIn>', on_entry_click9)
#      noc.bind('<FocusOut>', on_exit7)
#      noa.bind('<FocusOut>', on_exit8)
#      nod.bind('<FocusOut>', on_exit9)
#
#      noc.pack(ipady=4, ipadx=15)
#      noa.pack(ipady=4, ipadx=15)
#      nod.pack(ipady=4, ipadx=15)
#      nocf.place(x=20, y=220)
#      noaf.place(x=235, y=220)
#      nodf.place(x=450, y=220)
#
#      roomnf = Frame(b_frame, height=1, width=1)
#      roomn = Entry(roomnf)
#      roomn.insert(0, 'Enter Room Number *')
#
#      def on_entry_click10(event):
#          if roomn.get() == 'Enter Room Number *':
#              roomn.delete(0, END)
#              roomn.insert(0, '')
#
#      def on_exit10(event):
#          if roomn.get() == '':
#              roomn.insert(0, 'Enter Room Number *')
#
#      roomn.bind('<FocusIn>', on_entry_click10)
#      roomn.bind('<FocusOut>', on_exit10)
#      roomn.pack(ipady=4, ipadx=15)
#      roomnf.place(x=20, y=270)
#
#      pmethod = IntVar()
#
#      def booking():
#          if fn.get() == 'First Name' or ln.get() == 'Last Name' or cn.get() == 'Contact Number *' or em.get() == 'Email' or ad.get() == "Guest's Address" or noc.get() == 'Number of Children' or noa.get() == 'Number of Adults' or nod.get() == 'Number of Days of Stay' or roomn.get() == 'Enter Room Number':
#              messagebox.showinfo('Incomplete', 'Fill All the Fields marked by *')
#          elif fn.get() == '' or ln.get() == '' or cn.get() == '' or em.get() == '' or ad.get() == "" or noc.get() == '' or noa.get() == '' or nod.get() == '' or roomn.get() == '':
#              messagebox.showinfo('Incomplete', 'Fill All the Fields marked by *')
#          # cur.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar)")
#
#      Res = Button(b_frame, text='Reserve', bg='white', fg='cyan4', font='timenewroman 11', activebackground='green',command=booking).place(x=235, y=270)
#      unres = Button(b_frame, text='Unreserve', bg='white', fg='cyan4', font='timenewroman 11',activebackground='green').place(x=327, y=270)
#      b_frame.place(x=0, y=120 + 6 + 20 + 60 + 11)
#      b_frame.pack_propagate(False)
#      b_frame.tkraise()
#
#
# Button(text="press",command=reserve).pack()
#
# mainloop()


#--HOTEL DEMO-----------------------------------------------------------------H


# code written by shubhank

