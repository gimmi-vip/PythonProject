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
cur.execute("create table if not exists hoteld(t_r number,r_r number,t_s number)")
cur.execute("create table if not exists roomd(rn number primary key,beds number,ac varchar(10),tv varchar(10),internet varchar(10),price number(10))")
cur.execute("create table if not exists food(Menu TEXT,Price INTEGER)")

# pmethod=0

# rstatus extra column
# for i in range (1,21):
# cur.execute("update roomd set tv='Yes' where rn = ? ",(19,))
cur.execute("create table if not exists payments(id number primary key,dot varchar(15),time varchar(10),amt number,method varchar(10))")
cur.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,checkin varchar,checkout varchar,time varchar , method varchar,totalamt varchar)")
# cur.execute("insert into paymentsf values(1,'Shubhank','Khare','9589861196','Shubhank7673@gmail.com',2,'1','11','2018','11:20:27 PM','Cash','3500')")
# cur.execute("alter table paymentsf add totalamt varchar")
con.commit()
con.commit()
# cur.execute("drop table paymentsf")
# cur.execute("insert into hoteld values(20,11,30)")
con.commit()
cur.execute("select * from payments")
con.commit()
x = cur.fetchall()
con.commit()




root = Tk()
root.geometry('1366x768')
# root.minsize(width=1250, height=610)
root.maxsize(width=1500, height=800)
root.configure(bg='skyblue')
root.title("home")
# filename = PhotoImage(file="hotel.png")
# background_label = Label(root, image=filename)
# background_label.place(x=0,y=0)
# --------------seperator-------------------------------------------------------------------------------------------------------------------

# sep = Frame(height=500, bd=1, relief='sunken', bg='white')

# sep.place(x=20,y=0)
# ----------------Connection with printer-------------------------------------------------------------------------------------------------------------

def connectprinter():
    os.startfile("C:/jjj/TestFile.txt", "print")

# ---------------top frame-----------------------------------------------------------------------------------------------------------------
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













p16=PhotoImage(file="exitt.png")
p17=p16.subsample(3,3)
b8 = Button(sl_frame, image=p17, text='b1', bg='skyblue', width=150,command=root.destroy)
# b5.image = img
b8.place(x=1095, y=0)
Label(sl_frame, text='Exit', font='msserif 13', bg='skyblue',fg="black").place(x=1135, y=72)

#-----------------------------------------------------------------BOOKING___________________________________________________________________________________
def booking():
    b_frame = Frame(root, height=545, width=1280, bg='skyblue')
    '''path = "newbg6lf.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    label = Label(b_frame, image=img, height=420, width=1080)
    label.image = img
    label.place(x=0, y=0)'''

    # hline = Frame(b_frame,height=10,width=960,bg='cyan4')
    # hline.place(x=122,y=27)
    vline = Frame(b_frame, height=400, width=7, bg='lightsteelblue3')
    vline.place(x=700, y=0)

    Label(b_frame, text='-: Personal Information :-', font='msserif 15', bg='skyblue').place(x=225, y=0)

    fnf = Frame(b_frame, height=1, width=1)
    fn = Entry(fnf)

    mnf = Frame(b_frame, height=1, width=1)
    mn = Entry(mnf)

    lnf = Frame(b_frame, height=1, width=1)
    ln = Entry(lnf)

    fn.insert(0, 'First Name *')
    mn.insert(0, 'Middle Name')
    ln.insert(0, 'Last Name *')

    def on_entry_click1(event):
        if fn.get() == 'First Name *':
            fn.delete(0, END)
            fn.insert(0, '')

    def on_entry_click2(event):
        if mn.get() == 'Middle Name':
            mn.delete(0, END)
            mn.insert(0, '')

    def on_entry_click3(event):
        if ln.get() == 'Last Name *':
            ln.delete(0, END)
            ln.insert(0, '')

    def on_exit1(event):
        if fn.get() == '':
            fn.insert(0, 'First Name *')

    def on_exit2(event):
        if mn.get() == '':
            mn.insert(0, 'Middle Name')

    def on_exit3(event):
        if ln.get() == '':
            ln.insert(0, 'Last Name *')

    fn.bind('<FocusIn>', on_entry_click1)
    mn.bind('<FocusIn>', on_entry_click2)
    ln.bind('<FocusIn>', on_entry_click3)
    fn.bind('<FocusOut>', on_exit1)
    mn.bind('<FocusOut>', on_exit2)
    ln.bind('<FocusOut>', on_exit3)

    fn.pack(ipady=4, ipadx=15)
    mn.pack(ipady=4, ipadx=15)
    ln.pack(ipady=4, ipadx=15)
    fnf.place(x=20, y=42)
    mnf.place(x=235, y=42)
    lnf.place(x=450, y=42)

    Label(b_frame, text='-: Contact Information :-', font='msserif 15', bg='skyblue').place(x=225, y=90)

    cnf = Frame(b_frame, height=1, width=1)
    cn = Entry(cnf)

    emf = Frame(b_frame, height=1, width=1)
    em = Entry(emf)

    adf = Frame(b_frame, height=1, width=1)
    ad = Entry(adf)

    cn.insert(0, 'Contact Number *')
    em.insert(0, 'Email *')
    ad.insert(0, "Guest's Address *")

    def on_entry_click4(event):
        if cn.get() == 'Contact Number *':
            cn.delete(0, END)
            cn.insert(0, '')

    def on_entry_click5(event):
        if em.get() == 'Email *':
            em.delete(0, END)
            em.insert(0, '')

    def on_entry_click6(event):
        if ad.get() == "Guest's Address *":
            ad.delete(0, END)
            ad.insert(0, '')

    def on_exit4(event):
        if cn.get() == '':
            cn.insert(0, 'Contact Number *')

    def on_exit5(event):
        if em.get() == '':
            em.insert(0, 'Email *')

    def on_exit6(event):
        if ad.get() == '':
            ad.insert(0, "Guest's Address *")

    cn.bind('<FocusIn>', on_entry_click4)
    em.bind('<FocusIn>', on_entry_click5)
    ad.bind('<FocusIn>', on_entry_click6)
    cn.bind('<FocusOut>', on_exit4)
    em.bind('<FocusOut>', on_exit5)
    ad.bind('<FocusOut>', on_exit6)

    cn.pack(ipady=4, ipadx=15)
    em.pack(ipady=4, ipadx=15)
    ad.pack(ipady=4, ipadx=15)
    cnf.place(x=20, y=130)
    emf.place(x=235, y=130)
    adf.place(x=450, y=130)
    # l = Label(b_frame,text='Please Enter The Unique Payment ID',font='msserif 15',bg='cyan4',fg='white')
    # l.place(x=245,y=0)

    Label(b_frame, text='-: Room booking Information :-', font='msserif 15', bg='skyblue').place(x=210, y=175)

    nocf = Frame(b_frame, height=1, width=1)
    noc = Entry(nocf)

    noaf = Frame(b_frame, height=1, width=1)
    noa = Entry(noaf)

    nodf = Frame(b_frame, height=1, width=1)
    nod = Entry(nodf)

    noc.insert(0, 'Number of Children *')
    noa.insert(0, 'Number of Adults *')
    nod.insert(0, 'Number of Days of Stay *')

    def on_entry_click7(event):
        if noc.get() == 'Number of Children *':
            noc.delete(0, END)
            noc.insert(0, '')

    def on_entry_click8(event):
        if noa.get() == 'Number of Adults *':
            noa.delete(0, END)
            noa.insert(0, '')

    def on_entry_click9(event):
        if nod.get() == 'Number of Days of Stay *':
            nod.delete(0, END)
            nod.insert(0, '')

    def on_exit7(event):
        if noc.get() == '':
            noc.insert(0, 'Number of Children *')

    def on_exit8(event):
        if noa.get() == '':
            noa.insert(0, 'Number of Adults *')

    def on_exit9(event):
        if nod.get() == '':
            nod.insert(0, 'Number of Days of Stay *')

    noc.bind('<FocusIn>', on_entry_click7)
    noa.bind('<FocusIn>', on_entry_click8)
    nod.bind('<FocusIn>', on_entry_click9)
    noc.bind('<FocusOut>', on_exit7)
    noa.bind('<FocusOut>', on_exit8)
    nod.bind('<FocusOut>', on_exit9)

    noc.pack(ipady=4, ipadx=15)
    noa.pack(ipady=4, ipadx=15)
    nod.pack(ipady=4, ipadx=15)
    nocf.place(x=20, y=220)
    noaf.place(x=235, y=220)
    nodf.place(x=450, y=220)

    roomnf = Frame(b_frame, height=1, width=1)
    global roomn
    roomn = Entry(roomnf)
    roomn.insert(0, 'Enter Room Number *')
    roomn.pack(ipady=4, ipadx=15)
    roomnf.place(x=20, y=270)

    check = Frame(b_frame, height=1, width=1)
    checkin = Entry(check)
    to=date.today()
    checkin.insert(0,to)
    checkin.pack(ipady=4, ipadx=15)
    check.place(x=235, y=270)

    checkout = Frame(b_frame, height=1, width=1)
    checkout1 = Entry(checkout)
    checkout1.insert(0,'checkout date *')
    checkout1.pack(ipady=4, ipadx=15)
    checkout.place(x=450, y=270)



    id = Frame(b_frame, height=1, width=1)
    Label(b_frame,text="id-proof no:-",bg="skyblue").place(x=370,y=300)
    id1 = Entry(id)
    # checkout1.insert(0, 'checkout date *')
    id1.pack(ipady=4, ipadx=15)
    id.place(x=450, y=300)


    def on_entry_click10(event):
        if roomn.get() == 'Enter Room Number *':
            roomn.delete(0, END)
            roomn.insert(0, '')

    def on_exit10(event):
        if roomn.get() == '':
            roomn.insert(0, 'Enter Room Number *')


    # def on_entry_click11(event):
    #     if checkin.get() == 'checkin date *':
    #         checkin.delete(0, END)
    #         checkin.insert(0, '')

    # def on_exit11(event):
    #     if checkin.get() == '':
    #         checkin.insert(0, 'checkin date *')

    def on_entry_click12(event):
        if checkout1.get() == 'checkout date *':
            checkout1.delete(0, END)
            checkout1.insert(0, '')

    def on_exit12(event):
        if checkout1.get() == '':
            checkout1.insert(0, 'checkout date *')



    roomn.bind('<FocusIn>', on_entry_click10)
    roomn.bind('<FocusOut>', on_exit10)
    # checkin.bind('<FocusIn>', on_entry_click11)
    # checkin.bind('<FocusOut>', on_exit11)
    checkout1.bind('<FocusIn>', on_entry_click12)
    checkout1.bind('<FocusOut>', on_exit12)

    pmethod = IntVar()

    def booking():
        if fn.get() == 'First Name' or ln.get() == 'Last Name' or cn.get() == 'Contact Number *' or em.get() == 'Email' or ad.get() == "Guest's Address" or noc.get() == 'Number of Children' or noa.get() == 'Number of Adults' or nod.get() == 'Number of Days of Stay' or roomn.get() == 'Enter Room Number':
            messagebox.showinfo('Incomplete', 'Fill All the Fields marked by *')
        elif fn.get() == '' or ln.get() == '' or cn.get() == '' or em.get() == '' or ad.get() == "" or noc.get() == '' or noa.get() == '' or nod.get() == '' or roomn.get() == '':
            messagebox.showinfo('Incomplete', 'Fill All the Fields marked by *')
        # cur.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar)")
        else:
            cur.execute("select rstatus from roomd where rn = ?", (roomn.get(),))
            temp = cur.fetchone()
            if temp[0] == 'Reserved':
                cur.execute("select checkin from paymentsf where r_n = ?", (roomn.get(),))
                tem = cur.fetchone()
                if tem[0] == checkin.get():
                    messagebox.showwarning('Room is Booked', 'Room number ' + str(roomn.get()) + ' is Booked')
                else:
                    print("aao kbhi hveli pe")
                    cur.execute("select id from paymentsf order by id desc")
                    x = cur.fetchone()
                    cid = int(x[0])
                    cid += 1

                    cur.execute("select price from roomd where rn = (?)", (roomn.get(),))
                    rp = cur.fetchone()
                    print(rp)
                    global amtpd10
                    amtpd1 = str(int(rp[0]) * int(nod.get()))

                    # cur.execute(
                    #     "create table if not exists advancebooking(id number  primary key,f_name varchar,m_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar,totalamt varchar)")
                    cur.execute("create table if not exists advancebooking1(id	INTEGER,f_name	varchar,m_name	varchar,l_name	varchar,c_number	varchar,email	varchar,r_n	number,checkin	varchar,checkout	varchar,time	varchar,method	varchar,totalamt	varchar)")
                    cur.execute("insert into advancebooking1 values(?,?,?,?,?,?,?,?,?,?,?,?)", (
                    cid, fn.get(), mn.get(), ln.get(), cn.get(), em.get(), roomn.get(), checkin.get(), checkout1.get(),
                    str(now.strftime("%H:%M")), str(pmethod.get()), amtpd1))
                    # cur.execute("update roomd set rstatus='Reserved' where rn = ? ", (roomn.get(),))
                    messagebox.showinfo("Successful", "Room Booked successfully")
                    con.commit()
                    fn.delete(0, END)
                    mn.delete(0, END)
                    ln.delete(0, END)
                    cn.delete(0, END)
                    em.delete(0, END)
                    roomn.delete(0, END)
                    checkin.delete(0, END)
                    checkout1.delete(0, END)
                    noa.delete(0, END)
                    ad.delete(0, END)
                    noc.delete(0, END)
                    nod.delete(0, END)

                    ask = messagebox.askyesno("Successful", "Payment Successful\nDo you want to print reciept ?")
                    if ask == 'yes':
                        def createfile():
                            fl = open("reciept.txt", "w")
                            fl.write("reciept will come here")
                    booking()
                    # payroot.destroy()
                # else:
                # messagebox.showwarning("Not selected", "Please Select the payment method")
            else:
                payroot = Tk()
                payroot.title("Payment")
                payroot.minsize(height=236, width=302)
                payroot.configure(bg='White')
                # global pmethod
                cur.execute("select price from roomd where rn = (?)", (roomn.get(),))
                rp = cur.fetchone()
                print(rp)
                global amtpd
                amtpd = str(int(rp[0]) * int(nod.get()))

                Label(payroot, text='Select an option to pay ' + str(int(rp[0]) * int(nod.get())),font='msserif 14 bold', bg='White').place(x=0, y=0)
                Frame(payroot, height=4, width=300, bg='cyan4').place(x=0, y=39)
                Radiobutton(payroot, text='Cash  ', bg='White', variable=pmethod, value=1, font='helvetica 15',width=5).place(x=0, y=43 + 10)
                Radiobutton(payroot, text='Card   ', bg='White', variable=pmethod, value=2, font='helvetica 15',width=5).place(x=0, y=80 + 10)
                Radiobutton(payroot, text='UPI     ', bg='White', variable=pmethod, value=3, font='helvetica 15',width=5).place(x=0, y=115 + 10)
                Radiobutton(payroot, text='Paytm ', bg='White', variable=pmethod, value=4, font='helvetica 15',width=5).place(x=0, y=150 + 10)

                def f():
                    if pmethod != '':
                        print(pmethod.get())
                        print('pmethod value')
                        cur.execute("select id from paymentsf order by id desc")
                        x = cur.fetchone()
                        cid = int(x[0])
                        cid += 1
                        # print (cid)
                        # print (pmethod.get())



                        cur.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,m_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar,totalamt varchar)")
                        cur.execute("insert into paymentsf values(?,?,?,?,?,?,?,?,?,?,?,?)", (cid, fn.get(),mn.get() ,ln.get(), cn.get(), em.get(), roomn.get(),checkin.get(),checkout1.get(), str(now.strftime("%H:%M")),str(pmethod.get()), amtpd))
                        cur.execute("update roomd set rstatus='Reserved' where rn = ? ", (roomn.get(),))
                        messagebox.showinfo("Successful", "Room Booked successfully")
                        con.commit()
                        fn.delete(0,END)
                        mn.delete(0, END)
                        ln.delete(0, END)
                        cn.delete(0, END)
                        em.delete(0, END)
                        roomn.delete(0, END)
                        checkin.delete(0, END)
                        checkout1.delete(0, END)
                        noa.delete(0,END)
                        ad.delete(0,END)
                        noc.delete(0,END)
                        nod.delete(0,END)

                        ask = messagebox.askyesno("Successful","Payment Successful\nDo you want to print reciept ?")
                        if ask == 'yes':
                            def createfile():
                                fl = open("reciept.txt", "w")
                                fl.write("reciept will come here")
                        booking()
                        payroot.destroy()
                    else:
                        messagebox.showwarning("Not selected", "Please Select the payment method")





                Button(payroot, text='Pay', font='msserif 12', bg='Green', fg='White', width=28, command=f).place(x=0, y=200)
                Label(payroot, text='Your unique payment id :', font='msserif', bg='White')  # .place(x=0,y=25)

    '''def unreserve():
        if (roomn.get() == 'Enter Room Number') or (roomn.get() == ''):
            messagebox.showerror('Entries not filled', 'Kindly Enter room Number')
        else:
            cur.execute("update roomd set rstatus='Unreserved' where rn = ? ", (roomn.get(),))
            messagebox.showinfo("Successful", "Room empty successfully")
            booking()
            con.commit()'''

    # --------------------------------------------------------ROOM FILTER---------------------------------------------------
    Label(b_frame, text='-: Room Filter :-', font='msserif 20', bg='skyblue').place(x=850, y=0)

    nbb = IntVar()
    acb = IntVar()
    tvb = IntVar()
    wifib = IntVar()

    style = ttk.Style()
    style.map('TCombobox', fieldbackground=[('readonly', 'white')])
    Label(b_frame, text='Bed(s) :', bg='skyblue', font='17').place(x=730, y=50)

    nb = ttk.Combobox(b_frame, values=['please select...', '1', '2', '3'], state='readonly', width=22)
    nb.place(x=830, y=50)
    nb.current(0)

    Label(b_frame, text='AC :', font='17', bg='skyblue').place(x=732, y=75)

    ac = ttk.Combobox(b_frame, values=['please select...', 'Yes', 'No'], state='readonly', width=22)
    ac.place(x=830, y=75)
    ac.current(0)

    Label(b_frame, text='TV :', font='17', bg='skyblue').place(x=732, y=100)

    tv = ttk.Combobox(b_frame, values=['please select...', 'Yes', 'No'], state='readonly', width=22)
    tv.place(x=830, y=100)
    tv.current(0)

    Label(b_frame, text='Wifi :', font='17', bg='skyblue').place(x=732, y=125)

    wifi = ttk.Combobox(b_frame, values=['please select...', 'Yes', 'No'], state='readonly', width=22)
    wifi.place(x=830, y=125)
    wifi.current(0)

    listofrooms = Listbox(b_frame, height=6, width=36)
    listofrooms.place(x=735, y=190)
    listofrooms.insert(END, 'Rooms of Your Choice will appear Here')
    listofrooms.insert(END, 'once you apply filter')

    def findrooms():
        cur.execute('select rn,price,rstatus from roomd where beds = ? and ac = ? and tv = ? and internet = ? order by price asc',((nb.get()), ac.get(), tv.get(), wifi.get()))
        x = cur.fetchall()
        # print (x)
        listofrooms.delete(0, END)
        if x == []:
            listofrooms.insert(END, 'No Matching Found')
        for i in x:
            listofrooms.insert(END, 'Room Number ' + str(i[0]) + ' - Price - ' + str(i[1]))

    Res = Button(b_frame, text='SAVE', bg='cyan', fg='black', relief='ridge',font='timenewroman 15', activebackground='green',command=booking).place(x=235, y=350)
    # unres = Button(b_frame, text='Cancel', bg='cyan', fg='black', relief='ridge',font='timenewroman 15',activebackground='green', command=unreserve).place(x=327, y=350)
    findrooms = Button(b_frame, text='Find Rooms', bg='cyan', fg='black',relief='ridge', font='timenewroman 15',activebackground='green', command=findrooms).place(x=870, y=320)

    scrollbar = Scrollbar(b_frame, orient="vertical")
    scrollbar.config(command=listofrooms.yview)
    scrollbar.place(x=1014, y=191, height=111)
    listofrooms.config(yscrollcommand=scrollbar.set)

    b_frame.place(x=20, y=120 + 6 + 20 + 40)
    b_frame.pack_propagate(False)
    b_frame.tkraise()
#------------------------------------del function--------------------------------------
def delete():
    box1 = messagebox.askyesno("CONFARMATION", "if you delete you will be unable to see previous data again")


    if box1 > 0:
        SEARCH = delentry.get()
        conn = sqlite3.connect("hm_proj.db")
        with conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM paymentsf WHERE r_n=?", (SEARCH,))
            conn.commit()
    delentry.delete(0,END)
    rot.destroy()
    customer()




    #_______________________________________________________________________________-customer data____________________________________________________________
def customer():
    global rot
    global delentry
    # rot = Frame(root,height=1000,width=1200)
    # rot.config(bg="black")
    # mainlabel = Label(rot, text="RECORD DETAILS", font=("times new roman", 35), bg='white')
    # mainlabel.pack(side=TOP, pady=180, padx=270)
    rot = Frame(root, height=545, width=1280, bg='skyblue')
    rot.place(x=20, y=120 + 6 + 20 + 40)
    rot.pack_propagate(False)
    rot.tkraise()
    form = ttk.Treeview(rot, height=15, columns=('Fname', 'Mname', 'Lname', 'contact', 'E-mail','room_no','check_in','check_out','total'),selectmode="extended")

    form.heading('#0', text="F-name", anchor=W)
    form.heading('#1', text='M-name', anchor=W)
    form.heading('#2', text='L-name', anchor=W)
    form.heading('#3', text='Contact', anchor=W)
    form.heading('#4', text='E-maill', anchor=W)
    form.heading('#5', text="Room no.", anchor=W)
    form.heading('#6', text="Check-in", anchor=W)
    form.heading('#7', text="Check-out", anchor=W)
    form.heading('#8', text="Time", anchor=W)
    form.heading('#9', text="Total", anchor=W)


    form.column('#0', stretch=YES, width=90)
    form.column('#1', stretch=YES, width=70)
    form.column('#2', stretch=YES, width=70)
    form.column('#3', stretch=YES, width=90)
    form.column('#4', stretch=YES, width=90)
    form.column('#5', stretch=YES, width=90)
    form.column('#6', stretch=YES, width=90)
    form.column('#7', stretch=YES, width=90)
    form.column('#8', stretch=YES, width=60)
    form.column('#9', stretch=YES, width=60)


    form.place(x=0, y=0)
    ttk.Style().configure("Treeview", background="skyblue", foreground="red")
    ttk.Style().configure("Treeview.Heading", bg="red" ,foreground="black")


    vsb = ttk.Scrollbar(rot, orient="vertical", command=form.yview)
    vsb.place(x=795, y=1, height=300 + 22)
    form.configure(yscrollcommand=vsb.set)

    conn = sqlite3.connect("hm_proj.db")
    with conn:
        cur = conn.cursor()
        # cursor.execute('CREATE TABLE if not exists mj (Fname TEXT,Mname TEXT,Lname TEXT,id_no TEXT,Height TEXT,Weight TEXT,increhabit TEXT,Gender TEXT,fathername TEXT,mothername TEXT, Age TEXT,emailid TEXT,Address TEXT,Contact TEXT)')
        cur.execute('SELECT * FROM paymentsf')
        for row in cur.fetchall():
            form.insert('', 0, text=row[1], values=(row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[11]))
    # Button(rot, text="X", font=("times new roman", 10), width=5, bg="red", fg="white", command=rot.destroy).place(x=1200,y=0)

    global  deel
    deel=Frame(root,height=400,width=500,bg="skyblue")
    Button(deel, text="DELETE", font=("times new roman", 10), width=5, bg="red", fg="white",command=delete).place(x=100, y=130)

    Label(deel,text="Enter Room no.",font=("times new roman", 15),fg="red",bg="skyblue").place(x=10,y=30)
    delentry = Entry(deel, font=("times new roman", 15), width=10, bd=5)
    delentry.place(x=10, y=80)
    listofrooms = Listbox(deel, height=9, width=30)
    listofrooms.place(x=5, y=180)
    listofrooms.insert(END, "your searched details")


    def findrooms():
        SEARCH=delentry.get()
        cur.execute("select * FROM paymentsf WHERE r_n=?", (SEARCH,))
        for x in cur.fetchall():
        # print (x)
            listofrooms.delete(0, END)
            listofrooms.insert(END, 'Fname ->' + str(x[1]),"\n" + 'Mname ->' + str(x[2]),"\n"+ "Lname ->"+str(x[3]),"\n"+"contact ->"+str(x[4]),"\n"+"e-mail ->"+str(x[5]),"\n"+"checkin ->"+str(x[7]),"\n"+"checkout ->"+str(x[8]),"\n"+"Time ->"+str(x[9]),"\n"+"Total ->"+str(x[11]),"\n")
            breakpoint()
        listofrooms.delete(0, END)
        listofrooms.insert(0,"no matching found")
        messagebox.showinfo("message","not reserved")
    def advance():
        rot = Frame(root, height=545, width=1200, bg='skyblue')
        rot.place(x=20, y=120 + 6 + 20 + 40)
        rot.pack_propagate(False)
        rot.tkraise()
        Label(rot, text=" -: ADVANCE-BOOKING :-", font=("times new roman", 20), bg="skyblue").place(x=200, y=10)
        form = ttk.Treeview(rot, height=15, columns=(
        'Fname', 'Mname', 'Lname', 'contact', 'E-mail', 'room_no', 'check_in', 'check_out', 'total'),
                            selectmode="extended")

        form.heading('#0', text="F-name", anchor=W)
        form.heading('#1', text='M-name', anchor=W)
        form.heading('#2', text='L-name', anchor=W)
        form.heading('#3', text='Contact', anchor=W)
        form.heading('#4', text='E-maill', anchor=W)
        form.heading('#5', text="Room no.", anchor=W)
        form.heading('#6', text="Check-in", anchor=W)
        form.heading('#7', text="Check-out", anchor=W)
        form.heading('#8', text="Time", anchor=W)
        form.heading('#9', text="Total", anchor=W)

        form.column('#0', stretch=YES, width=90)
        form.column('#1', stretch=YES, width=70)
        form.column('#2', stretch=YES, width=70)
        form.column('#3', stretch=YES, width=90)
        form.column('#4', stretch=YES, width=90)
        form.column('#5', stretch=YES, width=90)
        form.column('#6', stretch=YES, width=90)
        form.column('#7', stretch=YES, width=90)
        form.column('#8', stretch=YES, width=60)
        form.column('#9', stretch=YES, width=60)

        form.place(x=0, y=100)
        ttk.Style().configure("Treeview", background="skyblue", foreground="red")
        ttk.Style().configure("Treeview.Heading", bg="red", foreground="black")

        vsb = ttk.Scrollbar(rot, orient="vertical", command=form.yview)
        vsb.place(x=795, y=100, height=300 + 22)
        form.configure(yscrollcommand=vsb.set)

        conn = sqlite3.connect("hm_proj.db")
        with conn:
            cur = conn.cursor()
            # cursor.execute('CREATE TABLE if not exists mj (Fname TEXT,Mname TEXT,Lname TEXT,id_no TEXT,Height TEXT,Weight TEXT,increhabit TEXT,Gender TEXT,fathername TEXT,mothername TEXT, Age TEXT,emailid TEXT,Address TEXT,Contact TEXT)')
            cur.execute('SELECT * FROM advancebooking1')
            for row in cur.fetchall():
                form.insert('', 0, text=row[1],
                            values=(row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[11]))
        global deel
        deel = Frame(root, height=400, width=500, bg="skyblue")

        def delete1():
            box1 = messagebox.askyesno("CONFARMATION", "if you delete you will be unable to see previous data again")

            if box1 > 0:
                SEARCH = delentry.get()
                conn = sqlite3.connect("hm_proj.db")
                with conn:
                    cur = conn.cursor()
                    cur.execute("DELETE FROM advancebooking1 WHERE r_n=?", (SEARCH,))
                    cur.execute("DELETE FROM advancebooking1 WHERE f_name=?", (SEARCH,))
                    conn.commit()
            delentry.delete(0, END)
            rot.destroy()
            advance()
        Button(deel, text="DELETE", font=("times new roman", 10), width=5, bg="red", fg="white", command=delete1).place(x=100, y=130)

        Label(deel, text="Enter Room no.", font=("times new roman", 15), fg="red", bg="skyblue").place(x=10, y=30)
        delentry = Entry(deel, font=("times new roman", 15), width=10, bd=5)
        delentry.place(x=10, y=80)
        listofrooms = Listbox(deel, height=9, width=30)
        listofrooms.place(x=5, y=180)
        listofrooms.insert(END, "your searched details")

        def findrooms1():
            SEARCH = delentry.get()
            cur.execute("select * FROM advancebooking1 WHERE r_n=?", (SEARCH,))

            for x in cur.fetchall():
                # print (x)
                listofrooms.delete(0, END)
                listofrooms.insert(END, 'Fname ->' + str(x[1]), "\n" + 'Mname ->' + str(x[2]),
                                   "\n" + "Lname ->" + str(x[3]), "\n" + "contact ->" + str(x[4]),
                                   "\n" + "e-mail ->" + str(x[5]), "\n" + "checkin ->" + str(x[7]),
                                   "\n" + "checkout ->" + str(x[8]), "\n" + "Time ->" + str(x[9]),
                                   "\n" + "Total ->" + str(x[11]), "\n")
                breakpoint()
            listofrooms.delete(0, END)
            listofrooms.insert(0, "no matching found")
            messagebox.showinfo("message", "not reserved")

        Button(deel, text="Search1", font=("times new roman", 10), width=5, bg="red", fg="white",command=findrooms1).place(x=10, y=130)
        deel.place(x=850, y=200)

        rot.place(x=20, y=120 + 6 + 20 + 40)


    Button(rot, text="View Advance Booking", bg="red", relief="groove", fg="white", font=('times new roman', 20),command=advance).place(x=50, y=350)

    Button(deel, text="Search", font=("times new roman", 10), width=5, bg="red", fg="white", command=findrooms).place(x=10, y=130)
    deel.place(x=850,y=200)


    rot.place(x=20, y=120 + 6 + 20 + 40)



def rooms():
        b_frame = Frame(root, height=545, width=1280, bg='skyblue')
        b_frame.place(x=20, y=120 + 6 + 20 + 40)
        b_frame.pack_propagate(False)
        b_frame.tkraise()

        Label(b_frame, text="Room no.",bg="skyblue").place(x=50, y=20)
        Label(b_frame, text="bed", bg="skyblue").place(x=200, y=20)
        Label(b_frame, text="AC", bg="skyblue").place(x=350, y=20)
        Label(b_frame, text="T.v", bg="skyblue").place(x=500, y=20)
        Label(b_frame, text="internet", bg="skyblue").place(x=650, y=20)
        Label(b_frame, text="price", bg="skyblue").place(x=800, y=20)
        Label(b_frame, text="status", bg="skyblue").place(x=950, y=20)

        roome1=Entry(b_frame,bd=3,width=10)
        roome1.place(x=50,y=50)
        bede1=ttk.Combobox(b_frame,width=10)
        bede1.insert(INSERT,'select')
        bede1["values"]=['1','2','3']
        bede1.place(x=200,y=50)

        ace1 = ttk.Combobox(b_frame, width=10)
        ace1.insert(INSERT, 'select')
        ace1["values"] = ['yes', 'No']
        ace1.place(x=350, y=50)

        tve1 = ttk.Combobox(b_frame, width=10)
        tve1.insert(INSERT, 'select')
        tve1["values"] = ['yes', 'No']
        tve1.place(x=500, y=50)

        nete1 = ttk.Combobox(b_frame, width=10)
        nete1.insert(INSERT, 'select')
        nete1["values"] = ['yes', 'No']
        nete1.place(x=650, y=50)

        price1 = Entry(b_frame,bd=3,width=10)
        price1.place(x=800, y=50)

        status=Entry(b_frame,bd=3,width=10)
        status.insert(INSERT,'Unreserved')
        status.place(x=950,y=50)

        def add():
            if roome1.get()=="":
                messagebox.showerror("error","please enter room number!")
            else:

                conn = sqlite3.connect("hm_proj.db")
                with conn:
                    cur = conn.cursor()
                    cur.execute("insert into roomd values(?,?,?,?,?,?,?)",(roome1.get(),bede1.get(),ace1.get(),tve1.get(),nete1.get(),price1.get(),status.get()))
                    messagebox.showinfo("Successful", "Room added successfully")
                    con.commit()
                    rooms()

        def search():
            if roome1.get()=="":
                messagebox.showerror("error","please enter room number!")

            SEARCH = roome1.get()
            conn = sqlite3.connect("hm_proj.db")
            with conn:
                cur = conn.cursor()
                cur.execute('SELECT beds FROM roomd WHERE rn=?', (SEARCH,))
                for row1 in cur.fetchone():
                    bede1.set(row1)
                cur.execute('SELECT ac FROM roomd WHERE rn=?', (SEARCH,))
                for row2 in cur.fetchone():
                    ace1.set(row2)
                cur.execute('SELECT tv FROM roomd WHERE rn=?', (SEARCH,))
                for row3 in cur.fetchone():
                    tve1.set(row3)
                cur.execute('SELECT internet FROM roomd WHERE rn=?', (SEARCH,))
                for row4 in cur.fetchone():
                    nete1.set(row4)
                cur.execute('SELECT price FROM roomd WHERE rn=?', (SEARCH,))
                for row5 in cur.fetchone():
                    price1.delete(0,END)
                    price1.insert(INSERT,row5)

                cur.execute('SELECT rstatus FROM roomd WHERE rn=?', (SEARCH,))
                for row6 in cur.fetchone():
                    status.delete(0,END)
                    status.insert(INSERT,row6)

        def update():
            if roome1.get()=="":
                messagebox.showerror("error","please enter room number!")
            else:

                box1 = messagebox.askyesno("CONFARMATION","if you update you will be unable to see previous data again")
                if box1 > 0:
                    SEARCH = roome1.get()
                    conn = sqlite3.connect("hm_proj.db")
                    with conn:
                        cur = conn.cursor()
                        cur.execute('UPDATE roomd SET beds=? WHERE rn=?', (bede1.get(), SEARCH,))
                        cur.execute('UPDATE roomd SET ac=? WHERE rn=?', (ace1.get(), SEARCH,))
                        cur.execute('UPDATE roomd SET tv=? WHERE rn=?', (tve1.get(), SEARCH,))
                        cur.execute('UPDATE roomd SET internet=? WHERE rn=?', (nete1.get(), SEARCH,))
                        cur.execute('UPDATE roomd SET price=? WHERE rn=?', (price1.get(), SEARCH,))
                        cur.execute('UPDATE roomd SET rstatus=? WHERE rn=?', (status.get(), SEARCH,))
                        conn.commit()
                        rooms()

        def de():
            if roome1.get()=="":
                messagebox.showerror("error","please enter room number!")
            else:

                box1 = messagebox.askyesno("CONFARMATION", "Do you want to delete room data? ")
                if box1>0:
                    SEARCH=roome1.get()
                    conn = sqlite3.connect("hm_proj.db")
                    with conn:
                        cur = conn.cursor()
                        cur.execute("DELETE FROM roomd WHERE rn=?", (SEARCH,))
                        conn.commit()

                        rooms()

        Button(b_frame,text="  ADD ",bg="cyan",fg="red",relief="groove",font=('times new roman',15),command=add).place(x=250,y=100)
        Button(b_frame, text=" EDIT ", bg="cyan", fg="red", relief="groove",font=('times new roman',15),command=search).place(x=350, y=100)
        Button(b_frame, text="UPDATE", bg="cyan", fg="red", relief="groove",font=('times new roman',15),command=update).place(x=450, y=100)
        Button(b_frame, text="DELETE", bg="cyan", fg="red", relief="groove",font=('times new roman',15),command=de).place(x=600, y=100)






        form = ttk.Treeview(b_frame, height=15, columns=('Room no.','bed','Ac','T.v','internet','price','status'),selectmode="extended")

        form.heading('#0', text="Room no.", anchor=W)
        form.heading('#1', text='bed', anchor=W)
        form.heading('#2', text='Ac', anchor=W)
        form.heading('#3', text='T.v', anchor=W)
        form.heading('#4', text='internet', anchor=W)
        form.heading('#5', text="price", anchor=W)
        form.heading('#6', text="status", anchor=W)


        form.column('#0', stretch=YES, width=80)
        form.column('#1', stretch=YES, width=80)
        form.column('#2', stretch=YES, width=80)
        form.column('#3', stretch=YES, width=80)
        form.column('#4', stretch=YES, width=80)
        form.column('#5', stretch=YES, width=80)
        form.column('#6', stretch=YES, width=80)


        form.place(x=150, y=180)
        ttk.Style().configure("Treeview", background="skyblue", foreground="red")
        ttk.Style().configure("Treeview.Heading", bg="red", foreground="black")

        vsb = ttk.Scrollbar(b_frame, orient="vertical", command=form.yview)
        vsb.place(x=895, y=180, height=300 + 22)
        form.configure(yscrollcommand=vsb.set)

        conn = sqlite3.connect("hm_proj.db")
        with conn:
            cur = conn.cursor()
            # cursor.execute('CREATE TABLE if not exists mj (Fname TEXT,Mname TEXT,Lname TEXT,id_no TEXT,Height TEXT,Weight TEXT,increhabit TEXT,Gender TEXT,fathername TEXT,mothername TEXT, Age TEXT,emailid TEXT,Address TEXT,Contact TEXT)')
            cur.execute('SELECT * FROM roomd')
            for row in cur.fetchall():
                form.insert('', 0, text=row[0],values=(row[1], row[2], row[3], row[4], row[5],row[6]))






        '''sidebuttons = Text(b_frame, width=1, height=19)
        sc = Scrollbar(b_frame, command=sidebuttons.yview, width=10, bg='lightsteelblue3')
        sidebuttons.configure(yscrollcommand=sc.set)
        sc.pack(side='left', fill=Y)
        sidebuttons.place(x=10, y=0)

        def roomdet(rno):
            Label(b_frame, text='Room %s' % rno, font='msserif 15', fg='white', bg='cyan4', width=10).place(x=535, y=0)
            cur.execute("select * from roomd where rn = ?", (rno,))
            rdata = cur.fetchall()
            # print (rdata)
            smf1 = Frame(b_frame, height=120, width=145, bg='white')
            hline = Frame(b_frame, height=10, width=960, bg='cyan4')
            hline.place(x=122, y=27)
            vline = Frame(b_frame, height=400, width=7, bg='lightsteelblue3')
            vline.place(x=122, y=0)
            tr = Label(smf1, text='Total Bed(s):', fg='white', bg='cyan4', width=100, height=2, font='msserif 15')
            tr.pack(side='top')
            smf1.pack_propagate(False)
            smf1.place(x=129 + 3, y=30)
            Label(smf1, text=str(rdata[0][1]), fg='cyan4', bg='white', font='msserif 35').pack()
            smf2 = Frame(b_frame, height=120, width=145, bg='white')
            tr = Label(smf2, text='AC Available?', fg='white', bg='cyan4', width=100, height=2, font='msserif 15')
            tr.pack(side='top')
            smf2.pack_propagate(False)
            smf2.place(x=140 * 2 + 5 + 3 * 2, y=30)
            Label(smf2, text=str(rdata[0][2]), fg='cyan4', bg='white', font='msserif 35').pack()
            smf2 = Frame(b_frame, height=120, width=145, bg='white')
            tr = Label(smf2, text='TV Available?', fg='white', bg='cyan4', width=100, height=2, font='msserif 15')
            tr.pack(side='top')
            smf2.pack_propagate(False)
            smf2.place(x=140 * 3 + 12 + 5 * 2 + 3 * 3, y=30)
            Label(smf2, text=str(rdata[0][3]), fg='cyan4', bg='white', font='msserif 35').pack()
            smf2 = Frame(b_frame, height=120, width=145, bg='white')
            tr = Label(smf2, text='  Wifi ?', fg='white', bg='cyan4', width=100, height=2, font='msserif 15')
            tr.pack(side='top')
            smf2.pack_propagate(False)
            smf2.place(x=140 * 4 + 12 * 2 + 5 * 3 + 3 * 4, y=30)
            Label(smf2, text=str(rdata[0][4]), fg='cyan4', bg='white', font='msserif 35').pack()
            smf2 = Frame(b_frame, height=120, width=145, bg='white')
            tr = Label(smf2, text=' Price ?', fg='white', bg='cyan4', width=100, height=2, font='msserif 15')
            tr.pack(side='top')
            smf2.pack_propagate(False)
            smf2.place(x=140 * 5 + 12 * 3 + 5 * 4 + 3 * 5, y=30)
            Label(smf2, text=str(rdata[0][5]), fg='cyan4', bg='white', font='msserif 35').pack()
            smf2 = Frame(b_frame, height=120, width=145, bg='white')
            tr = Label(smf2, text='Booked ?', fg='white', bg='cyan4', width=100, height=2, font='msserif 15')
            tr.pack(side='top')
            # print (rdata)
            smf2.pack_propagate(False)
            smf2.place(x=140 * 6 + 12 * 4 + 5 * 5 + 3 * 6, y=30)
            p = ''
            if rdata[0][6] == 'Unreserved':
                p = 'No'
            else:
                p = 'Yes'
            Label(smf2, text=p, fg='cyan4', bg='white', font='msserif 35').pack()

        roomdet(1)
        
        sidebuttons.configure(state='disabled')
        
        b1 = Button(b_frame, font='mssherif 10', text="Room 1", bg='white', fg='cyan4', width=10,command=lambda: roomdet(1))
        b2 = Button(b_frame, font='mssherif 10', text="Room 2", bg='white', fg='cyan4', width=10,command=lambda: roomdet(2))
        b3 = Button(b_frame, font='mssherif 10', text="Room 3", bg='white', fg='cyan4', width=10,command=lambda: roomdet(3))
        b4 = Button(b_frame, font='mssherif 10', text="Room 4", bg='white', fg='cyan4', width=10,command=lambda: roomdet(4))
        b5 = Button(b_frame, font='mssherif 10', text="Room 5", bg='white', fg='cyan4', width=10,command=lambda: roomdet(5))
        b6 = Button(b_frame, font='mssherif 10', text="Room 6", bg='white', fg='cyan4', width=10,command=lambda: roomdet(6))
        b7 = Button(b_frame, font='mssherif 10', text="Room 7", bg='white', fg='cyan4', width=10,command=lambda: roomdet(7))
        b8 = Button(b_frame, font='mssherif 10', text="Room 8", bg='white', fg='cyan4', width=10,command=lambda: roomdet(8))
        b9 = Button(b_frame, font='mssherif 10', text="Room 9", bg='white', fg='cyan4', width=10,command=lambda: roomdet(9))
        b10 = Button(b_frame, font='mssherif 10', text="Room 10", bg='white', fg='cyan4', width=10, command=lambda: roomdet(10))
        b11 = Button(b_frame, font='mssherif 10', text="Room 11", bg='white', fg='cyan4', width=10,command=lambda: roomdet(11))
        b12 = Button(b_frame, font='mssherif 10', text="Room 12", bg='white', fg='cyan4', width=10,command=lambda: roomdet(12))
        b13 = Button(b_frame, font='mssherif 10', text="Room 13", bg='white', fg='cyan4', width=10, command=lambda: roomdet(13))
        b14 = Button(b_frame, font='mssherif 10', text="Room 14", bg='white', fg='cyan4', width=10,command=lambda: roomdet(14))
        b15 = Button(b_frame, font='mssherif 10', text="Room 15", bg='white', fg='cyan4', width=10, command=lambda: roomdet(15))
        b16 = Button(b_frame, font='mssherif 10', text="Room 16", bg='white', fg='cyan4', width=10,  command=lambda: roomdet(16))
        b17 = Button(b_frame, font='mssherif 10', text="Room 17", bg='white', fg='cyan4', width=10,   command=lambda: roomdet(17))
        b18 = Button(b_frame, font='mssherif 10', text="Room 18", bg='white', fg='cyan4', width=10, command=lambda: roomdet(18))
        b19 = Button(b_frame, font='mssherif 10', text="Room 19", bg='white', fg='cyan4', width=10,      command=lambda: roomdet(19))
        b20 = Button(b_frame, font='mssherif 10', text="Room 20", bg='white', fg='cyan4', width=10,  command=lambda: roomdet(20))
        sidebuttons.window_create("end", window=b1)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b2)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b3)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b4)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b5)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b6)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b7)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b8)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b9)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b10)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b11)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b12)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b13)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b14)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b15)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b16)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b17)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b18)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b19)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b20)'''


def staff():
        b_frame = Frame(root, height=530, width=1280, bg='skyblue')
        '''path = "newbg6lf.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(b_frame, image=img, height=400, width=1080)
        label.image = img
        label.place(x=0, y=0)
        l = Label(b_frame, text='Details of Staff will be Available soon')
        # l.place(x=180,y=0)'''
        '''smf4 = Frame(b_frame,height=150,width=175,bg='white')
        tc = Label(smf4,text='Total Customers:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
        tc.pack(side='top')
        smf4.pack_propagate(False)
        smf4.place(x=540+8,y=30)
        Label(smf4,text='40',fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')
        '''
        emp1f = Frame(b_frame)
        path1 = "newman.jpg"
        img1 = ImageTk.PhotoImage(Image.open(path1))
        emp1 = Label(emp1f, image=img1,bg="skyblue")
        emp1.image = img1
        emp1.pack()
        emp1f.place(x=0, y=0)
        emp1inf = Frame(b_frame, bg='skyblue', height=122, width=300)
        Label(emp1inf, text="Manager", bg='skyblue', font='msserif 17 bold').place(x=60, y=0)
        Label(emp1inf, text="Mr. Mahi varshney", bg='skyblue', fg="Grey", font='msserif 10').place(x=60, y=37)
        Label(emp1inf, text="Extention : 025", bg='skyblue', fg="Grey", font='msserif 10').place(x=60, y=59)
        Label(emp1inf, text="Mail : Manager@hotelname.com", bg='skyblue', fg="Grey", font='msserif 10').place(x=60, y=83)
        emp1inf.pack_propagate(False)
        emp1inf.place(x=117, y=1)

        emp1f = Frame(b_frame)
        path2 = "receptionnew.jpg"
        img2 = ImageTk.PhotoImage(Image.open(path2))
        emp1 = Label(emp1f, image=img2)
        emp1.image = img2
        emp1.pack()
        emp1f.place(x=657, y=0)
        emp1inf = Frame(b_frame, bg='skyblue', height=116, width=310)
        Label(emp1inf, text="Customer Executive", bg='skyblue', font='msserif 17 bold').place(x=45,
                                                                                            y=0)  # pack(side='top')
        Label(emp1inf, text="Ms. Garima varshney", bg='skyblue', fg="Grey", font='msserif 10').place(x=45, y=37)
        Label(emp1inf, text="Extention : 032", bg='skyblue', fg="Grey", font='msserif 10').place(x=45, y=59)
        Label(emp1inf, text="Mail : Costoexe@hotelname.com", bg='skyblue', fg="Grey", font='msserif 10').place(x=45, y=83)
        emp1inf.pack_propagate(False)
        emp1inf.place(x=767, y=2)

        emp1f = Frame(b_frame)
        path3 = "fchefnew.jpg"
        img3 = ImageTk.PhotoImage(Image.open(path3))
        emp1 = Label(emp1f, image=img3)
        emp1.image = img3
        emp1.pack()
        emp1f.place(x=0, y=152)
        emp1inf = Frame(b_frame, bg='skyblue', height=121, width=320)
        Label(emp1inf, text="Restaurant", bg='skyblue', font='msserif 17 bold').place(x=72, y=0)  # pack(side='top')
        Label(emp1inf, text="Ms. Reshu varshney (Head)", bg='skyblue', fg="Grey", font='msserif 10').place(x=72, y=37)
        Label(emp1inf, text="Extention : 028", bg='skyblue', fg="Grey", font='msserif 10').place(x=72, y=59)
        Label(emp1inf, text="Mail : Restaurant@hotelname.com", bg='skyblue', fg="Grey", font='msserif 10').place(x=72,
                                                                                                               y=83)
        emp1inf.pack_propagate(False)
        emp1inf.place(x=99, y=153)
        emp1inf.tkraise()

        emp1f = Frame(b_frame)
        path4 = "roomservicenew.jpg"
        img4 = ImageTk.PhotoImage(Image.open(path4))
        emp1 = Label(emp1f, image=img4,bg="skyblue")
        emp1.image = img4
        emp1.pack()
        emp1f.place(x=657, y=152)
        emp1inf = Frame(b_frame, bg='skyblue', height=124, width=315)
        Label(emp1inf, text="Room Service", bg='skyblue', font='msserif 17 bold').place(x=55, y=0)  # pack(side='top')
        Label(emp1inf, text="Mr. Ajaypal tripathi (Head)", bg='skyblue', fg="Grey", font='msserif 10').place(x=55, y=37)
        Label(emp1inf, text="Extention : 041", bg='skyblue', fg="Grey", font='msserif 10').place(x=55, y=59)
        Label(emp1inf, text="Mail : Roomsserv@hotelname.com", bg='skyblue', fg="Grey", font='msserif 10').place(x=55,
                                                                                                              y=83)
        emp1inf.pack_propagate(False)
        emp1inf.place(x=763, y=153)
        # b_frame.pack_propagate(False)
        '''sidebuttons = Text(b_frame,width=1,height=19)
        sc = Scrollbar(b_frame,command=sidebuttons.yview,width=10,bg='lightsteelblue3')
        sidebuttons.configure(yscrollcommand=sc.set)
        sc.pack(side='left',fill=Y)
        sidebuttons.place(x=10,y=0)
        b1  = Button(b_frame,font='mssherif 10', text="Room 1", bg='white',fg='cyan4',width=10)
        b2  = Button(b_frame,font='mssherif 10', text="Room 2", bg='white',fg='cyan4',width=10)
        b3  = Button(b_frame,font='mssherif 10', text="Room 3", bg='white',fg='cyan4',width=10)
        b4  = Button(b_frame,font='mssherif 10', text="Room 4", bg='white',fg='cyan4',width=10)
        b5  = Button(b_frame,font='mssherif 10', text="Room 5", bg='white',fg='cyan4',width=10)
        b6  = Button(b_frame,font='mssherif 10', text="Room 6", bg='white',fg='cyan4',width=10)
        b7  = Button(b_frame,font='mssherif 10', text="Room 7", bg='white',fg='cyan4',width=10)
        b8  = Button(b_frame,font='mssherif 10', text="Room 8", bg='white',fg='cyan4',width=10)
        b9  = Button(b_frame,font='mssherif 10', text="Room 9", bg='white',fg='cyan4',width=10)
        b10 = Button(b_frame,font='mssherif 10', text="Room 10",bg='white',fg='cyan4',width=10)
        sidebuttons.window_create("end",window=b1)
        sidebuttons.insert("end","\n")
        sidebuttons.window_create("end",window=b2)
        sidebuttons.insert("end","\n")
        sidebuttons.window_create("end",window=b3)
        sidebuttons.insert("end","\n")
        sidebuttons.window_create("end",window=b4)
        sidebuttons.insert("end","\n")
        sidebuttons.window_create("end",window=b5)
        sidebuttons.insert("end","\n")
        sidebuttons.window_create("end",window=b6)
        sidebuttons.insert("end","\n")
        sidebuttons.window_create("end",window=b7)
        sidebuttons.insert("end","\n")
        sidebuttons.window_create("end",window=b8)
        sidebuttons.insert("end","\n")
        sidebuttons.window_create("end",window=b9)
        sidebuttons.insert("end","\n")
        sidebuttons.window_create("end",window=b10)'''
        Frame(b_frame, height=13, width=250, bg='Skyblue').place(x=410, y=2)
        Frame(b_frame, height=13, width=250, bg='skyblue').place(x=410, y=153)
        # Frame(b_frame,height=180,width=13,bg='white').place(x=406,y=20)

        b_frame.place(x=20, y=120 + 6 + 20 + 40)
        b_frame.pack_propagate(False)
        b_frame.tkraise()



def hotel_status():
        global b_frame
        b_frame = Frame(root, height=530, width=1280, bg='skyblue')
        b_frame.place(x=20, y=120 + 6 + 20 + 40)
        b_frame.pack_propagate(False)
        '''path = "newbg6lf.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(b_frame, image=img, height=400, width=1080)
        label.image = img
        label.place(x=0, y=0)'''
        cur.execute("select * from hoteld")
        x = cur.fetchall()
        # print(x)
        cur.execute("select count(rn) from roomd")
        x = cur.fetchone()
        print(x)
        cur.execute("select count(rn) from roomd where rstatus = 'Reserved'")
        y = cur.fetchone()
        print(y)
        tor = x[0]
        rer = y[0]
        tos = 21
        avr = int(tor) - int(rer)
        avr = str(avr)
        # print(tor,rer,tos,avr)
        hts = Label(b_frame, text='Hotel Status', font='msserif 15', fg='black', bg='gray91', height=1)
        # ------------inner frames of bottom frame-------------------------

        smf1 = Frame(b_frame, height=150, width=175, bg='white')
        tr = Label(smf1, text='Total Rooms:', fg='white', bg='cyan4', width=100, height=2, font='helvetica 15')
        tr.pack(side='top')
        smf1.pack_propagate(False)
        smf1.place(x=0, y=30)
        Label(smf1, text=tor, fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')

        smf2 = Frame(b_frame, height=150, width=175, bg='white')
        ar = Label(smf2, text='Available Rooms:', fg='white', bg='cyan4', width=130, height=2, font='helvetica 15')
        ar.pack(side='top')
        smf2.pack_propagate(False)
        smf2.place(x=180 + 4, y=30)
        Label(smf2, text=avr, fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')

        smf3 = Frame(b_frame, height=150, width=175, bg='white')
        tre = Label(smf3, text='Total Booking:', fg='white', bg='cyan4', width=130, height=2, font='helvetica 15')
        tre.pack(side='top')
        smf3.pack_propagate(False)
        smf3.place(x=360 + 6, y=30)
        Label(smf3, text=rer, fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')

        smf4 = Frame(b_frame, height=150, width=175, bg='white')
        tc = Label(smf4, text='Total Customers:', fg='white', bg='cyan4', width=130, height=2, font='helvetica 15')
        tc.pack(side='top')
        smf4.pack_propagate(False)
        smf4.place(x=540 + 8, y=30)
        Label(smf4, text='40', fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')

        smf5 = Frame(b_frame, height=150, width=175, bg='white')
        ts = Label(smf5, text='Total Staff:', fg='white', bg='cyan4', width=130, height=2, font='helvetica 15')
        ts.pack(side='top')
        smf5.pack_propagate(False)
        smf5.place(x=720 + 10, y=30)
        Label(smf5, text=tos, fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')
        redf1 = Frame(b_frame, height=8, width=1080, bg='cyan4')

        '''smf6 = Frame(b_frame, height=150, width=175, bg='white')
        ts = Label(smf6, text='Under renovation:', fg='white', bg='cyan4', width=130, height=2, font='helvetica 15')
        ts.pack(side='top')
        smf6.pack_propagate(False)
        smf6.place(x=915, y=30)
        Label(smf6, text='3', fg='cyan4', bg='white', font='msserif 50').place(x=60, y=60)'''
        # redf1 = Frame(b_frame,height=8,width=1080,bg='cyan4')

        # Label(b_frame,text='==================================================================================',fg='cyan4').place(x=0,y=20)
        redf1.place(x=0, y=22)
        Label(b_frame, text='Hotel Status', font='msserif 12', bg='cyan4', fg='white').pack(anchor='center')
        redf1.pack_propagate(False)


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
    categoryentry=Entry(b_frame,width=20,bd=3,bg='cyan')
    categoryentry.place(x=190,y=295)
    # Label(b_frame, text='food name').place(x=10, y=30)
    foodnameentry=Entry(b_frame,width=20,bd=3,bg='cyan')
    foodnameentry.place(x=190,y=350)
    # Label(b_frame,text="price").place(x=10,y=60)
    priceentry=Entry(b_frame,width=20,bd=3,bg='cyan')
    priceentry.place(x=190,y=405)
    conn = sqlite3.connect("hm_proj.db")
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS foodmenu2(category TEXT,item TEXT,price INTEGER,date DATE)')
        con.commit()

    def addfood():
        if categoryentry.get()=="" or foodnameentry.get()=="" or priceentry.get()=="":
            messagebox.showerror('error','please enter all fields')
        else:
            conn = sqlite3.connect("hm_proj.db")
            with conn:
                cur = conn.cursor()
                cur.execute("insert into foodmenu2 values(?,?,?,?)",(categoryentry.get(),foodnameentry.get(),priceentry.get(), today,))
                messagebox.showinfo("Successful", "food added successfully")
                con.commit()
                food()
                categoryentry.delete(0,END)
                foodnameentry.delete(0,END)
                priceentry.delete(0,END)


    form = ttk.Treeview(b_frame, height=15, columns=('CATEGORY','FOOD-NAME','PRICE'),selectmode="extended")

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


    Button(b_frame,text="SAVE",bg="red",relief="groove",fg="white",font=('times new roman',10),command=addfood).place(x=150,y=450)
    cur.execute("select category from foodmenu2")
    con.commit()
    x = cur.fetchall()
    print(x[0])
    # tve1 = ttk.Combobox( width=10,values=['selsect',x[0],x[1],x[2]]

    def orderfood():
        t=date.today()
        print(t)
        c_frame = Frame(root, height=530, width=1280, bg='blue')
        path = "orderfood2.png"
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(c_frame, image=img, height=525, width=1280)
        label.image = img
        label.place(x=0, y=0)

        cur.execute("select category from foodmenu2")
        con.commit()
        x = cur.fetchall()
        print(x[0])
        # tve1 = ttk.Combobox( width=10,values=['selsect',x[0],x[1],x[2]])
        menu = ttk.Combobox(c_frame, width=20)
        menu.insert(INSERT, "select")
        menu["values"] = x  # [:] #[x[0],x[1],x[2]]
        menu.place(x=180, y=250)
        rentry=Entry(c_frame,width=20,bd=3,bg='cyan')
        rentry.place(x=220,y=150)
        qentry = Entry(c_frame, width=20, bd=3, bg='cyan')
        qentry.place(x=410, y=350)
        amtentry = Entry(c_frame, width=20, bd=3, bg='cyan')
        amtentry.place(x=600, y=300)
        amtentry.insert(INSERT, "0.00")


        def scategory(event):
            global fooditem
            itemm = menu.get()
            # cur.execute('select item from foodmenu2 where category=?',(menu.get()))
            cur.execute("select item FROM foodmenu2 WHERE category=?", (itemm,))
            con.commit()
            y = cur.fetchall()
            fooditem = ttk.Combobox(c_frame,width=20)
            fooditem.insert(INSERT, "select item")
            fooditem["values"] = y  # [:] #[x[0],x[1],x[2]]

            fooditem.place(x=180, y=350)

            fooditem.bind("<FocusIn>", sitem)

        def sitem(event):
            global priceitem
            ppp = fooditem.get()
            # cur.execute('select item from foodmenu2 where category=?',(menu.get()))
            cur.execute("select price FROM foodmenu2 WHERE item=?", (ppp,))
            con.commit()
            z = cur.fetchall()
            print(z)
            global priceitem
            priceitem = Entry(c_frame, width=20,bd=3,bg='cyan')
            priceitem.insert(INSERT, z)
            # priceitem["values"] = z  # [:] #[x[0],x[1],x[2]]

            priceitem.place(x=180, y=450)

        menu.bind("<FocusIn>", scategory)


        def amtfb():
            pi = priceitem.get()
            qi = qentry.get()
            conn = sqlite3.connect("hm_proj.db")
            with conn:
                cur = conn.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS foodbills(roomno INTEGER,food TEXT,rate INTEGER,quantity INTEGER,amount INTEGER,date DATE)')
                con.commit()

            # pi=priceitem.get()
            # qi=qentry.get()
            # print(pi)
            # print(qi)
            amt=float(pi)*float(qi)
            conn = sqlite3.connect("hm_proj.db")
            with conn:
                cur = conn.cursor()
                cur.execute("insert into foodbills values(?,?,?,?,?,?)",(rentry.get(), fooditem.get(), priceitem.get(),qentry.get(),amt, today,))
                con.commit()
            # print(amt)
            amtget = float(amtentry.get())
            # print(amtget)
            amtv=amt+amtget
            print(amtv)

            # amtv=float(amtget)+float(amt)

            # afb = str(int(pi)*int(qi))
            amtentry.delete(0,END)
            amtentry.insert(INSERT,amtv)
            messagebox.showinfo("done","booked")
            priceitem.delete(0,END)
            qentry.delete(0,END)


        # qentry.bind("<FocusIn>",amtfb)

        Button(c_frame,text="Book",relief="groove",bg='red',fg="white",command=amtfb).place(x=450,y=400)
        c_frame.place(x=20, y=120 + 6 + 20 + 40)



    # itmee = Button(b_frame, text="select", bg="red", command=sitem)
    # itmee.place(x=200, y=200)
    # cate=Button(b_frame, text="select", bg="red", command=scategory)
    # cate.place(x=200, y=100)
    # b_frame.bind("<Key>",key_pressed)
    # Button(b_frame, text="select", bg="red", command=scategory).place(x=400, y=200)
    Button(b_frame, text="ORDER-FOOD", bg="red", relief="groove", fg="white", font=('times new roman', 20),command=orderfood).place(x=950, y=370)
    b_frame.place(x=20, y=120 + 6 + 20 + 40)





    '''fe1=Entry(b_frame,width=5,bd=3)
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
    Button(b_frame, text="Save", bd=3, bg="red", fg="white", command=foodbill).place(x=1100, y=200)'''



def detailss():
    chklist.delete(0,END)
    conn = sqlite3.connect("hm_proj.db")
    cur=conn.cursor()
    SEARCH = chkout.get()
    cur.execute("select * FROM paymentsf WHERE r_n=?", (SEARCH,))
    for x in cur.fetchall():
        room = int(str(x[11]))
        print(room)
        # print (x)
        chklist.delete(0, END)
        chklist.insert(END, "*---------------------------HOTEL BILL--------------------------*","\n","\n","\n"+'Name ->          ' + str(x[1])+" "+ str(x[2])+" "+ str(x[3]),"\n" + "contact ->        " + str(x[4]), "\n" + "e-mail ->          " + str(x[5]),
                       "\n" + "checkin ->        " + str(x[7]),"\n" + "Time ->            " + str(x[9]), "\n","\n"+ "Room rent ->            " + str(x[11]), "\n")
        global rrent
        rrent=int(x[11])
        print(rrent)
        chklist.insert(END,
                       "  -------------------------------------------------Food Bill-------------------------------------------------------",
                       "\n", "\t")

        form = ttk.Treeview(b_frame, height=5, columns=('food', 'rate', 'quantity','amount','date'), selectmode="extended")

        form.heading('#0', text="food", anchor=W)
        form.heading('#1', text='rate', anchor=W)
        form.heading('#2', text='quantity', anchor=W)
        form.heading('#3', text='amount', anchor=W)
        form.heading('#4', text='date', anchor=W)

        form.column('#0', stretch=YES, width=90)
        form.column('#1', stretch=YES, width=50)
        form.column('#2', stretch=YES, width=50)
        form.column('#3', stretch=YES, width=50)
        form.column('#4', stretch=NO, width=80)

        form.place(x=30, y=240)
        ttk.Style().configure("Treeview", background="skyblue", foreground="red")
        ttk.Style().configure("Treeview.Heading", bg="red", foreground="black")

        vsb = ttk.Scrollbar(b_frame, orient="vertical", command=form.yview)
        vsb.place(x=550, y=240, height=100 + 22)
        form.configure(yscrollcommand=vsb.set)

        conn = sqlite3.connect("hm_proj.db")
        with conn:
            cur = conn.cursor()
            # cursor.execute('CREATE TABLE if not exists mj (Fname TEXT,Mname TEXT,Lname TEXT,id_no TEXT,Height TEXT,Weight TEXT,increhabit TEXT,Gender TEXT,fathername TEXT,mothername TEXT, Age TEXT,emailid TEXT,Address TEXT,Contact TEXT)')
            cur.execute("select * FROM foodbills WHERE roomno=?", (SEARCH,))
            global sum
            sum=0
            for row in cur.fetchall():


                form.insert('', 0, text=row[1], values=(row[2], row[3],row[4],row[5]))
                sum = sum + int(row[4])
        chklist.insert(END, "\n","\n","\n","\n","\n","\n","\n","\n", "    Total Food Bill -->  " + str(sum) + "\n\n")
        global gtotal
        gtotal = int(rrent) + int(sum)
        print(gtotal)
        chklist.insert(END, "----------------------------------------------------------------------------",
                       "\n\n\n", " *GRAND TOTAL--> " + str(gtotal))
        breakpoint()

        # cur.execute("select * FROM foodbills WHERE roomno=?", (SEARCH,))

        # chklist.insert(END," FOOD               RATE.               QUANTITY               AMOUNT                  DATE")
        # global sum
        # sum=0
        # for x in cur.fetchall():

            # fody = int(str(x[1]))
            # print(fody)
            # print (str(x[:]))
            # chklist.insert(END,str(x[1])+"                 " + str(x[2])+"                 " + str(x[3])+"                 " + str(x[4])+"                 "+str(x[5]))

            # sum=sum+int(x[4])
            # chlist.insert(INSERT,)

            # chklist.insert(END,"foodbill ->                     "+str(x[1]),"\n","\n")

            # global gt
            # gt=str(room+fody)
            # /chklist.insert(END,"*Grand Total  ->         "+str(gt)+" Rs./")
        # chklist.insert(END,"\n","    Total Food Bill -->  "+str(sum)+"\n\n")
        # global gtotal
        # gtotal=int(rrent)+int(sum)
        # print(gtotal)
        # chklist.insert(END,"----------------------------------------------------------------------------","\n\n\n"," *GRAND TOTAL--> "+str(gtotal))
        # breakpoint()
    checkout()
    chklist.insert(END,"NO MATCHING FOUND !!!!")
def checkout():
    global b_frame
    global chkout
    global chklist
    b_frame = Frame(root, height=530, width=1280, bg='skyblue')
    b_frame.place(x=20, y=120 + 6 + 20 + 40)
    b_frame.pack_propagate(False)
    Label(b_frame,text="Room No. ",bg="skyblue",fg="white").place(x=15,y=10)
    chkout=Entry(b_frame,width=8,bd=3)
    chkout.place(x=100,y=10)
    Button(b_frame,text="check",bd=3,command=detailss,bg="red",fg="white",relief="groove").place(x=170,y=10)

    chklist = Listbox(b_frame, height=30, width=100,bg="skyblue",fg="red")
    chklist.place(x=10, y=40)
    # Label(b_frame,text="* Room rent ",bg='skyblue',fg="white").place(x=500,y=50)
    # Label(b_frame, text="* food bill ", bg='skyblue', fg="white").place(x=500, y=100)
    # roompay=Entry(b_frame,width=10,bd=1)
    # roompay.place(x=600,y=50)
    # foodpay = Entry(b_frame, width=10, bd=1)
    # foodpay.place(x=600, y=100)
    Label(b_frame, text="* Grand Total ", bg='skyblue').place(x=700, y=150)
    totalpay = Entry(b_frame, width=15, bd=5)
    totalpay.place(x=800, y=150)
    totalpay.delete(0,END)
    # paytotal=str(int(roompay.get())+int(foodpay.get()))
    def ppp():
        payroot = Tk()
        payroot.title("Payment")
        payroot.minsize(height=236, width=302)
        payroot.configure(bg='White')
        # global pmethod
        pmethod=StringVar()

        Label(payroot, text='Select an option to pay ' +totalpay.get(), font='msserif 14 bold',
              bg='White').place(x=0, y=0)
        Frame(payroot, height=4, width=300, bg='cyan4').place(x=0, y=39)
        Radiobutton(payroot, text='Cash  ', bg='White', variable=pmethod, value=1, font='helvetica 15', width=5).place(
            x=0, y=43 + 10)
        Radiobutton(payroot, text='Card   ', bg='White', variable=pmethod, value=2, font='helvetica 15', width=5).place(
            x=0, y=80 + 10)
        Radiobutton(payroot, text='UPI     ', bg='White', variable=pmethod, value=3, font='helvetica 15',
                    width=5).place(x=0, y=115 + 10)
        Radiobutton(payroot, text='Paytm ', bg='White', variable=pmethod, value=4, font='helvetica 15', width=5).place(
            x=0, y=150 + 10)

        def f():
            if pmethod != '':
                print(pmethod.get())
                print('pmethod value')
                cur.execute("select id from paymentsf order by id desc")

                x = cur.fetchone()
                cid = int(x[0])
                cid += 1

                ask = messagebox.askyesno("Successful", "Payment Successful\nDo you want to print reciept ?")
                if ask == 'yes':
                    def createfile():
                        fl = open("reciept.txt", "w")
                        fl.write("reciept will come here")

                payroot.destroy()
            else:
                messagebox.showwarning("Not selected", "Please Select the payment method")
                # print (cid)
                # print (pmethod.get())

        Button(payroot, text='Pay', font='msserif 12', bg='Green', fg='White', width=28, command=f).place(x=0, y=200)
        Label(payroot, text='Your unique payment id :', font='msserif', bg='White')  # .place(x=0,y=25)
    def unreserve():
        if (chkout.get() == 'Enter Room Number') or (chkout.get() == ''):
            messagebox.showerror('Entries not filled', 'Kindly Enter room Number')
        else:
            cur.execute("update roomd set rstatus='Unreserved' where rn = ? ", (chkout.get(),))
            messagebox.showinfo("Successful", "Room empty successfully")

            con.commit()
            cur.execute("create table if not exists checkoutlist(room INTEGER,name TEXT,chekin DATE,room_rent INTEGER,food_bill INTEGER,totalbill INTEGER,checkout DATE)")
            con.commit()
            cur.execute("select * FROM paymentsf WHERE r_n=?", (chkout.get(),))
            for x in cur.fetchall():
                name=x[1]+x[2]+x[3]
                chkin=x[7]
            con.commit()

            todaya=date.today()
            cur.execute("insert into checkoutlist values(?,?,?,?,?,?,?)",(chkout.get(),name,chkin,rrent,sum,gtotal,todaya))
            cur.execute("delete  FROM paymentsf WHERE r_n=?", (chkout.get(),))
            cur.execute("delete  FROM foodbills WHERE roomno=?", (chkout.get(),))
            con.commit()

    def checkoutlist():
        rot = Frame(root, height=545, width=1200, bg='skyblue')
        rot.place(x=20, y=120 + 6 + 20 + 40)
        rot.pack_propagate(False)
        rot.tkraise()
        Label(rot,text=" -: CHECK-OUT LIST :-",font=("times new roman",20),bg="skyblue").place(x=200,y=10)
        form = ttk.Treeview(rot, height=15, columns=('roomno','name','checkin','roomrent','foodbill','totalbill','checkout'),
                            selectmode="extended")

        form.heading('#0', text="Roomno", anchor=W)
        form.heading('#1', text='name', anchor=W)
        form.heading('#2', text='checkin', anchor=W)
        form.heading('#3', text='roomrent', anchor=W)
        form.heading('#4', text='foodbill', anchor=W)
        form.heading('#5', text="total bill", anchor=W)
        form.heading('#6', text="Check-out", anchor=W)


        form.column('#0', stretch=YES, width=90)
        form.column('#1', stretch=YES, width=100)
        form.column('#2', stretch=YES, width=70)
        form.column('#3', stretch=YES, width=90)
        form.column('#4', stretch=YES, width=90)
        form.column('#5', stretch=YES, width=90)
        form.column('#6', stretch=YES, width=90)


        form.place(x=0, y=100)
        ttk.Style().configure("Treeview", background="skyblue", foreground="red")
        ttk.Style().configure("Treeview.Heading", bg="red", foreground="black")

        vsb = ttk.Scrollbar(rot, orient="vertical", command=form.yview)
        vsb.place(x=805, y=100, height=300 + 22)
        form.configure(yscrollcommand=vsb.set)

        conn = sqlite3.connect("hm_proj.db")
        with conn:
            cur = conn.cursor()
            # cursor.execute('CREATE TABLE if not exists mj (Fname TEXT,Mname TEXT,Lname TEXT,id_no TEXT,Height TEXT,Weight TEXT,increhabit TEXT,Gender TEXT,fathername TEXT,mothername TEXT, Age TEXT,emailid TEXT,Address TEXT,Contact TEXT)')
            cur.execute('SELECT * FROM checkoutlist')
            for row in cur.fetchall():
                form.insert('', 0, text=row[0],
                            values=(row[1], row[2], row[3], row[4], row[5],row[6]))
        # Button(rot, text="X", font=("times new roman", 10), width=5, bg="red", fg="white", command=rot.destroy).place(x=1200,y=0)

        global deel
        chkdetails = Frame(root, height=400, width=500, bg="skyblue")


        Label(chkdetails, text="Enter Room no.", font=("times new roman", 15), fg="red", bg="skyblue").place(x=10, y=30)
        delentry = Entry(chkdetails, font=("times new roman", 15), width=10, bd=5)
        delentry.place(x=10, y=80)
        listofrooms = Listbox(chkdetails, height=9, width=30)
        listofrooms.place(x=5, y=180)
        listofrooms.insert(END, "your searched details")

        def delete2():
            box1 = messagebox.askyesno("CONFARMATION", "if you delete you will be unable to see previous data again")

            if box1 > 0:
                SEARCH = delentry.get()
                conn = sqlite3.connect("hm_proj.db")
                with conn:
                    cur = conn.cursor()
                    cur.execute("DELETE FROM checkoutlist WHERE room=?", (SEARCH,))
                    conn.commit()
            delentry.delete(0, END)
            rot.destroy()
            checkoutlist()


        def findcheckout():
            SEARCH = delentry.get()
            cur.execute("select * FROM checkoutlist WHERE room=?", (SEARCH,))
            for x in cur.fetchall():
                # print (x)
                listofrooms.delete(0, END)
                listofrooms.insert(END, 'Room ->' + str(x[0]), "\n" + 'Name ->' + str(x[1]),

                                   "\n" + "check-in ->" + str(x[2]), "\n" + "Room-rent ->" + str(x[3]),
                                   "\n" + "Food-bill ->" + str(x[4]), "\n" + "Total ->" + str(x[5]),
                                   "\n" + "check-out ->" + str(x[6]), "\n")

            # listofrooms.delete(0, END)
            # listofrooms.insert(0, "no matching found")
        Button(chkdetails, text="Search", font=("times new roman", 10), width=5, bg="red", fg="white",command=findcheckout).place(x=10, y=130)
        Button(chkdetails, text="DELETE", font=("times new roman", 10), width=5, bg="red", fg="white",command=delete2).place(x=100, y=130)
        chkdetails.place(x=850, y=200)

        rot.place(x=20, y=120 + 6 + 20 + 40)

    Button(b_frame,text="PAY",bg="red",bd=1,fg="white",command=ppp).place(x=900,y=150)
    Button(b_frame, text="Checkout", bg="red", bd=5,relief="groove", fg="white",command=unreserve).place(x=800, y=250)
    Button(b_frame, text="Checkout list", bg="red", bd=5, relief="groove", fg="white", command=checkoutlist).place(x=1000, y=250)









p12 = PhotoImage(file="purse.png")
p13 = p12.subsample(8, 8)
b6 = Button(sl_frame, image=p13, text='b1', bg='skyblue', width=150,command=checkout)
# b5.image = img
b6.place(x=782, y=0)
Label(sl_frame, text='Payments', font='msserif 13', bg='skyblue', fg="black").place(x=805, y=70)


p10=PhotoImage(file="food.png")
p11=p10.subsample(4,4)
b5 = Button(sl_frame, image=p11, text='b1', bg='skyblue', width=150,command=food)
# b5.image = img
b5.place(x=625, y=0)
Label(sl_frame, text='Foods', font='msserif 13', bg='skyblue',fg="black").place(x=670, y=70)


p2=PhotoImage(file="status.png")
p3=p2.subsample(8,8)
b1 = Button(sl_frame, image=p3, text='b1', bg='skyblue', width=150,command=hotel_status)
# b1.image = img
b1.place(x=0, y=0)
Label(sl_frame, text='Hotel Status', font='msserif 13', bg='skyblue',fg="black").place(x=40, y=70)





p14=PhotoImage(file="contacts.png")
p15=p14.subsample(8,8)
b7 = Button(sl_frame, image=p15, text='b1', bg='skyblue', width=150,command=staff)
# b5.image = img
b7.place(x=938, y=0)
Label(sl_frame, text='Contacts', font='msserif 13', bg='skyblue',fg="black").place(x=970, y=70)



p4=PhotoImage(file="room.png")
p5=p4.subsample(8,8)
b2 = Button(sl_frame, image=p5, text='b1', bg='skyblue', width=150,command=rooms)
# b2.image = img
b2.place(x=156, y=0)
Label(sl_frame, text='Rooms', font='msserif 13', bg='skyblue',fg="black").place(x=200, y=70)



p6=PhotoImage(file="coustomers.png")
p7=p6.subsample(4,4)
b3 = Button(sl_frame, image=p7, text='b1', bg='skyblue', width=150,command=customer)
# b3.image = img
b3.place(x=312, y=0)
Label(sl_frame, text='Coustomer Data', font='msserif 13', bg='skyblue',fg="black").place(x=335, y=70)


p8=PhotoImage(file="booking.png")
p9=p8.subsample(8,8)
b4 = Button(sl_frame, image=p9, text='b1', bg='skyblue', width=150,command=booking)
# b4.image = img
b4.place(x=468, y=0)
Label(sl_frame, text='Booking', font='msserif 13', bg='skyblue',fg="black").place(x=520, y=70)


if __name__ == "__main__":
    booking()


mainloop()

