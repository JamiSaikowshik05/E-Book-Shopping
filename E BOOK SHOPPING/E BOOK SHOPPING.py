import mysql.connector as c
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from tkinter import Tk, ttk
con = c.connect(user = 'root', host = "localhost", passwd = "admin")
cur = con.cursor()
cur.execute("create database if not exists library")
con.commit()
cur.execute("use library")
cur.execute("create table if not exists books(book_id int auto_increment primary key, book_name varchar(200), price int,status varchar(250),occ_name varchar(250),phone varchar(250))")
con.commit()

def borrow_book():
    window2 = Tk()
    window2.geometry("900x600")
    l1 = tk.Label(window2, text = "Book Name", width = 30, font = "bold")
    l1.grid(row =1 , column = 1)
    e1 = StringVar(window2)
    e1.set("Book Name")
    cmd = "select book_name from books where status = 'AVAILABLE'"
    cur.execute(cmd)
    data = cur.fetchall()
    ls = ['']
    for i in data:
        ls.append(i[0])

    drop = OptionMenu(window2, e1, *ls)
    drop.grid(row = 1, column = 3)
    l2 = tk.Label(window2, text = "Name",width = 30, font = "bold")
    l2.grid(row =2, column =1)
    e2 = tk.Entry(window2, width = 30)
    e2.grid(row = 2, column = 3)
    l3 = tk.Label(window2, text = "Phone Number", width = 30,font = "bold")
    l3.grid(row= 3, column = 1)
    e3 =tk.Entry(window2, width = 30)
    e3.grid(row = 3, column =3)
    b1 =  tk.Button(window2, text = "Procced", width = 30, command = lambda: borrow_book_true(e1,e2,e3))
    b1.grid(row = 4, column =2)
    window2.mainloop()
def borrow_book_true(e1,e2,e3):
    try:
        
        book_name = e1.get()
        name = e2.get()
        phone = e3.get()
        cmd = "select book_name from books where status = 'AVAILABLE'"
        cur.execute(cmd)
        data = cur.fetchall()
        ls5 = []
        for i in data:
            ls5.append(i[0])
        if book_name in ls5:
            cmd = "update books set status = 'BOOKED', occ_name = '{}', phone = '{}' where book_name = '{}'".format(name,phone,book_name)
            cur.execute(cmd)
            con.commit()
            messagebox.showinfo("Success","Record Updated")
        else:
            messagebox.showerror("Error","Please select a book")
    except Exception as e:
        messagebox.showerror("ERROR","We ran down into an error -->  "+ str(e) + "  please try again....")
def return_book():
    window3 = Tk()
    window3.geometry("900x400")
    l1 = tk.Label(window3, text ="Book Name", width = 30 , font="bold")
    l1.grid(row = 1, column =1)
    e1 = StringVar(window3)
    e1.set("Book")
    cmd = "select book_name from books where status = 'BOOKED'"
    cur.execute(cmd)
    data = cur.fetchall()
    ls = ['']
    for i in data:
        ls.append(i[0])

    drop = OptionMenu(window3, e1, *ls)
    drop.grid(row = 1, column = 3)
    b1 = tk.Button(window3,text = "Proceed",width = 30 , command= lambda:return_book_true(e1))
    b1.grid(row = 2, column =2)
    window3.mainloop()

def return_book_true(e1):
    try:
        book_name = e1.get()
        cmd = "update books set status = 'AVAILABLE', occ_name = ' ', phone = ' ' where book_name = '{}'".format(book_name)
        cur.execute(cmd)
        con.commit()
        messagebox.showinfo("Success","Record Updated")
    
    except Exception as e:
        messagebox.showerror("ERROR","We ran down into an error -->  "+ str(e) + "  please try again....")




def check_book():
    window4 = Tk()
    window4.geometry("600x400")
    l1 = tk.Label(window4, text ="Book Name", width = 30 , font="bold")
    l1.grid(row = 1, column =1)
    e1 = StringVar(window4)
    e1.set("Book")
    cmd = "select book_name from books"
    cur.execute(cmd)
    data = cur.fetchall()
    ls = ['']
    for i in data:
        ls.append(i[0])

    drop = OptionMenu(window4, e1, *ls)
    drop.grid(row = 1, column = 2)
    b1 = tk.Button(window4,text = "Check By Book Name",width = 30 , command= lambda:check_book_one(e1))
    b1.grid(row = 2, column =2)
    b2 =  tk.Button(window4, text = "Check All",width = 30 , command = lambda:check_book_all())
    b2.grid(row= 3, column = 2)
    window4.mainloop()

def check_book_one(e1):
    book_name = e1.get()
    window5 = Tk()
    window5.geometry("700x600")
    tree= ttk.Treeview(window5, columns =("c1","c2"), show = "headings", height = 10)
    tree.column("#1", anchor = "center")
    tree.heading("#1", text = "Book")
    tree.column("#2", anchor = "center")
    tree.heading("#2", text = "Details")
    cmd = "select * from books where book_name = '{}'".format(book_name)
    cur.execute(cmd)
    data = cur.fetchall()
    
    ls3 = ['Book ID','Book Name','Price','Status','Name','Phone']
    for i in data:
        ls2 = []
        ls2.append(i[0])
        ls2.append(i[1])
        ls2.append(i[2])
        ls2.append(i[3])
        ls2.append(i[4])
        ls2.append(i[5])
        for j in range(0,6):
            tree.insert('','end',text = j+1,values = (ls3[j],ls2[j]))
    tree.grid(row =1 , column =1)
    window5.mainloop()


def check_book_all():
    window6 = Tk()
    window6.geometry("1300x600")
    tree= ttk.Treeview(window6, columns =("c1","c2","c4","c5","c6","c7"), show = "headings", height = 10)
    tree.column("#1", anchor = "center")
    tree.heading("#1", text = "Book ID")
    tree.column("#2", anchor = "center")
    tree.heading("#2", text = "Book Name")
    tree.column("#3", anchor = "center")
    tree.heading("#3", text = "Price")
    tree.column("#4", anchor = "center")
    tree.heading("#4", text = "Status")
    tree.column("#5", anchor = "center")
    tree.heading("#5", text = "Name")
    tree.column("#6", anchor = "center")
    tree.heading("#6", text = "Phone")
    cmd = "select * from books"
    cur.execute(cmd)
    data = cur.fetchall()
    c =1
    for i in data:
        book_id = i[0]
        book_name = i[1]
        price = i[2]
        status = i[3]
        occ_name = i[4]
        phone = i[5]
        tree.insert('','end',text = c,values = (book_id,book_name,price,status,occ_name,phone))
        c +=1
    tree.grid(row = 1, column = 1)
    window6.mainloop()
        
def add_book():
    window7 = Tk()
    window7.geometry("900x600")
    l1 =  tk.Label(window7, text= "Book Name", width = 30 , font ="bold")
    l1.grid(row = 1, column = 1)
    e1 =  tk.Entry(window7)
    e1.grid(row = 1, column = 3)
    l2 =  tk.Label(window7, text = "Price",width = 30, font = "bold")
    l2.grid(row =2, column = 1)
    e2 = tk.Entry(window7)
    e2.grid(row =2, column = 3)
    b1 =  tk.Button(window7, text = "Proceed", width = 30 , command = lambda: add_book_true(e1,e2))
    b1.grid(row = 3, column = 2)
    window7.mainloop()
def add_book_true(e1,e2):
    try:
        
        book_name = e1.get()
        price= int(e2.get())
        cmd ="insert into books(book_name,price,status) values('{}',{},'AVAILABLE')".format(book_name, price)
        cur.execute(cmd)
        con.commit()
        messagebox.showinfo("Sccess","Record Added Succesfully")
    except Exception as e:
        messagebox.showerror("ERROR","We ran down some error -->  "+str(e) + "   please try again")

def remove_book():
    
    window8 = Tk()
    window8.geometry("900x600")
    l1 =  tk.Label(window8, text= "Book Name", width = 30 , font ="bold")
    l1.grid(row = 1, column = 1)
    e1 = StringVar(window8)
    e1.set("Book")
    cmd = "select book_name from books"
    cur.execute(cmd)
    data = cur.fetchall()
    ls = ['']
    for i in data:
        ls.append(i[0])

    drop = OptionMenu(window8, e1, *ls)
    drop.grid(row = 1, column = 3)
    b1 = tk.Button(window8,text = "Proceed",width = 30 , command= lambda:remove_book_true(e1))
    b1.grid(row = 2, column =2)
    window8.mainloop()
    
def remove_book_true(e1):
    try:
        book_name = e1.get()
        cmd = "delete from books where book_name = '{}'".format(book_name)
        cur.execute(cmd)
        con.commit()
        messagebox.showinfo("Sccess","Record Remove Succesfully")
    except Exception as e:
        messagebox.showerror("ERROR","We ran down some error -->  "+str(e) + "   please try again")

        
window = Tk()
window.geometry("500x500")
window.configure(bg = "blue")
l1 = tk.Label(window, text = "Welcome to Library", width = 30 , font ="bold")
l1.pack()
l1.configure(fg = "white", bg = "blue")
b1 = tk.Button(window, text = "Borrow Book", width = 30, command =  lambda: borrow_book())
b1.pack()
b2 = tk.Button(window, text = "Return Book", width = 30 , command = lambda: return_book())
b2.pack()
b3 = tk.Button(window, text = "Check Book", width = 30 , command =lambda:check_book())
b3.pack()
b4 = tk.Button(window, text = "Add Book", width = 30 , command =lambda:add_book())
b4.pack()
b5 = tk.Button(window, text = "Remove Book", width = 30 , command =lambda:remove_book())
b5.pack()
window.mainloop()
