from tkinter import *
from tkinter import ttk
import time
import datetime
from datetime import date
from PIL import ImageTk, Image
import os
import sqlite3
from tkinter import messagebox

now = datetime.datetime.now()
con = sqlite3.Connection('hm_proj.db')
cur = con.cursor()

root=Tk()
root.config(bg="skyblue")

top_frame = Frame(root, height=85, width=1500, bg='orange')
path = "hotel.png"
img = ImageTk.PhotoImage(Image.open(path))
label = Label(top_frame, image=img, height=78, width=1500)
label.image = img
label.place(x=0, y=0)
top_frame.place(x=0, y=0)
# tf_label = Label(top_frame, text='Hotel Management System', font=("seogoe",15), fg='black',bg="blue", height=30)
# tf_label.pack(anchor='center')
top_frame.pack_propagate(False)

# ---------------DATE TIME------------------------------------------------------------------------------------------------------------------
# localtime = now.strftime("%Y-%m-%d %H:%M")
path = "hotel.png"
img = ImageTk.PhotoImage(Image.open(path))
lblInfo = Label(top_frame, font='helvetica 20', image=img, fg='darkblue')
lblInfo.place(x=0,y=0)
Label(top_frame,image=img, fg='white').place(x=1094,y=0)
Label(top_frame,image=img, fg='white').place(x=1220,y=0)


sl_frame = Frame(root, height=91, width=1500, bg='skyblue')
sl_frame.place(x=0, y=85 )




# rot = Frame(root, height=545, width=1200, bg='skyblue')
# rot.place(x=20, y=120 + 6 + 20 + 40)
# rot.pack_propagate(False)
# rot.tkraise()
# rot.place(x=20, y=120 + 6 + 20 + 40)

def master():
    b_frame = Frame(root, height=530, width=1280, bg='skyblue')
    path = 'recp.jpg'
    img = ImageTk.PhotoImage(Image.open(path))
    label = Label(b_frame, image=img, height=525, width=1280)
    label.image = img
    label.place(x=0, y=0)
    b_frame.place(x=20, y=120 + 6 + 20 + 40)


    def mstinfo():
        b_frame = Frame(root, height=530, width=1280, bg='skyblue')
        path = 'ROOM.jpg'
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(b_frame, image=img, height=525, width=1280)
        label.image = img
        label.place(x=0, y=0)
        b_frame.place(x=20, y=120 + 6 + 20 + 40)

    def rooms():
        today = date.today()
        b_frame = Frame(root, height=530, width=1280, bg='skyblue')
        path = "mtrom.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(b_frame, image=img, height=525, width=1200)
        label.image = img
        label.place(x=0, y=0)

        roomnameentry = Entry(b_frame, width=20, bd=3, bg='cyan')
        roomnameentry.place(x=190, y=290)
        # Label(b_frame, text='food name').place(x=10, y=30)
        categoryentry= Entry(b_frame, width=20, bd=3, bg='cyan')
        categoryentry.place(x=190, y=345)
        # Label(b_frame,text="price").place(x=10,y=60)
        priceentry = Entry(b_frame, width=20, bd=3, bg='cyan')
        priceentry.place(x=190, y=400)

        conn = sqlite3.connect("hm_proj.db")
        with conn:
            cur = conn.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS roommenu2(roomno INTEGER,category TEXT,price INTEGER,date DATE)')
            con.commit()


        def addroom():
            if categoryentry.get() == "" or roomnameentry.get() == "" or priceentry.get() == "":
                messagebox.showerror('error', 'please enter all fields')
            else:
                conn = sqlite3.connect("hm_proj.db")
                with conn:
                    cur = conn.cursor()
                    cur.execute("insert into roommenu2 values(?,?,?,?)",
                                ( roomnameentry.get(),categoryentry.get(), priceentry.get(), today,))
                    messagebox.showinfo("Successful", "Room added successfully")
                    con.commit()
                    categoryentry.delete(0, END)
                    roomnameentry.delete(0, END)
                    priceentry.delete(0, END)
                    rooms()


        form = ttk.Treeview(b_frame, height=15, columns=('ROOM-N0','CATEGORY',  'PRICE'), selectmode="extended")

        form.heading('#0', text="ROOM-NO.", anchor=W)
        form.heading('#1', text='CATEGORY', anchor=W)
        form.heading('#2', text='PRICE', anchor=W)

        form.column('#0', stretch=YES, width=80)
        form.column('#1', stretch=YES, width=80)
        form.column('#2', stretch=YES, width=50)

        form.place(x=450, y=180)
        ttk.Style().configure("Treeview", background="skyblue", foreground="red")
        ttk.Style().configure("Treeview.Heading", bg="red", foreground="black")

        vsb = ttk.Scrollbar(b_frame, orient="vertical", command=form.yview)
        vsb.place(x=845, y=180, height=300 + 22)
        form.configure(yscrollcommand=vsb.set)

        conn = sqlite3.connect("hm_proj.db")
        with conn:
            cur = conn.cursor()
            # cursor.execute('CREATE TABLE if not exists mj (Fname TEXT,Mname TEXT,Lname TEXT,id_no TEXT,Height TEXT,Weight TEXT,increhabit TEXT,Gender TEXT,fathername TEXT,mothername TEXT, Age TEXT,emailid TEXT,Address TEXT,Contact TEXT)')
            cur.execute('SELECT * FROM roommenu2')
            for row in cur.fetchall():
                form.insert('', 0, text=row[0], values=(row[1], row[2]))


        Button(b_frame, text="Refresh", width=10, command=rooms).place(x=650, y=150)
        Button(b_frame, text="SAVE", bg="red", relief="groove", fg="white", font=('times new roman', 10),command=addroom).place(x=150, y=450)

        b_frame.place(x=20, y=120 + 6 + 20 + 40)

    def food():
        today = date.today()
        global b_frame
        global fe15
        global fe1
        b_frame = Frame(root, height=530, width=1280, bg='blue')
        path = "fbg11.png"
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(b_frame, image=img, height=525, width=1280)
        label.image = img
        label.place(x=0, y=0)
        # Label(b_frame,text='category').place(x=10,y=10)
        categoryentry = Entry(b_frame, width=20, bd=3, bg='cyan')
        categoryentry.place(x=190, y=295)
        # Label(b_frame, text='food name').place(x=10, y=30)
        foodnameentry = Entry(b_frame, width=20, bd=3, bg='cyan')
        foodnameentry.place(x=190, y=350)
        # Label(b_frame,text="price").place(x=10,y=60)
        priceentry = Entry(b_frame, width=20, bd=3, bg='cyan')
        priceentry.place(x=190, y=405)
        conn = sqlite3.connect("hm_proj.db")
        with conn:
            cur = conn.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS foodmenu2(category TEXT,item TEXT,price INTEGER,date DATE)')
            con.commit()

        def addfood():
            if categoryentry.get() == "" or foodnameentry.get() == "" or priceentry.get() == "":
                messagebox.showerror('error', 'please enter all fields')
            else:
                conn = sqlite3.connect("hm_proj.db")
                with conn:
                    cur = conn.cursor()
                    cur.execute("insert into foodmenu2 values(?,?,?,?)",
                                (categoryentry.get(), foodnameentry.get(), priceentry.get(), today,))
                    messagebox.showinfo("Successful", "food added successfully")
                    con.commit()
                    food()
                    categoryentry.delete(0, END)
                    foodnameentry.delete(0, END)
                    priceentry.delete(0, END)

        form = ttk.Treeview(b_frame, height=15, columns=('CATEGORY', 'FOOD-NAME', 'PRICE'), selectmode="extended")

        form.heading('#0', text="CATEGORY", anchor=W)
        form.heading('#1', text='FOOD-NAME', anchor=W)
        form.heading('#2', text='PRICE', anchor=W)

        form.column('#0', stretch=YES, width=80)
        form.column('#1', stretch=YES, width=80)
        form.column('#2', stretch=YES, width=50)

        form.place(x=450, y=180)
        ttk.Style().configure("Treeview", background="skyblue", foreground="red")
        ttk.Style().configure("Treeview.Heading", bg="red", foreground="black")

        vsb = ttk.Scrollbar(b_frame, orient="vertical", command=form.yview)
        vsb.place(x=845, y=180, height=300 + 22)
        form.configure(yscrollcommand=vsb.set)

        conn = sqlite3.connect("hm_proj.db")
        with conn:
            cur = conn.cursor()
            # cursor.execute('CREATE TABLE if not exists mj (Fname TEXT,Mname TEXT,Lname TEXT,id_no TEXT,Height TEXT,Weight TEXT,increhabit TEXT,Gender TEXT,fathername TEXT,mothername TEXT, Age TEXT,emailid TEXT,Address TEXT,Contact TEXT)')
            cur.execute('SELECT * FROM foodmenu2')
            for row in cur.fetchall():
                form.insert('', 0, text=row[0], values=(row[1], row[2]))

            # conn = sqlite3.connect("hm_proj.db")
            # cur.execute('INSERT INTO foodmenu2 VALUES(?,?,?,?)', (categoryentry.get(),foodnameentry.get(),priceentry.get(), today,))
            # con.commit()
            # messagebox.showinfo("saved","new food added")

        Button(b_frame, text="SAVE", bg="red", relief="groove", fg="white", font=('times new roman', 10),
               command=addfood).place(x=150, y=450)
        cur.execute("select category from foodmenu2")
        con.commit()
        x = cur.fetchall()
        print(x[0])
        Button(b_frame,text="Refresh",width=10,command=food).place(x=650,y=150)
        b_frame.place(x=20, y=120 + 6 + 20 + 40)




    path1 = "mstinfo.png"
    img1 = ImageTk.PhotoImage(Image.open(path1))
    label1 = Button(b_frame, image=img1,height=120, width=150,command=mstinfo)
    label1.image = img1
    label1.place(x=150, y=150)
    Button(b_frame,text='Master information',width=20).place(x=150,y=260)

    path2 = "room.png"
    img2 = ImageTk.PhotoImage(Image.open(path2))
    label2 = Button(b_frame, image=img2, height=120, width=150,command=rooms)
    label2.image = img2
    label2.place(x=500, y=150)
    Button(b_frame, text='Master Room', width=20).place(x=500, y=260)

    path3 = "food.png"
    img3 = ImageTk.PhotoImage(Image.open(path3))
    label3 = Button(b_frame, image=img3, height=120, width=150,command=food)
    label3.image = img3
    label3.place(x=800, y=150)


    Button(b_frame, text='Master food', width=20).place(x=800, y=260)

p2=PhotoImage(file="mstinfo.png")
p3=p2.subsample(8,8)
b1 = Button(sl_frame, image=p3, text='b1', bg='skyblue', width=150,command=master)
# b1.image = img
b1.place(x=0, y=0)
Label(sl_frame, text='Hotel Status', font='msserif 13', bg='skyblue',fg="black").place(x=40, y=70)


mainloop()