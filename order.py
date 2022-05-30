from ast import pattern
from calendar import c
from cgitb import enable, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import BOLD
from urllib.parse import parse_qs
from xml.dom.minidom import Entity
from xml.sax import parseString
from PIL import ImageTk, Image, ImageFile
from matplotlib.font_manager import json_dump
from numpy import choose, empty, place
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from pip import main
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import shutil
import csv
import json


fbilldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="fbillingsintgrtd", port="3306"
)
fbcursor = fbilldb.cursor()

ImageFile.LOAD_TRUNCATED_IMAGES = True

def reset():
  global root
  root.destroy()


# root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
def log():
    global user_name1
    user_name1=username1.get()
    passwd1=password1.get()
    if user_name1=="" or passwd1=="":
        Label(text='Plz enter both username and password',fg='red').place(x=85,y=260)
    else:
        sql='SELECT * FROM users WHERE username=%s AND password=%s'
        val=(user_name1,passwd1,)
        fbcursor.execute(sql,val)
        if fbcursor.fetchone()is not None:
            mainpage()
            if user_name1 != "adminstator":
              tab06.destroy()
            else:
              pass
            root.iconify()
        else:
            messagebox.showinfo('Acess denied','Username Or Password Wrong')

  
sql = "select * from users"
fbcursor.execute(sql)
user_log = fbcursor.fetchall()
if not user_log:
  def lo():
    mainpage()
  root=Tk()
  root.geometry("500x250")
  root.resizable(False, False)
  root.eval('tk::PlaceWindow . center')
  Label(text='Wellocome to F-Billing Revolution 2022',font='arial 13 bold').place(x=100,y=40)
  submitbtn1=Button(text='OPEN NOW', width=20,height=2,command=lo,activeforeground="white",activebackground="black",font='arial 8 bold').place(x=165,y=100)             
else:
    root=Tk()
    root.geometry("500x200")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    root.title("F-Billing Revolution 2022")
    p1 = PhotoImage(file = 'images/fbicon.png')
    root.iconphoto(False,p1)
    username1=StringVar()
    password1=StringVar()

    Label(text='Login F-Billing Revolution 2022',font='arial 13 bold').place(x=120,y=15)
    
  
    sql = "select username from users"
    fbcursor.execute(sql)
    user_log_name = fbcursor.fetchall()
    uss1=Label(text='Username').place(x=120,y=65)
    ee1 = ttk.Combobox(textvariable=username1)
    ee1.place(x=220,y=65)
    ee1["values"] = user_log_name

    pss1=Label(text='Password').place(x=120,y=105)
    ee2=Entry(textvariable=password1,show='*',width=23).place(x=220,y=105)
    
    submitbtn1=Button(text='Login', width=15,command=log,activeforeground="white",
                   activebackground="black").place(x=250,y=150)
    
  
invoices= PhotoImage(file="images/invoice.png")
orders = PhotoImage(file="images/order.png")
estimates = PhotoImage(file="images/estimate.png")
recurring = PhotoImage(file="images/recurring.png")
purchase = PhotoImage(file="images/purchase.png")
expenses = PhotoImage(file="images/expense.png")
customer = PhotoImage(file="images/customer.png")
product = PhotoImage(file="images/package.png")
reports = PhotoImage(file="images/report.png")
setting = PhotoImage(file="images/setting.png")
tick = PhotoImage(file="images/check.png")
warnin = PhotoImage(file="images/sign_warning.png")
cancel = PhotoImage(file="images/close.png")
saves = PhotoImage(file="images/save.png")
folder = PhotoImage(file="images/folder-black.png")
photo11 = PhotoImage(file = "images/invoice-pvt.png")
customer = PhotoImage(file="images/customer.png")
smslog = PhotoImage(file = "images/smslog.png")
video = PhotoImage(file = "images/video.png")
mark1 = PhotoImage(file="images/mark.png")
mark2 = PhotoImage(file="images/mark2.png")
photo10 = PhotoImage(file = "images/text-message.png")
addnew = PhotoImage(file="images/plus.png")
delete = PhotoImage(file="images/delete_E.png")

selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")
  
right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
remove = PhotoImage(file="images/eraser.png")
  
  
photo = PhotoImage(file = "images/plus.png")
photo1 = PhotoImage(file = "images/edit.png")
photo2 = PhotoImage(file = "images/delete_E.png")
photo3 = PhotoImage(file = "images/export-file.png")
photo4 = PhotoImage(file = "images/seo.png")
photo5 = PhotoImage(file = "images/printer.png")
photo6 = PhotoImage(file = "images/gmail.png")
photo7 = PhotoImage(file = "images/priewok.png")
photo8 = PhotoImage(file = "images/refresh_E.png")
photo9 = PhotoImage(file = "images/sum.png")
photo10 = PhotoImage(file = "images/text-message.png")

################ expenses button images ####################
exprefreshIcon = ImageTk.PhotoImage(Image.open("images/refresh.png"))
expsearchIcon = ImageTk.PhotoImage(Image.open("images/search-icon.png"))
expdeleteIcon = ImageTk.PhotoImage(Image.open("images/delete.png"))
expeditIcon = ImageTk.PhotoImage(Image.open("images/edit.png"))
expenseIcon = ImageTk.PhotoImage(Image.open("images/plus.png"))
################ Product service button images ####################
prorefreshIcon = ImageTk.PhotoImage(Image.open("images/refresh.png"))
proexportIcon = ImageTk.PhotoImage(Image.open("images/export-file.png"))
proimportIcon = ImageTk.PhotoImage(Image.open("images/import.png"))
prosearchIcon = ImageTk.PhotoImage(Image.open("images/research.png"))
prodeleteIcon = ImageTk.PhotoImage(Image.open("images/delete.png"))
productIcon = ImageTk.PhotoImage(Image.open("images/plus.png"))
proeditIcon = ImageTk.PhotoImage(Image.open("images/edit.png"))


def mainpage():
  root.iconify()
  main = Toplevel()
  main.geometry("1360x730")
  p1 = PhotoImage(file = 'images/fbicon.png')
  main.iconphoto(False, p1)
  main.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
  s = ttk.Style()
  s.theme_use('default')
  s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
  tabControl = ttk.Notebook(main)
  tab1 = ttk.Frame(tabControl)
  tab2 = ttk.Frame(tabControl)
  tab3=  ttk.Frame(tabControl)
  tab4 = ttk.Frame(tabControl)
  tab5 = ttk.Frame(tabControl)
  tab6=  ttk.Frame(tabControl)
  tab7 = ttk.Frame(tabControl)
  tab8 = ttk.Frame(tabControl)
  tab9 =  ttk.Frame(tabControl)
  tab10=  ttk.Frame(tabControl)
  tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoices',)
  tabControl.add(tab2,image=orders,compound = LEFT, text ='Orders')
  tabControl.add(tab3,image=estimates,compound = LEFT, text ='Estimates')
  tabControl.add(tab4,image=recurring,compound = LEFT, text ='Recurring')
  tabControl.add(tab5,image=purchase,compound = LEFT, text ='Purchase Orders') 
  tabControl.add(tab6,image=expenses,compound = LEFT, text ='Expenses')
  tabControl.add(tab7,image=customer,compound = LEFT, text ='Customers')
  tabControl.add(tab8,image=product,compound = LEFT, text ='Product/Services')
  tabControl.add(tab9,image=reports,compound = LEFT, text ='Report')
  tabControl.add(tab10,image=setting,compound = LEFT, text ='Settings')
  tabControl.pack(expand = 1, fill ="both")
  
  def check_empty() :
       if entry.get():
           pass     #your function where you want to jump
       else:
          messagebox.showinfo("Information", "Required entry")


#ORDER MODULE



##create new order##

  def order_create():
    pop=Toplevel(order_midFrame)
    pop.title("Orders")
    pop.geometry("950x690+150+0")

    def ord_attach_doc():
      file_type = [('png files','.png'),('jpg files','.jpg'),('all files','.')]
      file = filedialog.askopenfilename(initialdir="/",filetypes=file_type)
      shutil.copyfile(file, os.getcwd()+'/images/'+file.split('/')[-1])
      file_size = crate_convertion(os.path.getsize(file))
      ord_create_doc_tree.insert(parent='',index='end',iid=file.split('/')[-1],text='',values=('',file.split('/')[-1],file_size))
    def crate_convertion(B):
      BYTE = float(B)
      KB = float(1024)
      MB = float(KB**2)
      if BYTE < KB:
        return '{0} {1}'.format(BYTE,'Bytes' if 0 == B > 1 else 'Byte')
      elif KB <= BYTE < MB:
        return '{0:.2f} KB'.format(BYTE / KB)
      elif MB <= BYTE:
        return '{0:.2f} MB'.format(BYTE / MB)

    def crate_order():
      ord_cus_name = ord_to.get()
      ord_cus_address = ord_addr.get("1.0","end-1c")
      ord_ship_name = ord_ship.get()
      ord_ship_address = ord_shipaddr.get("1.0","end-1c")
      ord_cus_email = ord_email.get()
      ord_cus_num  = ord_smsnum.get()
      ord_order_id = ord_orderid.get()
      ord_order_date = ord_date.get_date()
      # ord_duedatecheck = checkvarStatus522.get()
      ord_due_date = ord_duedate.get_date()
      ord_terms_pay = ord_terms.get()
      # ord_order_ref = ord_orderref.get()
      ord_extra_costname = ord_extracostname.get()
      ord_discountrate = ord_disrate.get()
      ord_extra_cost = ord_extracost.get()
      ord_tax_1 = ord_tax.get()
      ord_tax_2 = ord_tax2.get()
      ord_templat = ord_template.get()
      ord_sales_person = ord_sales.get()
      ord_category = ord_cate.get()
      ord_status = draft.cget("text")
      ord_title_text = ord_titletext.get()
      ord_pageheader_text = ord_pageheadertext.get()
      ord_footer_text = ord_footertext.get()
      ord_private_notes = ord_privatenotes.get("1.0","end-1c")
      ord_terms_notes = ord_termsnotes.get("1.0","end-1c")
      ord_comm_notes = ord_commnotes.get("1.0","end-1c")
      sum_discount = discount1.cget("text")
      sum_subtotal = sub1.cget("text")
      sum_tax1 = tax1sum.cget("text")
      sum_tax2 = tax2sum.cget("text")
      # sum_sum_extra_cost = cost1.cget()
      order_total = order1.cget("text")
      # total_paid = total1.cget()
      # balance = balance1.cget()
      #________________ Order Insert___________________#
      sql = 'insert into orders(businessname,businessaddress,shipname,shipaddress,cpemail,cpmobileforsms,order_number,order_date,due_date,terms_of_payment,extra_cost_name,discount_rate,extra_cost,tax1,tax2,template,sales_person,category,status,title_text,page_header_text,footer_text,private_notes,terms_notes,comments,sum_discount,sum_subtotal,sum_tax,sum_tax2,Order_total) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
      val = (ord_cus_name,ord_cus_address,ord_ship_name,ord_ship_address,ord_cus_email,ord_cus_num,ord_order_id,ord_order_date,ord_due_date,ord_terms_pay,ord_extra_costname,ord_discountrate,ord_extra_cost,ord_tax_1,ord_tax_2,ord_templat,ord_sales_person,ord_category,ord_status,ord_title_text,ord_pageheader_text,ord_footer_text,ord_private_notes,ord_terms_notes,ord_comm_notes,sum_discount,sum_subtotal,sum_tax1,sum_tax2,order_total)
      fbcursor.execute(sql, val)
      fbilldb.commit()
      
      #_______________ Order product service  insert _____________#
      sql = "select * from company"
      fbcursor.execute(sql)
      ord_insertpro_service = fbcursor.fetchone()
      for child in ord_pro_create_tree.get_children():
        insert_pro_list = list(ord_pro_create_tree.item(child, 'values'))
        if not ord_insertpro_service:
          sql = 'insert into storingproduct(order_number,sku,name,description,unitprice,quantity,peices,price) values(%s,%s,%s,%s,%s,%s,%s,%s)'
          val = (ord_order_id,insert_pro_list[0],insert_pro_list[1],insert_pro_list[2],insert_pro_list[3],insert_pro_list[4],insert_pro_list[5],insert_pro_list[6])
          fbcursor.execute(sql, val)
          fbilldb.commit()
        elif ord_insertpro_service[12] == "1":
          sql = 'insert into storingproduct(order_number,sku,name,description,unitprice,quantity,peices,price) values(%s,%s,%s,%s,%s,%s,%s,%s)'
          val = (ord_order_id,insert_pro_list[0],insert_pro_list[1],insert_pro_list[2],insert_pro_list[3],insert_pro_list[4],insert_pro_list[5],insert_pro_list[6])
          fbcursor.execute(sql, val)
          fbilldb.commit()
        elif ord_insertpro_service[12] == "2":
          sql = 'insert into storingproduct(order_number,sku,name,description,unitprice,quantity,peices,tax1,price) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
          val = (ord_order_id,insert_pro_list[0],insert_pro_list[1],insert_pro_list[2],insert_pro_list[3],insert_pro_list[4],insert_pro_list[5],insert_pro_list[6],insert_pro_list[7])
          fbcursor.execute(sql, val)
          fbilldb.commit()
        elif ord_insertpro_service[12] == "3":
          sql = 'insert into storingproduct(order_number,sku,name,description,unitprice,quantity,peices,tax1,tax2,price) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
          val = (ord_order_id,insert_pro_list[0],insert_pro_list[1],insert_pro_list[2],insert_pro_list[3],insert_pro_list[4],insert_pro_list[5],insert_pro_list[6],insert_pro_list[7],insert_pro_list[8])
          fbcursor.execute(sql, val)
          fbilldb.commit()

      #_____________Documents Insert________________#
      for child in ord_create_doc_tree.get_children():
        insert_doc_list = list(ord_create_doc_tree.item(child, 'values'))
        sql = 'insert into documents (order_number,documents) values(%s,%s)'
        val = (ord_order_id,insert_doc_list[1])
        fbcursor.execute(sql, val)
        fbilldb.commit()
      
      #_________Refresh insert tree________#
  
      for record in ordtree.get_children():
       ordtree.delete(record)
      sql = "select * from orders"
      fbcursor.execute(sql)
      refreshinsert = fbcursor.fetchall()
      count0 = 0
      for i in refreshinsert:
        ordtree.insert(parent='', index='end', iid=count0, text='', values=(' ',i[31], i[1], i[2], i[3], i[4],i[5], i[6], i[7], i[8], i[9], i[10]))
        count0 += 1
      pop.destroy()
        
    #select customer
    def order_custom():
      cuselection=Toplevel()
      cuselection.title("Select Customer")
      cuselection.geometry("930x650+240+10")
      cuselection.resizable(False, False)


      #add new customer
      def order_create_customer():
        ven=Toplevel(order_midFrame)
        ven.title("Add new Customer")
        ven.geometry("930x650+240+10")
        checkvar1=IntVar()
        checkvar2=IntVar()
        radio=IntVar()
        createFrame=Frame(ven, bg="#f5f3f2", height=650)
        createFrame.pack(side="top", fill="both")
        labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
        labelframe1.place(x=10,y=5,width=910,height=600)
        text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
        e1=Entry(labelframe1,width=25).place(x=150,y=10)
        text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
        e2=ttk.Combobox(labelframe1,width=25,value="Default").place(x=460 ,y=10)
        text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
        Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
        
        labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
        labelframe2.place(x=5,y=40,width=420,height=150)
        name = Label(labelframe2, text="Ship to name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
        e1 = Entry(labelframe2,width=28).place(x=130,y=5)
        addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
        e2 = Entry(labelframe2,width=28).place(x=130,y=40,height=80)
        
        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

        labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
        labelframe3.place(x=480,y=40,width=420,height=150)
        name = Label(labelframe3, text="Business name:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe3,width=28).place(x=130,y=5)
        addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
        e2 = Entry(labelframe3,width=28).place(x=130,y=40,height=80)
        
        labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe4.place(x=5,y=195,width=420,height=150)
        name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe4,width=28).place(x=130,y=5)
        email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
        e2 = Entry(labelframe4,width=28).place(x=130,y=35)
        tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        e3 = Entry(labelframe4,width=11).place(x=130,y=65)
        fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        e4 = Entry(labelframe4,width=11).place(x=280,y=65)
        sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
        e5 = Entry(labelframe4,width=15).place(x=248,y=95)      

        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

        
        labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
        labelframe5.place(x=480,y=195,width=420,height=125)
        name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe5,width=28).place(x=130,y=5)
        email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
        e2 = Entry(labelframe5,width=28).place(x=130,y=35)
        tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        e3 = Entry(labelframe5,width=11).place(x=130,y=65)
        fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        e4 = Entry(labelframe5,width=11).place(x=280,y=65)

        labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe6.place(x=5,y=350,width=420,height=100)
        Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
        tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
        e1 = Entry(labelframe6,width=10).place(x=290,y=5)
        discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
        e2 = Entry(labelframe6,width=10).place(x=100,y=35)

        labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe7.place(x=480,y=330,width=420,height=100)
        country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe7,width=28).place(x=130,y=5)
        city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
        e2 = Entry(labelframe7,width=28).place(x=130,y=35)

        labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
        labelframe8.place(x=5,y=460,width=420,height=100)
        R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
        R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
        R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
        

        labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
        labelframe9.place(x=480,y=430,width=420,height=150)
        e1 = Entry(labelframe9).place(x=10,y=10,height=100,width=390)

        btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK").place(x=20, y=615)
        btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
      
      def order_edit_customer():
        ven=Toplevel(order_midFrame)
        ven.title("Add new Customer")
        ven.geometry("930x650+240+10")
        checkvar1=IntVar()
        checkvar2=IntVar()
        radio=IntVar()
        createFrame=Frame(ven, bg="#f5f3f2", height=650)
        createFrame.pack(side="top", fill="both")
        labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
        labelframe1.place(x=10,y=5,width=910,height=600)
        text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
        ord_cusid=Entry(labelframe1,width=25).place(x=150,y=10)
        text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
        ord_cuscat=ttk.Combobox(labelframe1,width=25,value="Default").place(x=460 ,y=10)
        text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
        Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
        
        labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
        labelframe2.place(x=5,y=40,width=420,height=150)
        name = Label(labelframe2, text="Ship to name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
        ord_cusshipname = Entry(labelframe2,width=28).place(x=130,y=5)
        addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
        ord_cusaddr = Entry(labelframe2,width=28).place(x=130,y=40,height=80)
        
        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

        labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
        labelframe3.place(x=480,y=40,width=420,height=150)
        name = Label(labelframe3, text="Business name:",bg="#f5f3f2").place(x=5,y=5)
        ord_cusbusname = Entry(labelframe3,width=28).place(x=130,y=5)
        addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
        ord_cusadd1 = Entry(labelframe3,width=28).place(x=130,y=40,height=80)
        
        labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe4.place(x=5,y=195,width=420,height=150)
        name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        ord_cusconta = Entry(labelframe4,width=28).place(x=130,y=5)
        email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
        ord_cusemail = Entry(labelframe4,width=28).place(x=130,y=35)
        tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        ord_custel = Entry(labelframe4,width=11).place(x=130,y=65)
        fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        ord_cusfax = Entry(labelframe4,width=11).place(x=280,y=65)
        sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
        ord_cussmsnofi = Entry(labelframe4,width=15).place(x=248,y=95)      

        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

        
        labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
        labelframe5.place(x=480,y=195,width=420,height=125)
        name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        ord_cuscont1 = Entry(labelframe5,width=28).place(x=130,y=5)
        email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
        ord_cusemail1 = Entry(labelframe5,width=28).place(x=130,y=35)
        tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        ord_custel1 = Entry(labelframe5,width=11).place(x=130,y=65)
        fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        ord_cusfax1 = Entry(labelframe5,width=11).place(x=280,y=65)

        labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe6.place(x=5,y=350,width=420,height=100)
        Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
        tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
        ord_custax = Entry(labelframe6,width=10).place(x=290,y=5)
        discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
        ord_cusdis = Entry(labelframe6,width=10).place(x=100,y=35)

        labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe7.place(x=480,y=330,width=420,height=100)
        country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
        ord_cuscountry = Entry(labelframe7,width=28).place(x=130,y=5)
        city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
        ord_cuscity = Entry(labelframe7,width=28).place(x=130,y=35)

        labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
        labelframe8.place(x=5,y=460,width=420,height=100)
        R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
        R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
        R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
        

        labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
        labelframe9.place(x=480,y=430,width=420,height=150)
        ord_cusnotes = Entry(labelframe9).place(x=10,y=10,height=100,width=390)

        btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK").place(x=20, y=615)
        btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
          
                

      enter=Label(cuselection, text="Enter filter text").place(x=5, y=10)
      e1=Entry(cuselection, width=20).place(x=110, y=10)
      text=Label(cuselection, text="Filtered column").place(x=340, y=10)
      e2=Entry(cuselection, width=20).place(x=450, y=10)

      ord_create_cusventtree=ttk.Treeview(cuselection, height=27)
      ord_create_cusventtree["columns"]=["1","2","3", "4"]
      ord_create_cusventtree.column("#0", width=35)
      ord_create_cusventtree.column("1", width=160)
      ord_create_cusventtree.column("2", width=160)
      ord_create_cusventtree.column("3", width=140)
      ord_create_cusventtree.column("4", width=140)
      ord_create_cusventtree.heading("#0",text="")
      ord_create_cusventtree.heading("1",text="Customer/Ventor ID")
      ord_create_cusventtree.heading("2",text="Customer/Ventor Name")
      ord_create_cusventtree.heading("3",text="Tel.")
      ord_create_cusventtree.heading("4",text="Contact Person")
      ord_create_cusventtree.place(x=5, y=45)

      fbcursor.execute('SELECT * FROM Customer;') 
      j = 0
      for i in fbcursor:
        ord_create_cusventtree.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[10],i[8]))
        j += 1


      ctegorytree=ttk.Treeview(cuselection, height=27)
      ctegorytree["columns"]=["1"]
      ctegorytree.column("#0", width=35, minwidth=20)
      ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      ctegorytree.heading("#0",text="", anchor=W)
      ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      ctegorytree.place(x=660, y=45)

      scrollbar = Scrollbar(cuselection)
      scrollbar.place(x=640, y=45, height=560)
      scrollbar.config( command=ord_create_cusventtree.yview )
      
      ###### add customer deatils to ordertree ####
      def selectcus():
        cusid = ord_create_cusventtree.item(ord_create_cusventtree.focus())["values"][0]
        sql = "select * from customer where customerid = %s"
        val = (cusid,)
        fbcursor.execute(sql,val)
        cussel = fbcursor.fetchone()
        ord_to.delete(0, END)
        ord_to.insert(0, cussel[4])
        ord_addr.delete("1.0", END)
        ord_addr.insert("1.0", cussel[5])
        ord_ship.delete(0, END)
        ord_ship.insert(0, cussel[6])
        ord_shipaddr.delete("1.0", END)
        ord_shipaddr.insert("1.0", cussel[7])
        ord_email.delete(0, END)
        ord_email.insert(0, cussel[9])
        ord_smsnum.delete(0, END)
        ord_smsnum.insert(0, cussel[8])
        cuselection.destroy()

      btn1=Button(cuselection,compound = LEFT,image=tick ,text="ok", width=60,command=selectcus).place(x=15, y=610)
      btn1=Button(cuselection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=order_create_customer).place(x=250, y=610)
      btn1=Button(cuselection,compound = LEFT,image=tick, text="Add new customer", width=150,command=order_edit_customer).place(x=435, y=610)
      btn1=Button(cuselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)   



      

    #add new line item
    def order_newline():
      cus = ord_to.get()
      if cus == "":
        messagebox.showwarning("F-billing", "Customer is required, please select customer\nbefore adding line item to order")
        pop.deiconify()
      else:
        newselection=Toplevel()
        newselection.title("Select Customer")
        newselection.geometry("930x650+240+10")
        newselection.resizable(False, False)

        


      #add new product
      #add new product
        def order_create_product():  
          top = Toplevel()  
          top.title("Add a new Product/Service")
          p2 = PhotoImage(file = 'images/fbicon.png')
          top.iconphoto(False, p2)
        
          top.geometry("700x550+390+15")
          tabControl = ttk.Notebook(top)
          s = ttk.Style()
          s.theme_use('default')
          s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


          tab1 = ttk.Frame(tabControl)
          tab2 = ttk.Frame(tabControl)
        
          tabControl.add(tab1,compound = LEFT, text ='Product/Service')
          tabControl.add(tab2,compound = LEFT, text ='Product Image')
        
          tabControl.pack(expand = 1, fill ="both")
        
          innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
          innerFrame.pack(side="top",fill=BOTH)

          Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
          Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

          code1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
          code1.place(x=20,y=0)
          codeentry = Entry(Customerlabelframe,width=35)
          codeentry.place(x=120,y=8)

          checkvarStatus=IntVar()
          status1=Label(Customerlabelframe,text="Status:")
          status1.place(x=500,y=8)
          Button1 = Checkbutton(Customerlabelframe,
                            variable = checkvarStatus,text="Active",compound="right",
                            onvalue =0 ,
                            offvalue = 1,
                          
                            width = 10)

          Button1.place(x=550,y=5)

          category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
          category1.place(x=20,y=40)
          n = StringVar()
          country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
          
          country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
          
          country.place(x=120,y=45)
          country.current(0)


          name1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
          name1.place(x=20,y=70)
          nameentry = Entry(Customerlabelframe,width=60)
          nameentry.place(x=120,y=75)

          des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
          des1.place(x=20,y=100)
          desentry = Entry(Customerlabelframe,width=60)
          desentry.place(x=120,y=105)

          uval = IntVar(Customerlabelframe, value='$0.00')
          unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
          unit1.place(x=20,y=130)
          unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
          unitentry.place(x=120,y=135)

          pcsval = IntVar(Customerlabelframe, value='$0.00')
          pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
          pcs1.place(x=320,y=140)
          pcsentry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
          pcsentry.place(x=410,y=140)

          costval = IntVar(Customerlabelframe, value='$0.00')
          cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
          cost1.place(x=20,y=160)
          costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
          costentry.place(x=120,y=165)

          priceval = IntVar(Customerlabelframe, value='$0.00')
          price1=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
          price1.place(x=20,y=190)
          priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
          priceentry.place(x=120,y=195)

          checkvarStatus2=IntVar()
        
          Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                            text="Taxable Tax1rate",compound="right",
                            onvalue =0 ,
                            offvalue = 1,
                            height=2,
                            width = 12)

          Button2.place(x=415,y=170)


          checkvarStatus3=IntVar()
        
          Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                            text="No stock Control",
                            onvalue =1 ,
                            offvalue = 0,
                            height=3,
                            width = 15)

          Button3.place(x=40,y=220)


          stockval = IntVar(Customerlabelframe, value='0')
          stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
          stock1.place(x=90,y=260)
          stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
          stockentry.place(x=150,y=265)

          lowval = IntVar(Customerlabelframe, value='0')
          low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
          low1.place(x=300,y=260)
          lowentry = Entry(Customerlabelframe,width=10,textvariable=lowval)
          lowentry.place(x=495,y=265)

        
          ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
          ware1.place(x=60,y=290)
          wareentry = Entry(Customerlabelframe,width=50)
          wareentry.place(x=150,y=295)

          text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
          text1.place(x=20,y=330)

          txt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
          txt.place(x=32,y=358)




          okButton = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60)
          okButton.pack(side=LEFT)

          cancelButton = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
          cancelButton.pack(side=RIGHT)

          imageFrame = Frame(tab2, relief=GROOVE,height=580)
          imageFrame.pack(side="top",fill=BOTH)

          browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
          browseimg.place(x=15,y=35)

          browsebutton=Button(imageFrame,text = 'Browse')
          browsebutton.place(x=580,y=30,height=30,width=50)
          
          removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
          removeButton.place(x=400,y=450)
        
        def order_edit_product():  
          top = Toplevel()  
          top.title("Add a new Product/Service")
          p2 = PhotoImage(file = 'images/fbicon.png')
          top.iconphoto(False, p2)
        
          top.geometry("700x550+390+15")
          tabControl = ttk.Notebook(top)
          s = ttk.Style()
          s.theme_use('default')
          s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


          tab1 = ttk.Frame(tabControl)
          tab2 = ttk.Frame(tabControl)
        
          tabControl.add(tab1,compound = LEFT, text ='Product/Service')
          tabControl.add(tab2,compound = LEFT, text ='Product Image')
        
          tabControl.pack(expand = 1, fill ="both")
        
          innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
          innerFrame.pack(side="top",fill=BOTH)

          Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
          Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

          code1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
          code1.place(x=20,y=0)
          codeentry = Entry(Customerlabelframe,width=35)
          codeentry.place(x=120,y=8)

          checkvarStatus=IntVar()
          status1=Label(Customerlabelframe,text="Status:")
          status1.place(x=500,y=8)
          Button1 = Checkbutton(Customerlabelframe,
                            variable = checkvarStatus,text="Active",compound="right",
                            onvalue =0 ,
                            offvalue = 1,
                          
                            width = 10)

          Button1.place(x=550,y=5)

          category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
          category1.place(x=20,y=40)
          n = StringVar()
          country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
          
          country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
          
          country.place(x=120,y=45)
          country.current(0)


          name1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
          name1.place(x=20,y=70)
          nameentry = Entry(Customerlabelframe,width=60)
          nameentry.place(x=120,y=75)

          des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
          des1.place(x=20,y=100)
          desentry = Entry(Customerlabelframe,width=60)
          desentry.place(x=120,y=105)

          uval = IntVar(Customerlabelframe, value='$0.00')
          unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
          unit1.place(x=20,y=130)
          unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
          unitentry.place(x=120,y=135)

          pcsval = IntVar(Customerlabelframe, value='$0.00')
          pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
          pcs1.place(x=320,y=140)
          pcsentry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
          pcsentry.place(x=410,y=140)

          costval = IntVar(Customerlabelframe, value='$0.00')
          cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
          cost1.place(x=20,y=160)
          costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
          costentry.place(x=120,y=165)

          priceval = IntVar(Customerlabelframe, value='$0.00')
          price1=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
          price1.place(x=20,y=190)
          priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
          priceentry.place(x=120,y=195)

          checkvarStatus2=IntVar()
        
          Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                            text="Taxable Tax1rate",compound="right",
                            onvalue =0 ,
                            offvalue = 1,
                            height=2,
                            width = 12)

          Button2.place(x=415,y=170)


          checkvarStatus3=IntVar()
        
          Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                            text="No stock Control",
                            onvalue =1 ,
                            offvalue = 0,
                            height=3,
                            width = 15)

          Button3.place(x=40,y=220)


          stockval = IntVar(Customerlabelframe, value='0')
          stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
          stock1.place(x=90,y=260)
          stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
          stockentry.place(x=150,y=265)

          lowval = IntVar(Customerlabelframe, value='0')
          low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
          low1.place(x=300,y=260)
          lowentry = Entry(Customerlabelframe,width=10,textvariable=lowval)
          lowentry.place(x=495,y=265)

        
          ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
          ware1.place(x=60,y=290)
          wareentry = Entry(Customerlabelframe,width=50)
          wareentry.place(x=150,y=295)

          text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
          text1.place(x=20,y=330)

          txt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
          txt.place(x=32,y=358)




          okButton = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60)
          okButton.pack(side=LEFT)

          cancelButton = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
          cancelButton.pack(side=RIGHT)

          imageFrame = Frame(tab2, relief=GROOVE,height=580)
          imageFrame.pack(side="top",fill=BOTH)

          browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
          browseimg.place(x=15,y=35)

          browsebutton=Button(imageFrame,text = 'Browse')
          browsebutton.place(x=580,y=30,height=30,width=50)
          
          removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
          removeButton.place(x=400,y=450)



        
                        
        enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
        e1=Entry(newselection, width=20).place(x=110, y=10)
        text=Label(newselection, text="Filtered column").place(x=340, y=10)
        e2=Entry(newselection, width=20).place(x=450, y=10)

        ord_create_protree=ttk.Treeview(newselection, height=27)
        ord_create_protree["columns"]=["1","2","3", "4","5"]
        ord_create_protree.column("#0", width=35)
        ord_create_protree.column("1", width=160)
        ord_create_protree.column("2", width=160)
        ord_create_protree.column("3", width=140)
        ord_create_protree.column("4", width=70)
        ord_create_protree.column("5", width=70)
        ord_create_protree.heading("#0",text="")
        ord_create_protree.heading("1",text="ID/SKU")
        ord_create_protree.heading("2",text="Product/Service Name")
        ord_create_protree.heading("3",text="Unit price")
        ord_create_protree.heading("4",text="Service")
        ord_create_protree.heading("5",text="Stock")
        ord_create_protree.tag_configure('green', foreground='green')
        ord_create_protree.tag_configure('red', foreground='red')
        ord_create_protree.tag_configure('blue', foreground='blue')
        ord_create_protree.place(x=5, y=45)
        
        countp = 0
        sql = 'select * from Productservice'
        fbcursor.execute(sql)
        prodata = fbcursor.fetchall()
        for i in prodata:
          if i[12] == '1':
            servi = '🗹'
          else:
            servi = ''
          sql = "select currencysign,currsignplace from company"
          fbcursor.execute(sql)
          currsymb = fbcursor.fetchone()
          if not currsymb: 
            if i[13] > i[14]:
              ord_create_protree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
              countp += 1              
            elif i[12] == '1':
              ord_create_protree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
              countp += 1
            else:
              ord_create_protree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
              countp += 1
                  
          elif currsymb[1] == "before amount":
            if (i[13]) > (i[14]):
              ord_create_protree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              ord_create_protree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('blue',))
              countp += 1
            else:
              ord_create_protree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('red',))
              countp += 1

          elif currsymb[1] == "before amount with space":
            if i[13] > i[14]:
              ord_create_protree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              ord_create_protree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
              countp += 1
            else:
              ord_create_protree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
              countp += 1

          elif currsymb[1] == "after amount":
            if i[13] > i[14]:
              ord_create_protree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              ord_create_protree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('blue',))
              countp += 1
            else:
              ord_create_protree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('red',))
              countp += 1

          elif currsymb[1] == "after amount with space":
            if i[13] > i[14]:
              ord_create_protree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              ord_create_protree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('blue',))
              countp += 1
            else:
              ord_create_protree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('red',))
              countp += 1 

        
        ctegorytree=ttk.Treeview(newselection, height=27)
        ctegorytree["columns"]=["1"]
        ctegorytree.column("#0", width=35, minwidth=20)
        ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
        ctegorytree.heading("#0",text="", anchor=W)
        ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
        ctegorytree.place(x=660, y=45)

        scrollbar = Scrollbar(newselection)
        scrollbar.place(x=640, y=45, height=560)
        scrollbar.config( command=ord_create_protree.yview )
      
        def selepro():
          priceview = Label(listFrame,bg="#f5f3f2")
          priceview.place(x=850,y=200,width=78,height=18)
          proskuid = ord_create_protree.item(ord_create_protree.focus())["values"][0]
          sql = "select * from Productservice where sku = %s"
          val = (proskuid,)
          fbcursor.execute(sql,val)
          prosele = fbcursor.fetchone()
          sql = "select * from company"
          fbcursor.execute(sql)
          create_maintree_insert = fbcursor.fetchone()
          if prosele[10] == '1':
            tax1 = '🗹'
          else:
            tax1 = ''
          if prosele[19] == '1':
            tax2 = '🗹'
          else:
            tax2 = ''
          if not create_maintree_insert:
            ord_pro_create_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],prosele[7],1,prosele[8],tax1,prosele[7]*1))

          elif create_maintree_insert[12] == "1":
            ord_pro_create_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],prosele[7],1,prosele[8],prosele[7]*1))
            extracs = 0.0
            discou = 0.0
            total = 0.0
            for child in ord_pro_create_tree.get_children():
              total += float(ord_pro_create_tree.item(child, 'values')[6])
            discou = (total*float(ord_disrate.get())/100)
            extracs = (extracs+float(ord_extracost.get()))
            cost1.config(text=ord_extracost.get())
            discount1.config(text=discou)
            priceview.config(text=total)
            order1.config(text=total-discou+extracs)
            balance1.config(text=total-discou+extracs)
            sub1.config(text=total-discou)
          elif create_maintree_insert[12] == "2":
            ord_pro_create_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],prosele[7],1,prosele[8],tax1,prosele[7]*1))
            extracs = 0.0
            discou = 0.0
            total = 0.0
            for child in ord_pro_create_tree.get_children():
              total += float(ord_pro_create_tree.item(child, 'values')[7])
            discou = (total*float(ord_disrate.get())/100)
            extracs = (extracs+float(ord_extracost.get()))
            cost1.config(text=ord_extracost.get())
            discount1.config(text=discou)
            priceview.config(text=total)
            sub1.config(text=total-discou)
            

            tot = 0.0
            totaltax1 = 0.0
            for child in ord_pro_create_tree.get_children():
              checktax1 = list(ord_pro_create_tree.item(child, 'values'))
              if checktax1[6] == "🗹":
                totaltax1 =(totaltax1 + float(checktax1[7]))
                tax1sum.config(text=(float(totaltax1)*float(ord_tax.get())/100))
                tot = (float(totaltax1)*float(ord_tax.get())/100)
              else:
                pass
            order1.config(text=total+tot-discou+extracs)
            balance1.config(text=total+tot-discou+extracs)
              
          elif create_maintree_insert[12] == "3":
            ord_pro_create_tree.insert(parent='', index='end',text='', values=(prosele[2],prosele[4],prosele[5],prosele[7],1,prosele[8],tax1,tax2,prosele[7]*1))
            extracs = 0.0
            discou = 0.0
            total = 0.0
            for child in ord_pro_create_tree.get_children():
              total += float(ord_pro_create_tree.item(child, 'values')[8])
            extracs = (extracs+float(ord_extracost.get()))
            cost1.config(text=ord_extracost.get())
            discou = (total*float(ord_disrate.get())/100)
            discount1.config(text=discou)
            priceview.config(text=total)
            sub1.config(text=total-discou)
            
            tot = 0.0
            totaltax1 = 0.0
            for child in ord_pro_create_tree.get_children():
              checktax1 = list(ord_pro_create_tree.item(child, 'values'))
              if checktax1[6] == "🗹":
                totaltax1 =(totaltax1 + float(checktax1[8]))
                tax1sum.config(text=(float(totaltax1)*float(ord_tax.get())/100))
                tot = (float(totaltax1)*float(ord_tax.get())/100)
              else:
                pass
            
            tot2 = 0.0
            totaltax2 = 0.0
            for child in ord_pro_create_tree.get_children():
              checktax1 = list(ord_pro_create_tree.item(child, 'values'))
              if checktax1[7] == "🗹":
                totaltax2 =(totaltax2 + float(checktax1[8]))
                tax2sum.config(text=(float(totaltax2)*float(ord_tax2.get())/100))
                
                tot2 = (float(totaltax2)*float(ord_tax2.get())/100)
              else:
                pass

            order1.config(text=total+tot+tot2-discou+extracs)
            balance1.config(text=total+tot+tot2-discou+extracs)

          newselection.destroy()

        btn1=Button(newselection,compound = LEFT,image=tick ,text="ok", width=60,command=selepro).place(x=15, y=610)
        btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=order_edit_product).place(x=250, y=610)
        btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=order_create_product).place(x=435, y=610)
        btn1=Button(newselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)



    #preview new line
    def order_create_previewline():
      messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")


    
    #sms notification
    def order_create_sms1():
      send_SMS=Toplevel()
      send_SMS.geometry("700x480+240+150")
      send_SMS.title("Send SMS notification")

      style = ttk.Style()
      style.theme_use('default')
      style.configure('TNotebook.Tab', background="#999999", padding=5)
      sms_Notebook = ttk.Notebook(send_SMS)
      SMS_Notification = Frame(sms_Notebook, height=470, width=700)
      SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
      sms_Notebook.add(SMS_Notification, text="SMS Notification")
      sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
      sms_Notebook.place(x=0, y=0)

      numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
      numlbel.place(x=10, y=10)
      numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
      stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
      stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
      
      dclbel=Label(SMS_Notification, text="Double click to insert into text")
      dclbel.place(x=410, y=60)
      dcl=Entry(SMS_Notification, width=30)
      dcl.place(x=400, y=85,height=200)
      
      smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
      smstype.place(x=10, y=223)
      snuvar=IntVar()
      normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
      normal_rbtn.place(x=5, y=5)
      unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
      unicode_rbtn.place(x=190, y=5)
      tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
      tiplbf.place(x=10, y=290)
      tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
      tiplabl.place(x=5, y=5)

      btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
      btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
      btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
      

      smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
      smstype.place(x=10, y=5)
      snumvar=IntVar()
      normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
      normal_rbtn.place(x=5, y=5)
      unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
      unicode_rbtn.place(x=290, y=5)

      sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
      sms1type.place(x=10, y=80)
      name=Label(sms1type, text="Username").place(x=10, y=5)
      na=Entry(sms1type, width=20).place(x=100, y=5)
      password=Label(sms1type, text="Password").place(x=10, y=45)
      pas=Entry(sms1type, width=20).place(x=100, y=45)
      combo=Label(sms1type, text="Route").place(x=400, y=5)
      n = StringVar()
      combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
      btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

      
      tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
      tiplbf.place(x=10, y=190)
      tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
      tiplabl.place(x=0, y=5)
      tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
      tiplabl1.place(x=0, y=60)
      tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
      tiplabl2.place(x=0, y=100)
      tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
      tiplabl3.place(x=0, y=140)
      checkvar1=IntVar()
      chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 



    
    #delete line item  
    def order_create_delete1():
      try:
        selected_item = ord_pro_create_tree.selection()[0]
        ord_pro_create_tree.delete(selected_item)
        sql = "select * from company"
        fbcursor.execute(sql)
        delrefresh = fbcursor.fetchone()
        if not delrefresh:
          extracs = 0.0
          discou = 0.0
          total= 0.0
          for child in ord_pro_create_tree.get_children():
            total += float(ord_pro_create_tree.item(child, 'values')[6])
          discou = (total*float(ord_disrate.get())/100)
          extracs = extracs + float(ord_extracost.get())
          cost1.config(text=ord_extracost.get())
          discount1.config(text=discou)
          priceview.config(text=total)
          order1.config(text=total-discou+extracs)
          balance1.config(text=total-discou+extracs)
          sub1.config(text=total-discou)
        elif delrefresh[12] == "1":
          extracs = 0.0
          discou = 0.0
          total= 0.0
          for child in ord_pro_create_tree.get_children():
            total += float(ord_pro_create_tree.item(child, 'values')[6])
          discou = (total*float(ord_disrate.get())/100)
          extracs = extracs + float(ord_extracost.get())
          cost1.config(text=ord_extracost.get())
          discount1.config(text=discou)
          priceview.config(text=total)
          order1.config(text=total-discou+extracs)
          balance1.config(text=total-discou+extracs)
          sub1.config(text=total-discou)
        elif delrefresh[12] == "2":
          extracs = 0.0
          discou = 0.0
          total = 0.0
          for child in ord_pro_create_tree.get_children():
            total += float(ord_pro_create_tree.item(child, 'values')[7])
          discou = (total*float(ord_disrate.get())/100)
          extracs = extracs + float(ord_extracost.get())
          cost1.config(text=ord_extracost.get())
          discount1.config(text=discou)
          priceview.config(text=total)
          sub1.config(text=total-discou)

          tot = 0.0
          totaltax1 = 0.0
          for child in ord_pro_create_tree.get_children():
            checktax1 = list(ord_pro_create_tree.item(child, 'values'))
            if checktax1[6] == "🗹":
              totaltax1 =(totaltax1 + float(checktax1[7]))
              tax1sum.config(text=(float(totaltax1)*float(ord_tax.get())/100))
              tot = (float(totaltax1)*float(ord_tax.get())/100)
            else:
              pass
          order1.config(text=total+tot-discou+extracs)
          balance1.config(text=total+tot-discou+extracs)
        elif delrefresh[12] == "3":
          extracs = 0.0
          discou = 0.0
          total = 0.0
          for child in ord_pro_create_tree.get_children():
            total += float(ord_pro_create_tree.item(child, 'values')[8])
          discou = (total*float(ord_disrate.get())/100)
          extracs = extracs + float(ord_extracost.get())
          cost1.config(text=ord_extracost.get())
          discount1.config(text=discou)
          priceview.config(text=total)
          sub1.config(text=total-discou)
          
          tot = 0.0
          totaltax1 = 0.0
          for child in ord_pro_create_tree.get_children():
            checktax1 = list(ord_pro_create_tree.item(child, 'values'))
            if checktax1[6] == "🗹":
              totaltax1 =(totaltax1 + float(checktax1[8]))
              tax1sum.config(text=(float(totaltax1)*float(ord_tax.get())/100))
              tot = (float(totaltax1)*float(ord_tax.get())/100)
            else:
              pass
          
          tot2 = 0.0
          totaltax2 = 0.0
          for child in ord_pro_create_tree.get_children():
            checktax1 = list(ord_pro_create_tree.item(child, 'values'))
            if checktax1[7] == "🗹":
              totaltax2 =(totaltax2 + float(checktax1[8]))
              tax2sum.config(text=(float(totaltax2)*float(ord_tax2.get())/100))
              tot2 = (float(totaltax2)*float(ord_tax2.get())/100)
            else:
              pass

          order1.config(text=total+tot+tot2-discou+extracs)
          balance1.config(text=total+tot+tot2-discou+extracs)
      except: 
        pass
      
      
      

    firFrame=Frame(pop, bg="#f5f3f2", height=60)
    firFrame.pack(side="top", fill=X)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    create = Button(firFrame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_custom)
    create.pack(side="left", pady=3, ipadx=4)


    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    add= Button(firFrame,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_newline)
    add.pack(side="left", pady=3, ipadx=4)

    dele= Button(firFrame,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_create_delete1)
    dele.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    prev= Button(firFrame,compound="top", text="Preview\nOrder",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_create_previewline)
    prev.pack(side="left", pady=3, ipadx=4)

    prin= Button(firFrame,compound="top", text="Print \nOrder",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_create_printsele)
    prin.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    mail= Button(firFrame,compound="top", text="Email\nOrder",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_email)
    mail.pack(side="left", pady=3, ipadx=4)

    sms1= Button(firFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_create_sms1)
    sms1.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    calc= Button(firFrame,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
    calc.pack(side="left", pady=3, ipadx=4)

    calc= Button(firFrame,compound="top", text="save",relief=RAISED, image=tick,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=crate_order)
    calc.pack(side="right", pady=3, ipadx=4)

    fir1Frame=Frame(pop, height=180,bg="#f5f3f2")
    fir1Frame.pack(side="top", fill=X)

    global ord_to,ord_addr,ord_ship,ord_shipaddr,ord_email,ord_smsnum

    def selecombobox(event):
      ord_cus = ord_to.get()
      sql = "select * from customer where businessname = %s"
      val = (ord_cus,)
      fbcursor.execute(sql,val)
      cussel = fbcursor.fetchone()
      ord_addr.delete("1.0", END)
      ord_addr.insert("1.0", cussel[5])
      ord_ship.delete(0, END)
      ord_ship.insert(0, cussel[6])
      ord_shipaddr.delete("1.0", END)
      ord_shipaddr.insert("1.0", cussel[7])
      ord_email.delete(0, END)
      ord_email.insert(0, cussel[9])
      ord_smsnum.delete(0, END)
      ord_smsnum.insert(0, cussel[8])
    
    sql = "select businessname from customer"
    fbcursor.execute(sql)
    cusna = fbcursor.fetchall()
    labelframe1 = LabelFrame(fir1Frame,text="Customers",font=("arial",15))
    labelframe1.place(x=10,y=5,width=640,height=160)
    order = Label(labelframe1, text="Order to").place(x=10,y=5)
    ord_to = ttk.Combobox(labelframe1,width=28)
    ord_to["values"] = cusna
    ord_to.bind("<<ComboboxSelected>>",selecombobox)
    ord_to.place(x=80,y=5)
    address=Label(labelframe1,text="Address").place(x=10,y=30)
    ord_addr=Text(labelframe1,width=23)
    ord_addr.place(x=80,y=30,height=70)
    ship=Label(labelframe1,text="Ship to").place(x=342,y=5)
    ord_ship=Entry(labelframe1,width=30)
    ord_ship.place(x=402,y=3)
    address1=Label(labelframe1,text="Address").place(x=340,y=30)
    ord_shipaddr=Text(labelframe1,width=23)
    ord_shipaddr.place(x=402,y=30,height=70)

    btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=280, y=50)
    
    labelframe2 = LabelFrame(fir1Frame,text="")
    labelframe2.place(x=10,y=130,width=640,height=42)
    email=Label(labelframe2,text="Email").place(x=10,y=5)
    ord_email=Entry(labelframe2,width=30)
    ord_email.place(x=80,y=5)
    sms=Label(labelframe2,text="SMS Number").place(x=328,y=5)
    ord_smsnum=Entry(labelframe2,width=30)
    ord_smsnum.place(x=402,y=5)
      
    labelframe = LabelFrame(fir1Frame,text="Order",font=("arial",15))
    labelframe.place(x=652,y=5,width=290,height=170)
    order=Label(labelframe,text="Order#").place(x=5,y=5)
    ord_orderid=Entry(labelframe,width=25)
    ord_orderid.place(x=100,y=5,)
    def inv_num_increment(inum):
      result = ""
      numberStr = ""
      print(inum)
      i = len(inum) - 1
      while i > 0:
        c = inum[i]
        if not c.isdigit():
          break
        numberStr = c + numberStr
        i -= 1
      number = int(numberStr)
      number += 1
      result += inum[0 : i + 1]
      result += "0000" if number < 10 else ""
      result += str(number)
      return result
    fbcursor.execute("SELECT order_number FROM orders ORDER BY orderid DESC LIMIT 1")
    ord_number_data = fbcursor.fetchone()
    if not ord_number_data == None:
      a = ord_number_data[0]
      ord_no = inv_num_increment(a)
    else:
      ord_no = 1
    ord_orderid.insert(0, ord_no)
    orderdate=Label(labelframe,text="Order date").place(x=5,y=33)
    ord_date=DateEntry(labelframe,width=20)
    ord_date.place(x=150,y=33)
    def ord_due():
      if checkvarStatus522.get():
        ord_duedate["state"] = NORMAL
      else:
        ord_duedate["state"] = DISABLED
        ord_duedate.delete(0, END)
        
    checkvarStatus522=BooleanVar()
    ord_duedatecheck=Checkbutton(labelframe,variable = checkvarStatus522,text="Due date",onvalue =1,offvalue = 0,command=ord_due)
    ord_duedatecheck.select()
    ord_duedatecheck.place(x=5,y=62)
    ord_duedate=DateEntry(labelframe,width=20)
    ord_duedate.place(x=150,y=62)
    terms=Label(labelframe,text="Terms").place(x=5,y=92)
    ord_terms=ttk.Combobox(labelframe, value="",width=25)
    ord_terms.place(x=100,y=92)
    ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
    ord_orderref=Entry(labelframe,width=27)
    ord_orderref.place(x=100,y=118)

    fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
    fir2Frame.pack(side="top", fill=X)
    listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
    
    
    sql = "select * from company"
    fbcursor.execute(sql)
    create_maintree = fbcursor.fetchone()
    
    
    if  not create_maintree:
      ord_pro_create_tree=ttk.Treeview(listFrame)
      ord_pro_create_tree["columns"]=["1","2","3","4","5","6","7","8"]
      ord_pro_create_tree.column("#0", width=40)
      ord_pro_create_tree.column("1", width=80)
      ord_pro_create_tree.column("2", width=190)
      ord_pro_create_tree.column("3", width=190)
      ord_pro_create_tree.column("4", width=80)
      ord_pro_create_tree.column("5", width=60)
      ord_pro_create_tree.column("6", width=60)
      ord_pro_create_tree.column("7", width=60)
      ord_pro_create_tree.column("8", width=80)
      
      ord_pro_create_tree.heading("#0")
      ord_pro_create_tree.heading("1",text="ID/SKU")
      ord_pro_create_tree.heading("2",text="Product/Service")
      ord_pro_create_tree.heading("3",text="Description")
      ord_pro_create_tree.heading("4",text="Unit Price")
      ord_pro_create_tree.heading("5",text="Quality")
      ord_pro_create_tree.heading("6",text="Pcs/Weight")
      ord_pro_create_tree.heading("7",text="Tax1")
      ord_pro_create_tree.heading("8",text="Price")

    elif create_maintree[12] == "1":
      ord_pro_create_tree=ttk.Treeview(listFrame)
      ord_pro_create_tree["columns"]=["1","2","3","4","5","6","7"]
      ord_pro_create_tree.column("#0", width=40)
      ord_pro_create_tree.column("1", width=80)
      ord_pro_create_tree.column("2", width=190)
      ord_pro_create_tree.column("3", width=190)
      ord_pro_create_tree.column("4", width=80)
      ord_pro_create_tree.column("5", width=60)
      ord_pro_create_tree.column("6", width=60)
      ord_pro_create_tree.column("7", width=60)
      
      ord_pro_create_tree.heading("#0")
      ord_pro_create_tree.heading("1",text="ID/SKU")
      ord_pro_create_tree.heading("2",text="Product/Service")
      ord_pro_create_tree.heading("3",text="Description")
      ord_pro_create_tree.heading("4",text="Unit Price")
      ord_pro_create_tree.heading("5",text="Quality")
      ord_pro_create_tree.heading("6",text="Pcs/Weight")
      ord_pro_create_tree.heading("7",text="Price")
    elif create_maintree[12] == "2":
      ord_pro_create_tree=ttk.Treeview(listFrame)
      ord_pro_create_tree["columns"]=["1","2","3","4","5","6","7","8"]
      ord_pro_create_tree.column("#0", width=40)
      ord_pro_create_tree.column("1", width=80)
      ord_pro_create_tree.column("2", width=190)
      ord_pro_create_tree.column("3", width=190)
      ord_pro_create_tree.column("4", width=80)
      ord_pro_create_tree.column("5", width=60)
      ord_pro_create_tree.column("6", width=60)
      ord_pro_create_tree.column("7", width=60)
      ord_pro_create_tree.column("8", width=80)
      
      ord_pro_create_tree.heading("#0")
      ord_pro_create_tree.heading("1",text="ID/SKU")
      ord_pro_create_tree.heading("2",text="Product/Service")
      ord_pro_create_tree.heading("3",text="Description")
      ord_pro_create_tree.heading("4",text="Unit Price")
      ord_pro_create_tree.heading("5",text="Quality")
      ord_pro_create_tree.heading("6",text="Pcs/Weight")
      ord_pro_create_tree.heading("7",text="Tax1")
      ord_pro_create_tree.heading("8",text="Price")
    elif create_maintree[12] == "3":
      ord_pro_create_tree=ttk.Treeview(listFrame)
      ord_pro_create_tree["columns"]=["1","2","3","4","5","6","7","8","9"]
      ord_pro_create_tree.column("#0", width=40)
      ord_pro_create_tree.column("1", width=80)
      ord_pro_create_tree.column("2", width=190)
      ord_pro_create_tree.column("3", width=190)
      ord_pro_create_tree.column("4", width=80)
      ord_pro_create_tree.column("5", width=60)
      ord_pro_create_tree.column("6", width=60)
      ord_pro_create_tree.column("7", width=60)
      ord_pro_create_tree.column("8", width=80)
      ord_pro_create_tree.column("9", width=80)
      
      ord_pro_create_tree.heading("#0")
      ord_pro_create_tree.heading("1",text="ID/SKU")
      ord_pro_create_tree.heading("2",text="Product/Service")
      ord_pro_create_tree.heading("3",text="Description")
      ord_pro_create_tree.heading("4",text="Unit Price")
      ord_pro_create_tree.heading("5",text="Quality")
      ord_pro_create_tree.heading("6",text="Pcs/Weight")
      ord_pro_create_tree.heading("7",text="Tax1")
      ord_pro_create_tree.heading("8",text="Tax2")
      ord_pro_create_tree.heading("9",text="Price")
      
    ord_pro_create_tree.pack(fill="both", expand=1)
    listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    priceview = Label(listFrame,bg="#f5f3f2")
    priceview.place(x=850,y=200,width=78,height=18)

    new_value = StringVar()
    def edit_window_box(val):
        
        edit_window = Toplevel()
        edit_window.title("Edit the value or cancel")
        edit_window.geometry("400x200+350+300")
        label_edit = Label(edit_window , text='Enter value to edit', 
        font = ("Times New Roman", 10)).place(x=68,y=60)
        #create edit box
        edit_box = Entry(edit_window)
        edit_box.insert(0,val)
        edit_box.place(x=200,y=63)
        #auto select edit window 
        edit_window.focus()
        
        def value_assignment(event):
            printing = edit_box.get()
            new_value.set(printing)
            #only destroy will not update the value (perhaps event keeps running in background)
            #quit allows event to stop n update value in tree but does not close the window in single click 
            #rather on dbl click shuts down entire app 
            edit_window.quit()
            edit_window.destroy()
        
        edit_window.bind('<Return>', value_assignment )
    
        B1 = Button(edit_window, text="Okay")
        B1.bind('<Button-1>',value_assignment)
        B1.place(x=70,y=130)
        
        B2 = Button(edit_window, text="Cancel", command = edit_window.destroy).place(x=276,y=130)
        edit_window.mainloop()
        
    #will explain
    #variable to hold col value (col clicked)
    shape1 = IntVar()
    #tracks both col , row on mouse click
    def tree_click_handler(event):
        cur_item = ord_pro_create_tree.item(ord_pro_create_tree.focus())
        col = ord_pro_create_tree.identify_column(event.x)[1:]
        rowid = ord_pro_create_tree.identify_row(event.y)[1:]
        #updates list
        shape1.set(col)
        try:
            x,y,w,h = ord_pro_create_tree.bbox('I'+rowid,'#'+col)
        except:pass
        #tree.tag_configure("highlight", background="yellow")
        return(col)
        
    #code linked to event    
    ord_pro_create_tree.bind('<ButtonRelease-1>', tree_click_handler)
    def edit(event):
      try:
        selected_item = ord_pro_create_tree.selection()[0]
        temp = list(ord_pro_create_tree.item(selected_item , 'values'))
        tree_click_handler
        col_selected = int(shape1.get())-1
        edit_window_box(temp[col_selected])
        #do not run if edit window is open
        #use edit_window.mainloop() so value assign after window closes
        temp[col_selected] = new_value.get()
        ord_pro_create_tree.item(selected_item, values= temp)
      except: pass
    
     
#binding allows to edit on screen double click
    ord_pro_create_tree.bind('<Double-Button-1>' , edit)

    fir3Frame=Frame(pop,height=200,width=700,bg="#f5f3f2")
    fir3Frame.place(x=0,y=490)

    tabStyle = ttk.Style()
    tabStyle.theme_use('default')
    tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
    myNotebook=ttk.Notebook(fir3Frame)
    orderFrame = Frame(myNotebook, height=200, width=800)
    headerFrame = Frame(myNotebook, height=200, width=800)
    commentFrame = Frame(myNotebook, height=200, width=800)
    termsFrame = Frame(myNotebook, height=200, width=800)
    noteFrame = Frame(myNotebook, height=200, width=800)
    documentFrame = Frame(myNotebook, height=200, width=800)
    
    myNotebook.add(orderFrame,compound="left", text="Order")
    myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
    myNotebook.add(commentFrame,compound="left",  text="Comments")
    myNotebook.add(termsFrame,compound="left", text="Terms")
    myNotebook.add(noteFrame,compound="left",  text="Private notes")
    myNotebook.add(documentFrame,compound="left",  text="Documents")
    myNotebook.pack(expand = 1, fill ="both")  

    labelframe1 = LabelFrame(orderFrame,text="",font=("arial",15))
    labelframe1.place(x=1,y=1,width=800,height=170)
    cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)

    sql = "select extra_cost_name from extra_cost_name"
    fbcursor.execute(sql,)
    extra_cname = fbcursor.fetchall()
    extra_cnamedata = []
    for i in extra_cname:
      extra_cnamedata.append(i[0])

    ord_extracostname=ttk.Combobox(labelframe1, value="",width=20)
    ord_extracostname["value"] = extra_cnamedata
    ord_extracostname.place(x=115,y=5)
    def binddisc(event):
      discount.config(text=ord_disrate.get()+"%Discount")
      sql = "select * from company"
      fbcursor.execute(sql)
      disbind = fbcursor.fetchone()
      if not disbind:
        extracs = 0.0
        discou = 0.0
        total = 0.0
        for child in ord_pro_create_tree.get_children():
          total += float(ord_pro_create_tree.item(child, 'values')[6])
        discou = (total*float(ord_disrate.get())/100)
        extracs = extracs + float(ord_extracost.get())
        cost1.config(text=ord_extracost.get())
        discount1.config(text=discou)
        priceview.config(text=total)
        order1.config(text=total-discou+extracs)
        balance1.config(text=total-discou+extracs)
        sub1.config(text=total-discou)

      elif disbind[12] == "1":
        extracs = 0.0
        discou = 0.0
        total = 0.0
        for child in ord_pro_create_tree.get_children():
          total += float(ord_pro_create_tree.item(child, 'values')[6])
        discou = (total*float(ord_disrate.get())/100)
        extracs = extracs + float(ord_extracost.get())
        cost1.config(text=ord_extracost.get())
        discount1.config(text=discou)
        priceview.config(text=total)
        order1.config(text=total-discou+extracs)
        balance1.config(text=total-discou+extracs)
        sub1.config(text=total-discou)
        
      elif disbind[12] == "2":
        extracs = 0.0
        discou = 0.0
        total = 0.0
        for child in ord_pro_create_tree.get_children():
          total += float(ord_pro_create_tree.item(child, 'values')[7])
        extracs = extracs + float(ord_extracost.get())
        cost1.config(text=ord_extracost.get())
        discou = (total*float(ord_disrate.get())/100)
        discount1.config(text=discou)
        priceview.config(text=total)
        sub1.config(text=total-discou)
        tot = 0.0
        totaltax1 = 0.0
        for child in ord_pro_create_tree.get_children():
          checktax1 = list(ord_pro_create_tree.item(child, 'values'))
          if checktax1[6] == "🗹":
            totaltax1 =(totaltax1 + float(checktax1[7]))
            tax1sum.config(text=(float(totaltax1)*float(ord_tax.get())/100))
            tot = (float(totaltax1)*float(ord_tax.get())/100)
          else:
            pass
        order1.config(text=total+tot-discou+extracs)
        balance1.config(text=total+tot-discou+extracs)
          
      elif disbind[12] == "3":
        extracs = 0.0
        discou = 0.0
        total = 0.0
        for child in ord_pro_create_tree.get_children():
          total += float(ord_pro_create_tree.item(child, 'values')[8])
        discou = (total*float(ord_disrate.get())/100)
        extracs = extracs + float(ord_extracost.get())
        cost1.config(text=ord_extracost.get())
        discount1.config(text=discou)
        priceview.config(text=total)
        sub1.config(text=total-discou)
        tot = 0.0
        totaltax1 = 0.0
        for child in ord_pro_create_tree.get_children():
          checktax1 = list(ord_pro_create_tree.item(child, 'values'))
          if checktax1[6] == "🗹":
            totaltax1 =(totaltax1 + float(checktax1[8]))
            tax1sum.config(text=(float(totaltax1)*float(ord_tax.get())/100))
            tot = (float(totaltax1)*float(ord_tax.get())/100)
          else:
            pass
        tot2 = 0.0
        totaltax2 = 0.0
        for child in ord_pro_create_tree.get_children():
          checktax1 = list(ord_pro_create_tree.item(child, 'values'))
          if checktax1[7] == "🗹":
            totaltax2 =(totaltax2 + float(checktax1[8]))
            tax2sum.config(text=(float(totaltax2)*float(ord_tax2.get())/100))
            tot2 = (float(totaltax2)*float(ord_tax2.get())/100)
          else:
            pass
        order1.config(text=total+tot+tot2-discou+extracs)
        balance1.config(text=total+tot+tot2-discou+extracs)


    rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
    ord_disrate=Spinbox(labelframe1,width=6,from_=0,to=100)
    ord_disrate.place(x=460,y=5)
    ord_disrate.bind('<Button-1>', binddisc)
    def extracostbind(event):
      sql = "select * from company"
      fbcursor.execute(sql)
      disbind = fbcursor.fetchone()
      if not disbind:
        extracs=0.0
        discou = 0.0
        total = 0.0
        for child in ord_pro_create_tree.get_children():
          total += float(ord_pro_create_tree.item(child, 'values')[6])
        discou = (total*float(ord_disrate.get())/100)
        extracs = extracs + float(ord_extracost.get())
        cost1.config(text=ord_extracost.get())
        cost1.config(ord_extracost.get())
        discount1.config(text=discou)
        priceview.config(text=total)
        order1.config(text=total-discou+extracs)
        balance1.config(text=total-discou+extracs)
        sub1.config(text=total-discou)

      elif disbind[12] == "1":
        extracs=0.0
        discou = 0.0
        total = 0.0
        for child in ord_pro_create_tree.get_children():
          total += float(ord_pro_create_tree.item(child, 'values')[6])
        discou = (total*float(ord_disrate.get())/100)
        extracs = (extracs+float(ord_extracost.get()))
        cost1.config(text=ord_extracost.get())
        discount1.config(text=discou)
        priceview.config(text=total)
        order1.config(text=total-discou+extracs)
        balance1.config(text=total-discou+extracs)
        sub1.config(text=total-discou)
        
      elif disbind[12] == "2":
        extracs=0.0
        discou = 0.0
        total = 0.0
        for child in ord_pro_create_tree.get_children():
          total += float(ord_pro_create_tree.item(child, 'values')[7])
        discou = (total*float(ord_disrate.get())/100)
        extracs = (extracs+float(ord_extracost.get()))
        cost1.config(text=ord_extracost.get())
        discount1.config(text=discou)
        priceview.config(text=total)
        sub1.config(text=total-discou)
        tot = 0.0
        totaltax1 = 0.0
        for child in ord_pro_create_tree.get_children():
          checktax1 = list(ord_pro_create_tree.item(child, 'values'))
          if checktax1[6] == "🗹":
            totaltax1 =(totaltax1 + float(checktax1[7]))
            tax1sum.config(text=(float(totaltax1)*float(ord_tax.get())/100))
            tot = (float(totaltax1)*float(ord_tax.get())/100)
          else:
            pass
        order1.config(text=total+tot-discou+extracs)
        balance1.config(text=total+tot-discou+extracs)
          
      elif disbind[12] == "3":
        extracs = 0.0
        discou = 0.0
        total = 0.0
        for child in ord_pro_create_tree.get_children():
          total += float(ord_pro_create_tree.item(child, 'values')[8])
        discou = (total*float(ord_disrate.get())/100)
        extracs = (extracs+float(ord_extracost.get()))
        cost1.config(text=ord_extracost.get())
        priceview.config(text=total)
        sub1.config(text=total-discou)
        tot = 0.0
        totaltax1 = 0.0
        for child in ord_pro_create_tree.get_children():
          checktax1 = list(ord_pro_create_tree.item(child, 'values'))
          if checktax1[6] == "🗹":
            totaltax1 =(totaltax1 + float(checktax1[8]))
            tax1sum.config(text=(float(totaltax1)*float(ord_tax.get())/100))
            tot = (float(totaltax1)*float(ord_tax.get())/100)
          else:
            pass
        tot2 = 0.0
        totaltax2 = 0.0
        for child in ord_pro_create_tree.get_children():
          checktax1 = list(ord_pro_create_tree.item(child, 'values'))
          if checktax1[7] == "🗹":
            totaltax2 =(totaltax2 + float(checktax1[8]))
            tax2sum.config(text=(float(totaltax2)*float(ord_tax2.get())/100))
            tot2 = (float(totaltax2)*float(ord_tax2.get())/100)
          else:
            pass
        order1.config(text=total+tot+tot2-discou+extracs)
        balance1.config(text=total+tot+tot2-discou+extracs)
    cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
    ord_extracoint = IntVar(value=0)
    ord_extracost=Entry(labelframe1,width=10,textvariable=ord_extracoint)
    ord_extracost.place(x=115,y=35)
    ord_extracost.bind('<KeyRelease>',extracostbind)
    def bindtax1(event):
      sql = "select * from company"
      fbcursor.execute(sql)
      tax1bind = fbcursor.fetchone()
      if tax1bind[12] == "2":
        extracs= 0.0
        discou = 0.0
        total = 0.0
        for child in ord_pro_create_tree.get_children():
          total += float(ord_pro_create_tree.item(child, 'values')[7])
        discou = (total*float(ord_disrate.get())/100)
        extracs = extracs + float(ord_extracost.get())
        cost1.config(text=ord_extracost.get())
        discount1.config(text=discou)
        priceview.config(text=total)
        sub1.config(text=total-discou)
  
        tot = 0.0
        totaltax1 = 0.0
        for child in ord_pro_create_tree.get_children():
          checktax1 = list(ord_pro_create_tree.item(child, 'values'))
          if checktax1[6] == "🗹":
            totaltax1 =(totaltax1 + float(checktax1[7]))
            tax1sum.config(text=(float(totaltax1)*float(ord_tax.get())/100))
            tot = (float(totaltax1)*float(ord_tax.get())/100)
          else:
            pass
        order1.config(text=total+tot-discou+extracs)
        balance1.config(text=total+tot-discou+extracs)
      elif tax1bind[12] == "3":
        extracs= 0.0
        discou = 0.0
        total = 0.0
        for child in ord_pro_create_tree.get_children():
          total += float(ord_pro_create_tree.item(child, 'values')[8])
        extracs = extracs + float(ord_extracost.get())
        cost1.config(text=ord_extracost.get())
        discou = (total*float(ord_disrate.get())/100)
        discount1.config(text=discou)
        priceview.config(text=total)
        sub1.config(text=total-discou)
        
        tot = 0.0
        totaltax1 = 0.0
        for child in ord_pro_create_tree.get_children():
          checktax1 = list(ord_pro_create_tree.item(child, 'values'))
          if checktax1[6] == "🗹":
            totaltax1 =(totaltax1 + float(checktax1[8]))
            tax1sum.config(text=(float(totaltax1)*float(ord_tax.get())/100))
            tot = (float(totaltax1)*float(ord_tax.get())/100)
          else:
            pass
        
        tot2 = 0.0
        totaltax2 = 0.0
        for child in ord_pro_create_tree.get_children():
          checktax1 = list(ord_pro_create_tree.item(child, 'values'))
          if checktax1[7] == "🗹":
            totaltax2 =(totaltax2 + float(checktax1[8]))
            tax2sum.config(text=(float(totaltax2)*float(ord_tax2.get())/100))
            tot2 = (float(totaltax2)*float(ord_tax2.get())/100)
          else:
            pass
  
        order1.config(text=total+tot+tot2-discou+extracs)
        balance1.config(text=total+tot+tot2-discou+extracs)
  
    def bindtax2(event):
      extracs= 0.0
      discou = 0.0
      total = 0.0
      for child in ord_pro_create_tree.get_children():
        total += float(ord_pro_create_tree.item(child, 'values')[8])
      discou = (total*float(ord_disrate.get())/100)
      extracs = extracs + float(ord_extracost.get())
      cost1.config(text=ord_extracost.get())
      discount1.config(text=discou)
      priceview.config(text=total)
      sub1.config(text=total-discou)
      
      tot = 0.0
      totaltax1 = 0.0
      for child in ord_pro_create_tree.get_children():
        checktax1 = list(ord_pro_create_tree.item(child, 'values'))
        if checktax1[6] == "🗹":
          totaltax1 =(totaltax1 + float(checktax1[8]))
          tax1sum.config(text=(float(totaltax1)*float(ord_tax.get())/100))
          tot = (float(totaltax1)*float(ord_tax.get())/100)
        else:
          pass
      
      tot2 = 0.0
      totaltax2 = 0.0
      for child in ord_pro_create_tree.get_children():
        checktax1 = list(ord_pro_create_tree.item(child, 'values'))
        if checktax1[7] == "🗹":
          totaltax2 =(totaltax2 + float(checktax1[8]))
          tax2sum.config(text=(float(totaltax2)*float(ord_tax2.get())/100))
          tot2 = (float(totaltax2)*float(ord_tax2.get())/100)
        else:
          pass

      order1.config(text=total+tot+tot2-discou+extracs)
      balance1.config(text=total+tot+tot2-discou+extracs)
    
    sql = "select taxtype,tax1rate,tax2rate from company"
    fbcursor.execute(sql)
    taxdis = fbcursor.fetchone()
    if not taxdis:
      pass
    elif taxdis[0] == "1":
      pass
    elif taxdis[0] == "2":
      tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
      ord_tax=Entry(labelframe1,width=7)
      ord_tax.place(x=460,y=35)
      if not taxdis:
        pass
      else:
        ord_tax.insert(0, taxdis[1])
      ord_tax.bind('<KeyRelease>', bindtax1)
    elif taxdis[0] == "3":
      tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
      ord_tax=Entry(labelframe1,width=7)
      ord_tax.place(x=460,y=35)
      tax2l=Label(labelframe1,text="Tax2").place(x=420,y=67)
      ord_tax2=Entry(labelframe1,width=7)
      ord_tax2.place(x=460,y=67)
      if not taxdis:
        pass
      else:
        ord_tax.insert(0, taxdis[1])
        ord_tax2.insert(0, taxdis[2])
      ord_tax.bind('<KeyRelease>', bindtax1)
      ord_tax2.bind('<KeyRelease>', bindtax2)

    
    template=Label(labelframe1,text="Template").place(x=37,y=70)
    ord_template=ttk.Combobox(labelframe1, value="",width=25)
    ord_template.place(x=115,y=70,width=200)
    ord_template["values"] = ["Professional 1 (logo on left side,UTF8","Professional 1 (logo on right side","Simplified 1(logo on left side)","Simplified 1(logo on right side)","Business Classic(UTF-8)"]
    sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
    ord_sales=Entry(labelframe1,width=18)
    ord_sales.place(x=115,y=100)
    category=Label(labelframe1,text="Category").place(x=300,y=100)
    ord_cate=Entry(labelframe1,width=22)
    ord_cate.place(x=370,y=100)
    
    statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
    statusfrme.place(x=540,y=0,width=160,height=160)
    draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey")
    draft.place(x=50, y=3)
    on1=Label(statusfrme, text="Emailed on:").place( y=50)
    nev1=Label(statusfrme, text="Never").place(x=100,y=50)
    on2=Label(statusfrme, text="Printed on:").place( y=90)
    nev2=Label(statusfrme, text="Never").place(x=100,y=90)
    
    sql = "select headerandfooter from header_and_footer"
    fbcursor.execute(sql,)
    extra_cname = fbcursor.fetchall()
    header = []
    for i in extra_cname:
      header.append(i[0])

    text1=Label(headerFrame,text="Title text").place(x=50,y=5)
    ord_titletext=ttk.Combobox(headerFrame,width=60)
    ord_titletext.place(x=125,y=5)
    ord_titletext["values"] = header
    text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
    ord_pageheadertext=ttk.Combobox(headerFrame, value="",width=60)
    ord_pageheadertext.place(x=125,y=45)
    ord_pageheadertext["values"] = header
    text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
    ord_footertext=ttk.Combobox(headerFrame, value="",width=60)
    ord_footertext.place(x=125,y=85)
    ord_footertext["values"] = header
    
    text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
    ord_privatenotes=Text(noteFrame,width=100,height=7)
    ord_privatenotes.place(x=10,y=32)

    ord_termsnotes=Text(termsFrame,width=100,height=9)
    ord_termsnotes.place(x=10,y=10)

    ord_commnotes=Text(commentFrame,width=100,height=9)
    ord_commnotes.place(x=10,y=10)

    add_doc=Button(documentFrame,height=2,width=3,text="+",command=ord_attach_doc).place(x=5,y=10)
    def ord_doc_del():
      try:
        selected_doc_item = ord_create_doc_tree.selection()[0]
        ord_create_doc_tree.delete(selected_doc_item)
      except:
        pass
    del_doc=Button(documentFrame,height=2,width=3,text="-",command=ord_doc_del).place(x=5,y=50)
    text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
    ord_create_doc_tree=ttk.Treeview(documentFrame, height=5)
    ord_create_doc_tree["columns"]=["1","2","3"]
    ord_create_doc_tree.column("#0", width=20)
    ord_create_doc_tree.column("1", width=250)
    ord_create_doc_tree.column("2", width=250)
    ord_create_doc_tree.column("2", width=200)
    ord_create_doc_tree.heading("#0",text="", anchor=W)
    ord_create_doc_tree.heading("1",text="Attach to Email")
    ord_create_doc_tree.heading("2",text="Filename")
    ord_create_doc_tree.heading("3",text="Filesize")  
    ord_create_doc_tree.place(x=50, y=45)
    
    
   
    fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
    fir4Frame.place(x=740,y=520)
    summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
    summaryfrme.place(x=0,y=0,width=200,height=170)
    discount=Label(summaryfrme, text="Discount")
    discount1=Label(summaryfrme, text="0.00")
    sub=Label(summaryfrme, text="Subtotal")
    sub1=Label(summaryfrme, text="0.00")
    tax=Label(summaryfrme, text="Tax1")
    tax1sum=Label(summaryfrme, text="0.00")
    tax22=Label(summaryfrme, text="Tax2")
    tax2sum=Label(summaryfrme, text="0.00")
    cost=Label(summaryfrme, text="Extra cost")
    cost1=Label(summaryfrme, text="0.00")
    order=Label(summaryfrme, text="Order total")
    order1=Label(summaryfrme, text="0.00")
    total=Label(summaryfrme, text="Total paid")
    total1=Label(summaryfrme, text="0.00")
    balance=Label(summaryfrme, text="Balance")
    balance1=Label(summaryfrme, text="0.00")

    sql = "select taxtype from company"
    fbcursor.execute(sql)
    taxsummarysym = fbcursor.fetchone()
    sql = "select currencysign,currsignplace from company"
    fbcursor.execute(sql)
    symbollabal = fbcursor.fetchone()
    discountsym = Label(summaryfrme,text=symbollabal[0])
    subsym = Label(summaryfrme,text=symbollabal[0])
    tax1sym = Label(summaryfrme,text=symbollabal[0])
    tax2sym = Label(summaryfrme,text=symbollabal[0])
    costsym = Label(summaryfrme,text=symbollabal[0])
    ordersym = Label(summaryfrme,text=symbollabal[0])
    totalsym = Label(summaryfrme,text=symbollabal[0])
    balsym = Label(summaryfrme,text=symbollabal[0])
    if not taxsummarysym:
      discountsym.place(x=105,y=7)
      subsym.place(x=105,y=28)
      costsym.place(x=105,y=54)
      ordersym.place(x=105,y=77)
      totalsym.place(x=105,y=98)
      balsym.place(x=105,y=119)
    elif taxsummarysym[0] == "1":
      discountsym.place(x=105,y=7)
      subsym.place(x=105,y=28)
      costsym.place(x=105,y=54)
      ordersym.place(x=105,y=77)
      totalsym.place(x=105,y=98)
      balsym.place(x=105,y=119)
    elif taxsummarysym[0] == "2":
      discountsym.place(x=105,y=0)
      subsym.place(x=105,y=21)
      tax1sym.place(x=105,y=42)
      costsym.place(x=105,y=63)
      ordersym.place(x=105,y=84)
      totalsym.place(x=105,y=105)
      balsym.place(x=105,y=126)
    elif taxsummarysym[0] == "3":
      discountsym.place(x=105,y=0)
      subsym.place(x=105,y=16)
      tax1sym.place(x=105,y=36)
      tax2sym.place(x=105,y=52)
      costsym.place(x=105,y=69)
      ordersym.place(x=105,y=89)
      totalsym.place(x=105,y=110)
      balsym.place(x=105,y=126)

    
    sql = "select taxtype from company"
    fbcursor.execute(sql)
    taxsummary = fbcursor.fetchone()
    if not taxsummary:
      discount.place(x=0 ,y=7)
      discount1.place(x=130 ,y=7)
      sub.place(x=0 ,y=28)
      sub1.place(x=130 ,y=28)
      cost.place(x=0 ,y=54)
      cost1.place(x=130 ,y=54)
      order.place(x=0 ,y=77)
      order1.place(x=130 ,y=77)
      total.place(x=0 ,y=98)
      total1.place(x=130 ,y=98)
      balance.place(x=0 ,y=119)
      balance1.place(x=130 ,y=119)
    elif taxsummary[0] == "1":
      discount.place(x=0 ,y=7)
      discount1.place(x=130 ,y=7)
      sub.place(x=0 ,y=28)
      sub1.place(x=130 ,y=28)
      cost.place(x=0 ,y=54)
      cost1.place(x=130 ,y=54)
      order.place(x=0 ,y=77)
      order1.place(x=130 ,y=77)
      total.place(x=0 ,y=98)
      total1.place(x=130 ,y=98)
      balance.place(x=0 ,y=119)
      balance1.place(x=130 ,y=119)
    elif taxsummary[0] == "2":
      tax.place(x=0 ,y=42)
      tax1sum.place(x=130 ,y=42)
      discount.place(x=0 ,y=0)
      discount1.place(x=130 ,y=0)
      sub.place(x=0 ,y=21)
      sub1.place(x=130 ,y=21)
      cost.place(x=0 ,y=63)
      cost1.place(x=130 ,y=63)
      order.place(x=0 ,y=84)
      order1.place(x=130 ,y=84)
      total.place(x=0 ,y=105)
      total1.place(x=130 ,y=105)
      balance.place(x=0 ,y=126)
      balance1.place(x=130 ,y=126)
    elif taxsummary[0] == "3":
      tax.place(x=0 ,y=36)
      tax1sum.place(x=130 ,y=36)
      tax22.place(x=0 ,y=52)
      tax2sum.place(x=130 ,y=52)
      discount.place(x=0 ,y=0)
      discount1.place(x=130 ,y=0)
      sub.place(x=0 ,y=16)
      sub1.place(x=130 ,y=16)
      cost.place(x=0 ,y=69)
      cost1.place(x=130 ,y=69)
      order.place(x=0 ,y=89)
      order1.place(x=130 ,y=89)
      total.place(x=0 ,y=110)
      total1.place(x=130 ,y=110)
      balance.place(x=0 ,y=126)
      balance1.place(x=130 ,y=126)

    fir5Frame=Frame(pop,height=38,width=210)
    fir5Frame.place(x=735,y=485)

    btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
    btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)

  ### End Create Order ###

  ##View/Edit order##
  def order_edit():
    pop=Toplevel(order_midFrame)
    pop.title("Orders")
    pop.geometry("950x690+150+0")


    #select customer
    def order_custom():
      cuselection=Toplevel()
      cuselection.title("Select Customer")
      cuselection.geometry("930x650+240+10")
      cuselection.resizable(False, False)


      #add new customer
      def order_create_customer():
        ven=Toplevel(order_midFrame)
        ven.title("Add new Customer")
        ven.geometry("930x650+240+10")
        checkvar1=IntVar()
        checkvar2=IntVar()
        radio=IntVar()
        createFrame=Frame(ven, bg="#f5f3f2", height=650)
        createFrame.pack(side="top", fill="both")
        labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
        labelframe1.place(x=10,y=5,width=910,height=600)
        text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
        e1=Entry(labelframe1,width=25).place(x=150,y=10)
        text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
        e2=ttk.Combobox(labelframe1,width=25,value="Default").place(x=460 ,y=10)
        text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
        Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
        
        labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
        labelframe2.place(x=5,y=40,width=420,height=150)
        name = Label(labelframe2, text="Ship to name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
        e1 = Entry(labelframe2,width=28).place(x=130,y=5)
        addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
        e2 = Entry(labelframe2,width=28).place(x=130,y=40,height=80)
        
        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

        labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
        labelframe3.place(x=480,y=40,width=420,height=150)
        name = Label(labelframe3, text="Business name:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe3,width=28).place(x=130,y=5)
        addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
        e2 = Entry(labelframe3,width=28).place(x=130,y=40,height=80)
        
        labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe4.place(x=5,y=195,width=420,height=150)
        name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe4,width=28).place(x=130,y=5)
        email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
        e2 = Entry(labelframe4,width=28).place(x=130,y=35)
        tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        e3 = Entry(labelframe4,width=11).place(x=130,y=65)
        fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        e4 = Entry(labelframe4,width=11).place(x=280,y=65)
        sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
        e5 = Entry(labelframe4,width=15).place(x=248,y=95)      

        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

        
        labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
        labelframe5.place(x=480,y=195,width=420,height=125)
        name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe5,width=28).place(x=130,y=5)
        email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
        e2 = Entry(labelframe5,width=28).place(x=130,y=35)
        tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        e3 = Entry(labelframe5,width=11).place(x=130,y=65)
        fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        e4 = Entry(labelframe5,width=11).place(x=280,y=65)

        labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe6.place(x=5,y=350,width=420,height=100)
        Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
        tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
        e1 = Entry(labelframe6,width=10).place(x=290,y=5)
        discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
        e2 = Entry(labelframe6,width=10).place(x=100,y=35)

        labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe7.place(x=480,y=330,width=420,height=100)
        country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe7,width=28).place(x=130,y=5)
        city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
        e2 = Entry(labelframe7,width=28).place(x=130,y=35)

        labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
        labelframe8.place(x=5,y=460,width=420,height=100)
        R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
        R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
        R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
        

        labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
        labelframe9.place(x=480,y=430,width=420,height=150)
        e1 = Entry(labelframe9).place(x=10,y=10,height=100,width=390)

        btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK").place(x=20, y=615)
        btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
      
      def order_edit_customer():
        ven=Toplevel(order_midFrame)
        ven.title("Add new Customer")
        ven.geometry("930x650+240+10")
        checkvar1=IntVar()
        checkvar2=IntVar()
        radio=IntVar()
        createFrame=Frame(ven, bg="#f5f3f2", height=650)
        createFrame.pack(side="top", fill="both")
        labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
        labelframe1.place(x=10,y=5,width=910,height=600)
        text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
        e1=Entry(labelframe1,width=25).place(x=150,y=10)
        text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
        e2=ttk.Combobox(labelframe1,width=25,value="Default").place(x=460 ,y=10)
        text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
        Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
        
        labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
        labelframe2.place(x=5,y=40,width=420,height=150)
        name = Label(labelframe2, text="Ship to name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
        e1 = Entry(labelframe2,width=28).place(x=130,y=5)
        addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
        e2 = Entry(labelframe2,width=28).place(x=130,y=40,height=80)
        
        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

        labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
        labelframe3.place(x=480,y=40,width=420,height=150)
        name = Label(labelframe3, text="Business name:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe3,width=28).place(x=130,y=5)
        addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
        e2 = Entry(labelframe3,width=28).place(x=130,y=40,height=80)
        
        labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe4.place(x=5,y=195,width=420,height=150)
        name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe4,width=28).place(x=130,y=5)
        email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
        e2 = Entry(labelframe4,width=28).place(x=130,y=35)
        tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        e3 = Entry(labelframe4,width=11).place(x=130,y=65)
        fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        e4 = Entry(labelframe4,width=11).place(x=280,y=65)
        sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
        e5 = Entry(labelframe4,width=15).place(x=248,y=95)      

        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

        
        labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
        labelframe5.place(x=480,y=195,width=420,height=125)
        name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe5,width=28).place(x=130,y=5)
        email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
        e2 = Entry(labelframe5,width=28).place(x=130,y=35)
        tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        e3 = Entry(labelframe5,width=11).place(x=130,y=65)
        fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        e4 = Entry(labelframe5,width=11).place(x=280,y=65)

        labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe6.place(x=5,y=350,width=420,height=100)
        Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
        tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
        e1 = Entry(labelframe6,width=10).place(x=290,y=5)
        discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
        e2 = Entry(labelframe6,width=10).place(x=100,y=35)

        labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe7.place(x=480,y=330,width=420,height=100)
        country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe7,width=28).place(x=130,y=5)
        city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
        e2 = Entry(labelframe7,width=28).place(x=130,y=35)

        labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
        labelframe8.place(x=5,y=460,width=420,height=100)
        R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
        R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
        R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
        

        labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
        labelframe9.place(x=480,y=430,width=420,height=150)
        e1 = Entry(labelframe9).place(x=10,y=10,height=100,width=390)

        btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK").place(x=20, y=615)
        btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
          
                

      enter=Label(cuselection, text="Enter filter text").place(x=5, y=10)
      e1=Entry(cuselection, width=20).place(x=110, y=10)
      text=Label(cuselection, text="Filtered column").place(x=340, y=10)
      e2=Entry(cuselection, width=20).place(x=450, y=10)

      ord_edit_cusventtree=ttk.Treeview(cuselection, height=27)
      ord_edit_cusventtree["columns"]=["1","2","3", "4"]
      ord_edit_cusventtree.column("#0", width=35)
      ord_edit_cusventtree.column("1", width=160)
      ord_edit_cusventtree.column("2", width=160)
      ord_edit_cusventtree.column("3", width=140)
      ord_edit_cusventtree.column("4", width=140)
      ord_edit_cusventtree.heading("#0",text="")
      ord_edit_cusventtree.heading("1",text="Customer/Ventor ID")
      ord_edit_cusventtree.heading("2",text="Customer/Ventor Name")
      ord_edit_cusventtree.heading("3",text="Tel.")
      ord_edit_cusventtree.heading("4",text="Contact Person")
      ord_edit_cusventtree.place(x=5, y=45)


      ctegorytree=ttk.Treeview(cuselection, height=27)
      ctegorytree["columns"]=["1"]
      ctegorytree.column("#0", width=35, minwidth=20)
      ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      ctegorytree.heading("#0",text="", anchor=W)
      ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      ctegorytree.place(x=660, y=45)

      scrollbar = Scrollbar(cuselection)
      scrollbar.place(x=640, y=45, height=560)
      scrollbar.config( command=ord_edit_cusventtree.yview )

      btn1=Button(cuselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
      btn1=Button(cuselection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=order_create_customer).place(x=250, y=610)
      btn1=Button(cuselection,compound = LEFT,image=tick, text="Add new customer", width=150,command=order_edit_customer).place(x=435, y=610)
      btn1=Button(cuselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)   



      

    #add new line item
    def order_newline():
      newselection=Toplevel()
      newselection.title("Select Customer")
      newselection.geometry("930x650+240+10")
      newselection.resizable(False, False)


      #add new product
      #add new product
      def order_create_product():  
        top = Toplevel()  
        top.title("Add a new Product/Service")
        p2 = PhotoImage(file = 'images/fbicon.png')
        top.iconphoto(False, p2)
      
        top.geometry("700x550+390+15")
        tabControl = ttk.Notebook(top)
        s = ttk.Style()
        s.theme_use('default')
        s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
      
        tabControl.add(tab1,compound = LEFT, text ='Product/Service')
        tabControl.add(tab2,compound = LEFT, text ='Product Image')
      
        tabControl.pack(expand = 1, fill ="both")
      
        innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
        innerFrame.pack(side="top",fill=BOTH)

        Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
        Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

        code1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
        code1.place(x=20,y=0)
        codeentry = Entry(Customerlabelframe,width=35)
        codeentry.place(x=120,y=8)

        checkvarStatus=IntVar()
        status1=Label(Customerlabelframe,text="Status:")
        status1.place(x=500,y=8)
        Button1 = Checkbutton(Customerlabelframe,
                          variable = checkvarStatus,text="Active",compound="right",
                          onvalue =0 ,
                          offvalue = 1,
                        
                          width = 10)

        Button1.place(x=550,y=5)

        category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
        category1.place(x=20,y=40)
        n = StringVar()
        country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
        
        country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
        
        country.place(x=120,y=45)
        country.current(0)


        name1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
        name1.place(x=20,y=70)
        nameentry = Entry(Customerlabelframe,width=60)
        nameentry.place(x=120,y=75)

        des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
        des1.place(x=20,y=100)
        desentry = Entry(Customerlabelframe,width=60)
        desentry.place(x=120,y=105)

        uval = IntVar(Customerlabelframe, value='$0.00')
        unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
        unit1.place(x=20,y=130)
        unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
        unitentry.place(x=120,y=135)

        pcsval = IntVar(Customerlabelframe, value='$0.00')
        pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
        pcs1.place(x=320,y=140)
        pcsentry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
        pcsentry.place(x=410,y=140)

        costval = IntVar(Customerlabelframe, value='$0.00')
        cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
        cost1.place(x=20,y=160)
        costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
        costentry.place(x=120,y=165)

        priceval = IntVar(Customerlabelframe, value='$0.00')
        price1=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
        price1.place(x=20,y=190)
        priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
        priceentry.place(x=120,y=195)

        checkvarStatus2=IntVar()
      
        Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                          text="Taxable Tax1rate",compound="right",
                          onvalue =0 ,
                          offvalue = 1,
                          height=2,
                          width = 12)

        Button2.place(x=415,y=170)


        checkvarStatus3=IntVar()
      
        Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                          text="No stock Control",
                          onvalue =1 ,
                          offvalue = 0,
                          height=3,
                          width = 15)

        Button3.place(x=40,y=220)


        stockval = IntVar(Customerlabelframe, value='0')
        stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
        stock1.place(x=90,y=260)
        stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
        stockentry.place(x=150,y=265)

        lowval = IntVar(Customerlabelframe, value='0')
        low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
        low1.place(x=300,y=260)
        lowentry = Entry(Customerlabelframe,width=10,textvariable=lowval)
        lowentry.place(x=495,y=265)

      
        ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
        ware1.place(x=60,y=290)
        wareentry = Entry(Customerlabelframe,width=50)
        wareentry.place(x=150,y=295)

        text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
        text1.place(x=20,y=330)

        txt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
        txt.place(x=32,y=358)




        okButton = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60)
        okButton.pack(side=LEFT)

        cancelButton = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
        cancelButton.pack(side=RIGHT)

        imageFrame = Frame(tab2, relief=GROOVE,height=580)
        imageFrame.pack(side="top",fill=BOTH)

        browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
        browseimg.place(x=15,y=35)

        browsebutton=Button(imageFrame,text = 'Browse')
        browsebutton.place(x=580,y=30,height=30,width=50)
        
        removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
        removeButton.place(x=400,y=450)
      
      def order_edit_product():  
        top = Toplevel()  
        top.title("Add a new Product/Service")
        p2 = PhotoImage(file = 'images/fbicon.png')
        top.iconphoto(False, p2)
      
        top.geometry("700x550+390+15")
        tabControl = ttk.Notebook(top)
        s = ttk.Style()
        s.theme_use('default')
        s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
      
        tabControl.add(tab1,compound = LEFT, text ='Product/Service')
        tabControl.add(tab2,compound = LEFT, text ='Product Image')
      
        tabControl.pack(expand = 1, fill ="both")
      
        innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
        innerFrame.pack(side="top",fill=BOTH)

        Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
        Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

        code1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
        code1.place(x=20,y=0)
        codeentry = Entry(Customerlabelframe,width=35)
        codeentry.place(x=120,y=8)

        checkvarStatus=IntVar()
        status1=Label(Customerlabelframe,text="Status:")
        status1.place(x=500,y=8)
        Button1 = Checkbutton(Customerlabelframe,
                          variable = checkvarStatus,text="Active",compound="right",
                          onvalue =0 ,
                          offvalue = 1,
                        
                          width = 10)

        Button1.place(x=550,y=5)

        category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
        category1.place(x=20,y=40)
        n = StringVar()
        country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
        
        country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
        
        country.place(x=120,y=45)
        country.current(0)


        name1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
        name1.place(x=20,y=70)
        nameentry = Entry(Customerlabelframe,width=60)
        nameentry.place(x=120,y=75)

        des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
        des1.place(x=20,y=100)
        desentry = Entry(Customerlabelframe,width=60)
        desentry.place(x=120,y=105)

        uval = IntVar(Customerlabelframe, value='$0.00')
        unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
        unit1.place(x=20,y=130)
        unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
        unitentry.place(x=120,y=135)

        pcsval = IntVar(Customerlabelframe, value='$0.00')
        pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
        pcs1.place(x=320,y=140)
        pcsentry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
        pcsentry.place(x=410,y=140)

        costval = IntVar(Customerlabelframe, value='$0.00')
        cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
        cost1.place(x=20,y=160)
        costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
        costentry.place(x=120,y=165)

        priceval = IntVar(Customerlabelframe, value='$0.00')
        price1=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
        price1.place(x=20,y=190)
        priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
        priceentry.place(x=120,y=195)

        checkvarStatus2=IntVar()
      
        Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                          text="Taxable Tax1rate",compound="right",
                          onvalue =0 ,
                          offvalue = 1,
                          height=2,
                          width = 12)

        Button2.place(x=415,y=170)


        checkvarStatus3=IntVar()
      
        Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                          text="No stock Control",
                          onvalue =1 ,
                          offvalue = 0,
                          height=3,
                          width = 15)

        Button3.place(x=40,y=220)


        stockval = IntVar(Customerlabelframe, value='0')
        stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
        stock1.place(x=90,y=260)
        stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
        stockentry.place(x=150,y=265)

        lowval = IntVar(Customerlabelframe, value='0')
        low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
        low1.place(x=300,y=260)
        lowentry = Entry(Customerlabelframe,width=10,textvariable=lowval)
        lowentry.place(x=495,y=265)

      
        ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
        ware1.place(x=60,y=290)
        wareentry = Entry(Customerlabelframe,width=50)
        wareentry.place(x=150,y=295)

        text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
        text1.place(x=20,y=330)

        txt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
        txt.place(x=32,y=358)




        okButton = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60)
        okButton.pack(side=LEFT)

        cancelButton = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
        cancelButton.pack(side=RIGHT)

        imageFrame = Frame(tab2, relief=GROOVE,height=580)
        imageFrame.pack(side="top",fill=BOTH)

        browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
        browseimg.place(x=15,y=35)

        browsebutton=Button(imageFrame,text = 'Browse')
        browsebutton.place(x=580,y=30,height=30,width=50)
        
        removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
        removeButton.place(x=400,y=450)



      
                      
      enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
      e1=Entry(newselection, width=20).place(x=110, y=10)
      text=Label(newselection, text="Filtered column").place(x=340, y=10)
      e2=Entry(newselection, width=20).place(x=450, y=10)

      ord_edit_protree=ttk.Treeview(newselection, height=27)
      ord_edit_protree["columns"]=["1","2","3", "4","5"]
      ord_edit_protree.column("#0", width=35)
      ord_edit_protree.column("1", width=160)
      ord_edit_protree.column("2", width=160)
      ord_edit_protree.column("3", width=140)
      ord_edit_protree.column("4", width=70)
      ord_edit_protree.column("5", width=70)
      ord_edit_protree.heading("#0",text="")
      ord_edit_protree.heading("1",text="ID/SKU")
      ord_edit_protree.heading("2",text="Product/Service Name")
      ord_edit_protree.heading("3",text="Unit price")
      ord_edit_protree.heading("4",text="Service")
      ord_edit_protree.heading("5",text="Stock")
      ord_edit_protree.place(x=5, y=45)


      ctegorytree=ttk.Treeview(newselection, height=27)
      ctegorytree["columns"]=["1"]
      ctegorytree.column("#0", width=35, minwidth=20)
      ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      ctegorytree.heading("#0",text="", anchor=W)
      ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      ctegorytree.place(x=660, y=45)

      scrollbar = Scrollbar(newselection)
      scrollbar.place(x=640, y=45, height=560)
      scrollbar.config( command=ord_edit_protree.yview )
    

      btn1=Button(newselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
      btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=order_edit_product).place(x=250, y=610)
      btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=order_create_product).place(x=435, y=610)
      btn1=Button(newselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)



    #preview new line
    def order_edit_previewline():
      messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")


    
    #sms notification
    def order_edit_sms1():
      send_SMS=Toplevel()
      send_SMS.geometry("700x480+240+150")
      send_SMS.title("Send SMS notification")

      style = ttk.Style()
      style.theme_use('default')
      style.configure('TNotebook.Tab', background="#999999", padding=5)
      sms_Notebook = ttk.Notebook(send_SMS)
      SMS_Notification = Frame(sms_Notebook, height=470, width=700)
      SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
      sms_Notebook.add(SMS_Notification, text="SMS Notification")
      sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
      sms_Notebook.place(x=0, y=0)

      numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
      numlbel.place(x=10, y=10)
      numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
      stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
      stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
      
      dclbel=Label(SMS_Notification, text="Double click to insert into text")
      dclbel.place(x=410, y=60)
      dcl=Entry(SMS_Notification, width=30)
      dcl.place(x=400, y=85,height=200)
      
      smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
      smstype.place(x=10, y=223)
      snuvar=IntVar()
      normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
      normal_rbtn.place(x=5, y=5)
      unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
      unicode_rbtn.place(x=190, y=5)
      tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
      tiplbf.place(x=10, y=290)
      tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
      tiplabl.place(x=5, y=5)

      btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
      btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
      btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
      

      smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
      smstype.place(x=10, y=5)
      snumvar=IntVar()
      normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
      normal_rbtn.place(x=5, y=5)
      unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
      unicode_rbtn.place(x=290, y=5)

      sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
      sms1type.place(x=10, y=80)
      name=Label(sms1type, text="Username").place(x=10, y=5)
      na=Entry(sms1type, width=20).place(x=100, y=5)
      password=Label(sms1type, text="Password").place(x=10, y=45)
      pas=Entry(sms1type, width=20).place(x=100, y=45)
      combo=Label(sms1type, text="Route").place(x=400, y=5)
      n = StringVar()
      combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
      btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

      
      tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
      tiplbf.place(x=10, y=190)
      tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
      tiplabl.place(x=0, y=5)
      tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
      tiplabl1.place(x=0, y=60)
      tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
      tiplabl2.place(x=0, y=100)
      tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
      tiplabl3.place(x=0, y=140)
      checkvar1=IntVar()
      chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 



    
    #delete line item  
    def order_edit_delete1():
      messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item .")
      
      

    firFrame=Frame(pop, bg="#f5f3f2", height=60)
    firFrame.pack(side="top", fill=X)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    create = Button(firFrame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_custom)
    create.pack(side="left", pady=3, ipadx=4)


    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    add= Button(firFrame,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_newline)
    add.pack(side="left", pady=3, ipadx=4)

    dele= Button(firFrame,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_edit_delete1)
    dele.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    prev= Button(firFrame,compound="top", text="Preview\nOrder",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_edit_previewline)
    prev.pack(side="left", pady=3, ipadx=4)

    prin= Button(firFrame,compound="top", text="Print \nOrder",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_create_printsele)
    prin.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    mail= Button(firFrame,compound="top", text="Email\nOrder",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_email)
    mail.pack(side="left", pady=3, ipadx=4)

    sms1= Button(firFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_edit_sms1)
    sms1.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    calc= Button(firFrame,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
    calc.pack(side="left", pady=3, ipadx=4)

    fir1Frame=Frame(pop, height=180,bg="#f5f3f2")
    fir1Frame.pack(side="top", fill=X)

    labelframe1 = LabelFrame(fir1Frame,text="Customers",font=("arial",15))
    labelframe1.place(x=10,y=5,width=640,height=160)
    order = Label(labelframe1, text="Order to").place(x=10,y=5)
    e1 = ttk.Combobox(labelframe1, value="Hello",width=28).place(x=80,y=5)
    address=Label(labelframe1,text="Address").place(x=10,y=30)
    e2=Text(labelframe1,width=23).place(x=80,y=30,height=70)
    ship=Label(labelframe1,text="Ship to").place(x=342,y=5)
    e3=Entry(labelframe1,width=30).place(x=402,y=3)
    address1=Label(labelframe1,text="Address").place(x=340,y=30)
    e4=Text(labelframe1,width=23).place(x=402,y=30,height=70)

    btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=280, y=50)
    
    labelframe2 = LabelFrame(fir1Frame,text="")
    labelframe2.place(x=10,y=130,width=640,height=42)
    email=Label(labelframe2,text="Email").place(x=10,y=5)
    e5=Entry(labelframe2,width=30).place(x=80,y=5)
    sms=Label(labelframe2,text="SMS Number").place(x=328,y=5)
    e6=Entry(labelframe2,width=30).place(x=402,y=5)
      
    labelframe = LabelFrame(fir1Frame,text="Order",font=("arial",15))
    labelframe.place(x=652,y=5,width=290,height=170)
    order=Label(labelframe,text="Order#").place(x=5,y=5)
    e1=Entry(labelframe,width=25).place(x=100,y=5,)
    orderdate=Label(labelframe,text="Order date").place(x=5,y=33)
    e2=Entry(labelframe,width=20).place(x=150,y=33)
    checkvarStatus5=IntVar()
    duedate=Checkbutton(labelframe,variable = checkvarStatus5,text="Due date",onvalue =0 ,offvalue = 1).place(x=5,y=62)
    e3=Entry(labelframe,width=20).place(x=150,y=62)
    terms=Label(labelframe,text="Terms").place(x=5,y=92)
    e4=ttk.Combobox(labelframe, value="",width=25).place(x=100,y=92)
    ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
    e1=Entry(labelframe,width=27).place(x=100,y=118)

    fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
    fir2Frame.pack(side="top", fill=X)
    listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
    
    edit_pro_tree=ttk.Treeview(listFrame)
    edit_pro_tree["columns"]=["1","2","3","4","5","6","7","8"]

    edit_pro_tree.column("#0", width=40)
    edit_pro_tree.column("1", width=80)
    edit_pro_tree.column("2", width=190)
    edit_pro_tree.column("3", width=190)
    edit_pro_tree.column("4", width=80)
    edit_pro_tree.column("5", width=60)
    edit_pro_tree.column("6", width=60)
    edit_pro_tree.column("7", width=60)
    edit_pro_tree.column("8", width=80)
    
    edit_pro_tree.heading("#0")
    edit_pro_tree.heading("1",text="ID/SKU")
    edit_pro_tree.heading("2",text="Product/Service")
    edit_pro_tree.heading("3",text="Description")
    edit_pro_tree.heading("4",text="Unit Price")
    edit_pro_tree.heading("5",text="Quality")
    edit_pro_tree.heading("6",text="Pcs/Weight")
    edit_pro_tree.heading("7",text="Tax1")
    edit_pro_tree.heading("8",text="Price")
    
    edit_pro_tree.pack(fill="both", expand=1)
    listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    fir3Frame=Frame(pop,height=200,width=700,bg="#f5f3f2")
    fir3Frame.place(x=0,y=490)

    tabStyle = ttk.Style()
    tabStyle.theme_use('default')
    tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
    myNotebook=ttk.Notebook(fir3Frame)
    orderFrame = Frame(myNotebook, height=200, width=800)
    headerFrame = Frame(myNotebook, height=200, width=800)
    commentFrame = Frame(myNotebook, height=200, width=800)
    termsFrame = Frame(myNotebook, height=200, width=800)
    noteFrame = Frame(myNotebook, height=200, width=800)
    documentFrame = Frame(myNotebook, height=200, width=800)
    
    myNotebook.add(orderFrame,compound="left", text="Order")
    myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
    myNotebook.add(commentFrame,compound="left",  text="Comments")
    myNotebook.add(termsFrame,compound="left", text="Terms")
    myNotebook.add(noteFrame,compound="left",  text="Private notes")
    myNotebook.add(documentFrame,compound="left",  text="Documents")
    myNotebook.pack(expand = 1, fill ="both")  

    labelframe1 = LabelFrame(orderFrame,text="",font=("arial",15))
    labelframe1.place(x=1,y=1,width=800,height=170)
    cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
    e1=ttk.Combobox(labelframe1, value="",width=20).place(x=115,y=5)
    rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
    e2=Entry(labelframe1,width=6).place(x=460,y=5)
    cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
    e3=Entry(labelframe1,width=10).place(x=115,y=35)
    tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
    e4=Entry(labelframe1,width=7).place(x=460,y=35)
    template=Label(labelframe1,text="Template").place(x=37,y=70)
    e5=ttk.Combobox(labelframe1, value="",width=25).place(x=115,y=70)
    sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
    e6=Entry(labelframe1,width=18).place(x=115,y=100)
    category=Label(labelframe1,text="Category").place(x=300,y=100)
    e7=Entry(labelframe1,width=22).place(x=370,y=100)
    
    statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
    statusfrme.place(x=540,y=0,width=160,height=160)
    draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
    on1=Label(statusfrme, text="Emailed on:").place( y=50)
    nev1=Label(statusfrme, text="Never").place(x=100,y=50)
    on2=Label(statusfrme, text="Printed on:").place( y=90)
    nev2=Label(statusfrme, text="Never").place(x=100,y=90)

    text1=Label(headerFrame,text="Title text").place(x=50,y=5)
    e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=5)
    text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
    e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=45)
    text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
    e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=85)

    text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
    e1=Text(noteFrame,width=100,height=7).place(x=10,y=32)

    e1=Text(termsFrame,width=100,height=9).place(x=10,y=10)

    e1=Text(commentFrame,width=100,height=9).place(x=10,y=10)

    btn1=Button(documentFrame,height=2,width=3,text="+").place(x=5,y=10)
    btn2=Button(documentFrame,height=2,width=3,text="-").place(x=5,y=50)
    text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
    ord_edit_doc_tree=ttk.Treeview(documentFrame, height=5)
    ord_edit_doc_tree["columns"]=["1","2","3"]
    ord_edit_doc_tree.column("#0", width=20)
    ord_edit_doc_tree.column("1", width=250)
    ord_edit_doc_tree.column("2", width=250)
    ord_edit_doc_tree.column("2", width=200)
    ord_edit_doc_tree.heading("#0",text="", anchor=W)
    ord_edit_doc_tree.heading("1",text="Attach to Email")
    ord_edit_doc_tree.heading("2",text="Filename")
    ord_edit_doc_tree.heading("3",text="Filesize")  
    ord_edit_doc_tree.place(x=50, y=45)
    

    fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
    fir4Frame.place(x=740,y=520)
    summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
    summaryfrme.place(x=0,y=0,width=200,height=170)
    discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
    discount1=Label(summaryfrme, text="$0.00").place(x=130 ,y=0)
    sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
    sub1=Label(summaryfrme, text="$0.00").place(x=130 ,y=21)
    tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
    tax1=Label(summaryfrme, text="$0.00").place(x=130 ,y=42)
    cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
    cost=Label(summaryfrme, text="$0.00").place(x=130 ,y=63)
    order=Label(summaryfrme, text="Order total").place(x=0 ,y=84)
    order1=Label(summaryfrme, text="$0.00").place(x=130 ,y=84)
    total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
    total1=Label(summaryfrme, text="$0.00").place(x=130 ,y=105)
    balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
    balance1=Label(summaryfrme, text="$0.00").place(x=130 ,y=126)

    fir5Frame=Frame(pop,height=38,width=210)
    fir5Frame.place(x=735,y=485)
    btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
    btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)

  ### End View or Edit Order ###

  
  #printselected order
    
  def order_create_printsele():

    def property1():
      propert=Toplevel()
      propert.title("Microsoft Print To PDF Advanced Document Settings")
      propert.geometry("670x500+240+150")

      def property2():
        propert1=Toplevel()
        propert1.title("Microsoft Print To PDF Advanced Document Settings")
        propert1.geometry("670x500+240+150")

        name=Label(propert1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
        paper=Label(propert1, text="Paper/Output").place(x=30, y=35)
        size=Label(propert1, text="Paper size").place(x=55, y=65)
        n = StringVar()
        search = ttk.Combobox(propert1, width = 15, textvariable = n )
        search['values'] = ('letter')
        search.place(x=150,y=65)
        search.current(0)
        copy=Label(propert1, text="Copy count:").place(x=55, y=95)

        okbtn=Button(propert1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=450)
        canbtn=Button(propert1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=450)
        
        


      style = ttk.Style()
      style.theme_use('default')
      style.configure('TNotebook.Tab', background="#999999", padding=5)
      property_Notebook = ttk.Notebook(propert)
      property_Frame = Frame(property_Notebook, height=500, width=670)
      property_Notebook.add(property_Frame, text="Layout")
      property_Notebook.place(x=0, y=0)

      name=Label(property_Frame, text="Orientation:").place(x=10, y=5)
      n = StringVar()
      search = ttk.Combobox(property_Frame, width = 23, textvariable = n )
      search['values'] = ('Portrait')
      search.place(x=10,y=25)
      search.current(0)

      text=Text(property_Frame,width=50).place(x=250, y=5,height=350)

      btn=Button(property_Frame, text="Advanced",command=property2).place(x=550, y=380)
      btn=Button(property_Frame,compound = LEFT,image=tick  ,text="OK", width=60,).place(x=430, y=420)
      btn=Button(property_Frame,compound = LEFT,image=cancel , text="Cancel", width=60,).place(x=550, y=420)     


      
    if(False):
        messagebox.showwarning("FBilling Revelution 2020", "Customer is required, Please select customer for this invoice\nbefore printing")
    elif(False):
        messagebox.showinfo("FBilling Revelution 2020", "Print job has been completed.")
    else:
        print1=Toplevel()
        print1.title("Print")
        print1.geometry("670x400+240+150")
        
        printerframe=LabelFrame(print1, text="Printer", height=80, width=650)
        printerframe.place(x=7, y=5)      
        name=Label(printerframe, text="Name:").place(x=10, y=5)
        e1= ttk.Combobox(printerframe, width=40).place(x=70, y=5)
        where=Label(printerframe, text="Where:").place(x=10, y=30)
        printocheckvar=IntVar()
        printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
        printochkbtn.place(x=450, y=30)
        btn=Button(printerframe, text="Properties", width=10,command=property1).place(x=540, y=5)

        pageslblframe=LabelFrame(print1, text="Pages", height=140, width=320)
        pageslblframe.place(x=10, y=90)
        radvar=IntVar()
        radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
        radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
        radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
        pagecountentry = Entry(pageslblframe, width=23).place(x=80, y=47)
        pageinfolabl=Label(pageslblframe, text="Enter page numbers and/or page ranges\nseperated by commas. For example:1,3,5-12")
        pageinfolabl.place(x=5, y=75)

        copylblframe=LabelFrame(print1, text="Copies", height=140, width=320)
        copylblframe.place(x=335, y=90)
        nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
        noentry = Entry(copylblframe, width=18).place(x=130, y=5)      
        one=Frame(copylblframe, width=30, height=40, bg="black").place(x=20, y=40)     
        two=Frame(copylblframe, width=30, height=40, bg="grey").place(x=15, y=45)     
        three=Frame(copylblframe, width=30, height=40, bg="white").place(x=10, y=50)      
        four=Frame(copylblframe, width=30, height=40, bg="black").place(x=80, y=40)      
        fiv=Frame(copylblframe, width=30, height=40, bg="grey").place(x=75, y=45)      
        six=Frame(copylblframe, width=30, height=40, bg="white").place(x=70, y=50)      
        collatecheckvar=IntVar()
        collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
        collatechkbtn.place(x=130, y=70)

        othrlblframe=LabelFrame(print1, text="Other", height=120, width=320)
        othrlblframe.place(x=10, y=235)
        printlb=Label(othrlblframe, text="Print").place(x=5, y=0)
        dropprint = ttk.Combobox(othrlblframe, width=23).place(x=80, y=0)
        orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
        dropord = ttk.Combobox(othrlblframe, width=23).place(x=80, y=25)
        duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)
        droplex = ttk.Combobox(othrlblframe, width=23).place(x=80, y=50)

        prmodelblframe=LabelFrame(print1, text="Print mode", height=120, width=320)
        prmodelblframe.place(x=335, y=235)
        dropscal = ttk.Combobox(prmodelblframe, width=30).place(x=5, y=5)
        poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=35)
        droppos = ttk.Combobox(prmodelblframe, width=10).place(x=155, y=35)

        okbtn=Button(print1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=370)
        canbtn=Button(print1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=370)
        


  #email
        
  def order_email():
    mailDetail=Toplevel()
    mailDetail.title("Invoice E-Mail")
    mailDetail.geometry("1080x550")
    mailDetail.resizable(False, False)
    def my_SMTP():
        if True:
            em_ser_conbtn.destroy()
            mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
            mysmtpservercon.place(x=610, y=110)
            lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
            hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
            lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
            portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
            lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
            unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
            lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
            pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
            ssl_chkvar=IntVar()
            ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
            ssl_chkbtn.place(x=50, y=110)
            em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
        else:
            pass
      
    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    email_Notebook = ttk.Notebook(mailDetail)
    email_Frame = Frame(email_Notebook, height=500, width=1080)
    account_Frame = Frame(email_Notebook, height=550, width=1080)
    email_Notebook.add(email_Frame, text="E-mail")
    email_Notebook.add(account_Frame, text="Account")
    email_Notebook.place(x=0, y=0)

    messagelbframe=LabelFrame(email_Frame,text="Message", height=500, width=730)
    messagelbframe.place(x=5, y=5)
    lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
    emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
    sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1,command="").place(x=600, y=10)
    lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
    carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
    stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
    lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
    subent=Entry(messagelbframe, width=50).place(x=120, y=59)

    
    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
    mess_Notebook = ttk.Notebook(messagelbframe)
    emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
    htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
    mess_Notebook.add(emailmessage_Frame, text="E-mail message")
    mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
    mess_Notebook.place(x=5, y=90)

    btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

    
    btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
    btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
    btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
    btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
    btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
    btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
    btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
    btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
    btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
    btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
    btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
    btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
    
    btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)


    dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
    dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
    mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
    mframe.place(x=0, y=28)



    btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

    
    btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
    btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
    btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
    mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
    mframe.place(x=0, y=28)

    attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
    attachlbframe.place(x=740, y=5)
    htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
    lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
    btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
    btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
    lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
    lbl_tt_info.place(x=740, y=370)

    ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
    
    sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
    sendatalbframe.place(x=5, y=5)
    lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
    sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
    lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
    nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
    lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
    replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
    lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
    signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
    confirm_chkvar=IntVar()
    confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
    confirm_chkbtn.place(x=200, y=215)
    btn18=Button(account_Frame, width=15, text="Save settings",command="").place(x=25, y=285)

    sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
    sendatalbframe.place(x=610, y=5)
    servar=IntVar()
    SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
    SMTP_rbtn.place(x=10, y=10)
    MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=my_SMTP)
    MySMTP_rbtn.place(x=10, y=40)
    em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
    em_ser_conbtn.place(x=710, y=110)




  #sms notification order
    
  def order_sms():
    send_SMS=Toplevel()
    send_SMS.geometry("700x480+240+150")
    send_SMS.title("Send SMS notification")

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    sms_Notebook = ttk.Notebook(send_SMS)
    SMS_Notification = Frame(sms_Notebook, height=470, width=700)
    SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
    sms_Notebook.add(SMS_Notification, text="SMS Notification")
    sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
    sms_Notebook.place(x=0, y=0)

    numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
    numlbel.place(x=10, y=10)
    numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
    stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
    stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
    
    dclbel=Label(SMS_Notification, text="Double click to insert into text")
    dclbel.place(x=410, y=60)
    dcl=Entry(SMS_Notification, width=30)
    dcl.place(x=400, y=85,height=200)
    
    smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
    smstype.place(x=10, y=223)
    snuvar=IntVar()
    normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
    unicode_rbtn.place(x=190, y=5)
    tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
    tiplbf.place(x=10, y=290)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
    tiplabl.place(x=5, y=5)

    btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
    btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
    btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
    

    smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
    smstype.place(x=10, y=5)
    snumvar=IntVar()
    normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
    unicode_rbtn.place(x=290, y=5)

    sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
    sms1type.place(x=10, y=80)
    name=Label(sms1type, text="Username").place(x=10, y=5)
    na=Entry(sms1type, width=20).place(x=100, y=5)
    password=Label(sms1type, text="Password").place(x=10, y=45)
    pas=Entry(sms1type, width=20).place(x=100, y=45)
    combo=Label(sms1type, text="Route").place(x=400, y=5)
    n = StringVar()
    combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
    btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

    
    tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
    tiplbf.place(x=10, y=190)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
    tiplabl.place(x=0, y=5)
    tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
    tiplabl1.place(x=0, y=60)
    tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
    tiplabl2.place(x=0, y=100)
    tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
    tiplabl3.place(x=0, y=140)
    checkvar1=IntVar()
    chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200)  



  #print preview order
  def order_printpreview():
    messagebox.showerror("F-Billing Revolution","Customer is required,please select customer for this order before printing.")



  #convert to invoice
  def order_convert():
    if messagebox.askyesno("Make invoice from Orders", "Are you sure to make invoice from this Orders ") == True:
          messagebox.askyesno("Make invoice from Estimate", "Invoice Creation was Successfull.\n New Invoice is \n Would you like to open this invoice ")
    else:
        messagebox.destroy()
    

  #delete orders  
  def order_delete():  
    messagebox.askyesno("Delete order", "Are you sure to delete this order? All products will be placed back into stock")




  #search in orders  
  def order_search():  
      top = Toplevel()     
      top.title("Find Text")   
      top.geometry("600x250+390+250")
      findwhat1=Label(top,text="Find What:",pady=5,padx=10).place(x=5,y=20)
      n = StringVar()
      findwhat = ttk.Combobox(top, width = 40, textvariable = n ).place(x=90,y=25)
    
      findin1=Label(top,text="Find in:",pady=5,padx=10).place(x=5,y=47)
      n = StringVar()
      findIN = ttk.Combobox(top, width = 30, textvariable = n )
      findIN['values'] = ('Product/Service id', ' Category', ' Active',' name',' stock',' location', ' image',' <<All>>')                       
      findIN.place(x=90,y=54)
      findIN.current(0)

      findButton = Button(top, text ="Find next",width=10).place(x=480,y=22)
      closeButton = Button(top,text ="Close",width=10).place(x=480,y=52)
      
      match1=Label(top,text="Match:",pady=5,padx=10).place(x=5,y=74)
      n = StringVar()
      match = ttk.Combobox(top, width = 23, textvariable = n )   
      match['values'] = ('From Any part',' Whole Field',' From the beginning of the field')                                   
      match.place(x=90,y=83)
      match.current(0)

      search1=Label(top,text="Search:",pady=5,padx=10).place(x=5,y=102)
      n = StringVar()
      search = ttk.Combobox(top, width = 23, textvariable = n )
      search['values'] = ('All', 'up',' Down')
      search.place(x=90,y=112)
      search.current(0)
      checkvarStatus4=IntVar()  
      Button4 = Checkbutton(top,variable = checkvarStatus4,text="Match Case",onvalue =0 ,offvalue = 1,height=3,width = 15)
      Button4.place(x=90,y=141)
      checkvarStatus5=IntVar()   
      Button5 = Checkbutton(top,variable = checkvarStatus5,text="Match Format",onvalue =0 ,offvalue = 1,height=3,width = 15)
      Button5.place(x=300,y=141)





  order_mainFrame=Frame(tab2, relief=GROOVE, bg="#f8f8f2")
  order_mainFrame.pack(side="top", fill=BOTH)

  order_midFrame=Frame(order_mainFrame, bg="#f5f3f2", height=60)
  order_midFrame.pack(side="top", fill=X)

  w = Canvas(order_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=(5, 2))
  w = Canvas(order_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=(0, 5))

  invoiceLabel = Button(order_midFrame,compound="top", text="Create new\nOrder",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=order_create)
  invoiceLabel.pack(side="left", pady=3, ipadx=4)

  orderLabel = Button(order_midFrame,compound="top", text="View/Edit\nOrders",relief=RAISED, image=photo1,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=order_edit)
  orderLabel.pack(side="left")

  estimateLabel = Button(order_midFrame,compound="top", text="Delete\nSelected",relief=RAISED, image=photo2,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=order_delete)
  estimateLabel.pack(side="left")

  w = Canvas(order_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  recurLabel = Button(order_midFrame,compound="top", text="Convert to\nInvoice",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=order_convert)
  recurLabel.pack(side="left")

  w = Canvas(order_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  previewLabel = Button(order_midFrame,compound="top", text="Print\nPreview",relief=RAISED, image=photo4,bg="#f8f8f2", fg="black", height=55, bd=1, width=55, activebackground="red",command=order_printpreview)
  previewLabel.pack(side="left")

  purchaseLabel = Button(order_midFrame,compound="top", text="Print\nSelected",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=order_create_printsele)#temperay
  purchaseLabel.pack(side="left")

  w = Canvas(order_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  expenseLabel = Button(order_midFrame,compound="top", text=" E-mail \nOrder",relief=RAISED, image=photo6,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=order_email)
  expenseLabel.pack(side="left")

  smsLabel = Button(order_midFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=order_sms)
  smsLabel.pack(side="left")

  w = Canvas(order_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  productLabel = Button(order_midFrame,compound="top", text="Search\nOrders",relief=RAISED, image=photo7,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=order_search)
  productLabel.pack(side="left")

  lbframe = LabelFrame(order_midFrame, height=60, width=200, bg="#f8f8f2")
  lbframe.pack(side="left", padx=10, pady=0)
  lbl_invdt = Label(lbframe, text="Order date from : ", bg="#f8f8f2")
  lbl_invdt.grid(row=0, column=0, pady=5, padx=(5, 0))
  lbl_invdtt = Label(lbframe, text="Order date to  :  ", bg="#f8f8f2")
  lbl_invdtt.grid(row=1, column=0, pady=5, padx=(5, 0))
  invdt = Entry(lbframe, width=15)
  invdt.grid(row=0, column=1)
  invdtt = Entry(lbframe, width=15)
  invdtt.grid(row=1, column=1)
  checkvar1 = IntVar()
  chkbtn1 = Checkbutton(lbframe, text = "Apply filter", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2")
  chkbtn1.grid(row=0, column=2, rowspan=2, padx=(5,5))

  productLabel = Button(order_midFrame,compound="top", text="Refresh\nOrders list",relief=RAISED, image=photo8,fg="black", height=55, bd=1, width=55)
  productLabel.pack(side="left")

  w = Canvas(order_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  productLabel = Button(order_midFrame,compound="top", text="Hide totals\nSum",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  productLabel.pack(side="left")

  invoilabel = Label(order_mainFrame, text="Orders(All)", font=("arial", 18), bg="#f8f8f2")
  invoilabel.pack(side="left", padx=(20,0))
  drop = ttk.Combobox(order_mainFrame, value="Hello")
  drop.pack(side="right", padx=(0,10))
  invoilabel = Label(order_mainFrame, text="Category filter", font=("arial", 15), bg="#f8f8f2")
  invoilabel.pack(side="right", padx=(0,10))
  
  #_________(Prdouct,Private_notes,Documents)_________#
  def view_details(event):
    for record in ord_pro_tree.get_children():
       ord_pro_tree.delete(record)
    orderitemnumber = ordtree.item(ordtree.focus())["values"][1]
    sql = 'select * from storingproduct where order_number = %s'
    val = (orderitemnumber,)
    fbcursor.execute(sql,val)
    storingpro = fbcursor.fetchall()
    sql = 'select * from company'
    fbcursor.execute(sql)
    check_pro_tax = fbcursor.fetchone()
    counto = 0
    if not check_pro_tax:
      for i in storingpro:
        ord_pro_tree.insert(parent='', index='end',text='', values=('',i[1],i[6],i[7],i[8],i[9],i[13]))
        counto +=1
    elif check_pro_tax[12] == '1':
      for i in storingpro:
        ord_pro_tree.insert(parent='', index='end',text='', values=('',i[1],i[6],i[7],i[8],i[9],i[13]))
        counto +=1
    elif check_pro_tax[12] == '2':
      for i in storingpro:
        ord_pro_tree.insert(parent='', index='end',text='', values=('',i[1],i[6],i[7],i[8],i[9],i[11],i[13]))
        counto +=1
    elif check_pro_tax[12] == '3':
      for i in storingpro:
        ord_pro_tree.insert(parent='', index='end',text='', values=('',i[1],i[6],i[7],i[8],i[9],i[11],i[12],i[13]))
        counto +=1
    

    #____Private note disply man tree_____#
    sql = 'select private_notes from orders where order_number = %s'
    val = (orderitemnumber,)
    fbcursor.execute(sql,val)
    privatenotes = fbcursor.fetchone()
    ord_private_note1.delete('1.0',END)
    ord_private_note1.insert('1.0',privatenotes[0])
    
    #___Documents_____#
    for record in ord_doc_tree.get_children():
       ord_doc_tree.delete(record)
    sql = 'select * from documents where order_number = %s'
    val = (orderitemnumber,)
    fbcursor.execute(sql,val)
    docu = fbcursor.fetchall()
    countd = 0
    for i in docu:
      file_size = check_convertion(os.path.getsize('images'+i[6]))
      ord_doc_tree.insert(parent='', index='end',text='', values=('',i[6],file_size))
      countd += 1
      def check_convertion(B):
        BYTE = float(B)
        KB = float(1024)
        MB = float(KB**2)
        if BYTE < KB:
          return '{0} {1}'.format(BYTE,'Bytes' if 0 == B > 1 else 'Byte')
        elif KB <= BYTE < MB:
          return '{0:.2f} KB'.format(BYTE / KB)
        elif MB <= BYTE:
          return '{0:.2f} MB'.format(BYTE / MB)
    



  class MyApp:
    def __init__(self, parent):
      
      self.myParent = parent 

      self.myContainer1 = Frame(parent) 
      self.myContainer1.pack()
      
      self.top_frame = Frame(self.myContainer1) 
      self.top_frame.pack(side=TOP,
        fill=BOTH, 
        expand=YES,
        )  

      self.left_frame = Frame(self.top_frame, background="white",
        borderwidth=5,  relief=RIDGE,
        height=250, 
        width=2000, 
        )
      self.left_frame.pack(side=LEFT,
        fill=BOTH, 
        expand=YES,
        )

      global ordtree
      ordtree = ttk.Treeview(self.left_frame, columns = (1,2,3,4,5,6,7,8,9,10), height = 15, show = "headings")
      ordtree.pack(side = 'top')
      ordtree.heading(1)
      ordtree.heading(2, text="Order#")
      ordtree.heading(3, text="Order date")
      ordtree.heading(4, text="Due date")
      ordtree.heading(5, text="Customer Name")
      ordtree.heading(6, text="Status")
      ordtree.heading(7, text="Emailed on")
      ordtree.heading(8, text="Printed on")
      ordtree.heading(9, text="SMS on")
      ordtree.heading(10, text="Order Total")   
      ordtree.column(1, width = 50)
      ordtree.column(2, width = 140)
      ordtree.column(3, width = 140)
      ordtree.column(4, width = 140)
      ordtree.column(5, width = 210)
      ordtree.column(6, width = 130)
      ordtree.column(7, width = 150)
      ordtree.column(8, width = 130)
      ordtree.column(9, width = 130)
      ordtree.column(10, width = 130)
      ordtree.bind('<ButtonRelease-1>',view_details)
      fbcursor.execute('SELECT * FROM Orders;')
      counto = 0
      for i in fbcursor:
        ordtree.insert(parent='', index='end', iid=counto, text='', values=(' ',i[31], i[1], i[2], i[3], i[4],i[5], i[6], i[7], i[8], i[9], i[10]))
        counto += 1





      scrollbar = Scrollbar(self.left_frame)
      scrollbar.place(x=990+300+50, y=0, height=300+20)
      scrollbar.config( command=ordtree.yview )

      tabControl = ttk.Notebook(self.left_frame,width=1)
      tab1 = ttk.Frame(tabControl)
      tab2 = ttk.Frame(tabControl)
      tab3=  ttk.Frame(tabControl)
      tab4 = ttk.Frame(tabControl)
      tabControl.add(tab1,image=invoices,compound = LEFT, text ='Order Items',)
      tabControl.add(tab2,image=orders,compound = LEFT, text ='Private Notes')
      tabControl.add(tab3,image=estimates,compound = LEFT, text ='SMS Log')
      tabControl.add(tab4,image=estimates,compound = LEFT, text ='Documents')
      tabControl.pack(expand = 1, fill ="both")
      
      global ord_pro_tree
      sql = 'select * from company'
      fbcursor.execute(sql)
      check_pro_tax = fbcursor.fetchone()
      if not check_pro_tax:
        ord_pro_tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7), height = 15, show = "headings")
        ord_pro_tree.pack(side = 'top')
        ord_pro_tree.heading(1)
        ord_pro_tree.heading(2, text="Product/Service ID",)
        ord_pro_tree.heading(3, text="Name")
        ord_pro_tree.heading(4, text="Description")
        ord_pro_tree.heading(5, text="Price")
        ord_pro_tree.heading(6, text="QTY")
        ord_pro_tree.heading(8, text="Line Total")   
        ord_pro_tree.column(1, width = 50)
        ord_pro_tree.column(2, width = 270)
        ord_pro_tree.column(3, width = 270)
        ord_pro_tree.column(4, width = 300)
        ord_pro_tree.column(5, width = 130)
        ord_pro_tree.column(6, width = 100)
        ord_pro_tree.column(7, width = 100)
      elif check_pro_tax[12] == '1':
        ord_pro_tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7), height = 15, show = "headings")
        ord_pro_tree.pack(side = 'top')
        ord_pro_tree.heading(1)
        ord_pro_tree.heading(2, text="Product/Service ID",)
        ord_pro_tree.heading(3, text="Name")
        ord_pro_tree.heading(4, text="Description")
        ord_pro_tree.heading(5, text="Price")
        ord_pro_tree.heading(6, text="QTY")
        ord_pro_tree.heading(7, text="Line Total")   
        ord_pro_tree.column(1, width = 10)
        ord_pro_tree.column(2, width = 310)
        ord_pro_tree.column(3, width = 310)
        ord_pro_tree.column(4, width = 300)
        ord_pro_tree.column(5, width = 170)
        ord_pro_tree.column(6, width = 120)
        ord_pro_tree.column(7, width = 115)
      elif check_pro_tax[12] == '2':
        ord_pro_tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8,), height = 15, show = "headings")
        ord_pro_tree.pack(side = 'top')
        ord_pro_tree.heading(1)
        ord_pro_tree.heading(2, text="Product/Service ID",)
        ord_pro_tree.heading(3, text="Name")
        ord_pro_tree.heading(4, text="Description")
        ord_pro_tree.heading(5, text="Price")
        ord_pro_tree.heading(6, text="QTY")
        ord_pro_tree.heading(7, text="Tax1")
        ord_pro_tree.heading(8, text="Line Total")   
        ord_pro_tree.column(1, width = 10)
        ord_pro_tree.column(2, width = 270)
        ord_pro_tree.column(3, width = 270)
        ord_pro_tree.column(4, width = 300)
        ord_pro_tree.column(5, width = 130)
        ord_pro_tree.column(6, width = 100)
        ord_pro_tree.column(7, width = 100)
        ord_pro_tree.column(8, width = 150)
      elif check_pro_tax[12] == '3':
        ord_pro_tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8,9), height = 15, show = "headings")
        ord_pro_tree.pack(side = 'top')
        ord_pro_tree.heading(1)
        ord_pro_tree.heading(2, text="Product/Service ID",)
        ord_pro_tree.heading(3, text="Name")
        ord_pro_tree.heading(4, text="Description")
        ord_pro_tree.heading(5, text="Price")
        ord_pro_tree.heading(6, text="QTY")
        ord_pro_tree.heading(7, text="Tax1")
        ord_pro_tree.heading(8, text="Tax2")
        ord_pro_tree.heading(9, text="Line Total")   
        ord_pro_tree.column(1, width = 10)
        ord_pro_tree.column(2, width = 270)
        ord_pro_tree.column(3, width = 270)
        ord_pro_tree.column(4, width = 200)
        ord_pro_tree.column(5, width = 130)
        ord_pro_tree.column(6, width = 100)
        ord_pro_tree.column(7, width = 100)
        ord_pro_tree.column(8, width = 100)
        ord_pro_tree.column(9, width = 150)
      
      
      global ord_private_note1
      ord_private_note1=Text(tab2, width=220,height=10)
      ord_private_note1.place(x=10, y=10)

      note1=Text(tab3, width=2200,height=10).place(x=10, y=10)

      global ord_doc_tree
      ord_doc_tree = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
      ord_doc_tree.pack(side = 'top')
      ord_doc_tree.heading(1)
      ord_doc_tree.heading(2, text="Filename",)
      ord_doc_tree.heading(3, text="Filename Size")
      ord_doc_tree.column(1, width = 50)
      ord_doc_tree.column(2, width = 1000)
      ord_doc_tree.column(3, width = 290)

      scrollbar = Scrollbar(self.left_frame)
      scrollbar.place(x=990+300+50, y=360, height=190)
      scrollbar.config( command=ord_doc_tree.yview )
        
  myapp = MyApp(tab2)

######################## FRONT PAGE OF Settings module  #######################################################################
  
      
  settingsframe=Frame(tab10, relief=GROOVE, bg="#f8f8f2")
  settingsframe.pack(side="top", fill=BOTH)
  
  settframe=Frame(settingsframe, bg="#f5f3f2", height=60)
  settframe.pack(side="top", fill=X)
  
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(5, 2))
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  # def upload_filelogo():
  #   global imglogo,filename
  #   f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
  #   filena = filedialog.askopenfilename(filetypes=f_types)
  #   shutil.copyfile(filena, os.getcwd()+'/images/'+filena.split('/')[-1])
  #   print(filena.split('/')[-1])
  #   image = Image.open(filena)
  #   resize_image = image.resize((280, 160))
  #   imglogo = ImageTk.PhotoImage(resize_image)
    # b2 = Button(secondtab,image=img)
    # b2.place(x=130, y=80)
  
    # btlogo = Button(secondtab,width=280,height=160,image=imglogo)
    # btlogo.place(x=580,y=280)
  global filename
  filename = ""
  def save_company():
    company_name = comname.get()
    company_address = caddent.get(1.0,END)
    company_mail = comemail.get()
    company_salestax =comsalestax.get()
    currency = comcur.get()
    currencysign = comcursign.get()
    currencysign_placement = comcursignpla.get()
    decimal_sepator = comdecsep.get()
    currency_example = comex.get()
    date_format = comdaf.get()
    example_dateformat = exd.get_date()
    tax = radtax.get()
    tax1name = tax1namee.get()
    tax1rate = tax1ratee.get()
    printtax1 = comptax1.get()
    tax2name = tax2namee.get()
    tax2rate = tax2ratee.get()
    printtax2 = comptax2.get()
    printimage = compimg.get()
    win_menu_colour = win_menu.get()
    radiobut = radema.get()
    cbut1 = checkb1.get()
    cbut2 = checkb2.get()
    cbut3 = checkb3.get()
    cbut4 = checkb4.get()
    cbut5 = checkb5.get()
    cbut6 = checkb6.get()
    child = exctree.get_children()
    var = json.dumps(child)
    sql = "select image from company"
    fbcursor.execute(sql)
    im = fbcursor.fetchone()
    sql = "select * from company"
    fbcursor.execute(sql)
    i = fbcursor.fetchall()
    if not i:
      if filename == "":
        print(12)
        sql = 'insert into company(name, address, email,salestaxno,currency,currencysign,currsignplace,  decimalseperator,excurrency,dateformat,exdate,taxtype,printimageornot,tax1name,tax1rate,printtax1,  tax2name,tax2rate,printtax2,attachment_file_type,miscellanoustab_cbutton1,miscellanoustab_cbutton2,miscellanoustab_cbutton3,miscellanoustab_cbutton4,miscellanoustab_cbutton5,miscellanoustab_cbutton6) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        sql = 'insert into company(name, address, email,salestaxno,currency,currencysign,currsignplace,  decimalseperator,excurrency,dateformat,exdate,taxtype,printimageornot,tax1name,tax1rate,printtax1,  tax2name,tax2rate,printtax2,image,attachment_file_type,miscellanoustab_cbutton1,miscellanoustab_cbutton2,miscellanoustab_cbutton3,miscellanoustab_cbutton4,miscellanoustab_cbutton5,miscellanoustab_cbutton6) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,filename.split('/')[-1],radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6)
        fbcursor.execute(sql, val)
        fbilldb.commit()
    else:
      if filename == "":
        sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,currency=%s,currencysign=%s,  currsignplace=%s,decimalseperator=%s,excurrency=%s,dateformat=%s,exdate=%s,taxtype=%s,  printimageornot=%s,tax1name=%s,tax1rate=%s,printtax1=%s,tax2name=%s,tax2rate=%s,printtax2=%s,attachment_file_type=%s,miscellanoustab_cbutton1=%s,miscellanoustab_cbutton2=%s,miscellanoustab_cbutton3=%s,miscellanoustab_cbutton4=%s,miscellanoustab_cbutton5=%s,miscellanoustab_cbutton6=%s"
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,currency=%s,currencysign=%s,  currsignplace=%s,decimalseperator=%s,excurrency=%s,dateformat=%s,exdate=%s,taxtype=%s,  printimageornot=%s,tax1name=%s,tax1rate=%s,printtax1=%s,tax2name=%s,tax2rate=%s,printtax2=%s,image=%s,attachment_file_type=%s,miscellanoustab_cbutton1=%s,miscellanoustab_cbutton2=%s,miscellanoustab_cbutton3=%s,miscellanoustab_cbutton4=%s,miscellanoustab_cbutton5=%s,miscellanoustab_cbutton6=%s"
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,filename.split('/')[-1],radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      
      
  
  
  save_setting = Button(settframe,compound="top", text="Save\nSettings",relief=RAISED,    command=save_company, image=saves, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  save_setting.pack(side="left", pady=3, ipadx=4)
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  
  def wiz_page():
    global filname
    filname = ""
    def upload_cfilelogo():
      global filname
      f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
      filname = filedialog.askopenfilename(filetypes=f_types)
      shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
      image = Image.open(filname)
      resize_image = image.resize((280, 140))
      imgclogo = ImageTk.PhotoImage(resize_image)
      btclogo = Button(wiz,width=280,height=140,image=imgclogo)
      btclogo.place(x=30,y=240)
      btclogo.photo = imgclogo
    def csave():
      company_name = company_namee.get()
      company_address = company_addresse.get('1.0', 'end-1c')
      company_email = company_emaile.get()
      salestaxregno = salestaxregnoe.get()
      cprint_logopic = cplogopic.get()
      sql = "select image from company"
      fbcursor.execute(sql)
      im = fbcursor.fetchone()
      sql = "select * from company"
      fbcursor.execute(sql)
      i = fbcursor.fetchall()
      if not i:
        if filname == "":
          sql = 'insert into company(name, address, email,salestaxno,printimageornot) values(%s, %s, %s, %s, %s)'
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic)
          fbcursor.execute(sql, val)
          fbilldb.commit()
        else:
          shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
          sql = 'insert into company(name, address, email,salestaxno,printimageornot,image) values(%s, %s, %s, %s, %s, %s)'
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic,filname.split('/')[-1],)
          fbcursor.execute(sql, val)
          fbilldb.commit()
      else:
        if filname == "":
          sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,printimageornot=%s"
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic)
          fbcursor.execute(sql, val)
          fbilldb.commit()
        else:
          shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
          sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,printimageornot=%s,image=%s"
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic,filname.split('/')[-1])
          fbcursor.execute(sql, val)
          fbilldb.commit()
      centry.delete(0, END)
      centry.insert(0, company_name)
      caddent.delete('1.0', END)
      caddent.insert('1.0', company_address)
      cemailentry.delete(0, END)
      cemailentry.insert(0, company_email)
      ste.delete(0, END)
      ste.insert(0, salestaxregno)
      if cprint_logopic == 1:
        primage.select()
      else:
        primage.deselect()
      try:
        image = Image.open("images/"+filname.split('/')[-1])
        resize_image = image.resize((280, 160))
        image = ImageTk.PhotoImage(resize_image)
        btlogo = Button(secondtab,width=280,height=160,image=image)
        btlogo.place(x=580,y=280)
        btlogo.photo = image
      except:
        pass
      wiz.destroy()


      
      

    
    wiz = Toplevel()
    wiz.geometry("500x449+400+167")
    wiz.title("Wellcome to Quick Start Wizard")
    sql = "select * from company"
    fbcursor.execute(sql)
    secctab = fbcursor.fetchone()
    comp_infor = Label(wiz,text="Enter Your Company Information",font='arial 13 bold',fg="blue")
    comp_infor.place(x=15,y=15)
    company_da_laframe = LabelFrame(wiz,text="Company data",height=180, width=460)
    company_da_laframe.place(x=15,y=40)
    company_name = Label(wiz,text="Company name")
    company_name.place(x=30,y=60)
    company_namee = Entry(wiz,width=50)
    company_namee.place(x=160,y=60)
    if  not secctab:
      pass
    else:
      company_namee.insert(0, secctab[1])
  
    company_address = Label(wiz,text="Company address")
    company_address.place(x=30,y=90)
    company_addresse = scrolledtext.ScrolledText(wiz,)
    company_addresse.place(x=160,y=90,width=250,height=60)
    if  not secctab:
      pass
    else:
      company_addresse.insert('1.0', secctab[2])

    company_email = Label(wiz,text="Email address")
    company_email.place(x=30,y=160)
    company_emaile = Entry(wiz,width=50)
    company_emaile.place(x=160,y=160)
    if  not secctab:
      pass
    else:
      company_emaile.insert(0, secctab[3])

    salestaxregno = Label(wiz,text="Sales Tax.Reg.No")
    salestaxregno.place(x=30,y=190)
    salestaxregnoe = Entry(wiz,width=50)
    salestaxregnoe.place(x=160,y=190)
    if  not secctab:
      pass
    else:
      salestaxregnoe.insert(0, secctab[4])
    
    
    company_da_laframe = LabelFrame(wiz,text="Company logo",height=190, width=460)
    company_da_laframe.place(x=15,y=220)
    try:
      image_wiz = Image.open("images/"+secctab[13])
      resize_image = image_wiz.resize((280, 140))
      image_wiza = ImageTk.PhotoImage(resize_image)
      btclogo = Button(wiz,width=280,height=140,image=image_wiza)
      btclogo.place(x=30,y=240)
      btclogo.photo = image_wiza
    except:
      pass
    cplogopic = BooleanVar()
    cprint_logopic = Checkbutton(wiz,text='Print logo picture',bg='white',onvalue =1,
                        offvalue = 0,variable=cplogopic)
    cprint_logopic.place(x=320,y=250)
    if  not secctab:
      pass
    else:
      if secctab[14] == 1:
        cprint_logopic.select()
      else:
        cprint_logopic.deselect()
      
    load_img = Button(wiz,text='Load logo image',command=upload_cfilelogo)
    load_img.place(x=320,y=360)
    save_com_wiz = Button(wiz,text='Save',width=10,command=csave)
    save_com_wiz.place(x=370,y=415)

  quick_start_wiz = Button(settframe,compound="top", text="Quick\nStart Wizard ",relief=RAISED,    command=wiz_page, image=photo, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  quick_start_wiz.pack(side="left", pady=3, ipadx=4)
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  
  
  
  invoi1label = Label(settingsframe, text="Settings", font=("arial", 18), bg="#f8f8f2")
  invoi1label.pack(side="left", padx=(20,0))
  
  global tab06
  m = ttk.Style()
  m.theme_use('default')
  m.configure('one.TNotebook.Tab', background="white", width=20, padding=10)
  tabControl = ttk.Notebook(tab10,style='one.TNotebook.Tab')
  tab01 = ttk.Frame(tabControl)
  tab02 = ttk.Frame(tabControl)
  tab03=  ttk.Frame(tabControl)
  tab04 = ttk.Frame(tabControl)
  tab05 = ttk.Frame(tabControl)
  tab06=  ttk.Frame(tabControl)
  tab07 = ttk.Frame(tabControl)
  tab08 = ttk.Frame(tabControl)
  tab09 =  ttk.Frame(tabControl)
  tab010=  ttk.Frame(tabControl)
  tabControl.add(tab01,image=invoices,compound = LEFT, text ='Miscellaneous',)
  tabControl.add(tab02,image=orders,compound = LEFT, text ='Company settings')
  tabControl.add(tab03,image=estimates,compound = LEFT, text ='Invoiced settings')
  tabControl.add(tab04,image=recurring,compound = LEFT, text ='Order settings')
  tabControl.add(tab05,image=purchase,compound = LEFT, text ='Estimate settings') 
  tabControl.add(tab06,image=expenses,compound = LEFT, text ='Administrator panel')
  tabControl.add(tab07,image=customer,compound = LEFT, text ='Advanced settings')
  tabControl.add(tab08,image=product,compound = LEFT, text ='Email templates')
  tabControl.add(tab09,image=reports,compound = LEFT, text ='Payments')
  tabControl.add(tab010,image=setting,compound = LEFT, text ='Purchase Order')
  tabControl.pack(expand = 1, fill ="both")
  
  ################### tab01 ###################################
  sql = "select * from company"
  fbcursor.execute(sql)
  sectab = fbcursor.fetchone()
  
  firsttab1=Frame(tab01, relief=GROOVE, bg="#f8f8f2")
  firsttab1.pack(side="top", fill=BOTH)
  
  firsttab=Frame(firsttab1, bg="#f5f3f2", height=700)
  firsttab.pack(side="top", fill=BOTH)
  
  messagelbframe=LabelFrame(firsttab,text="Menu and Window Color Style", height=60, width=180)
  messagelbframe.place(x=5, y=15)
  
  win_menu = StringVar()
  winstyle = ttk.Combobox(firsttab,textvariable=win_menu)
  winstyle.place(x=22 ,y=40)
  winstyle['values'] = ('whidbey','windows XP','windows 7','windows 8','windows 10')
  winstyle.current(0)
  fbill = Label(firsttab,text="F-Billing Revolution 2022",font="arial 12 bold").place(x=220,y=20)
  
  dbhost=LabelFrame(firsttab,text="Database Server Hostname", height=60, width=415)
  dbhost.place(x=5, y=85)
  
  db = Label(firsttab, text="DESKTOP-2K")
  db.place(x=15,y=110)
  
  exc=LabelFrame(firsttab,text="Extra cost name", height=180, width=415)
  exc.place(x=5, y=155)
  
  
  
  def insert_valueexc():
    i = varexc.get()
    if i == "":
      pass
    else:
      entryexc.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into extra_cost_name(companyid,extra_cost_name) values(%s,%s)'
        val = (companyid,i)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in exctree.get_children():
          exctree.delete(record)
        sql = 'select * from extra_cost_name'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          immm = str(i[2])
          imn = str.replace(immm," ","_")
          exctree.insert(parent='', index='end', iid=countp, text='hello', values=(imn))
          countp += 1
  # new_value = String
        
        
  
  def edit_valueexc(event):
    selected_item = exctree.selection()[0]
    temp = list(exctree.item(selected_item , 'values'))
    entryexc.delete(0, END)
    entryexc.insert(0, temp)
  
  def save_valueexc():
    i = entryexc.get()
    if i == "":
      pass
    else:
      selected0 = exctree.focus()
      valuz1= exctree.item(selected0)["values"]
      idgettingextracnid=valuz1[0]
      print(i,idgettingextracnid)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      companyid = com[0]
      if not com:
        pass
      else:
        sql = 'update extra_cost_name set extra_cost_name=%s where extra_cost_name=%s'
        val = (i,idgettingextracnid)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        entryexc.delete(0, END)
        for record in exctree.get_children():
            exctree.delete(record)
        fbcursor.execute("select *  from extra_cost_name")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          immm = str(i[2])
          imn = str.replace(immm," ","_")
          exctree.insert('', index='end', iid=countp, text='', values=(imn))
          countp += 1
    
    
  
  def del_valueexc():
    itemid = exctree.item(exctree.focus())["values"][0]
    sql = "delete from extra_cost_name where extra_cost_name = %s"
    val = (itemid, )
    fbcursor.execute(sql, val)
    fbilldb.commit()
    exctree.delete(exctree.selection()[0])
      
      
  
    
    
    
  
  
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  exctree = ttk.Treeview(firsttab, columns=("1"),height=40,selectmode='browse', yscrollcommand=scrollbary.set,   xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=exctree.yview)
  scrollbary.place(x=394,y=200,height=125)
  scrollbarx.config(command=exctree.xview)
  scrollbarx.place(x=15,y=310, width=380)
  exctree.heading('1', text="Extra cost name",)
  # exctree.column('#0', stretch=NO, minwidth=0, width=0)
  exctree.column("#0",width=0, stretch=False)
  exctree.column('1',width=378,)
  exctree.place(x=15,y=200,height=115,width=380)
  exctree.bind('<Double-Button-1>' , edit_valueexc)
  sql = 'select * from extra_cost_name'
  fbcursor.execute(sql)
  setexctree = fbcursor.fetchall()
  countp = 0
  for i in setexctree:
      immm = str(i[2])
      imn = str.replace(immm," ","_")
      exctree.insert(parent='', index='end', iid=countp, text='', values=(imn))
      countp += 1
  # new_value = StringVar()
  
  # def edit_window_box(val):
      
  #     edit_window = Toplevel(root)
  #     edit_window.title("Edit the value or cancel")
  #     edit_window.geometry("1000x250")
  #     label_edit = Label(edit_window , text='Enter value to edit or press cancel', 
  #     font = ("Times New Roman", 10)).grid(column=0,row=1,padx=0, pady = 2)
  #     #create edit box
  #     edit_box = Entry(edit_window)
  #     edit_box.insert(0,val)
  #     edit_box.grid(column=1,row=1,padx=0,pady=2)
  #     #auto select edit window 
  #     edit_window.focus()
      
  #     def value_assignment(event):
  #         printing = edit_box.get()
  #         new_value.set(printing)
  #         #only destroy will not update the value (perhaps event keeps running in background)
  #         #quit allows event to stop n update value in tree but does not close the window in single click 
  #         #rather on dbl click shuts down entire app 
  #         edit_window.quit()
  #         edit_window.destroy()
      
  #     edit_window.bind('<Return>', value_assignment )
  
  #     B1 = Button(edit_window, text="Okay")
  #     B1.bind('<Button-1>',value_assignment)
  #     B1.grid(column=0,row=10,padx=0, pady = 20)
      
  #     B2 = Button(edit_window, text="Cancel", command = edit_window.destroy).grid(column=1,row=10,padx=10,   pady = 20)
  #     edit_window.mainloop()
      
  # #will explain
  # #variable to hold col value (col clicked)
  # shape1 = IntVar()
  # #tracks both col , row on mouse click
  # def tree_click_handler(event):
  #     cur_item = exctree.item(exctree.focus())
  #     col = exctree.identify_column(event.x)[1:]
  #     rowid = exctree.identify_row(event.y)[1:]
  #     #updates list
  #     shape1.set(col)
  #     try:
  #         x,y,w,h = exctree.bbox('I'+rowid,'#'+col)
  #     except:pass
  #     #tree.tag_configure("highlight", background="yellow")
  #     return(col)
      
  # #code linked to event    
  # exctree.bind('<ButtonRelease-1>', tree_click_handler)
  
  # def edit(event):
  #     try:
  #         selected_item = exctree.selection()[0]
  #         temp = list(exctree.item(selected_item , 'values'))
  #         tree_click_handler
  #         col_selected = int(shape1.get())-1
  #         edit_window_box(temp[col_selected])
  #         #do not run if edit window is open
  #         #use edit_window.mainloop() so value assign after window closes
  #         temp[col_selected] = new_value.get()
  #         exctree.item(selected_item, values= temp)
  #     except: pass
      
      
  # #binding allows to edit on screen double click
  # exctree.bind('<Double-Button-1>' , edit)
  varexc = StringVar()
  entryexc = Entry(firsttab,width=25,textvariable=varexc)
  entryexc.place(x=15,y=173)
  
  btexcadd = Button(firsttab,text="Add new line",command=insert_valueexc)
  btexcadd.place(x=175,y=171)
  
  btexcedit = Button(firsttab,text="Edit line   ",command=save_valueexc)
  btexcedit.place(x=260,y=171)
  btexcadd = Button(firsttab,text=" Delete line  ",command=del_valueexc)
  btexcadd.place(x=330,y=171)
  
  exc=LabelFrame(firsttab,text="Predefined text records for header and footer", height=180, width=415)
  exc.place(x=5, y=350)
  
  def insert_valuepre():
    i = prestr.get()
    if i == "":
      pass
    else:
      entrypre.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into header_and_footer(companyid,headerandfooter) values(%s,%s)'
        val = (companyid,i)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in pretree.get_children():
          pretree.delete(record)
        sql = 'select * from header_and_footer'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          pret = str(i[2])
          pre = str.replace(pret," ","_")
          pretree.insert(parent='', index='end', iid=countp, text='hello', values=(pre))
          countp += 1
  # new_value = String
        
        
  
  def edit_valuepre(event):
    selected_item = pretree.selection()[0]
    temp = list(pretree.item(selected_item , 'values'))
    entrypre.delete(0, END)
    entrypre.insert(0, temp)
  
  def save_valuepre():
    i = prestr.get()
    if i == "":
      pass
    else:
      selected0 = pretree.focus()
      valuz1= pretree.item(selected0)["values"]
      idgettingextracnid=valuz1[0]
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      companyid = com[0]
      if not com:
        pass
      else:
        sql = 'update header_and_footer set headerandfooter=%s where headerandfooter=%s'
        val = (i,idgettingextracnid)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        entryexc.delete(0, END)
        for record in pretree.get_children():
            pretree.delete(record)
        fbcursor.execute("select *  from header_and_footer")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          pret = str(i[2])
          pre = str.replace(pret," ","_")
          pretree.insert('', index='end', iid=countp, text='', values=(pre))
          countp += 1
    
    
  
  def del_valuepre():
    itemid = pretree.item(pretree.focus())["values"][0]
    sql = "delete from header_and_footer where headerandfooter = %s"
    val = (itemid,)
    fbcursor.execute(sql, val)
    fbilldb.commit()
    for record in pretree.get_children():
      pretree.delete(record)
    fbcursor.execute("select *  from header_and_footer")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      pret = str(i[2])
      pre = str.replace(pret," ","_")
      pretree.insert('', index='end', iid=countp, text='', values=(pre))
      countp += 1
    
      
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  pretree = ttk.Treeview(firsttab, columns=("1"),height=400,     selectmode="extended",   yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=pretree.yview)
  scrollbary.place(x=395,y=400,height=115)
  scrollbarx.config(command=pretree.xview)
  scrollbarx.place(x=15,y=510, width=380)
  pretree.heading('1', text="header and footer",)
  pretree.column('#0', stretch=NO, minwidth=0, width=0)
  pretree.column('1', stretch=NO, width=378)
  pretree.place(x=15,y=400,height=115,width=380)
  pretree.bind('<Double-Button-1>' , edit_valuepre)
  sql = 'select * from header_and_footer'
  fbcursor.execute(sql)
  setexctree = fbcursor.fetchall()
  countp = 0
  for i in setexctree:
    pret = str(i[2])
    pre = str.replace(pret," ","_")
    pretree.insert(parent='', index='end', iid=countp, text='hello', values=(pre))
    countp += 1
  prestr = StringVar()
  entrypre = Entry(firsttab,width=25,textvariable=prestr)
  entrypre.place(x=15,y=370)
  btexcadd = Button(firsttab,text="Add new line",command=insert_valuepre)
  btexcadd.place(x=175,y=370)
  btpredit = Button(firsttab,text="Edit line   ",command=save_valuepre)
  btpredit.place(x=260,y=370)
  btexcadd = Button(firsttab,text=" Delete line   ",command=del_valuepre)
  btexcadd.place(x=330,y=370)
  
  ver = Label(firsttab,text="FREE version.Upgrade PRO version for all features and Ad free invoice")
  ver.place(x=480,y=15)
  
  
  chapass=LabelFrame(firsttab,text="Change Password", height=150, width=500)
  chapass.place(x=480, y=40)
  
  enterold = StringVar()
  lenold = Label(firsttab,text="Enter your old password")
  lenold.place(x=495,y=60)
  enold = Entry(firsttab,textvariable=enterold)
  enold.place(x=640,y=60)
  
  enternew = StringVar()
  ennew = Label(firsttab,text="New password")
  ennew.place(x=495,y=90)
  newpass = Entry(firsttab,textvariable=enternew)
  newpass.place(x=640,y=90)
  
  
  cnewpass = StringVar()
  cnp = Label(firsttab,text="Confirm new password")
  cnp.place(x=495,y=120)
  cnewp = Entry(firsttab,textvariable=cnewpass)
  cnewp.place(x=640,y=120)

  def change_pass():
    old_pass = enterold.get()
    new_pass = enternew.get()
    cnew_pass = cnewpass.get()
    usna = username1.get()
    sql='SELECT * FROM users WHERE username=%s'
    val=(usna,)
    fbcursor.execute(sql,val)
    chpass = fbcursor.fetchone()
    if old_pass == "" or new_pass == "" or cnew_pass == "":
        messagebox.showerror('Password Error','Plz enter password')
    elif old_pass == chpass[4]:
      if new_pass == cnew_pass:
        sqll='UPDATE users SET password=%s,confirm_password=%s WHERE userID=%s'
        vall=(new_pass,cnew_pass,chpass[0])
        fbcursor.execute(sqll,vall,)
        fbilldb.commit()
        messagebox.showinfo('Updated','Password updated successfully')
      else:
        messagebox.showerror('Password Error','password is not match')
    else:
      messagebox.showerror('Password Error','Old Password is Incorrect')
  chabtn = Button(firsttab,text="Change password",command=change_pass)
  chabtn.place(x=840,y=150)
  
  termf=LabelFrame(firsttab,text="Terms of payment", height=150, width=500)
  termf.place(x=480, y=190)


  def insert_valueterm():
    first = entrytopstr.get()
    second = entrydsstr.get()
    if first == "" or second == "":
      pass
    else:
      entrytop.delete(0, END)
      entryds.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into terms_of_payment(companyid,terms_of_payment,Date_shift) values(%s,%s,%s)'
        val = (companyid,first,second)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in termtree.get_children():
          termtree.delete(record)
        sql = 'select * from terms_of_payment'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          
          termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
          countp += 1
  # new_value = String
        
        
  
  def edit_valueterm(event):
    itemid = termtree.item(termtree.focus())["values"][0]
    sql = "select * from terms_of_payment where terms_of_payment = %s"
    val = (itemid,)
    fbcursor.execute(sql,val)
    editterm = fbcursor.fetchone()
    entrytop.delete(0, END)
    entryds.delete(0, END)
    entrytop.insert(0, editterm[2])
    entryds.insert(0, editterm[3])
  
  def save_valueterm():
    first = entrytopstr.get()
    second = entrydsstr.get()
    if first == "" or second == "":
      pass
    else:
      itemid = termtree.item(termtree.focus())["values"][0]
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        pass
      else:
        sql = "select * from terms_of_payment where terms_of_payment=%s"
        val = (itemid,)
        fbcursor.execute(sql,val)
        payt = fbcursor.fetchone()
        sql2 = 'update terms_of_payment set terms_of_payment=%s,Date_shift=%s where terms_of_paymentID=%s'
        val2 = (first,second,payt[0])
        fbcursor.execute(sql2,val2)
        fbilldb.commit()
        entrytop.delete(0, END)
        entryds.delete(0, END)
        for record in termtree.get_children():
          termtree.delete(record)
        fbcursor.execute("select *  from terms_of_payment")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          
          termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
          countp += 1
    
    
  
  def del_valueterm():
    itemid = termtree.item(termtree.focus())["values"][0]
    print(itemid)
    sql = "delete from terms_of_payment where terms_of_payment = %s"
    val = (itemid,)
    fbcursor.execute(sql, val)
    fbilldb.commit()
    for record in termtree.get_children():
        termtree.delete(record)
    fbcursor.execute("select *  from terms_of_payment")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
      countp += 1
  
  
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  termtree = ttk.Treeview(firsttab, columns=("1","2"),height=400,selectmode="extended",   yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=termtree.yview)
  scrollbary.place(x=870,y=228,height=100)
  scrollbarx.config(command=termtree.xview)
  scrollbarx.place(x=495,y=313, width=380)
  termtree.heading('1', text="Terms of payment",)
  termtree.heading('2', text="Date shift (days)",)
  termtree.column('#0', stretch=NO, minwidth=0, width=0)
  termtree.column('1', stretch=NO, minwidth=0, width=250)
  termtree.column('2', stretch=NO, minwidth=0, width=128)
  termtree.place(x=495,y=235,height=80,width=380)
  termtree.bind('<Double-Button-1>' , edit_valueterm)

  sql = 'select * from terms_of_payment'
  fbcursor.execute(sql)
  termt = fbcursor.fetchall()
  countp = 0
  for i in termt:
      termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
      countp += 1
  entrytopstr = StringVar()
  entrytop = Entry(firsttab,width=25,textvariable=entrytopstr)
  entrytop.place(x=495,y=208)
  entrydsstr = StringVar()
  entryds = Entry(firsttab,textvariable=entrydsstr)
  entryds.place(x=670,y=208)
  bttermadd = Button(firsttab,text="Add new line",command=insert_valueterm)
  bttermadd.place(x=800,y=205)
  bttermedit = Button(firsttab,text="     Edit line  ",command=save_valueterm)
  bttermedit.place(x=890,y=205)
  bttermdel = Button(firsttab,text="  Delete line  ",command=del_valueterm)
  bttermdel.place(x=890,y=240)
  
  radem=LabelFrame(firsttab,text="Invoice/Oder/Estimate/P.order Email Attachment file type", height=60,   width=500)
  radem.place(x=480, y=340)
  radema = StringVar()
  radpdf = Radiobutton(firsttab,variable=radema,value="PDF",text='PDF')
  radpdf.place(x= 485, y= 360 )
  radhtml = Radiobutton(firsttab,variable=radema,value="HTML",text='HTML')
  radhtml.place(x= 660, y= 360 )
  if  not sectab:
    pass
  else:
    if sectab[22] == 'PDF':
      radpdf.select()
    elif sectab[22] == 'HTML':
      radhtml.select()
    else:
      pass
  
  checkb1 = IntVar()
  check1 = Checkbutton(firsttab,variable = checkb1, 
                        text="PDF attachment with Embedded Fonts (PDF file size will be larger,but readable on   all devices) ", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  
  check1.place(x=480,y=400)
  if  not sectab:
    pass
  else:
    if sectab[23] == 1:
      check1.select()
    else:
      check1.deselect()
  
  checkb2 = IntVar()
  check2 = Checkbutton(firsttab,variable = checkb2, 
                        text="invoice numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                       )
  
  check2.place(x=480,y=420)
  if  not sectab:
    pass
  else:
    if sectab[24] == 1:
      check2.select()
    else:
      check2.deselect()
  
  checkb3 = IntVar()
  check3 = Checkbutton(firsttab,variable = checkb3, 
                        text="Order numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  
  check3.place(x=480,y=440)
  if  not sectab:
    pass
  else:
    if sectab[25] == 1:
      check3.select()
    else:
      check3.deselect()
  
  checkb4 = IntVar()
  check4 = Checkbutton(firsttab,variable = checkb4, 
                        text="Estimate numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                       )
  
  check4.place(x=480,y=460)
  if  not sectab:
    pass
  else:
    if sectab[26] == 1:
      check4.select()
    else:
      check4.deselect()
  
  checkb5 = IntVar()
  check5 = Checkbutton(firsttab,variable = checkb5, 
                        text="Purchsae order numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  check5.place(x=480,y=480)
  if  not sectab:
    pass
  else:
    if sectab[27] == 1:
      check5.select()
    else:
      check5.deselect()
  
  checkb6 = IntVar()
  check6 = Checkbutton(firsttab,variable = checkb6, 
                        text="Confirmation before closing F-billing Revolution", 
                        onvalue =1 ,
                        offvalue = 0,
                      )
  
  check6.place(x=480,y=500)
  if  not sectab:
    pass
  else:
    if sectab[28] == 1:
      check6.select()
    else:
      check6.deselect()
  
  ################### tab02 ###################################
  sql = "select * from company"
  fbcursor.execute(sql)
  sectab = fbcursor.fetchone()
  
  
  
  secondtab1=Frame(tab02, relief=GROOVE, bg="#f8f8f2")
  secondtab1.pack(side="top", fill=BOTH)
  
  secondtab=Frame(secondtab1, bg="#f5f3f2", height=700)
  secondtab.pack(side="top", fill=BOTH)
  
  comdata=LabelFrame(secondtab,text="Company data", height=200, width=500)
  comdata.place(x=5, y=15)
  cname = Label(secondtab,text="Company name")
  cname.place(x=20, y =35)
  comname = StringVar()
  centry = Entry(secondtab,textvariable=comname)
  if  not sectab:
    pass
  else:
    centry.insert(0, sectab[1])
  centry.place(x=160,y=35,width=280)
  
  
  cadd = Label(secondtab,text="Company Address")
  cadd.place(x=20, y =65)
  caddent = scrolledtext.ScrolledText(secondtab)
  if  not sectab:
    pass
  else:
    caddent.insert('1.0', sectab[2])
  caddent.place(x=160,y=65,height=80,width=280)
  
  cemail = Label(secondtab,text="E-mail Address")
  cemail.place(x=20, y =160)
  comemail = StringVar()
  cemailentry = Entry(secondtab,textvariable=comemail)
  if  not sectab:
    pass
  else:
    cemailentry.insert(0, sectab[3])
  cemailentry.place(x=160,y=160,width=280)
  
  stl = Label(secondtab,text="sales Tax.Reg.No.")
  stl.place(x=20, y =185)
  comsalestax = StringVar()
  ste = Entry(secondtab,textvariable=comsalestax)
  if  not sectab:
    pass
  else:
    ste.insert(0, sectab[4])
  ste.place(x=160,y=185,width=280)
  
  
  curre=LabelFrame(secondtab,text="Currency", height=125, width=500)
  curre.place(x=5, y=220)
  currl = Label(secondtab,text="Currency")
  currl.place(x=20,y= 240)
  comcur = StringVar()
  currbox = ttk.Combobox(secondtab,width=10,textvariable=comcur)
  currbox['values'] =('ALL','AFN','ARS','AWG','AUD','AZN','BSD','BBD','BYN','BZD','BMD','BOB','BAM','BWP',  'BGN','BRL','BND','KHR','CAD','KYD','CLP','CNY','COP','CRC','HRK','CUP','CZK','DKK','DOP','XCD','EGP','SVC',  'EUR','FKP','FJD','GHS','GIP','GTQ','GGP','GYD','HNL','HKD','HUF','ISK','INR','IDR','IRR','IMP','ILS','JMD',  'JPY','JEP','KZT','KPW','KRW','KGS','LAK','LBP','LRD','MKD','MYR','MUR','MXN','MNT','MNT','MZN','NAD','NPR',  'ANG','NZD','NIO','NGN','NOK','OMR','PKR','PAB','PYG','PEN','PHP','PLN','QAR','RON','RUB','SHP','SAR','RSD',  'SCR','SGD','SBD','SOS','KRW','ZAR','LKR','SEK','CHF','SRD','SYP','TWD','THB','TTD','TRY','TVD','UAH','AED',  'GBP','USD','UYU','UZS','VEF','VND','YER','ZWD',)
  if  not sectab:
    pass
  elif sectab[5]:
    currbox.insert(0, sectab[5])
  currbox.place(x=80,y=240)
  
  def signpl(event):
    amsgpl = comcursignpla.get()
    currsign = comcursign.get()
    if amsgpl == "before amount":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'8347.26')
    elif amsgpl == "after amount":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26'+currsign)
    elif amsgpl == "before amount with space":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'  8347.26')
    elif amsgpl == "after amount with space":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26  '+currsign)
  
  
  currsignl = Label(secondtab,text="Currency sign")
  currsignl.place(x=180,y=240)
  comcursign = StringVar()
  currsignbox = ttk.Combobox(secondtab,width=10,textvariable=comcursign)
  currsignbox.bind("<<ComboboxSelected>>", signpl)
  currsignbox["values"] = ('Lek','؋','$','ƒ','$','₼','$','$','Br','BZ$','$','$b','KM','P','лв','R$','$','៛',  '$','$','$','¥','$','₡','kn','₱','Kč','kr','RD$','$','£','$','€','£','$','¢','£','Q','£','$','L','$','Ft',  'kr','₹','Rp','﷼','£','₪','J$','¥','£','лв','₩','₩','₭','£','$','ден','RM','₨','$','₮',' د.إ','MT','$','₨',  'ƒ','$','C$','₦','kr','﷼','₨','B/.','Gs','S/.','₱','zł','﷼','lei','₽','£','﷼','Дин.','₨','S','₩','R','₨',  'kr','CHF','£','NT$','฿','TT$','₺','$','₴','د.إ','$U','лв','Bs','₫','﷼','Z$')
  if  not sectab:
    pass
  elif sectab[6]:
    currsignbox.insert(0, sectab[6])
  currsignbox.place(x=265,y=240)
  
  cspl = Label(secondtab,text="Currency sign placement")
  cspl.place(x=20,y=270)
  
  def amountsignspace(event):
    amsgpl = comcursignpla.get()
    currsign = comcursign.get()
    if amsgpl == "before amount":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'8347.26')
    elif amsgpl == "after amount":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26'+currsign)
    elif amsgpl == "before amount with space":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'  8347.26')
    elif amsgpl == "after amount with space":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26  '+currsign)
    
      
      
  comcursignpla = StringVar()
  cspe = ttk.Combobox(secondtab,width=24,textvariable=comcursignpla,)
  cspe.bind("<<ComboboxSelected>>", amountsignspace)
  cspe["values"] = ("before amount","after amount",'before amount with space',"after amount with space")
  if  not sectab:
    pass
  elif sectab[7]:
    cspe.insert(0, sectab[7])
  cspe.place(x=180,y=270)
  
  def decpl(event):
    dec = comdecsep.get()
    ex = comex.get()
    if dec == ",":
      var = str.replace(ex,".",",")
      exbox.delete(0, END)
      exbox.insert(0, var)
    elif dec == ".":
      var1 = str.replace(ex,",",".")
      exbox.delete(0, END)
      exbox.insert(0, var1)
  dsl = Label(secondtab,text="Decimal separator")
  dsl.place(x=20,y=300)
  comdecsep = StringVar()
  currbox = ttk.Combobox(secondtab,width=5,textvariable=comdecsep)
  currbox.bind("<<ComboboxSelected>>",decpl)
  currbox['values'] = ('.',',')
  if  not sectab:
    pass
  elif sectab[8]:
    currbox.insert(0, sectab[8])
  currbox.place(x=130,y=300)
  
  exl = Label(secondtab,text="Example")
  exl.place(x=185,y=300)
  comex = StringVar()
  exbox = Entry(secondtab,width=15,textvariable=comex)
  if  not sectab:
    exbox.insert(0, 84367.26)
  elif sectab[9]:
    exbox.insert(0, sectab[9])
  exbox.place(x=245,y=300)
  
  btred = Button(secondtab,text="Restore Default")
  btred.place(x=400,y=270)
  btsc = Button(secondtab,text="SET CURRENCY")
  btsc.place(x=400,y=300)
  
  datef=LabelFrame(secondtab,text="Date format", height=60, width=500)
  datef.place(x=5, y=355)
  
  def daffun(event):
    dafget = daf.get()
    if dafget == "mm-dd-yyyy":
      exd._set_text(exd._date.strftime('%m-%d-%Y'))
    elif dafget == "dd-mm-yyyy":
      exd._set_text(exd._date.strftime('%d-%m-%Y'))
    elif dafget == "yyy.mm.dd":
      exd._set_text(exd._date.strftime('%Y.%m.%d'))
    elif dafget == "mm/dd/yyyy":
      exd._set_text(exd._date.strftime('%m/%d/%Y'))
    elif dafget == "dd/mm/yyy":
      exd._set_text(exd._date.strftime('%d/%m/%Y'))
    elif dafget == "dd.mm.yyyy":
      exd._set_text(exd._date.strftime('%d.%m.%Y'))
    elif dafget == "yyyy/mm/dd":
      exd._set_text(exd._date.strftime('%Y/%m/%d'))
    
  
  comdaf = StringVar()
  daf = ttk.Combobox(secondtab,textvariable=comdaf)
  daf["values"] = ("Default",'mm-dd-yyyy','dd-mm-yyyy','yyy.mm.dd','mm/dd/yyyy','dd/mm/yyy','dd.mm.yyyy','yyyy/  mm/dd')
  daf.bind("<<ComboboxSelected>>",daffun)
  if not sectab:
    pass
  elif sectab[10]:
    daf.insert(0, sectab[10])
  daf.place(x=60,y=380)
  
  
  exd = DateEntry(secondtab,)
  exd.place(x=280,y=380)
  if  not sectab:
    pass
  elif sectab[11]:
    exd.delete(0, END)
    exd.insert(0, sectab[11])
  
  tnr=LabelFrame(secondtab,text="Tax name and rate", height=200, width=500)
  tnr.place(x=560, y=15)
  
  stt=LabelFrame(secondtab,text="Select tax type", height=120, width=180)
  stt.place(x=580, y=30)
  def rtax1():
    ch = radtax.get()
    if ch == 1:
      tax1namel.place_forget()
      tax1namee.place_forget()
      tax1ratel.place_forget()
      tax1ratee.place_forget()
      tax1ratee.place_forget()
      ptax1.place_forget()
  
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif ch == 2:
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif ch == 3:
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place(x=800, y=110)
      tax2namee.place(x=880,y=110)
      tax2ratel.place(x=800, y=140)
      tax2ratee.place(x=880,y=140)
      ptax2.place(x=580,y=185)
    
  radtax = IntVar()
  rdnotax = Radiobutton(secondtab,text="Do not use TAX",value="1",variable=radtax,command=rtax1)
  rdnotax.place(x=590,y=50)
  
  
  rdtax1 = Radiobutton(secondtab,text="1 level of Tax",value="2",variable=radtax,command=rtax1)
  rdtax1.place(x=590,y=80)
  ptax01 = IntVar()
  tax1namel = Label(secondtab,text="Tax1 name")
  
  
  tax1namee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[15]:
    tax1namee.insert(0, sectab[15])
  tax1namee.place(x=60,y=380)
  
  
  tax1ratel = Label(secondtab,text="Tax1 rate")
  
  
  tax1ratee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[16]:
    tax1ratee.insert(0, sectab[16])
  
  comptax1 = BooleanVar()
  ptax1 = Checkbutton(secondtab,text="Print TAX1" ,onvalue =1 ,offvalue = 0,variable=comptax1)
  if  not sectab:
    pass
  elif sectab[17] == 1:
    ptax1.select()
  else:
    ptax1.deselect()
  
  rdtax2 = Radiobutton(secondtab,text="2 level of Tax",value="3",variable=radtax,command=rtax1)
  rdtax2.place(x=590,y=110)
  
  
  tax2namel = Label(secondtab,text="Tax2 name")
  
  
  tax2namee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[18]:
    tax2namee.insert(0, sectab[18])
  
  tax2ratel = Label(secondtab,text="Tax2 rate")
  
  tax2ratee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[19]:
    tax2ratee.insert(0, sectab[19])
  
  comptax2 = BooleanVar()
  ptax2 = Checkbutton(secondtab,text="Print TAX2" ,onvalue =1 ,offvalue = 0,variable=comptax2)
  if  not sectab:
    pass
  else:
    if sectab[20] == 1:
      ptax2.select()
    else:
      ptax2.deselect()
  
  if  not sectab:
    pass
  else:
    if sectab[12] == "1":
      rdnotax.select()
      tax1namel.place_forget()
      tax1namee.place_forget()
      tax1ratel.place_forget()
      tax1ratee.place_forget()
      tax1ratee.place_forget()
      ptax1.place_forget()
  
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif sectab[12] == "2":
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
      rdtax1.select()
    elif sectab[12] == "3":
      rdtax2.select()
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place(x=800, y=110)
      tax2namee.place(x=880,y=110)
      tax2ratel.place(x=800, y=140)
      tax2ratee.place(x=880,y=140)
      ptax2.place(x=580,y=185)
    else:
      pass
  
  
  comlo=LabelFrame(secondtab,text="Comapny Logo", height=260, width=320)
  comlo.place(x=560, y=240)
  
  def upload_filelogo():
    global imglogo,filename
    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
    image = Image.open(filename)
    resize_image = image.resize((280, 160))
    imglogo = ImageTk.PhotoImage(resize_image)
    # b2 = Button(secondtab,image=img)
    # b2.place(x=130, y=80)
  
    btlogo = Button(secondtab,width=280,height=160,image=imglogo)
    btlogo.place(x=580,y=280)
  
  try:
    image = Image.open("images/"+sectab[13])
    resize_image = image.resize((280, 160))
    image = ImageTk.PhotoImage(resize_image)
    btlogo = Button(secondtab,width=280,height=160,image=image)
    btlogo.place(x=580,y=280)
    btlogo.photo = image
  except:
    pass
  
    
  btloadim = Button(secondtab,text="Load logo image",command=upload_filelogo)
  btloadim.place(x=580,y=460)
  
  compimg = BooleanVar()
  primage = Checkbutton(secondtab,text="Print logo image",variable = compimg,onvalue =1 ,offvalue = 0)
  primage.place(x=740,y=460)

  
  ################### tab06 ###################################
  
  def user():
    display = displaystart.get()
    user_name = usernae.get()
    password = userpase.get()
    conformpassword = usercpase.get()
   
    create_inv = creinvbol.get()
    delete_inv = delinvbol.get()
    void_inv = voinvbol.get()
    mark_inv_as_paid = markinvbol.get()
    
    create_ord = creordbol.get()
    delete_ord = delordbol.get()
    turn_inv_ord = turninvbol.get()
    smsnofi = smsinvbol.get()
    
    create_est = creestimatebol.get()
    delete_est = delestimatebol.get()
    turn_est = turnestiinvbol.get()
  
    create_exp = creexpensebol.get()
    delete_exp = delexpensebol.get()
    rebill_exp = rebillexpebol.get()
    
    create_cus = crecusbol.get()
    delete_cus = delcusbol.get()
    imp_cus = impcusbol.get()
  
    create_pros = creprosbol.get()
    delete_pros = delprosbol.get()
    import_pros = impprosbol.get()
  
    runrep = runrepbol.get()
    gen_rec = genrecinvbol.get()
  
    create_pur = crepurbol.get()
    delete_pur = delpurbol.get()
  
    modify_inv = modifyinvbol.get()
    modify_ord = modifyordbol.get()
    modify_est = modifyestibol.get()
  
    if user_name=="" or password=="":
      messagebox.showerror('',"Please complete the form")
    else:
      sql='SELECT * FROM users WHERE username=%s'# selecting entire table from db,taking username , nd check   the existance
      val=(user_name,)
      fbcursor.execute(sql,val)
      if fbcursor.fetchone()is not None:
        sql='SELECT * FROM users WHERE username=%s'
        val=(user_name,)
        fbcursor.execute(sql,val)
        whuser = fbcursor.fetchone()
        if password == conformpassword:
          if user_name == "adminstator":
            sqll= 'UPDATE users SET displayloginscreen=%s,username=%s,password=%s,confirm_password=%s WHERE userID=%s'
            vall=(display,user_name,password,conformpassword,whuser[0])
            fbcursor.execute(sqll,vall)
            fbilldb.commit()
          else:
            sqll= 'UPDATE users SET displayloginscreen=%s,username=%s,password=%s,confirm_password=%s,create_invoice=%s,delete_invoice=%s,void_invoice=%s,mark_invoice_as_paid=%s,create_order=%s,delete_order=%s,turn_order_into_invoice=%s,send_sms_nofitication=%s,create_estimate=%s,delete_estimate=%s,turn_oestimate_into_invoice=%s,create_expense=%s,delete_expense=%s,rebill_exprense=%s,create_customer=%s,delete_customer=%s,import_customer=%s,	create_product_service=%s,delete_product_service=%s,import_product_service=%s,run_reports=%s,generate_recurring_invoice=%s,create_purchase_order=%s,delete_purchase_order=%s,modify_invoice_settings=%s,modify_order_settings=%s,modify_estimate_settings=%s WHERE userID=%s'
            vall=(display,user_name,password,conformpassword,create_inv,delete_inv,void_inv,mark_inv_as_paid,  create_ord,delete_ord,turn_inv_ord,smsnofi,create_est,delete_est,turn_est,create_exp,delete_exp,  rebill_exp,create_cus,delete_cus,imp_cus,create_pros,delete_pros,import_pros,runrep,gen_rec,create_pur,  delete_pur,modify_inv,modify_ord,modify_est,whuser[0])
            fbcursor.execute(sqll,vall)
            fbilldb.commit()
        else:
          messagebox.showerror('Warming','Password not match!!')
      else:
        if password == conformpassword:
          if user_name == "adminstator":
            sql="INSERT INTO users(displayloginscreen,username,password,confirm_password,create_invoice,  delete_invoice,void_invoice,mark_invoice_as_paid,create_order,delete_order,turn_order_into_invoice,  send_sms_nofitication,create_estimate,delete_estimate,turn_oestimate_into_invoice,	create_expense,	  delete_expense,rebill_exprense,create_customer,delete_customer,import_customer,	create_product_service,  delete_product_service,	import_product_service,run_reports,generate_recurring_invoice,  create_purchase_order,delete_purchase_order,modify_invoice_settings,modify_order_settings,  modify_estimate_settings) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,  %s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
            val=(display,user_name,password,conformpassword,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
            fbcursor.execute(sql,val)
            fbilldb.commit()
            for record in uactree.get_children():
              uactree.delete(record)
            sql = "select * from users"
            fbcursor.execute(sql)
            sixuactree = fbcursor.fetchall()
            coutset = 0
            for i in sixuactree:
             uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
             coutset += 1
          else:
            sql="INSERT INTO users(displayloginscreen,username,password,confirm_password,create_invoice,  delete_invoice,void_invoice,mark_invoice_as_paid,create_order,delete_order,turn_order_into_invoice,  send_sms_nofitication,create_estimate,delete_estimate,turn_oestimate_into_invoice,	create_expense,	  delete_expense,rebill_exprense,create_customer,delete_customer,import_customer,	create_product_service,  delete_product_service,	import_product_service,run_reports,generate_recurring_invoice,  create_purchase_order,delete_purchase_order,modify_invoice_settings,modify_order_settings,  modify_estimate_settings) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,  %s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
            val=(display,user_name,password,conformpassword,create_inv,delete_inv,void_inv,mark_inv_as_paid,  create_ord,delete_ord,turn_inv_ord,smsnofi,create_est,delete_est,turn_est,create_exp,delete_exp,  rebill_exp,create_cus,delete_cus,imp_cus,create_pros,delete_pros,import_pros,runrep,gen_rec,create_pur,  delete_pur,modify_inv,modify_ord,modify_est)
            fbcursor.execute(sql,val)
            fbilldb.commit()
            for record in uactree.get_children():
              uactree.delete(record)
            sql = "select * from users"
            fbcursor.execute(sql)
            sixuactree = fbcursor.fetchall()
            coutset = 0
            for i in sixuactree:
             uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
             coutset += 1
        else:
          messagebox.showerror('Warming','Password not match!!')
        

   
    
  
  
  
  
    
  
    
  sixtab1=Frame(tab06, relief=GROOVE, bg="#f8f8f2")
  sixtab1.pack(side="top", fill=BOTH)
  
  sixtab=Frame(sixtab1, bg="#f5f3f2", height=700)
  sixtab.pack(side="top", fill=BOTH)
  
  displaystart = BooleanVar()
  displaylocsc = Checkbutton(sixtab,text="Display Login screen startup",onvalue =1 ,offvalue = 0,  variable=displaystart)
  displaylocsc.place(x=20,y=30)
  
  userac=LabelFrame(sixtab,text="User Acounts", height=400, width=260)
  userac.place(x=20, y=55)
  
  
  selper = Label(sixtab,text="Select username to modify permissions")
  selper.place(x=30,y=75)
  
  def focususer(event):
    itemid = uactree.item(uactree.focus())["values"][0]
    sql = "select * from users where username = %s"
    val = (itemid,)
    fbcursor.execute(sql,val)
    sixtabdataback = fbcursor.fetchone()
    usernae.delete(0,END)
    usernae.insert(0,itemid)
    if itemid == "adminstator":
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = DISABLED
        creinv["state"] = DISABLED
        delinv["state"] = DISABLED
        voinv["state"] = DISABLED
        markinv["state"] = DISABLED
        creord["state"] = DISABLED
        delord["state"] = DISABLED
        turninv["state"] = DISABLED
        smsinv["state"] = DISABLED
        creestimate["state"] = DISABLED
        delestimate["state"] = DISABLED
        turnestiinv["state"] = DISABLED
        creexpense["state"] = DISABLED
        delexpense["state"] = DISABLED
        rebillexpe["state"] = DISABLED
        crecus["state"] = DISABLED
        delcus["state"] = DISABLED
        impcus["state"] = DISABLED
        crepros["state"] = DISABLED
        delpros["state"] = DISABLED
        imppros["state"] = DISABLED
        runrep["state"] = DISABLED
        genrecinv["state"] = DISABLED
        crepur["state"] = DISABLED
        delpur["state"] = DISABLED
        modifyinv["state"] = DISABLED
        modifyord["state"] = DISABLED
        modifyesti["state"] = DISABLED
    else:
        userpase.delete(0, END)
        usercpase.delete(0, END)
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = NORMAL
        creinv["state"] = NORMAL
        delinv["state"] = NORMAL
        voinv["state"] = NORMAL
        markinv["state"] = NORMAL
        creord["state"] = NORMAL
        delord["state"] = NORMAL
        turninv["state"] = NORMAL
        smsinv["state"] = NORMAL
        creestimate["state"] = NORMAL
        delestimate["state"] = NORMAL
        turnestiinv["state"] = NORMAL
        creexpense["state"] = NORMAL
        delexpense["state"] = NORMAL
        rebillexpe["state"] = NORMAL
        crecus["state"] = NORMAL
        delcus["state"] = NORMAL
        impcus["state"] = NORMAL
        crepros["state"] = NORMAL
        delpros["state"] = NORMAL
        imppros["state"] = NORMAL
        runrep["state"] = NORMAL
        genrecinv["state"] = NORMAL
        crepur["state"] = NORMAL
        delpur["state"] = NORMAL
        modifyinv["state"] = NORMAL
        modifyord["state"] = NORMAL
        modifyesti["state"] = NORMAL
    if not sixtabdataback:
      userpase.delete(0, END)
      usercpase.delete(0, END)
      creinv.deselect()
      delinv.deselect()
      voinv.deselect()
      markinv.deselect()
      creord.deselect()
      delord.deselect()
      turninv.deselect()
      smsinv.deselect()
      creestimate.deselect()
      delestimate.deselect()
      turnestiinv.deselect()
      creexpense.deselect()
      delexpense.deselect()
      rebillexpe.deselect()
      crecus.deselect()
      delcus.deselect()
      impcus.deselect()
      crepros.deselect()
      delpros.deselect()
      imppros.deselect()
      runrep.deselect()
      genrecinv.deselect()
      crepur.deselect()
      delpur.deselect()
      modifyinv.deselect()
      modifyord.deselect()
      modifyesti.deselect()
      if itemid == "adminstator":
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = DISABLED
        creinv["state"] = DISABLED
        delinv["state"] = DISABLED
        voinv["state"] = DISABLED
        markinv["state"] = DISABLED
        creord["state"] = DISABLED
        delord["state"] = DISABLED
        turninv["state"] = DISABLED
        smsinv["state"] = DISABLED
        creestimate["state"] = DISABLED
        delestimate["state"] = DISABLED
        turnestiinv["state"] = DISABLED
        creexpense["state"] = DISABLED
        delexpense["state"] = DISABLED
        rebillexpe["state"] = DISABLED
        crecus["state"] = DISABLED
        delcus["state"] = DISABLED
        impcus["state"] = DISABLED
        crepros["state"] = DISABLED
        delpros["state"] = DISABLED
        imppros["state"] = DISABLED
        runrep["state"] = DISABLED
        genrecinv["state"] = DISABLED
        crepur["state"] = DISABLED
        delpur["state"] = DISABLED
        modifyinv["state"] = DISABLED
        modifyord["state"] = DISABLED
        modifyesti["state"] = DISABLED
      else:
        userpase.delete(0, END)
        usercpase.delete(0, END)
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = NORMAL
        creinv["state"] = NORMAL
        delinv["state"] = NORMAL
        voinv["state"] = NORMAL
        markinv["state"] = NORMAL
        creord["state"] = NORMAL
        delord["state"] = NORMAL
        turninv["state"] = NORMAL
        smsinv["state"] = NORMAL
        creestimate["state"] = NORMAL
        delestimate["state"] = NORMAL
        turnestiinv["state"] = NORMAL
        creexpense["state"] = NORMAL
        delexpense["state"] = NORMAL
        rebillexpe["state"] = NORMAL
        crecus["state"] = NORMAL
        delcus["state"] = NORMAL
        impcus["state"] = NORMAL
        crepros["state"] = NORMAL
        delpros["state"] = NORMAL
        imppros["state"] = NORMAL
        runrep["state"] = NORMAL
        genrecinv["state"] = NORMAL
        crepur["state"] = NORMAL
        delpur["state"] = NORMAL
        modifyinv["state"] = NORMAL
        modifyord["state"] = NORMAL
        modifyesti["state"] = NORMAL
    else:
      userpase.delete(0, END)
      usercpase.delete(0, END)
      userpase.insert(0, sixtabdataback[4])
      usercpase.insert(0, sixtabdataback[5])
      if sixtabdataback[6] == 1:
        creinv.select()
      else:
        creinv.deselect()
      if sixtabdataback[7] == 1:
        delinv.select()
      else:
        delinv.deselect()
      if sixtabdataback[8] == 1:
        voinv.select()
      else:
        voinv.deselect()
      if sixtabdataback[9] == 1:
        markinv.select()
      else:
        markinv.deselect()
      if sixtabdataback[10] == 1:
        creord.select()
      else:
        creord.deselect()
      if sixtabdataback[11] == 1:
        delord.select()
      else:
        delord.deselect()
      if sixtabdataback[12] == 1:
        turninv.select()
      else:
        turninv.deselect()
      if sixtabdataback[13] == 1:
        smsinv.select()
      else:
        smsinv.deselect()
      if sixtabdataback[14] == 1:
        creestimate.select()
      else:
        creestimate.deselect()
      if sixtabdataback[15] == 1:
        delestimate.select()
      else:
        delestimate.deselect()
      if sixtabdataback[16] == 1:
        turnestiinv.select()
      else:
        turnestiinv.deselect()
      if sixtabdataback[17] == 1:
        creexpense.select()
      else:
        creexpense.deselect()
      if sixtabdataback[18] == 1:
        delexpense.select()
      else:
        delexpense.deselect()
      if sixtabdataback[19] == 1:
        rebillexpe.select()
      else:
        rebillexpe.deselect()
      if sixtabdataback[20] == 1:
        crecus.select()
      else:
        crecus.deselect()
      if sixtabdataback[21] == 1:
        delcus.select()
      else:
        delcus.deselect()
      if sixtabdataback[22] == 1:
        impcus.select()
      else:
        impcus.deselect()
      if sixtabdataback[23] == 1:
        crepros.select()
      else:
        crepros.deselect()
      if sixtabdataback[24] == 1:
        delpros.select()
      else:
        delpros.deselect()
      if sixtabdataback[25] == 1:
        imppros.select()
      else:
        imppros.deselect()
      if sixtabdataback[26] == 1:
        runrep.select()
      else:
        runrep.deselect()
      if sixtabdataback[27] == 1:
        genrecinv.select()
      else:
        genrecinv.deselect()
      if sixtabdataback[28] == 1:
        crepur.select()
      else:
        crepur.deselect()
      if sixtabdataback[29] == 1:
        delpur.select()
      else:
        delpur.deselect()
      if sixtabdataback[30] == 1:
        modifyinv.select()
      else:
        modifyinv.deselect()
      if sixtabdataback[31] == 1:
        modifyord.select()
      else:
        modifyord.deselect()
      if sixtabdataback[32] == 1:
        modifyesti.select()
      else:
        modifyesti.deselect()
         
  
  scrollbarx = Scrollbar(sixtab, orient=HORIZONTAL)
  scrollbary = Scrollbar(sixtab, orient=VERTICAL)
  uactree = ttk.Treeview(sixtab, columns=("1"),height=400,selectmode="extended", yscrollcommand=scrollbary.  set, xscrollcommand=scrollbarx.set)
  scrollbary.config(command=uactree.yview)
  scrollbary.place(x=245,y=100,height=300)
  uactree.heading('1', text="Username",)
  uactree.column('#0', stretch=NO, minwidth=0, width=0)
  uactree.column('1', stretch=NO, minwidth=0, width=218)
  uactree.place(x=30,y=100,height=300,width=220)
  uactree.bind('<Double-Button-1>' , focususer)
  sql = "select * from users"
  fbcursor.execute(sql)
  sixuactree = fbcursor.fetchall()
  coutset = 0
  if not sixuactree:
    uactree.insert('', index='end', text='hello', values=("adminstator"))
  else:
    for i in sixuactree:
      uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
      coutset += 1
  
  def adduser():
    uactree.insert('', index='end', text='hello', values=("Rename User"))
  
  btadd = Button(sixtab,text="Add new User",command=adduser)
  btadd.place(x=30,y=415)
  
  def users():
    itemid = uactree.item(uactree.focus())["values"][0]
    if itemid == "adminstator":
      messagebox.showerror('F-Billing Revolution', 'Cannot delete adminstator user.')
    else:
      delusermess = messagebox.askyesno("Delete user", "Are you sure to delete this user?")
      if delusermess == True:
        sql = "delete from users where username = %s"
        val = (itemid, )
        fbcursor.execute(sql, val)
        fbilldb.commit()
        for record in uactree.get_children():
          uactree.delete(record)
        sql = "select * from users"
        fbcursor.execute(sql)
        sixuactree = fbcursor.fetchall()
        coutset = 0
        for i in sixuactree:
          uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
          coutset += 1
      else:
        pass
        
  
  btdus = Button(sixtab,text="Delete User",command=users)
  btdus.place(x=180,y=415)
  
  userpro=LabelFrame(sixtab,text="User Profile", height=400, width=750)
  userpro.place(x=300, y=55)
  
  
  userna = Label(sixtab,text="Username")
  userna.place(x=340,y=90)
  usernae = Entry(sixtab,)
  usernae.place(x=460,y=90)
  
  userpas = Label(sixtab,text="Password")
  userpas.place(x=340,y=120)
  userpase = Entry(sixtab,)
  userpase.place(x=460,y=120)
  
  usercpas = Label(sixtab,text="Confirm Password")
  usercpas.place(x=340,y=150)
  usercpase = Entry(sixtab,)
  usercpase.place(x=460,y=150)
  
  saveuserprofile = Button(sixtab,text="save user profile",command=user)
  saveuserprofile.place(x=650,y=120)
  
  creinvbol = BooleanVar()
  creinv = Checkbutton(sixtab,text="Create invoice",onvalue= 1 ,offvalue= 0,variable=creinvbol)
  creinv.place(x=340,y=200)
  delinvbol = BooleanVar()
  delinv = Checkbutton(sixtab,text="Delete invoice",onvalue= 1 ,offvalue= 0,variable=delinvbol)
  delinv.place(x=340,y=225)
  voinvbol = BooleanVar()
  voinv = Checkbutton(sixtab,text="Void invoice",onvalue= 1 ,offvalue= 0,variable=voinvbol)
  voinv.place(x=340,y=250)
  markinvbol = BooleanVar()
  markinv = Checkbutton(sixtab,text="Mark invoice as Paid",onvalue= 1 ,offvalue= 0,variable=markinvbol)
  markinv.place(x=340,y=275)
  
  creordbol = BooleanVar()
  creord = Checkbutton(sixtab,text="Create Order",onvalue= 1 ,offvalue= 0,variable=creordbol)
  creord.place(x=500,y=200)
  delordbol = BooleanVar()
  delord = Checkbutton(sixtab,text="Delete Order",onvalue= 1 ,offvalue= 0,variable=delordbol)
  delord.place(x=500,y=225)
  turninvbol = BooleanVar()
  turninv = Checkbutton(sixtab,text="Turn order into invoice",onvalue= 1 ,offvalue= 0,variable=turninvbol)
  turninv.place(x=500,y=250)
  smsinvbol = BooleanVar()
  smsinv = Checkbutton(sixtab,text="Send sms nofitication",onvalue= 1 ,offvalue= 0,variable=smsinvbol)
  smsinv.place(x=500,y=275)
  
  creestimatebol = BooleanVar()
  creestimate = Checkbutton(sixtab,text="Create estimate",onvalue= 1 ,offvalue= 0,variable=creestimatebol)
  creestimate.place(x=680,y=200)
  delestimatebol = BooleanVar()
  delestimate = Checkbutton(sixtab,text="Delete estimate",onvalue= 1 ,offvalue= 0,variable=delestimatebol)
  delestimate.place(x=680,y=225)
  turnestiinvbol = BooleanVar()
  turnestiinv = Checkbutton(sixtab,text="Turn estimates into invoice",onvalue= 1 ,offvalue= 0,  variable=turnestiinvbol)
  turnestiinv.place(x=680,y=250)
  
  creexpensebol = BooleanVar()
  creexpense = Checkbutton(sixtab,text="Create expenses",onvalue= 1 ,offvalue= 0,variable=creexpensebol)
  creexpense.place(x=880,y=200)
  delexpensebol = BooleanVar()
  delexpense = Checkbutton(sixtab,text="Delete expenses",onvalue= 1 ,offvalue= 0,variable=delexpensebol)
  delexpense.place(x=880,y=225)
  rebillexpebol = BooleanVar()
  rebillexpe = Checkbutton(sixtab,text="Rebill expenses",onvalue= 1 ,offvalue= 0,variable=rebillexpebol)
  rebillexpe.place(x=880,y=250)
  
  crecusbol = BooleanVar()
  crecus = Checkbutton(sixtab,text="Create customer",onvalue= 1 ,offvalue= 0,variable=crecusbol)
  crecus.place(x=340,y=320)
  delcusbol = BooleanVar()
  delcus = Checkbutton(sixtab,text="Delete customer",onvalue= 1 ,offvalue= 0,variable=delcusbol)
  delcus.place(x=340,y=340)
  impcusbol = BooleanVar()
  impcus = Checkbutton(sixtab,text="Import customer",onvalue= 1 ,offvalue= 0,variable=impcusbol)
  impcus.place(x=340,y=360)
  
  creprosbol = BooleanVar()
  crepros = Checkbutton(sixtab,text="Create product\services",onvalue= 1 ,offvalue= 0,variable=creprosbol)
  crepros.place(x=500,y=320)
  delprosbol = BooleanVar()
  delpros = Checkbutton(sixtab,text="Delete product\services",onvalue= 1 ,offvalue= 0,variable=delprosbol)
  delpros.place(x=500,y=340)
  impprosbol = BooleanVar()
  imppros = Checkbutton(sixtab,text="Import product\services",onvalue= 1 ,offvalue= 0,variable=impprosbol)
  imppros.place(x=500,y=360)
  
  runrepbol = BooleanVar()
  runrep = Checkbutton(sixtab,text="Run reports",onvalue= 1 ,offvalue= 0,variable=runrepbol)
  runrep.place(x=680,y=320)
  genrecinvbol = BooleanVar()
  genrecinv = Checkbutton(sixtab,text="Generate recurring invoices",onvalue= 1 ,offvalue= 0,  variable=genrecinvbol)
  genrecinv.place(x=680,y=340)
  
  crepurbol = BooleanVar()
  crepur = Checkbutton(sixtab,text="Create Purchase order",onvalue =1 ,offvalue = 0,variable=crepurbol)
  crepur.place(x=880,y=320)
  delpurbol = BooleanVar()
  delpur = Checkbutton(sixtab,text="Delete Purchase order",onvalue =1 ,offvalue = 0,variable=delpurbol)
  delpur.place(x=880,y=340)
  
  undersetlab = Label(sixtab,text="Under Settings menu tab")
  undersetlab.place(x=340,y=400)
  
  modifyinvbol = BooleanVar()
  modifyinv = Checkbutton(sixtab,text="Modify invoice settings",onvalue =1 ,offvalue = 0,variable=modifyinvbol)
  modifyinv.place(x=340,y=425)
  
  modifyordbol = BooleanVar()
  modifyord = Checkbutton(sixtab,text="Modify order settings",onvalue =1 ,offvalue = 0,variable=modifyordbol)
  modifyord.place(x=500,y=425)
  
  modifyestibol = BooleanVar()
  modifyesti = Checkbutton(sixtab,text="Modify estimate settings",onvalue =1 ,offvalue = 0,  variable=modifyestibol)
  modifyesti.place(x=680,y=425)
root.mainloop()

