from tkinter import *
from tkinter import ttk
import time
import datetime
from PIL import ImageTk, Image
import os
import sqlite3
from tkinter import messagebox

root=Tk()
# Button(text="dropdown",command=food).pack()
tve1 = ttk.Combobox( width=10)

con = sqlite3.Connection('hm_proj.db')
cur = con.cursor()
cur.execute("select * from food")
con.commit()
x = cur.fetchall()
print(x[0])
# tve1 = ttk.Combobox( width=10,values=['selsect',x[0],x[1],x[2]])
menu=ttk.Combobox(width=20)
menu.insert(INSERT,"select")
menu["values"]=x #[:] #[x[0],x[1],x[2]]

menu.pack()


def food():
    global b_frame
    global fe15
    global fe1
    b_frame = Frame(root, height=530, width=1200, bg='blue')
    path = "food1.png"
    img = ImageTk.PhotoImage(Image.open(path))
    label = Label(b_frame, image=img, height=525, width=1195)
    label.image = img
    label.place(x=0, y=0)

    fe1=Entry(b_frame,width=5,bd=3)
    fe1.place(x=500,y=93)
    fe2 = Entry(b_frame, width=5, bd=3)
    fe2.place(x=500, y=115)
    fe3 = Entry(b_frame, width=5, bd=3)
    fe3.place(x=500, y=175)
    fe4 = Entry(b_frame, width=5, bd=3)
    fe4.place(x=500, y=198)
    fe5 = Entry(b_frame, width=5, bd=3)
    fe5.place(x=500, y=221)
    fe6 = Entry(b_frame, width=5, bd=3)
    fe6.place(x=500, y=284)
    fe7 = Entry(b_frame, width=5, bd=3)
    fe7.place(x=500, y=307)
    fe8 = Entry(b_frame, width=5, bd=3)
    fe8.place(x=500, y=330)
    fe9 = Entry(b_frame, width=5, bd=3)
    fe9.place(x=500, y=351)
    fe10 = Entry(b_frame, width=5, bd=3)
    fe10.place(x=500, y=424)
    fe11 = Entry(b_frame, width=5, bd=3)
    fe11.place(x=500, y=449)
    fe12 = Entry(b_frame, width=5, bd=3)
    fe12.place(x=500, y=474)
    fe13 = Entry(b_frame, width=5, bd=3)
    fe13.place(x=1000, y=115)
    fe14 = Entry(b_frame, width=5, bd=3)
    fe14.place(x=1000, y=137)

    totall=Label(b_frame,text="TOTAL BILL :- ",bg="skyblue").place(x=700,y=200)
    fe15 = Entry(b_frame, width=13, bd=3)
    fe15.place(x=800, y=200)
    Label(b_frame,text="Enter Room no. :-",bg="skyblue").place(x=150,y=20)
    fe16=Entry(b_frame,width=8,bd=3)
    fe16.place(x=260,y=20)





    def cal():
        global fe15
        if fe1.get()=='':
            a1=0
        else:
            fe15.delete(0,END)
            print("mahi")
            cur.execute("select price from food where Menu = 'Grilled Sandwich'")
            a = cur.fetchone()
            a1=str(int(a[0])*int(fe1.get()))

        if fe2.get()=='':
            a2=0
        else:
            fe15.delete(0,END)
            cur.execute("select price from food where Menu = 'Veg Burger'")
            a = cur.fetchone()
            a2 = str(int(a[0]) * int(fe2.get()))

        if fe3.get()=='':
            a3=0
        else:
            fe15.delete(0, END)
            cur.execute("select price from food where Menu = 'Shahi Paneer'")
            a = cur.fetchone()
            a3 = str(int(a[0]) * int(fe3.get()))

        if fe4.get()=='':
            a4=0
        else:
            fe15.delete(0, END)
            cur.execute("select price from food where Menu = 'Kadhai Paneer'")
            a = cur.fetchone()
            a4 = str(int(a[0]) * int(fe4.get()))

        if fe5.get()=='':
            a5=0
        else:
            fe15.delete(0, END)
            cur.execute("select price from food where Menu = 'Malai Kofta'")
            a = cur.fetchone()
            a5 = str(int(a[0]) * int(fe5.get()))

        if fe6.get()=='':
            a6=0
        else:
            fe15.delete(0, END)
            cur.execute("select price from food where Menu = 'Dal Makhani'")
            a = cur.fetchone()
            a6 = str(int(a[0]) * int(fe6.get()))

        if fe7.get()=='':
            a7=0
        else:
            fe15.delete(0, END)
            cur.execute("select price from food where Menu = 'Yellow Dal'")
            a = cur.fetchone()
            a7 = str(int(a[0]) * int(fe7.get()))

        if fe8.get()=='':
            a8=0
        else:
            fe15.delete(0, END)
            cur.execute("select price from food where Menu = 'Rajma'")
            a = cur.fetchone()
            a8 = str(int(a[0]) * int(fe8.get()))

        if fe9.get()=='':
            a9=0
        else:
            fe15.delete(0, END)
            cur.execute("select price from food where Menu = 'Chhole'")
            a = cur.fetchone()
            a9 = str(int(a[0]) * int(fe9.get()))

        if fe10.get() == '':
            a10 = 0
        else:
            fe15.delete(0, END)
            cur.execute("select price from food where Menu = 'Tandoori Roti'")
            a = cur.fetchone()
            a10 = str(int(a[0]) * int(fe10.get()))

        if fe11.get() == '':
            a11 = 0
        else:
            fe15.delete(0, END)
            cur.execute("select price from food where Menu = 'Butter Roti'")
            a = cur.fetchone()
            a11 = str(int(a[0]) * int(fe11.get()))

        if fe12.get() == '':
            a12 = 0
        else:
            fe15.delete(0, END)
            cur.execute("select price from food where Menu = 'Papad'")
            a = cur.fetchone()
            a12 = str(int(a[0]) * int(fe12.get()))

        if fe13.get() == '':
            a13 = 0
        else:
            fe15.delete(0, END)
            cur.execute("select price from food where Menu = 'Rava Kesari'")
            a = cur.fetchone()
            a13 = str(int(a[0]) * int(fe13.get()))

        if fe14.get() == '':
            a14 = 0
        else:
            fe15.delete(0, END)
            cur.execute("select price from food where Menu = 'BOMBAY HALWA'")
            a = cur.fetchone()
            a14 = str(int(a[0]) * int(fe14.get()))





        t=str(int(a1)+int(a2)+int(a3)+int(a4)+int(a5)+int(a6)+int(a7)+int(a8)+int(a9)+int(a10)+int(a11)+int(a12)+int(a13)+int(a14))
        fe15.insert(INSERT,t)


    def foodbill():
        con = sqlite3.Connection('hm_proj.db')
        cur = con.cursor()
        cur.execute("select rstatus from roomd where rn = ?", (fe16.get(),))
        temp = cur.fetchone()
        if temp[0] == 'Unreserved':
            messagebox.showerror('error', 'Room number ' + str(fe16.get()) + ' is not Booked')
        elif temp[0]== 'Reserved':
            cur.execute("select * from foodbill where roomno = ?", (fe16.get(),))
            for x in cur.fetchall():
                if (fe16.get() == str(x[0])):
                    ek=int(str(x[1]))
                    print("bill save")
                    con = sqlite3.Connection('hm_proj.db')
                    cur = con.cursor()
                    rn = fe16.get()
                    fbill = (int(fe15.get()) + int(ek))
                    cur.execute("update foodbill set foodbill=? where roomno = ? ", (fbill,fe16.get(),))
                    # cur.execute("insert into foodbill values(?,?)", (rn , fbill))
                    con.commit()
                    messagebox.showinfo("saved", "your bill is saved")
                    food()


            print("bill save")
            con = sqlite3.Connection('hm_proj.db')
            cur=con.cursor()
            rn=fe16.get()
            fbill=fe15.get()
            cur.execute("insert into foodbill values(?,?)", (rn , fbill))
            con.commit()
            messagebox.showinfo("saved","your bill is"+fbill+"saved")
            food()


    Button(b_frame,text="Calculate",bd=3,bg="red",fg="white",command=cal).place(x=900,y=200)
    Button(b_frame, text="Save", bd=3, bg="red", fg="white", command=foodbill).place(x=1100, y=200)


    b_frame.place(x=20, y=120 + 6 + 20 + 40)

Button(text="dropdown",command=food).pack()
mainloop()