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

  ###########################    Expense Module   ##############################
  
  def add_expense():
      def upload_file():
        import shutil
        global filename,img, b2
        f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        print(filename, 'name')
        #import pdb; pdb.set_trace()
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        image = Image.open(filename)
        resize_image = image.resize((120, 120))
        img = ImageTk.PhotoImage(resize_image)
        b2 = Label(expenselabelframe,image=img, height=120, width=120)
        b2.place(x=450, y=240)
      
      global filename
      filename = ""
      def insert_expenses():# insert expenses data
        expense_amount = expamountval.get()
        date = expdate.get_date()
        vendor = vn.get()
        catagory = cn.get()
        description = expdescriptionentry.get()
        staff_members = expstaffentry.get()
        taxable = checkvarStatus4.get()
        customer = cus.get()
        id_sku = id_sku1.get()
        notes = exptxt.get('1.0', 'end-1c')
        rebill_amount = rebill_amoun.get()
        rebillab = rebill.get()
        recipt = imge.get()
        assign_cus = other.get()
        tax2 = tax2expstr.get()
    
        if filename == "":
          sql='INSERT INTO Expenses (expense_amount,date,vendor,catagory,description,staff_members,taxable,    customer,id_sku,notes,rebill_amount,rebillable,receipt,assign_customer,tax2) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,  %s,  %s,%s,%s,%s,%s,%s)' #adding values into db
          val=(expense_amount,date,vendor,catagory,description,staff_members,taxable,customer,id_sku,notes,    rebill_amount,rebillab,recipt,assign_cus,tax2)
          fbcursor.execute(sql,val)
          fbilldb.commit()
        else:
          shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
          sql='INSERT INTO Expenses (expense_amount,date,vendor,catagory,description,staff_members,taxable,customer,id_sku,notes,rebill_amount,image,rebillable,receipt,assign_customer,tax2) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' #adding values into db
          val=(expense_amount,date,vendor,catagory,description,staff_members,taxable,customer,id_sku,notes,  rebill_amount,filename.split('/')[-1],rebillab,recipt,assign_cus,tax2)
          fbcursor.execute(sql,val)
          fbilldb.commit()
        for record in exp_tree.get_children():
          exp_tree.delete(record)
        count=0
        fbcursor.execute('SELECT * FROM Expenses;')
        for i in fbcursor:
          if True:
            if i[13] == '1':
              e = 'Yes'
            else:
              e = 'No'
            exp_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[0], i[10], i[4], i[6], i[5], i[8], i[7], e , i[14], i[11],i[16],i[3]))
          count += 1
        window.destroy()


    

     
  
      window = Toplevel()  
      
      window.title("Add new Expense")
      window.resizable(0,0)
      p2 = PhotoImage(file = 'images/fbicon.png')
      window.iconphoto(False, p1)
  
      window.geometry("618x449+380+167")
  
      innerexpFrame = Frame(window, relief=GROOVE)
      innerexpFrame.pack(side="top",fill=BOTH)
  
      expenselabelframe = LabelFrame(innerexpFrame,text="Expense Cost",width=580,height=400)
      expenselabelframe.pack(side="top",fill=BOTH,padx=10)
  
      def number_expacount(S,d):
        sql = "select decimalseperator from company"
        fbcursor.execute(sql)
        deci_sgin = fbcursor.fetchone()
        if deci_sgin[0] == '.':
          if d == '1': #insert
            if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
              return False
            return True
        elif deci_sgin[0] == ',':
          if d == '1': #insert
            if not S in ['0','1','2','3','4','5','6','7','8','9',',']:
              return False
            return True
        if d.isdigit():
          return True
        
        
  
      def expaonclick(event):
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if not currsymb:
          pass
        else:
          if currsymb[1] == "before amount":
            expamountentry.insert (0, currsymb[0])
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='left')
          elif currsymb[1] == "before amount with space":
            expamountentry.insert (0, currsymb[0] + " ")
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='left')
          elif currsymb[1] == "after amount":
            expamountval.set(currsymb[0])
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='right')
          elif currsymb[1] == "after amount with space":
            expamountval.set(" " + currsymb[0])
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='right')
          else:
            pass
          
  
  
  
      expamountval = StringVar(expenselabelframe,)
      expamount=Label(expenselabelframe,text="Expense amount:",pady=10,padx=10)
      expamount.place(x=12,y=0)
      expamountentry = Entry(expenselabelframe,width=15,textvariable=expamountval)
    
      expamountentry.bind("<ButtonRelease>", expaonclick)
      expamountentry.place(x=130,y=10)
  
      
  
  
  
  
      lbl_date=Label(expenselabelframe,text=" Date :",fg='black')
      lbl_date.place(x=380,y=10)
      
      expdate=DateEntry(expenselabelframe)
      expdate.place(x=450,y=12)

      sql = "select dateformat from company"
      fbcursor.execute(sql)
      date_for = fbcursor.fetchone()
     
      if not date_for:
        pass
      else:
        if date_for[0] == "mm-dd-yyyy":
          expdate._set_text(expdate._date.strftime('%m-%d-%Y'))
        elif date_for[0] == "dd-mm-yyyy":
          expdate._set_text(expdate._date.strftime('%d-%m-%Y'))
        elif date_for[0] == "yyy.mm.dd":
          expdate._set_text(expdate._date.strftime('%Y.%m.%d'))
        elif date_for[0] == "mm/dd/yyyy":
          expdate._set_text(expdate._date.strftime('%m/%d/%Y'))
        elif date_for[0] == "dd/mm/yyy":
          expdate._set_text(expdate._date.strftime('%d/%m/%Y'))
        elif date_for[0] == "dd.mm.yyyy":
          expdate._set_text(expdate._date.strftime('%d.%m.%Y'))
        elif date_for[0] == "yyyy/mm/dd":
          expdate._set_text(expdate._date.strftime('%Y/%m/%d'))
        else:
          pass
  
      sql = "select businessname from Customer where customertype =%s or customertype =%s"
      val = ('vendor','both(client,vendor)')
      fbcursor.execute(sql,val)
      pdata = fbcursor.fetchall()
  
      vendor1=Label(expenselabelframe,text="Vendor:",pady=5,padx=10)
      vendor1.place(x=20,y=40)
      vn = StringVar() 
      vendor = ttk.Combobox(expenselabelframe, width = 27, textvariable = vn ) 
        
      # Adding combobox drop down list 
      vendor['values'] = pdata
        
      vendor.place(x=130,y=45) 
      # vendor.current(0)
  
      categoryexp1=Label(expenselabelframe,text="Category:",pady=5,padx=10)
      categoryexp1.place(x=330,y=40)
      cn = StringVar() 
      categorydrop = ttk.Combobox(expenselabelframe, width = 22, textvariable = cn ) 
        
      # Adding combobox drop down list 
      categorydrop['values'] = ('Default' ) 
        
      categorydrop.place(x=400,y=45) 
      categorydrop.current(0)
  
      
  
      expdescription=Label(expenselabelframe,text="Description:",pady=10,padx=10)
      expdescription.place(x=12,y=70)
      expdescriptionentry = Entry(expenselabelframe,width=70)
      expdescriptionentry.place(x=130,y=81)
  
      expstafftval = StringVar(expenselabelframe, value='Administrator')
      expstaff=Label(expenselabelframe,text="Staff member:",pady=10,padx=10)
      expstaff.place(x=12,y=108)
      expstaffentry = Entry(expenselabelframe,width=30,textvariable=expstafftval)
      expstaffentry.place(x=130,y=118)
  
      sql = "select taxtype from company"
      fbcursor.execute(sql)
      taxchoose = fbcursor.fetchone()
      
      
      
      checkvarStatus4=BooleanVar()
    
      Button4 = Checkbutton(expenselabelframe,variable = checkvarStatus4, 
                        text="Taxable Tax1 rate", 
                        onvalue ='1' ,
                        offvalue = '0',
                       )
      
      tax2expstr = BooleanVar()
      tax2exp = Checkbutton(expenselabelframe,variable = tax2expstr, 
                        text="Taxable Tax2 rate", 
                        onvalue ='1' ,
                        offvalue = '0',
                        )
  
      if not taxchoose:
        pass
      elif taxchoose[0] == '1':
        Button4.place_forget()
        tax2exp.place_forget()
      elif taxchoose[0] == '2':
        Button4.place(x=400,y=125)
        tax2exp.place_forget()
      elif taxchoose[0] == '3':
        tax2exp.place(x=400,y=105)
        Button4.place(x=400,y=125)
  
      sql = "select businessname from Customer"
      fbcursor.execute(sql,)
      cusdata = fbcursor.fetchall()
      print(cusdata)
  
      def toggle():
        if other.get():
          ent.place(x=45,y=180)
          button51.place(x=250, y=160)
        else:
          ent.place_forget()
          button51.place_forget()
          button51.deselect()
          ent.delete(0, END)
          id_skuentry.delete(0,END)
          rebill_entry.delete(0,END)
          id_skulabel.place_forget()
          id_skuentry.place_forget()
          rebill_label.place_forget()
          rebill_entry.place_forget()
      other = BooleanVar()
      button5 = Checkbutton(expenselabelframe, text="Assign to customer (optional)", variable=other, 
      command=toggle)
      button5.place(x=40, y=160)
      cus = StringVar()
      ent=ttk.Combobox(expenselabelframe,width=30,textvariable=cus,values=cusdata)
  
      ent.delete(0,'end')
      def toggle():
        id_skuentry.delete(0, END)
        rebill_entry.delete(0, END)
        if rebill.get():
          id_skulabel.place(x=375,y=160)
          id_skuentry.place(x=420,y=160)
          rebill_label.place(x=335,y=180)
          rebill_entry.place(x=420, y=180)
        else:
          id_skulabel.place_forget()
          id_skuentry.place_forget()
          rebill_label.place_forget()
          rebill_entry.place_forget()
      rebill = BooleanVar()

      sql = "select * from users"
      fbcursor.execute(sql)
      rebill_check_user = fbcursor.fetchall()
      
      if not rebill_check_user:
        button51 = Checkbutton(expenselabelframe, text="Rebillable" ,variable=rebill, command=toggle,onvalue   ='Yes' ,offvalue = 'NO')
      else:
        try:
          user_namech = username1.get()
          sql = "select rebill_exprense from users where username = %s"
          val = (user_namech,)
          fbcursor.execute(sql,val)
          disable_rebillabe_exp = fbcursor.fetchone()
          if disable_rebillabe_exp[0] == 1:
            button51 = Checkbutton(expenselabelframe, text="Rebillable" ,variable=rebill, command=toggle,onvalue   ='Yes' ,offvalue = 'NO')
          else:
            pass
        except:
           button51 = Checkbutton(expenselabelframe, text="Rebillable" ,variable=rebill, command=toggle,onvalue   ='Yes' ,offvalue = 'NO')
      
    
      
      id_sku1 = StringVar()
      id_skulabel=Label(expenselabelframe,text="id_sku:")
      id_skuentry = Entry(expenselabelframe,width=15,textvariable=id_sku1)
    
      def number_rebill_amoun(S,d):
        sql = "select decimalseperator from company"
        fbcursor.execute(sql)
        deci_sgin = fbcursor.fetchone()
        if deci_sgin[0] == '.':
          if d == '1': #insert
            if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
              return False
            return True
        elif deci_sgin[0] == ',':
          if d == '1': #insert
            if not S in ['0','1','2','3','4','5','6','7','8','9',',']:
              return False
            return True
        if d.isdigit():
          return True
        
        
        
  
      def rebillamoonclick(event):
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if currsymb[1] == "before amount":
          rebill_entry.insert (0, currsymb[0])
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='left')
        elif currsymb[1] == "before amount with space":
          rebill_entry.insert (0, currsymb[0] + " ")
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='left')
        elif currsymb[1] == "after amount":
          rebill_amoun.set(currsymb[0])
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='right')
        elif currsymb[1] == "after amount with space":
          rebill_amoun.set(" " + currsymb[0])
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='right')
  
      rebill_amoun = StringVar()
      rebill_label=Label(expenselabelframe,text="Rebill amount:")
      rebill_entry = Entry(expenselabelframe,width=15,textvariable=rebill_amoun)
      rebill_entry.bind("<ButtonRelease>", rebillamoonclick)
      
  
  
      
      
      def toggle():
        if imge.get():
          browseimg.place(x=40,y=220)
          browsebutton.place(x=350,y=220,height=30,width=50)
          
        else:
          browseimg.place_forget()
          browsebutton.place_forget()
        
      imge = BooleanVar()
      Button6 = Checkbutton(expenselabelframe, text = "Attach receipt image(optional,image will be stored to   the database)",command=toggle,variable=imge)
      Button6.place(x=40, y=200)
      browseimg=Label(expenselabelframe,text="(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
      browsebutton=Button(expenselabelframe,text = 'Browse',command=upload_file)
  
  
      exptext1=Label(expenselabelframe,text="Notes",pady=5,padx=10)
      exptext1.place(x=12,y=246)
      exptxt = scrolledtext.ScrolledText(expenselabelframe, undo=True,width=50,height=5)
      exptxt.place(x=22,y=280)
  
      expokButton = Button(window, text ="Ok",image=tick,width=70,compound = LEFT,command=insert_expenses)
      expokButton.place(x=280,y=415)
  
      window.mainloop()
  

  def add_expense_connection():
    sql = "select * from users"
    fbcursor.execute(sql)
    addexp_check_user = fbcursor.fetchall()
    if not addexp_check_user:
      add_expense()
    else:
      try:
        user_namech = username1.get()
        sql = "select create_expense from users where username = %s"
        val = (user_namech,)
        fbcursor.execute(sql,val)
        disable_create_exp = fbcursor.fetchone()
        if disable_create_exp[0] == 1:
          add_expense()
        else:
          messagebox.showerror("user","user does not have permission to perform this action")
      except:
        add_expense()
        
      
      
  
      
    

  

  

########################VIEW/EDIT EXPENSE#######################################################################



  def edit_expense():

    try:
      itemid = exp_tree.item(exp_tree.focus())["values"][0]
      sql = "select * from Expenses where expensesid = %s"
      val = (itemid, )

      fbcursor.execute(sql, val)
      psdata = fbcursor.fetchone()
      def upload_file1():
        global filename,img, b1
        f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        #import pdb; pdb.set_trace()
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        image = Image.open(filename)
        resize_image = image.resize((120, 120))
        img = ImageTk.PhotoImage(resize_image)
        b1 = Label(expenselabelframe,image=img, height=120, width=120)
        b1.place(x=450, y=240)

      global filename
      filename = ""
      def update_expenses():# Storing values into db (user)
        itemid = exp_tree.item(exp_tree.focus())["values"][0]
        expense_amount = expamountval.get()
        date = expdate.get_date()
        vendor = vn.get()
        catagory = cn.get()
        description = expdescriptionentry.get()
        staff_members = expstafftval.get()
        taxable = checkvarStatus4.get()
        customer = cus.get()
        id_sku = id_sku1.get()
        notes = exptxt.get('1.0', 'end-1c')
        rebill_amount = rebill_amoun.get()
        rebillabe = rebill.get()
        assign_cus = other.get()
        recepit = imge.get()
        tax2 = tax2expstr.get()

        itemid1 = exp_tree.item(exp_tree.focus())["values"][0]
        sq = 'select image from Expenses where expensesid = %s'
        va =(itemid1,)
        fbcursor.execute(sq,va)
        up = fbcursor.fetchone()
        # file = shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        if filename == "":
          sql='UPDATE Expenses set expense_amount=%s,date=%s,vendor=%s,catagory=%s,description=%s,    staff_members=%s,taxable=%s,customer=%s,id_sku=%s,notes=%s,rebill_amount=%s,rebillable=%s,assign_customer=%s,receipt=%s,tax2=%s where expensesid=%s'
          val=(expense_amount,date,vendor,catagory,description,staff_members,taxable,customer,id_sku,notes,
          rebill_amount,rebillabe,assign_cus,recepit,tax2,itemid)
          fbcursor.execute(sql,val)
          fbilldb.commit()
        else:
          file = shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
          sql='UPDATE Expenses set expense_amount=%s,date=%s,vendor=%s,catagory=%s,description=%s,    staff_members=%s,taxable=%s,customer=%s,id_sku=%s,notes=%s,rebill_amount=%s,image=%s,rebillable=%s,assign_customer=%s,receipt=%s,tax2=%s where expensesid=%s'
          val=(expense_amount,date,vendor,catagory,description,staff_members,taxable,customer,id_sku,notes,
          rebill_amount,filename.split('/')[-1],rebillabe,assign_cus,recepit,tax2,itemid)
          fbcursor.execute(sql,val)
          fbilldb.commit()
        for record in exp_tree.get_children():
            exp_tree.delete(record)
        count=0
        fbcursor.execute('SELECT * FROM Expenses;')
        for i in fbcursor:
            if True:
              if i[13] == '1':
                e = 'Yes'
              else:
                e = 'No'
              exp_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[0], i[10], i[4], i[6], i[5], i[8], i[7], e , i[14], i[11],i[16],i[3]))
            else:
                pass
        count += 1
        window1.destroy()
      
      
      window1 = Toplevel()  
      
      window1.title("Edit Expense")
      p2 = PhotoImage(file = 'images/fbicon.png')
      # recimage= PhotoImage(file= 'images/'+psdata[11])
     
      # image = Image.open(recimage)
      # resize_image = image.resize((120, 120))
      # imga = ImageTk.PhotoImage(resize_image)
      window1.iconphoto(False, p1)
   
      window1.geometry("618x449+380+167")
  
      innerexpFrame = Frame(window1, relief=GROOVE)
      innerexpFrame.pack(side="top",fill=BOTH)
  
      expenselabelframe = LabelFrame(innerexpFrame,text="Expense Cost",width=580,height=400)
      expenselabelframe.pack(side="top",fill=BOTH,padx=10)
  
      def number_expacount(S,d):
        sql = "select decimalseperator from company"
        fbcursor.execute(sql)
        deci_sgin = fbcursor.fetchone()
        if deci_sgin[0] == '.':
          if d == '1': #insert
            if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
              return False
            return True
        elif deci_sgin[0] == ',':
          if d == '1': #insert
            if not S in ['0','1','2','3','4','5','6','7','8','9',',']:
              return False
            return True
        if d.isdigit():
          return True
        
        
  
      def expaonclick(event):
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if not currsymb:
          pass
        else:
          if currsymb[1] == "before amount":
            expamountentry.delete (0, END)
            expamountentry.insert (0, currsymb[0])
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='left')
          elif currsymb[1] == "before amount with space":
            expamountentry.delete (0, END)
            expamountentry.insert (0, currsymb[0] + " ")
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='left')
          elif currsymb[1] == "after amount":
            expamountentry.delete (0, END)
            expamountval.set(currsymb[0])
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='right')
          elif currsymb[1] == "after amount with space":
            expamountentry.delete (0, END)
            expamountval.set(" " + currsymb[0])
            expamountnum = (expenselabelframe.register(number_expacount),'%S','%d')
            expamountentry.config(validate='key',validatecommand=(expamountnum),justify='right')
          else:
            pass
      expamountval = StringVar()
      expamount=Label(expenselabelframe,text="Expense amount:",pady=10,padx=10)
      expamount.place(x=12,y=0)
      expamountentry = Entry(expenselabelframe,width=15,textvariable=expamountval)
      expamountentry.bind("<ButtonRelease>", expaonclick)
      expamountentry.place(x=130,y=10)
      expamountentry.delete(0,'end')
      expamountentry.insert(0, psdata[3])
  
      lbl_date=Label(expenselabelframe,text=" Date :",fg='black')
      lbl_date.place(x=380,y=10)
      
      
      expdate=DateEntry(expenselabelframe)
      expdate.place(x=450,y=12)
      expdate.delete(0,'end')
      expdate.insert(0, psdata[4])

      sql = "select dateformat from company"
      fbcursor.execute(sql)
      date_for = fbcursor.fetchone()
     
      if not date_for:
        pass
      else:
        if date_for[0] == "mm-dd-yyyy":
          expdate._set_text(expdate._date.strftime('%m-%d-%Y'))
        elif date_for[0] == "dd-mm-yyyy":
          expdate._set_text(expdate._date.strftime('%d-%m-%Y'))
        elif date_for[0] == "yyy.mm.dd":
          expdate._set_text(expdate._date.strftime('%Y.%m.%d'))
        elif date_for[0] == "mm/dd/yyyy":
          expdate._set_text(expdate._date.strftime('%m/%d/%Y'))
        elif date_for[0] == "dd/mm/yyy":
          expdate._set_text(expdate._date.strftime('%d/%m/%Y'))
        elif date_for[0] == "dd.mm.yyyy":
          expdate._set_text(expdate._date.strftime('%d.%m.%Y'))
        elif date_for[0] == "yyyy/mm/dd":
          expdate._set_text(expdate._date.strftime('%Y/%m/%d'))
        else:
          pass
      
      

      sql = "select businessname from Customer where customertype =%s or customertype =%s"
      val = ('vendor','both(client,vendor)')
      fbcursor.execute(sql,val)
      pdat = fbcursor.fetchall()
      vendor1=Label(expenselabelframe,text="Vendor:",pady=5,padx=10)
      vendor1.place(x=20,y=40)
      vn = StringVar() 
      vendor = ttk.Combobox(expenselabelframe, width = 27, textvariable = vn ) 
     
        
      # Adding combobox drop down list 
      vendor['values'] = pdat
        
      vendor.place(x=130,y=45) 
      vendor.delete(0,'end')
      vendor.insert(0, psdata[5]) 
  
      categoryexp1=Label(expenselabelframe,text="Category:",pady=5,padx=10)
      categoryexp1.place(x=330,y=40)
      cn = StringVar() 
      categorydrop = ttk.Combobox(expenselabelframe, width = 22, textvariable = cn ) 
      categorydrop.delete(0,'end')
      categorydrop.insert(0, psdata[6])
   
        
      # Adding combobox drop down list 
      categorydrop['values'] = ('Default') 
        
      categorydrop.place(x=400,y=45)
    
  
      
  
      expdescription=Label(expenselabelframe,text="Description:",pady=10,padx=10)
      expdescription.place(x=12,y=70)
      expdescriptionentry = Entry(expenselabelframe,width=70)
      expdescriptionentry.place(x=130,y=81)
      expdescriptionentry.delete(0,'end')
      expdescriptionentry.insert(0, psdata[7])
  
      expstafftval = StringVar(expenselabelframe, value='Administrator')
      expstaff=Label(expenselabelframe,text="Staff member:",pady=10,padx=10)
      expstaff.place(x=12,y=108)
      expstaffentry = Entry(expenselabelframe,width=30,textvariable=expstafftval)
      expstaffentry.place(x=130,y=118)
      expstaffentry.delete(0,'end')
      expstaffentry.insert(0, psdata[8])


      
      sql = "select taxtype from company"
      fbcursor.execute(sql)
      taxchoose = fbcursor.fetchone()

  
      checkvarStatus4=BooleanVar()
     
      Button4 = Checkbutton(expenselabelframe,variable = checkvarStatus4, 
                        text="Taxable Tax1 rate", 
                        onvalue ='1',
                        offvalue = '0',
                        )
              
      tax2expstr = BooleanVar()
      tax2exp = Checkbutton(expenselabelframe,variable = tax2expstr, 
                        text="Taxable Tax2 rate", 
                        onvalue ='1' ,
                        offvalue = '0',
                        )

      if not taxchoose:
        pass
      elif taxchoose[0] == '1':
        Button4.place_forget()
        tax2exp.place_forget()
      elif taxchoose[0] == '2':
        Button4.place(x=400,y=125)
        tax2exp.place_forget()
      elif taxchoose[0] == '3':
        tax2exp.place(x=400,y=105)
        Button4.place(x=400,y=125)
  
      # Button4.bind("<Button-1>", getBool)
      
      ps = psdata[9]
      if ps == "1":
       Button4.select()
      else:
        Button4.deselect()
      
     
      if psdata[19] == "1":
        tax2exp.select()
      else:
        tax2exp.deselect()
          
      
 
  
      sql = "select businessname from Customer"
      fbcursor.execute(sql,)
      cusdta = fbcursor.fetchall()
      
  
      def toggle():
        if other.get():
          ent.place(x=45,y=180)
          try:
            user_namech = username1.get()
            sql = "select rebill_exprense from users where username = %s"
            val = (user_namech,)
            fbcursor.execute(sql,val)
            disable_rebillabe_exp = fbcursor.fetchone()
            if disable_rebillabe_exp[0] == 1:
              button51.place(x=250, y=160)
            else:
              id_skuentry.place_forget()
              rebill_entry.place_forget()
              button51.place_forget()
          except:
            button51.place(x=250, y=160)
        else:
          button51.deselect()
          ent.place_forget()
          button51.place_forget()
           
          ent.delete(0, END)
          id_skuentry.delete(0,END)
          rebill_entry.delete(0,END)
          id_skulabel.place_forget()
          id_skuentry.place_forget()
          rebill_label.place_forget()
          rebill_entry.place_forget()
      other = BooleanVar()
      button5 = Checkbutton(expenselabelframe, text="Assign to customer (optional)", variable=other, 
      command=toggle)
      button5.place(x=40, y=160)
      cus = StringVar()
      ent=ttk.Combobox(expenselabelframe,width=30,textvariable=cus)
      ent['values'] = cusdta
      ent.delete(0,'end')
      ent.insert(0, psdata[10])
      
      

      def toggle():
        if rebill.get():
          id_skuentry.delete(0,END)
          rebill_entry.delete(0,END)
          id_skulabel.place(x=375,y=160)
          id_skuentry.place(x=420,y=160)
          rebill_label.place(x=335,y=180)
          rebill_entry.place(x=420, y=180)
        else:
          id_skuentry.delete(0,END)
          rebill_entry.delete(0,END)
          id_skulabel.place_forget()
          id_skuentry.place_forget()
          rebill_label.place_forget()
          rebill_entry.place_forget()
      rebill = BooleanVar()
      button51 = Checkbutton(expenselabelframe, text="Rebillable" ,variable=rebill, command=toggle,onvalue=1,offvalue=0)

      
      # sql = "select * from users"
      # fbcursor.execute(sql)
      # rebill_check_user = fbcursor.fetchall()
      
      # if not rebill_check_user:
      #   pass
      # else:
      #   # try:
      #     user_namech = username1.get()
      #     sql = "select rebill_exprense from users where username = %s"
      #     val = (user_namech,)
      #     fbcursor.execute(sql,val)
      #     disable_rebillabe_exp = fbcursor.fetchone()
      #     if disable_rebillabe_exp[0] == 1:
      #       button51.place_forget()
      #     else:
      #       pass
      #   # except:
        #    pass
      
      cns = psdata[17]
      if cns == '1':
        button5.select()
        ent.place(x=45,y=180)
        button51.place(x=250, y=160)
      else:
        button5.deselect()
        try:
          user_namech = username1.get()
          sql = "select rebill_exprense from users where username = %s"
          val = (user_namech,)
          fbcursor.execute(sql,val)
          disable_rebillabe_exp = fbcursor.fetchone()
          if disable_rebillabe_exp[0] == 1:
            pass
          else:
            button51.place_forget()
        except:
          pass
        
      
      
      id_sku1 = StringVar()
      id_skulabel=Label(expenselabelframe,text="id_sku:")
      id_skuentry = Entry(expenselabelframe,width=15,textvariable=id_sku1)
      id_skuentry.delete(0,'end')
      id_skuentry.insert(0, psdata[15])
      
      def number_rebill_amoun(S,d):
        sql = "select decimalseperator from company"
        fbcursor.execute(sql)
        deci_sgin = fbcursor.fetchone()
        if deci_sgin[0] == '.':
          if d == '1': #insert
            if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
              return False
            return True
        elif deci_sgin[0] == ',':
          if d == '1': #insert
            if not S in ['0','1','2','3','4','5','6','7','8','9',',']:
              return False
            return True
        if d.isdigit():
          return True
        
        
        
  
      def rebillamoonclick(event):
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if currsymb[1] == "before amount":
          rebill_entry.insert (0, currsymb[0])
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='left')
        elif currsymb[1] == "before amount with space":
          rebill_entry.insert (0, currsymb[0] + " ")
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='left')
        elif currsymb[1] == "after amount":
          rebill_amoun.set(currsymb[0])
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='right')
        elif currsymb[1] == "after amount with space":
          rebill_amoun.set(" " + currsymb[0])
          rebi_amo = (expenselabelframe.register(number_rebill_amoun),'%S','%d')
          rebill_entry.config(validate='key',validatecommand=(rebi_amo),justify='right')
      rebill_amoun = StringVar()
      rebill_label=Label(expenselabelframe,text="Rebill amount:")
      rebill_entry = Entry(expenselabelframe,width=15,textvariable=rebill_amoun)
      rebill_entry.bind("<ButtonRelease>", rebillamoonclick)
      rebill_entry.delete(0,'end')
      rebill_entry.delete(0,'end')
      rebill_entry.insert(0, psdata[16])

      reb = psdata[13]
      print(ps)
      if reb == '1':
        button51.select()
        id_skulabel.place(x=375,y=160)
        id_skuentry.place(x=420,y=160)
        rebill_label.place(x=335,y=180)
        rebill_entry.place(x=420, y=180)
      else:
        button51.deselect()
  
  
      
      
      def toggle():
        if imge.get():
          browseimg.place(x=40,y=220)
          browsebutton.place(x=350,y=220,height=30,width=50)
          b2.place(x=450, y=240)

        else:
          browseimg.place_forget()
          browsebutton.place_forget()
          b2.place_forget()
        
      imge = BooleanVar()
      Button6 = Checkbutton(expenselabelframe, text = "Attach receipt image(optional,image will be stored   to the database)",command=toggle,variable=imge)
      Button6.place(x=40, y=200)
      browseimg=Label(expenselabelframe,text="(recommended image type:JPG,size 480x320 pixels) ",  bg='#f5f3f2')
      browsebutton=Button(expenselabelframe,text = 'Browse', command=upload_file1)
     
      try:
        image = Image.open("images/"+psdata[11])
        resize_image = image.resize((120, 120))
        recimage = ImageTk.PhotoImage(resize_image)
        b2 = Button(expenselabelframe,image=recimage, height=120, width=120,)
        b2.photo = recimage
        print(image)
      except:
        pass
      
      
      rec = psdata[18]
      print(rec)
      if rec == '1':
        Button6.select()
        browseimg.place(x=40,y=220)
        browsebutton.place(x=350,y=220,height=30,width=50)
        b2.place(x=450, y=240)
      else:
        Button6.deselect()

  
      exptext1=Label(expenselabelframe,text="Notes",pady=5,padx=10)
      exptext1.place(x=12,y=246)
      exptxt = scrolledtext.ScrolledText(expenselabelframe, undo=True,width=50,height=5)
      exptxt.place(x=22,y=280)
      exptxt.delete('1.0','end')
      exptxt.insert('1.0', psdata[12])

      expokButton = Button(window1, text ="Ok",image=tick,width=70,compound = LEFT,command=update_expenses)
      expokButton.place(x=280,y=415)
    except:
        try:
            window1.destroy()
        except: 
            pass
        messagebox.showerror('F-Billing Revolution', 'Select a record to edit.')
    

  
      
  def file_image(event):
    itemid = exp_tree.item(exp_tree.focus())["values"][0]
    sql = "select * from Expenses where expensesid = %s"
    val = (itemid, )
    fbcursor.execute(sql, val)
    psda = fbcursor.fetchone() 
    if psda[11] is None:
      pass
    else:
      edit_window = Toplevel()
      edit_window.title("Edit the value or cancel")
      edit_window.geometry("700x500")
      
        
        
      image = Image.open("images/"+psda[11])
      resize_image = image.resize((700, 500))
      eximage = ImageTk.PhotoImage(resize_image)
      b2 = Button(edit_window,image=eximage)
      b2.photo = eximage
      b2.pack()
  

######################## DELETE EXPENSE #######################################################################


  def delete_expense():
    # sql = "select * from users"
    # fbcursor.execute(sql)
    # addexp_check_user = fbcursor.fetchall()
    delmess = messagebox.askyesno("Delete Expense", "Are you sure to delete this Expense?")
    if delmess == True:
      itemid = exp_tree.item(exp_tree.focus())["values"][0]
      print(itemid)
      sql = 'DELETE FROM Expenses WHERE expensesid=%s'
      val = (itemid,)
      fbcursor.execute(sql, val)
      fbilldb.commit()
      #selrow = exp_tree.selection()[0]
      exp_tree.delete(exp_tree.selection()[0])
    else:
      pass
  
  def delete_expense_check():
    sql = "select * from users"
    fbcursor.execute(sql)
    delexp_check_user = fbcursor.fetchall()
    if not delexp_check_user:
      delete_expense()
    else:
      try:
        user_namech = username1.get()
        sql = "select delete_expense from users where username = %s"
        val = (user_namech,)
        fbcursor.execute(sql,val)
        disable_del_exp = fbcursor.fetchone()
        if disable_del_exp[0] == 1:
          delete_expense()
        else:
          messagebox.showerror("user","user does not have permission to perform this action")
      except:
        delete_expense()
  

######################## SEARCH EXPENSE ######################################################################
  def close_expenses():
    top.destroy()

  def search_exp():
    query = searchvar.get()
    selections = []
    for child in exp_tree.get_children():
        if query in exp_tree.item(child)['values']:
            print(exp_tree.item(child)['values'])
            selections.append(child)
    exp_tree.selection_set(selections)
  
  
  

  def search_expense():
    global top,searchvar
    top = Toplevel()  
    
    top.title("Find Text")
    
    
    top.geometry("520x200+390+250")
    findwhat1=Label(top,text="Find What:",pady=5,padx=10)
    findwhat1.place(x=5,y=20)
    searchvar = StringVar() 
    findwhat = ttk.Combobox(top, width = 50, textvariable = searchvar ) 
      
    # Adding combobox drop down list 
    
    findwhat.place(x=80,y=25) 
    

    findButton = Button(top, text ="Find next",width=10, command=search_exp)
    findButton.place(x=420,y=20)

    findin1=Label(top,text="Find in:",pady=5,padx=10)
    findin1.place(x=5,y=47)
    n = StringVar() 
    findIN = ttk.Combobox(top, width = 37, textvariable = n ) 
      
    # Adding combobox drop down list 
    findIN['values'] = ('Client',  
                              ' Date', 
                              ' Category', 
                              ' Vendor', 
                              ' Staff Member', 
                              ' Description', 
                              ' Rebillable',
                              'Invoiced',
                              'Image',
                              'Rebill Amount',
                              'Amount',
                        
                              ' <<All>>') 
      
    findIN.place(x=80,y=54) 
    findIN.current(0)

    closeButton = Button(top, text ="Close",width=10,command=close_expenses)
    closeButton.place(x=420,y=50)

    match1=Label(top,text="Match:",pady=5,padx=10)
    match1.place(x=5,y=74)
    n = StringVar() 
    match = ttk.Combobox(top, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    match['values'] = ('From Any part of the field',' Whole Field',  
                              ' From the beginning of the field')
      
    match.place(x=80,y=83) 
    match.current(0)

    search1=Label(top,text="Search:",pady=5,padx=10)
    search1.place(x=5,y=102)
    n = StringVar() 
    search = ttk.Combobox(top, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    search['values'] = ('All', 'up', 
                              ' Down')
      
    search.place(x=80,y=112) 
    search.current(0)


    checkvarStatus4=IntVar()
   
    Button4 = Checkbutton(top,variable = checkvarStatus4, 
                      text="Match Case", 
                      onvalue =1,
                      offvalue = 0,
                      height=3,
                      width = 15)

    Button4.place(x=60,y=141)

    checkvarStatus5=IntVar()
   
    Button5 = Checkbutton(top,variable = checkvarStatus5, 
                      text="Match Format", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button5.place(x=270,y=141)







  

######################## FRONT PAGE OF EXPENSE MODULE #######################################################################

    
  expframe = Frame(tab6,relief=GROOVE,bg="#f8f8f2")
  expframe.pack(side="top", fill=BOTH)
  
  expmidFrame=Frame(expframe, height=60,bg="#f5f3f2")
  expmidFrame.pack(side="top", fill=X)

  e = Canvas(expmidFrame, width=1, height=65, bg="#f8f8f2", bd=0)
  e.pack(side="left", padx=(5, 2))
  e = Canvas(expmidFrame, width=1, height=65, bg="#f8f8f2", bd=0)
  e.pack(side="left", padx=(0, 5))
  
  
  expenseLabel = Button(expmidFrame,compound="top", text="Create new\nExpense",relief=RAISED,   command=add_expense_connection, image=expenseIcon,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
  expenseLabel.pack(side="left", pady=3, ipadx=4)
  
  
  expeditLabel = Button(expmidFrame,compound="top", text="Edit/View\nExpense",relief=RAISED,    image=expeditIcon,command=edit_expense,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  expeditLabel.pack(side="left")
  
  expdeleteLabel = Button(expmidFrame,compound="top", text="Delete\nSelected", relief=RAISED,    command=delete_expense_check,image=expdeleteIcon,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  expdeleteLabel.pack(side="left")
  
  e = Canvas(expmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  e.pack(side="left", padx=5)
 
  expsearchLabel = Button(expmidFrame,compound="top", text="Search in\nExpenses",relief=RAISED,   command=search_expense, image=expsearchIcon,bg="#f8f8f2", fg="black", height=55, bd=1, width=55, )
  expsearchLabel.pack(side="left")
  
  
  lbframe = LabelFrame(expmidFrame, height=60, width=200)
  lbframe.pack(side="left", padx=10, pady=0)

  lbl_expdt=Label(lbframe,text="Expense date from:",fg='black')
  lbl_expdt.grid(row=0, column=0, pady=5, padx=(5, 0))
  
  lbl_expdtt=Label(lbframe,text="Expense date to:" , fg='black')
  lbl_expdtt.grid(row=1, column=0, pady=5, padx=(5, 0))

  def daterange_expenses(): # Start and stop dates for range
    var1=expdt1.get_date()
    var2=expdtt2.get_date()
    print(var1,var2)
    for record in exp_tree.get_children():
      exp_tree.delete(record)
    
    
    sqldate='SELECT * FROM Expenses WHERE date BETWEEN %s AND %s'
    valuz=(var1,var2,)
    fbcursor.execute(sqldate,valuz)
    filterdate=fbcursor.fetchall()
    print(filterdate)
    count=0
    for i in filterdate:
      if True:
        if i[13] == '1':
          e = 'Yes'
        else:
          e = 'No'
        exp_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[0], i[10], i[4], i[6], i[5], i [8], i[7], e , i[14], i[11],i[16],i[3]))
      else:
          pass
      count += 1

  
  expdt1=DateEntry(lbframe)
  expdt1.grid(row=0, column=1)
     
  expdtt2=DateEntry(lbframe)
  expdtt2.grid(row=1, column=1)

  sql = "select dateformat from company"
  fbcursor.execute(sql)
  date_for = fbcursor.fetchone()
  
  if not date_for:
    pass
  else:
    if date_for[0] == "mm-dd-yyyy":
      expdtt2._set_text(expdtt2._date.strftime('%m-%d-%Y'))
      expdt1._set_text(expdt1._date.strftime('%m-%d-%Y'))
    elif date_for[0] == "dd-mm-yyyy":
      expdt1._set_text(expdt1._date.strftime('%d-%m-%Y'))
      expdtt2._set_text(expdtt2._date.strftime('%d-%m-%Y'))
    elif date_for[0] == "yyy.mm.dd":
      expdt1._set_text(expdt1._date.strftime('%Y.%m.%d'))
      expdtt2._set_text(expdtt2._date.strftime('%Y.%m.%d'))
    elif date_for[0] == "mm/dd/yyyy":
      expdt1._set_text(expdt1._date.strftime('%m/%d/%Y'))
      expdtt2._set_text(expdtt2._date.strftime('%m/%d/%Y'))
    elif date_for[0] == "dd/mm/yyy":
      expdt1._set_text(expdt1._date.strftime('%d/%m/%Y'))
      expdtt2._set_text(expdtt2._date.strftime('%d/%m/%Y'))
    elif date_for[0] == "dd.mm.yyyy":
      expdt1._set_text(expdt1._date.strftime('%d.%m.%Y'))
      expdtt2._set_text(expdtt2._date.strftime('%d.%m.%Y'))
    elif date_for[0] == "yyyy/mm/dd":
      expdt1._set_text(expdt1._date.strftime('%Y/%m/%d'))
      expdtt2._set_text(expdtt2._date.strftime('%Y/%m/%d'))
    else:
      pass
     
  checkvar1 = IntVar()
  chkbtn1 = Checkbutton(lbframe, text = "Apply filter", variable = checkvar1, onvalue = 1, offvalue =0,     height = 2, width = 8,command=daterange_expenses)
  chkbtn1.grid(row=0, column=2, rowspan=2, padx=(5,5))
  
  exp_mainFrame=Frame(tab6, relief=GROOVE, bg="#f8f8f2")
  exp_mainFrame.pack(side="top", fill=BOTH)
  e = Canvas(exp_mainFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  e.pack(side="left", padx=5)

  def refresh_expenses():
    for record in exp_tree.get_children():
      exp_tree.delete(record)
    count=0
    fbcursor.execute('SELECT * FROM Expenses;')
    for i in fbcursor:
      if True:
        if i[13] == '1':
          e = 'Yes'
        else:
          e = 'No'
        exp_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[0], i[10], i[4], i[6], i[5], i[8], i[7], e , i[14], i[11],i[16],i[3]))
      else:
          pass
    count += 1
  

  
  exprefreshLabel = Button(expmidFrame,compound="top", text="Refresh\nExpense List",relief=RAISED,    image=exprefreshIcon,bg="#f8f8f2", fg="black", height=55, bd=1, width=63,command=refresh_expenses)
  exprefreshLabel.pack(side="left")


  
  invoi1label = Label(expframe, text="Expenses (All)", font=("arial", 18), bg="#f8f8f2")
  invoi1label.pack(side="left", padx=(20,0))

  def fil(event):
    filt = drop123.get()
    for record in exp_tree.get_children():
      exp_tree.delete(record)
  
  
  
  
    sql = "select * from Expenses where catagory = %s"
    val = (filt,)
    fbcursor.execute(sql, val)
    records = fbcursor.fetchall()
  
  
    count=0
    for i in records:
        if True:
          if i[13] == '1':
             e = 'Yes'
          else:
            e = 'No'
          exp_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[0], i[10], i[4], i[6], i[5], i[8], i[7], e , i[14], i[11],i[16],i[3]))
        else:
          pass
    count += 1

  sql = "SELECT DISTINCT catagory FROM Expenses"
  fbcursor.execute(sql,)
  rec = fbcursor.fetchall()
  drop123 = ttk.Combobox(expframe,)
  drop123['values'] = rec
  drop123.pack(side="right", padx=(0,10))
  drop123.bind("<<ComboboxSelected>>", fil)


 
  invoi1label = Label(expframe, text="Category filter", font=("arial", 15), bg="#f8f8f2")
  invoi1label.pack(side="right", padx=(0,10))

# sql= 'SELECT rebillable FROM Expenses '
# fbcursor.execute(sql,)
# c = fbcursor.fetchall()
# print (c[2])
# print(c == 1)
# for e in c:
#   m = e == c
#   m = ("Yes")
#   e != c
#   print("no")
#   else:
#     pass



#table 
  s = ttk.Style()
  s.configure('Treeview.Heading', background='white', State='DISABLE')
  
  
  exp_tree=ttk.Treeview(tab6,selectmode='browse')
  exp_tree.place(x=0,y=105,height=580)
  
  expverticalbar=ttk.Scrollbar(tab6,orient="vertical",command=exp_tree.yview,)
  expverticalbar.place(x=1345,y=102,height=570,)
  expverticalbar.place(x=1345,y=102,height=570)
  exp_tree["columns"]=("1","2","3","4","5","6","7","8","9","10","11","12")
  exp_tree["show"]='headings'
  exp_tree.column("1",width=5,anchor='c')
  exp_tree.column("2",width=130,anchor='c')
  exp_tree.column("3",width=110,anchor='c')
  exp_tree.column("4",width=120,anchor='c')
  exp_tree.column("5",width=120,anchor='c')
  exp_tree.column("6",width=120,anchor='c')
  exp_tree.column("7",width=220,anchor='c')
  exp_tree.column("8",width=120,anchor='c')
  exp_tree.column("9",width=100,anchor='c')
  exp_tree.column("10",width=100,anchor='c')
  exp_tree.column("11",width=100,anchor='c')
  exp_tree.column("12",width=100,anchor='c')
  exp_tree.heading("2",text="Client")
  exp_tree.heading("3",text="Date")
  exp_tree.heading("4",text="Category")
  exp_tree.heading("5",text="Vendor")
  exp_tree.heading("6",text="Staff member")
  exp_tree.heading("7",text="Description")
  exp_tree.heading("8",text="Rebillable")
  exp_tree.heading("9",text="Invoiced")
  exp_tree.heading("10",text="Image")
  exp_tree.heading("11",text="Rebill Amount")
  exp_tree.heading("12",text="Amount")
  exp_tree.bind('<Double-Button-1>',file_image)





  fbcursor.execute('SELECT * FROM Expenses;')

  j = 0
  
  for i in fbcursor:
    if i[13] == '1':
      e = 'Yes'
    else:
      e = 'No'
    exp_tree.insert(parent='', index='end', iid=i, text='hello', values=(i[0], i[10], i[4], i[6], i[5], i[8], i[7], e , i[14], i[11],i[16],i[3]))
    j += 1

############################ END OF Expense Module-############################
############################ ADD PRODUCT SERVICES  ############################
  def add_product_s_connection():
    sql = "select * from users"
    fbcursor.execute(sql)
    addexp_check_user = fbcursor.fetchall()
    if not addexp_check_user:
      adda_product()
    else:
      try:
        user_namech = username1.get()
        sql = "select create_product_service from users where username = %s"
        val = (user_namech,)
        fbcursor.execute(sql,val)
        disable_create_exp = fbcursor.fetchone()
        if disable_create_exp[0] == 1:
          adda_product()
        else:
          messagebox.showerror("user","user does not have permission to perform this action")
      except:
        adda_product()

  def adda_product():
    top = Toplevel()  
    
    top.title("Add a new Product/Service")
    p2 = PhotoImage(file = 'images/fbicon.png')
    top.iconphoto(False, p1)
    top.geometry("600x550+390+125")
    
    
    tabControl = ttk.Notebook(top)
    s = ttk.Style()
    s.theme_use('default')
    s.configure('TNotebook.Tab', background="#999999", width=50, padding=10,bd=0)


    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    
    tabControl.add(tab1,compound = LEFT, text ='Product/Service')
    tabControl.add(tab2,compound = LEFT, text ='Product Image')
    
    tabControl.pack(expand = 1, fill ="both")
    
    innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE, height=490)
    innerFrame.pack(side="top",fill=BOTH)

    Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=475)
    Customerlabelframe.pack(side="top",fill=BOTH,padx=10)
    
    global filename
    filename = ""
    
    def upload_file():
      global filename,img, b2
      f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
      filename = filedialog.askopenfilename(filetypes=f_types)
      shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
      image = Image.open(filename)
      resize_image = image.resize((350, 350))
      img = ImageTk.PhotoImage(resize_image)
      b2 = Button(imageFrame,image=img)
      b2.place(x=130, y=80)
    
    def addproducts():
      global img , filename 
      sku = codeentry.get()
      status = checkvarStatus.get()
      catgory = n.get()
      name = nameentry.get()
      description = desentry.get()
      unitprice = uval.get()
      peices = pcsentry.get()
      cost = costval.get()
      price_cost = priceval.get()
      taxable = checkvarStatus2.get()
      tax2 = checkvarStatustax2.get()
      nostockcontrol = checkvarStatus3.get()
      stock = stockentry.get()
      lowstock = lowentry.get()
      warehouse = wareentry.get()
      pnotes = sctxt.get("1.0",'end-1c')
      entries = [sku,name, unitprice, cost]
      entri = []
      for i in entries:
        if i == '':
          entri.append(i)
      if len(entri) == 0:
        sql = 'select * from Productservice where sku = %s or name = %s'
        val  = (sku, name)
        fbcursor.execute(sql, val)
        fbcursor.fetchall()
        row_count = fbcursor.rowcount
        if row_count == 0:
          if filename == "":
            sql = 'insert into Productservice(sku, category, name, description, status, unitprice, peices, cost, taxable, priceminuscost, serviceornot, stock, stocklimit, warehouse, privatenote,tax2) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'
            val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, pnotes,tax2)
            fbcursor.execute(sql, val)
            fbilldb.commit()
          else:
            file = shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
            sql = 'insert into Productservice(sku, category, name, description, status, unitprice, peices, cost, taxable, priceminuscost, serviceornot, stock, stocklimit, warehouse, image, privatenote,tax2) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'
            val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, filename.split('/')[-1], pnotes,tax2)
            fbcursor.execute(sql, val)
            fbilldb.commit()
        else:
          messagebox.showinfo("Alert", "Entry with same name or SKU already exists.\nTry again.")
          top.destroy()
        for record in treeproducts.get_children():
          treeproducts.delete(record)
        fbcursor.execute("select *  from Productservice")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          if i[6] == '1':
            acti = 'Active'
          else:
            acti = 'Inactive' 
          sql = "select currencysign,currsignplace from company"
          fbcursor.execute(sql)
          currsymb = fbcursor.fetchone()
          if not currsymb: 
            if i[13] > i[14]:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
              countp += 1              
            elif i[12] == '1':
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
              countp += 1
            else:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
              countp += 1
              
          elif currsymb[1] == "before amount":
            if (i[13]) > (i[14]):
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
              countp += 1
            else:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
              countp += 1
          elif currsymb[1] == "before amount with space":
            if i[13] > i[14]:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
              countp += 1
            else:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
              countp += 1
          elif currsymb[1] == "after amount":
            if i[13] > i[14]:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
              countp += 1
            else:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
              countp += 1
          elif currsymb[1] == "after amount with space":
            if i[13] > i[14]:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
              countp += 1
            else:
              treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
              countp += 1
        top.destroy()
      else:
        messagebox.showinfo("Alert", "Fields name and SKU should not be empty.\nFill out required fields and try again")
        
 
    fbcursor.execute("SELECT * FROM Productservice ORDER BY sku DESC LIMIT 1")
    skuin = fbcursor.fetchone()
    
    
    code1=Label(Customerlabelframe,text="Code or SKU* :",fg="blue",pady=10,padx=10)
    code1.place(x=20,y=0)
    codeentry = Entry(Customerlabelframe,width=35)
    codeentry.place(x=110,y=8)
    # if not skuin == None:
    #   fk=skuin[2]+1
    # else:
    #   fk=1
    # codeentry.insert(0, fk)

    checkvarStatus=IntVar()
    status1=Label(Customerlabelframe,text="Status:")
    status1.place(x=380,y=8)
    Button1 = Checkbutton(Customerlabelframe, 
                      variable = checkvarStatus,text="Active",compound="right",
                      onvalue =1,
                      offvalue = 0,
                      width = 10)

    Button1.place(x=420,y=5)

    category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
    category1.place(x=20,y=40)
    n = StringVar() 
    catgory = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n ) 
    catgory.place(x=110,y=45)
    catgory.insert(0, 'Default')


    name1=Label(Customerlabelframe,text="Name* :",fg="blue",pady=5,padx=10)
    name1.place(x=20,y=70)
    nameentry = Entry(Customerlabelframe,width=70)
    nameentry.place(x=110,y=75)

    des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
    des1.place(x=20,y=100)
    desentry = Entry(Customerlabelframe,width=70)
    desentry.place(x=110,y=105)

    def prdoucts_cal(S,d):
        if d == '1': #insert
          if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
            return False
          return True
        if d.isdigit():
          return True

    uval = StringVar()
    unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
    unit1.place(x=20,y=130)
    unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
    unitentry.place(x=110,y=135)
    cal_unit = (Customerlabelframe.register(prdoucts_cal),'%S','%d')
    unitentry.config(validate='key',validatecommand=(cal_unit),justify='right')
    

    # pcsval = IntVar()
    pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
    pcs1.place(x=320,y=130)
    pcsentry = Entry(Customerlabelframe,width=20)
    pcsentry.place(x=410,y=135)

    costval = StringVar(value="0")
    cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
    cost1.place(x=20,y=160)
    
    costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
    costentry.place(x=110,y=165)
    cal_cost = (Customerlabelframe.register(prdoucts_cal),'%S','%d')
    costentry.config(validate='key',validatecommand=(cal_cost),justify='right')
    
    def set_label(name, index, mode):
      copr = float(uval.get()) - float(costval.get())
      priceval.set(str(copr))
      
    priceval = StringVar()
    price1=Label(Customerlabelframe,text="(Price-Cost):",pady=5,padx=10)
    price1.place(x=20,y=190)
    priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval,state=DISABLED,disabledbackground="white",disabledforeground="black")
    priceentry.config(justify="right")
    priceentry.place(x=110,y=195)
    
    uval.trace('w', set_label)
    costval.trace('w', set_label)

    sql = "select taxtype from company"
    fbcursor.execute(sql)
    taxchoose = fbcursor.fetchone()

    checkvarStatus2=IntVar()
   
    Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2, 
                      text="Taxable Tax1rate",compound="right",
                      onvalue =1 ,
                      offvalue = 0,
                      height=2,
                      width = 12)
    
    checkvarStatustax2=IntVar()
    Buttontax2 = Checkbutton(Customerlabelframe,variable = checkvarStatustax2, 
                      text="Taxable Tax2rate",compound="right",
                      onvalue =1 ,
                      offvalue = 0,
                      height=2,
                      width = 12)
    
    
    if not taxchoose:
      pass
    elif taxchoose[0] == '1':
      Button2.place_forget()
      Buttontax2.place_forget()
    elif taxchoose[0] == '2':
      Button2.place(x=415,y=153)
      Buttontax2.place_forget()
    elif taxchoose[0] == '3':
      Button2.place(x=415,y=153)
      Buttontax2.place(x=415,y=203)

    

    def switch():
      if checkvarStatus3.get():
        stockentry["state"] = DISABLED
        lowentry["state"] = DISABLED
        wareentry["state"] = DISABLED
      else:
        stockentry["state"] = NORMAL
        lowentry["state"] = NORMAL
        wareentry["state"] = NORMAL
    checkvarStatus3=BooleanVar()
    Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,command=switch,text="This is a service(no stock control)", 
                      onvalue =1 ,
                      offvalue = 0,
                      height=3)

    Button3.place(x=40,y=220)
 
    def stocknum(input):
      if input.isdigit():
        return True
      elif input is "":
        return True
      else:
        return False
    stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
    stock1.place(x=90,y=260)
    stockentry = Entry(Customerlabelframe,width=15)
    stockentry.place(x=140,y=265)
    sto = Customerlabelframe.register(stocknum)
    stockentry.config(validate="key",validatecommand=(sto, '%S'))


    low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
    low1.place(x=280,y=260)
    lowentry = Entry(Customerlabelframe,width=15)
    lowentry.place(x=435,y=265)
    lowsto = Customerlabelframe.register(stocknum)
    lowentry.config(validate="key",validatecommand=(lowsto, '%S'))

   
    ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
    ware1.place(x=60,y=290)
    wareentry = Entry(Customerlabelframe,width=64)
    wareentry.place(x=140,y=295)

    # pnoteval = StringVar()
    text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
    text1.place(x=20,y=320)
    sctxt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
    sctxt.place(x=32,y=358)
    
    okButton = Button(innerFrame, text ="Ok",image=tick,width=70,compound = LEFT, command=addproducts)
    okButton.pack(side=LEFT, padx=(10, 0), pady=(5, 10))
    
    def closetab():
      top.destroy()

    cancelButton = Button(innerFrame,image=cancel,text="Cancel",width=70,compound = LEFT, command=closetab)
    cancelButton.pack(side=RIGHT, padx=(0, 10), pady=(5, 10))

    imageFrame = Frame(tab2, relief=GROOVE,height=580)
    imageFrame.pack(side="top",fill=BOTH)

    
      
    browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
    browseimg.place(x=30,y=35)
      
    browsebutton=Button(imageFrame,text = 'Browse',command=upload_file)
    browsebutton.place(x=485,y=30,height=30,width=50)

    removeButton = Button(imageFrame,image=cancel,text="Remove Product Image",width=150,compound = LEFT, command=lambda: b2.destroy())
    removeButton.place(x=410,y=460)

    top.mainloop()
  ##################### import product service ####################
  def import_productservice_check():
    sql = "select * from users"
    fbcursor.execute(sql)
    delexp_check_user = fbcursor.fetchall()
    if not delexp_check_user:
      fileimport_product()
    else:
      try:
        user_namech = username1.get()
        sql = "select 	import_product_service from users where username = %s"
        val = (user_namech,)
        fbcursor.execute(sql,val)
        disable_del_exp = fbcursor.fetchone()
        if disable_del_exp[0] == 1:
          fileimport_product()
        else:
          messagebox.showerror("user","user does not have permission to perform this action")
      except:
        fileimport_product()

  def fileimport_product():

    top=Toplevel()
    top.title("Import items list from Excel(XLS)File")
    top.geometry("785x520+280+100")
    importframe=Frame(top)
    importframe.place(x=0,y=0,height=700,width=785)
    impolbl=Label(importframe,text="Import source Excel(xlsx) File:").place(x=8,y=30)
    impoentry=Entry(importframe,bg="white")
    impoentry.place(x=8,y=50,width=280, height=25)
    previewlbl=Label(importframe,text="Source File preview").place(x=8,y=77)
   
    ###### LISTBOX #####################
    scrollbarx = Scrollbar(importframe, orient=HORIZONTAL)
    scrollbary = Scrollbar(importframe, orient=VERTICAL)
    imptree = ttk.Treeview(importframe, columns=("PRODUCT SERVICE ID","CODE OR SKU","NAME","CATEGORY","DESCRIPTION","QTY UNIT","COST","PRICE","TAX1","TAX2","STOCK","LOW STOCK","LOCATION","ACTIVE","SERVICE"), height=400,     selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=imptree.yview)
    scrollbary.place(x=754,y=100,height=325)
    scrollbarx.config(command=imptree.xview)
    scrollbarx.place(x=0,y=410, width=356)
    imptree.heading('PRODUCT SERVICE ID', text="PRODUCT SERVICE ID", anchor=W)
    imptree.heading('CODE OR SKU', text="CODE OR SKU", anchor=W)
    imptree.heading('NAME', text="NAME", anchor=W)
    imptree.heading('CATEGORY', text="CATEGORY", anchor=W)
    imptree.heading('NAME', text="NAME", anchor=W)
    imptree.heading('DESCRIPTION', text="DESCRIPTION", anchor=W)
    imptree.heading('QTY UNIT', text="QTY UNIT", anchor=W)
    imptree.heading('COST', text="COST", anchor=W)
    imptree.heading('PRICE', text="PRICE", anchor=W)
    imptree.heading('TAX1', text="TAX1", anchor=W)
    imptree.heading('TAX2', text="TAX2", anchor=W)
    imptree.heading('STOCK', text="STOCK", anchor=W)
    imptree.heading('LOW STOCK', text="LOW STOCK", anchor=W)
    imptree.heading('LOCATION', text="LOCATION", anchor=W)
    imptree.heading('ACTIVE', text="ACTIVE", anchor=W)
    imptree.heading('SERVICE', text="SERVICE", anchor=W)
    

    imptree.column('#0', stretch=NO, minwidth=0, width=0)
    imptree.column('#1', stretch=NO, minwidth=0, width=120)
    imptree.column('#2', stretch=NO, minwidth=0, width=100)
    imptree.column('#3', stretch=NO, minwidth=0, width=100)
    imptree.column('#4', stretch=NO, minwidth=0, width=100)
    imptree.column('#5', stretch=NO, minwidth=0, width=100)
    imptree.column('#6', stretch=NO, minwidth=0, width=100)
    imptree.column('#7', stretch=NO, minwidth=0, width=100)
    imptree.column('#8', stretch=NO, minwidth=0, width=100)
    imptree.column('#9', stretch=NO, minwidth=0, width=100)
    imptree.column('#10', stretch=NO, minwidth=0, width=100)
    imptree.column('#11', stretch=NO, minwidth=0, width=100)
    imptree.column('#12', stretch=NO, minwidth=0, width=100)
    imptree.column('#13', stretch=NO, minwidth=0, width=100)
    imptree.column('#14', stretch=NO, minwidth=0, width=100)

 

    imptree.place(x=5,y=100,height=315,width=750)
    
    
    lb1=Label(importframe,text="Select import source XLs file first after build column associations").place(x=8,y=480)

    def export_product_1():
      global Productserviceid,name12,category12,description,peices,cost12,priceminuscost,taxable,stock12,stocklimit,warehouse,status,serviceornot,name
      name = askopenfilename(filetypes=[('CSV', '*.csv',), ('Excel', ('*.xls', '*.xslm', '*.xlsx'))])
      # df = pd.read_csv(name)
      # for i in df:
      #   listbox.insert(END, df)
      with open(name) as f:
        reader = csv.DictReader(f, delimiter=',')
        print(reader)
        for row in reader:
          # "PRODUCT SERVICE ID","NAME","CATEGORY","DESCRIPTION","QTY UNIT","COST","PRICE","TAX1","STOCK","LOW STOCK","LOCATION","ACTIVE","SERVICE"
          Productserviceid = row['PRODUCT SERVICE ID']
          sku = row['CODE OR SKU']          
          name12 = row['NAME']
          category12 = row['CATEGORY']
          
          description = row['DESCRIPTION']
          peices = row['QTY UNIT']
          cost12 = row['COST']
          priceminuscost = row['PRICE']
          taxable = row['TAX1']
          tax2 = row['TAX2']
          stock12 = row['STOCK']
          stocklimit = row['LOW STOCK']
          warehouse = row['LOCATION']
          status = row['ACTIVE']
          serviceornot = row['SERVICE']
        
          imptree.insert("", 0, values=(Productserviceid,sku,name12,category12,description,peices,cost12,priceminuscost,taxable,tax2,stock12,stocklimit,warehouse,status,serviceornot))

      impoentry.delete(0, 'end')
      impoentry.insert(0, name)
      
    def nxtscreen():
      def save_pro_import():
        with open(name) as f:
          reader = csv.DictReader(f, delimiter=',')
          for row in reader:
            Productserviceid = int(row['PRODUCT SERVICE ID'])
            sku = int(row['CODE OR SKU'])  
            name12 = row['NAME']
            category12 = row['CATEGORY']
            description = row['DESCRIPTION']
            peices = int(row['QTY UNIT'])
            cost12 = int(row['COST'])
            unitprice = int(row['PRICE'])
            taxable = int(row['TAX1'])
            tax2 = row['TAX2']
            stock12 = int(row['STOCK'])
            stocklimit = int(row['LOW STOCK'])
            warehouse = row['LOCATION']
            status = int(row['ACTIVE'])
            serviceornot = int(row['SERVICE'])
            min = int(unitprice) - int(cost12)

            sql = 'select * from Productservice where Productserviceid = %s or name = %s or sku=%s'
            val  = (Productserviceid, name12,sku)
            fbcursor.execute(sql, val)
            fbcursor.fetchall()
            row_count = fbcursor.rowcount
            if row_count == 0:
              sql = 'insert into Productservice(Productserviceid,sku,name,category,description,peices,cost,unitprice,taxable,tax2,stock,stocklimit,warehouse,status,serviceornot,priceminuscost) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)'
              val = (Productserviceid,sku,name12,category12,description,peices,cost12,unitprice,taxable,tax2,stock12,stocklimit,warehouse,status,serviceornot,min)
              fbcursor.execute(sql, val)
              fbilldb.commit()
              topp.destroy()
              for record in treeproducts.get_children():
                treeproducts.delete(record)
              fbcursor.execute("select *  from Productservice")
              pandsdata = fbcursor.fetchall()
              countp = 0
              for i in pandsdata:
                if i[6] == '1':
                  acti = 'Active'
                else:
                  acti = 'Inactive' 
                sql = "select currencysign,currsignplace from company"
                fbcursor.execute(sql)
                currsymb = fbcursor.fetchone()
                if not currsymb: 
                  if i[13] > i[14]:
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
                    countp += 1              
                  elif i[12] == '1':
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
                    countp += 1
                  else:
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
                    countp += 1
                        
                elif currsymb[1] == "before amount":
                  if (i[13]) > (i[14]):
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
                    countp += 1
                  else:
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
                    countp += 1
                elif currsymb[1] == "before amount with space":
                  if i[13] > i[14]:
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
                    countp += 1
                  else:
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
                    countp += 1
                elif currsymb[1] == "after amount":
                  if i[13] > i[14]:
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
                    countp += 1
                  else:
                    treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
                    countp += 1
                elif currsymb[1] == "after amount with space":
                    if i[13] > i[14]:
                      treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
                      countp += 1
                    elif i[12] == '1':
                      treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
                      countp += 1
                    else:
                      treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
                      countp += 1
              topp.destroy()
            else:
              messagebox.showinfo("Alert", "Entry with same name or SKU already exists.\nTry again.")
            
     
      topp=Toplevel()
      topp.title("Import items list from Excel(XLS)File")
      topp.geometry("785x520+280+100")
      scrollbarx = Scrollbar(topp, orient=HORIZONTAL)
      scrollbary = Scrollbar(topp, orient=VERTICAL)
      nxttree = ttk.Treeview(topp, columns=("PRODUCT SERVICE ID","CODE OR SKU","NAME","CATEGORY","DESCRIPTION","QTY UNIT","COST","PRICE","TAX1","TAX2","STOCK","LOW STOCK","LOCATION","ACTIVE","SERVICE"),height=400,     selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
      scrollbary.config(command=nxttree.yview)
      scrollbary.place(x=768,y=0,height=490)
      scrollbarx.config(command=nxttree.xview)
      scrollbarx.place(x=0,y=470,width=763)
      nxttree.heading('CODE OR SKU', text="CODE OR SKU", anchor=W)
      nxttree.heading('PRODUCT SERVICE ID', text="PRODUCT SERVICE ID", anchor=W)
      nxttree.heading('NAME', text="NAME", anchor=W)
      nxttree.heading('CATEGORY', text="CATEGORY", anchor=W)
      nxttree.heading('NAME', text="NAME", anchor=W)
      nxttree.heading('DESCRIPTION', text="DESCRIPTION", anchor=W)
      nxttree.heading('QTY UNIT', text="QTY UNIT", anchor=W)
      nxttree.heading('COST', text="COST", anchor=W)
      nxttree.heading('PRICE', text="PRICE", anchor=W)
      nxttree.heading('TAX1', text="TAX1", anchor=W)
      nxttree.heading('TAX2', text="TAX2", anchor=W)
      nxttree.heading('STOCK', text="STOCK", anchor=W)
      nxttree.heading('LOW STOCK', text="LOW STOCK", anchor=W)
      nxttree.heading('LOCATION', text="LOCATION", anchor=W)
      nxttree.heading('ACTIVE', text="ACTIVE", anchor=W)
      nxttree.heading('SERVICE', text="SERVICE", anchor=W)
  
      nxttree.column('#0', stretch=NO, minwidth=0, width=0)
      nxttree.column('#1', stretch=NO, minwidth=0, width=120)
      nxttree.column('#2', stretch=NO, minwidth=0, width=100)
      nxttree.column('#3', stretch=NO, minwidth=0, width=100)
      nxttree.column('#4', stretch=NO, minwidth=0, width=100)
      nxttree.column('#5', stretch=NO, minwidth=0, width=100)
      nxttree.column('#6', stretch=NO, minwidth=0, width=100)
      nxttree.column('#7', stretch=NO, minwidth=0, width=100)
      nxttree.column('#8', stretch=NO, minwidth=0, width=100)
      nxttree.column('#9', stretch=NO, minwidth=0, width=100)
      nxttree.column('#10', stretch=NO, minwidth=0, width=100)
      nxttree.column('#11', stretch=NO, minwidth=0, width=100)
      nxttree.column('#12', stretch=NO, minwidth=0, width=100)
      nxttree.column('#13', stretch=NO, minwidth=0, width=100)
      nxttree.column('#14', stretch=NO, minwidth=0, width=100)
    
      with open(name) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
          # "PRODUCT SERVICE ID","NAME","CATEGORY","DESCRIPTION","QTY UNIT","COST","PRICE","TAX1","STOCK","LOW STOCK","LOCATION","ACTIVE","SERVICE"
          Productserviceid = row['PRODUCT SERVICE ID']
          sku = row['CODE OR SKU']
          name12 = row['NAME']
          category12 = row['CATEGORY']
          
          description = row['DESCRIPTION']
          peices = row['QTY UNIT']
          cost12 = row['COST']
          priceminuscost = row['PRICE']
          taxable = row['TAX1']
          tax2 = row['TAX2']
          stock12 = row['STOCK']
          stocklimit = row['LOW STOCK']
          warehouse = row['LOCATION']
          status = row['ACTIVE']
          serviceornot = row['SERVICE']
      

      
          nxttree.insert("", 0, values=(Productserviceid,sku,name12,category12,description,peices,cost12,  priceminuscost,taxable,tax2,stock12,stocklimit,warehouse,status,serviceornot))
       
    
      nxttree.place(x=0,y=0,height=470,width=770)
      back = Button(topp,text="back",command=lambda:topp.destroy())
      back.place(x=5,y=492)
      Finish = Button(topp,text="Finish",command=save_pro_import)
      Finish.place(x=740,y=492)
     
    
    importbutton=Button(top,command=export_product_1,text = 'Browse',compound=LEFT)
    importbutton.place(x=290,y=48,height=25,width=80)

    
    n = Button(importframe, text ="Next",command=nxtscreen).place(x=710,y=470)
  
    
    top.mainloop()
    
#########EXPORT PRODUCT#######################################################################################

  def export_product():
    cols = ["PRODUCT SERVICE ID","CODE OR SKU","NAME","CATEGORY","DESCRIPTION","QTY UNIT","COST","PRICE","TAX1","TAX2","STOCK","LOW STOCK","LOCATION","ACTIVE","SERVICE"] # Your column headings here
    path = filedialog.asksaveasfilename(initialdir=os.getcwd,title="Save File",filetypes=[('CSV File', '*.csv',)],defaultextension=".csv")
    
    lst = []
    with open(path, "w", newline='') as myfile:
        csvwriter = csv.writer(myfile, delimiter=',')
        sql = 'select Productserviceid,sku,name,category,description,peices,cost,unitprice,taxable,tax2,stock,stocklimit,warehouse,status,serviceornot from Productservice'
        fbcursor.execute(sql)
        pandsdata = fbcursor.fetchall()
        for row_id in pandsdata:
            row = row_id
            lst.append(row)
        lst = list(map(list,lst))
        lst.insert(0,cols)
        for row in lst:
            csvwriter.writerow(row)

    


######################## VIEW/EDIT PRODUCT #######################################################################

  
  def edit_product():  
    try:
      itemid = treeproducts.item(treeproducts.focus())["values"][1]
      
      global filename
      filename = ""
      
      def upload_file():
        global filename,img, b2
        f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        image = Image.open(filename)
        resize_image = image.resize((350, 350))
        img = ImageTk.PhotoImage(resize_image)
        b2 = Button(imageFrame,image=img)
        b2.place(x=130, y=80)
      
      def updateproducts():
        global img , filename 
        sku = codeentry.get()
        status = checkvarStatus.get()
        catgory = n.get()
        name = nameentry.get()
        description = desentry.get()
        unitprice = uval.get()
        peices = pcsentry.get()
        cost = costval.get()
        price_cost = priceval.get()
        taxable = checkvarStatus2.get()
        tax2 = checkvarStatustax2.get()
        nostockcontrol = checkvarStatus3.get()
        stock = stockval.get()
        lowstock = lowval.get()
        warehouse = wareentry.get()
        pnotes = sctxt.get("1.0", 'end-1c')
        entries = [sku, name, unitprice, cost]
        entri = []
        for i in entries:
          if i == '':
            entri.append(i)
        if len(entri) == 0:
          if filename == "":
            sql = "update Productservice set sku=%s, category=%s, name=%s, description=%s, status=%s, unitprice=%s, peices=%s, cost=%s, taxable=%s, priceminuscost=%s, serviceornot=%s, stock=%s, stocklimit=%s, warehouse=%s, privatenote=%s,tax2=%s where Productserviceid = %s"
            val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, pnotes,tax2, itemid)
            fbcursor.execute(sql, val)
            fbilldb.commit()
          else:
            file = shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
            sql = "update Productservice set category=%s, name=%s, description=%s, status=%s, unitprice=%s, peices=%s, cost=%s, taxable=%s, priceminuscost=%s, serviceornot=%s, stock=%s, stocklimit=%s, warehouse=%s, image=%s, privatenote=%s,tax2=%s where Productserviceid = %s"
            val = (catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse,filename.split('/')[-1], pnotes,tax2, itemid)
            fbcursor.execute(sql, val)
            fbilldb.commit()
            
          for record in treeproducts.get_children():
            treeproducts.delete(record)
          fbcursor.execute("select *  from Productservice")
          pandsdata = fbcursor.fetchall()
          countp = 0
          for i in pandsdata:
            if i[6] == '1':
              acti = 'Active'
            else:
              acti = 'Inactive' 
            sql = "select currencysign,currsignplace from company"
            fbcursor.execute(sql)
            currsymb = fbcursor.fetchone()
            if not currsymb: 
              if i[13] > i[14]:
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
                countp += 1              
              elif i[12] == '1':
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
                countp += 1
              else:
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
                countp += 1
                      
            elif currsymb[1] == "before amount":
              if (i[13]) > (i[14]):
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
                countp += 1
              else:
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
                countp += 1
            elif currsymb[1] == "before amount with space":
              if i[13] > i[14]:
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
                countp += 1
              else:
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
                countp += 1
            elif currsymb[1] == "after amount":
              if i[13] > i[14]:
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
                countp += 1
              elif i[12] == '1':
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
                countp += 1
              else:
                treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
                countp += 1
            elif currsymb[1] == "after amount with space":
                if i[13] > i[14]:
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
                  countp += 1
                elif i[12] == '1':
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
                  countp += 1
                else:
                  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
                  countp += 1
          top.destroy()
        else:
          messagebox.showinfo("F-Billing Revolution", "Fields name or SKU entered is already in database.")
          top.destroy()
        
         
      sql = "select * from Productservice where Productserviceid = %s"
      val = (itemid, )
      fbcursor.execute(sql, val)
      psdata = fbcursor.fetchone()
      
      
      top = Toplevel()  
      top.title("Edit Product/Service details")
      p3 = PhotoImage(file = 'images/fbicon.png')
      top.iconphoto(False, p1)
      top.geometry("600x550+390+125")
      tabControl = ttk.Notebook(top)
      s = ttk.Style()
      s.theme_use('default')
      s.configure('TNotebook.Tab', background="#999999", width=50, padding=10,bd=0)

      taba = ttk.Frame(tabControl)
      tabb = ttk.Frame(tabControl)
      
      tabControl.add(taba,compound = LEFT, text ='Product/Service')
      tabControl.add(tabb,compound = LEFT, text ='Product Image')
      
      tabControl.pack(expand = 1, fill ="both")
      
      innerFrame = Frame(taba,bg="#f5f3f2", relief=GROOVE)
      innerFrame.pack(side="top",fill=BOTH)

      updateframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
      updateframe.pack(side="top",fill=BOTH,padx=10)

      code1=Label(updateframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
      code1.place(x=20,y=0)
      codeentry = Entry(updateframe,width=35)
      codeentry.place(x=110,y=8)
      codeentry.insert(0, psdata[2])

      checkvarStatus=IntVar()
      status1=Label(updateframe,text="Status:")
      status1.place(x=380,y=8)
      Button1 = Checkbutton(updateframe, 
                        variable = checkvarStatus,text="Active",compound="right",
                        onvalue =1,
                        offvalue =0,
                        width = 10)
      Button1.place(x=420,y=5)
      sta = psdata[6]
      if sta == '1':
        Button1.select()
      else:
        Button1.deselect()



      category1=Label(updateframe,text="Category:",pady=5,padx=10)
      category1.place(x=20,y=40)
      n = StringVar() 
      category = Entry(updateframe,width=70,textvariable=n) 
      category.place(x=110,y=45)
      category.insert(0, psdata[3])


      name1=Label(updateframe,text="Name :",fg="blue",pady=5,padx=10)
      name1.place(x=20,y=70)
      nameentry = Entry(updateframe,width=70)
      nameentry.place(x=110,y=75)
      nameentry.insert(0, psdata[4])

      des1=Label(updateframe,text="Description :",pady=5,padx=10)
      des1.place(x=20,y=100)
      desentry = Entry(updateframe,width=70)
      desentry.place(x=110,y=105)
      desentry.insert(0, psdata[5])

      def set_label(name, index, mode):
        priceval.set(float(uval.get()) - float(costval.get()))

      def prdoucts_cal(S,d):
        if d == '1': #insert
          if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
            return False
          return True
        if d.isdigit():
          return True
      
      unit1=Label(updateframe,text="Unit Price:",fg="blue",pady=5,padx=10)
      unit1.place(x=20,y=130)
      
      uval = StringVar()
      unitentry = Entry(updateframe,width=20,textvariable=uval)
      unitentry.place(x=110,y=135)
      unitentry.delete(0,'end')
      unitentry.insert(0, psdata[7])
      cal_unit = (updateframe.register(prdoucts_cal),'%S','%d')
      unitentry.config(validate='key',validatecommand=(cal_unit),justify='right')
      

      pcsval = IntVar()
      pcs1=Label(updateframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
      pcs1.place(x=320,y=130)
      pcsentry = Entry(updateframe,width=20,textvariable=pcsval)
      pcsentry.place(x=410,y=135)
      pcsentry.delete(0,'end')
      pcsentry.insert(0, psdata[8])
      

      costval = StringVar()
      cost1=Label(updateframe,text="Cost:",pady=5,padx=10)
      cost1.place(x=20,y=160)
      costentry = Entry(updateframe,width=20,textvariable=costval)
      costentry.place(x=110,y=165)
      costentry.delete(0, END)
      costentry.insert(0, psdata[9])
      cal_cost = (updateframe.register(prdoucts_cal),'%S','%d')
      costentry.config(validate='key',validatecommand=(cal_cost),justify='right')
      

      priceval = StringVar()
      price1=Label(updateframe,text="(Price-Cost):",pady=5,padx=10)
      price1.place(x=20,y=190)
      priceentry = Entry(updateframe,width=20,textvariable=priceval)
      priceentry.place(x=110,y=195)
      priceentry.delete(0,'end')
      priceentry.insert(0, psdata[11])

      uval.trace('w', set_label)
      costval.trace('w', set_label)
      

      checkvarStatus2=IntVar()
    
      Button2 = Checkbutton(updateframe,variable = checkvarStatus2, 
                        text="Taxable Tax1rate",compound="right",
                        onvalue =1 ,
                        offvalue =0,
                        height=2,
                        width = 12)
      
      checkvarStatustax2=IntVar()
      Buttontax2 = Checkbutton(updateframe,variable = checkvarStatustax2, 
                      text="Taxable Tax2rate",compound="right",
                      onvalue =1 ,
                      offvalue = 0,
                      height=2,
                      width = 12)
      
      sql = "select taxtype from company"
      fbcursor.execute(sql)
      taxchoose = fbcursor.fetchone()
      if not taxchoose:
        pass
      elif taxchoose[0] == '1':
        Button2.place_forget()
        Buttontax2.place_forget()
      elif taxchoose[0] == '2':
        Button2.place(x=415,y=153)
        Buttontax2.place_forget()
      elif taxchoose[0] == '3':
        Button2.place(x=415,y=153)
        Buttontax2.place(x=415,y=203)

   
      tax = psdata[10]
      if tax == '1':
        Button2.select()
      else:
        Button2.deselect()

      if psdata[19] == '1':
        Buttontax2.select()
      else:
        Buttontax2.deselect()

      def switch():
        if checkvarStatus3.get():
          stockentry["state"] = DISABLED
          lowentry["state"] = DISABLED
          wareentry["state"] = DISABLED
        else:
          stockentry["state"] = NORMAL
          lowentry["state"] = NORMAL
          wareentry["state"] = NORMAL
      checkvarStatus3=BooleanVar()
    
      Button3 = Checkbutton(updateframe,variable = checkvarStatus3,command=switch, 
                        text="No stock Control", 
                        onvalue =1 ,
                        offvalue = 0,
                        height=3,
                        width = 15)

      Button3.place(x=40,y=220)

      

      def stocknum(input):
        if input.isdigit():
          return True
        elif input is "":
          return True
        else:
          return False
      stockval = IntVar(updateframe)
      stock1=Label(updateframe,text="Stock:",pady=5,padx=10)
      stock1.place(x=90,y=260)
      stockentry = Entry(updateframe,width=15,textvariable=stockval)
      stockentry.place(x=140,y=265)
      stockentry.delete(0,'end')
      stockentry.insert(0, psdata[13])
      sto = updateframe.register(stocknum)
      stockentry.config(validate="key",validatecommand=(sto, '%S'))
      

      lowval = IntVar(updateframe)
      low1=Label(updateframe,text="Low Stock Warning Limit:",pady=5,padx=10)
      low1.place(x=280,y=260)
      lowentry = Entry(updateframe,width=15,textvariable=lowval)
      lowentry.place(x=435,y=265)
      lowentry.delete(0,'end')
      lowentry.insert(0, psdata[14])
      lowsto = updateframe.register(stocknum)
      lowentry.config(validate="key",validatecommand=(lowsto, '%S'))
      

    
      ware1=Label(updateframe,text="Warehouse:",pady=5,padx=10)
      ware1.place(x=60,y=290)
      wareentry = Entry(updateframe,width=64)
      wareentry.place(x=140,y=295)
      wareentry.insert(0, psdata[15])

      scr = psdata[12]
      if scr == '1':
        Button3.select()
        stockentry["state"] = DISABLED
        lowentry["state"] = DISABLED
        wareentry["state"] = DISABLED
      else:
        Button3.deselect()
        stockentry["state"] = NORMAL
        lowentry["state"] = NORMAL
        wareentry["state"] = NORMAL
      
      

      

      text1=Label(updateframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
      text1.place(x=20,y=320)
      sctxt = scrolledtext.ScrolledText(updateframe, undo=True,width=62,height=4)
      sctxt.place(x=32,y=358)
      try:
        sctxt.insert("1.0", psdata[16])
      except:
        pass

      okButton = Button(innerFrame, text ="Ok",image=tick,width=70,compound = LEFT, command=updateproducts)
      okButton.pack(side=LEFT, padx=(10, 0))

      cancelButton = Button(innerFrame,image=cancel,text="Cancel",width=70,compound = LEFT, command=lambda : top.destroy())
      cancelButton.pack(side=RIGHT, padx=(0, 10))
      
      
      imageFrame = Frame(tabb, relief=GROOVE,height=580)
      imageFrame.pack(side="top",fill=BOTH)

      browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
      browseimg.place(x=15,y=35)

      browsebutton=Button(imageFrame,text = 'Browse', command=upload_file)
      browsebutton.place(x=470,y=30,height=30,width=50)

      try:
        image = Image.open("images/"+psdata[17])
        resize_image = image.resize((350, 350))
        image = ImageTk.PhotoImage(resize_image)
        b2 = Label(imageFrame,image=image,width=350,height=350)
        b2.photo = image
        b2.place(x=130, y=80)
        print(image)
      except:
        pass

      removeButton = Button(imageFrame,image=cancel,text="Remove Product Image",width=150,compound = LEFT)
      removeButton.place(x=410,y=460)
    except:
      try:
        top.destroy()
      except:
        pass
      messagebox.showerror('F-Billing Revolution', 'Select a record to edit.')
  


######################## DELETE PRODUCT #######################################################################
  def delete_product_check():
    sql = "select * from users"
    fbcursor.execute(sql)
    delexp_check_user = fbcursor.fetchall()
    if not delexp_check_user:
      delete_product()
    else:
      try:
        user_namech = username1.get()
        sql = "select 	delete_product_service from users where username = %s"
        val = (user_namech,)
        fbcursor.execute(sql,val)
        disable_del_exp = fbcursor.fetchone()
        if disable_del_exp[0] == 1:
          delete_product()
        else:
          messagebox.showerror("user","user does not have permission to perform this action")
      except:
        delete_product()

  def delete_product():
    delmess = messagebox.askyesno("Delete product/service", "Are you sure to delete this product/service?")
    if delmess == True:
      itemid = treeproducts.item(treeproducts.focus())["values"][1]
      sql = "delete from Productservice where Productserviceid = %s"
      val = (itemid, )
      fbcursor.execute(sql, val)
      fbilldb.commit()
      treeproducts.delete(treeproducts.selection()[0])
      # messagebox.showinfo("F-Billing Revolution", "Record deleted successfully.")
    else:
      pass


######################## SEARCH PRODUCT  #######################################################################

  def search_pro():
    query = searchvar.get()
    selections = []
    for child in treeproducts.get_children():
        if query in treeproducts.item(child)['values']:
            print(treeproducts.item(child)['values'])
            selections.append(child)
    treeproducts.selection_set(selections)
  

  def search_product():
    global searchvar, searchtop
    searchtop = Toplevel()  
    searchtop.title("Find Text")
    searchtop.geometry("520x200+390+250")
    
    findwhat1=Label(searchtop,text="Find What:",pady=5,padx=10)
    findwhat1.place(x=5,y=20)
    searchvar = StringVar() 
    findwhat = ttk.Combobox(searchtop, width = 50, textvariable = searchvar)
    findwhat.place(x=80,y=25) 
    

    findButton = Button(searchtop, text ="Find next",width=10, command=search_pro)
    findButton.place(x=420,y=20)
    
    findin1=Label(searchtop,text="Find in:",pady=5,padx=10)
    findin1.place(x=5,y=47)
    n = StringVar() 
    findIN = ttk.Combobox(searchtop, width = 37, textvariable = n ) 
    # Adding combobox drop down list 
    findIN['values'] = ('Product/Service id',  
                              'Category', 
                              'Active', 
                              'name', 
                              'stock', 
                              'location', 
                              'image', 
                              '<<All>>') 
      
    findIN.place(x=80,y=54) 
    findIN.current(0)

    closeButton = Button(searchtop, text ="Close",width=10, command=lambda : searchtop.destroy())
    closeButton.place(x=420,y=50)

    match1=Label(searchtop,text="Match:",pady=5,padx=10)
    match1.place(x=5,y=74)
    n = StringVar() 
    match = ttk.Combobox(searchtop, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    match['values'] = ('From Any part',' Whole Field',  
                              ' From the beginning of the field')
      
    match.place(x=80,y=83) 
    match.current(0)

    search1=Label(searchtop,text="Search:",pady=5,padx=10)
    search1.place(x=5,y=102)
    n = StringVar() 
    search = ttk.Combobox(searchtop, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    search['values'] = ('All', 'up', 
                              'Down')
      
    search.place(x=80,y=112) 
    search.current(0)


    checkvarStatus4=IntVar()
   
    Button4 = Checkbutton(searchtop,variable = checkvarStatus4, 
                      text="Match Case", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button4.place(x=60,y=141)

    checkvarStatus5=IntVar()
   
    Button5 = Checkbutton(searchtop,variable = checkvarStatus5, 
                      text="Match Format", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button5.place(x=270,y=141)

    searchtop.mainloop()


######################## REFRESH PRODUCT  #######################################################################

  def refresh_pro_s():
    for record in treeproducts.get_children():
      treeproducts.delete(record)
    fbcursor.execute("select *  from Productservice")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      if i[6] == '1':
        acti = 'Active'
      else:
        acti = 'Inactive'
      sql = "select currencysign,currsignplace from company"
      fbcursor.execute(sql)
      currsymb = fbcursor.fetchone()
      if not currsymb: 
        if i[13] > i[14]:
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
          countp += 1              
        elif i[12] == '1':
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
          countp += 1
        else:
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
          countp += 1
              
      elif currsymb[1] == "before amount":
        if (i[13]) > (i[14]):
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
          countp += 1
        elif i[12] == '1':
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
          countp += 1
        else:
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
          countp += 1
      elif currsymb[1] == "before amount with space":
        if i[13] > i[14]:
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
          countp += 1
        elif i[12] == '1':
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
          countp += 1
        else:
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
          countp += 1
      elif currsymb[1] == "after amount":
        if i[13] > i[14]:
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
          countp += 1
        elif i[12] == '1':
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
          countp += 1
        else:
          treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
          countp += 1
      elif currsymb[1] == "after amount with space":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
            countp += 1

######################## View Image
# #######################################################################
  def psfile_image(event):
      itemid = treeproducts.item(treeproducts.focus())["values"][1]
      sql = "select * from Productservice where Productserviceid = %s"
      val = (itemid,)

      fbcursor.execute(sql, val)
      psdata = fbcursor.fetchone() 
      if psdata[17] is None:
        pass
      else:
        edit_window_img = Toplevel()
        edit_window_img.title("View Image")
        edit_window_img.geometry("700x500")
        image = Image.open("images/"+psdata[17])
        resize_image = image.resize((700, 500))
        image = ImageTk.PhotoImage(resize_image)
        psimage = Label(edit_window_img,image=image)
        psimage.photo = image
        psimage.pack()
  
######################## FRONT PAGE OF PRODUCT SERVICE SECTION #######################################################################

    
  mainFrame=Frame(tab8, relief=GROOVE, bg="#f8f8f2")
  mainFrame.pack(side="top", fill=BOTH)

  midFrame=Frame(mainFrame, bg="#f5f3f2", height=60)
  midFrame.pack(side="top", fill=X)

  lFrame=Frame(tab8, bg="#f8f8f2", height=600)
  lFrame.pack(side="top", fill=X)



  pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(5, 2))
  pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))

  productLabel = Button(midFrame,compound="top", text="Add new\nProduct",relief=RAISED,command=add_product_s_connection, image=productIcon, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  productLabel.pack(side="left", pady=3, ipadx=4)
  
  
  proeditLabel = Button(midFrame,compound="top", text="Edit/View\nProduct",relief=RAISED, image=proeditIcon,command=edit_product, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  proeditLabel.pack(side="left")

  
  prodeleteLabel = Button(midFrame,compound="top", text="Delete\nSelected",relief=RAISED, command=delete_product_check,image=prodeleteIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  prodeleteLabel.pack(side="left")

  pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=5)

  
  prosearchLabel = Button(midFrame,compound="top", text="Search in\nproducts",relief=RAISED,command=search_product, image=prosearchIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55, activebackground="red")
  prosearchLabel.pack(side="left")

  
  proimportLabel = Button(midFrame,compound="top", text="Import\nProducts",relief=RAISED,command=import_productservice_check, image=proimportIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  proimportLabel.pack(side="left")

  pn = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=5)

  
  proexportLabel = Button(midFrame,compound="top",command=export_product, text="Export\nProducts",relief=RAISED, image=proexportIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  proexportLabel.pack(side="left")


  pn = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  pn.pack(side="left")

  
  productrefreshLabel = Button(midFrame,compound="top", text="Refresh\nProduct List",relief=RAISED, image=prorefreshIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55, command=refresh_pro_s)
  productrefreshLabel.pack(side="left")

  prolabel = Label(mainFrame, text="Products/Services", font=("arial", 18), bg="#f8f8f2")
  prolabel.pack(side="left", padx=(20,0))

  pr_label = Label(mainFrame, text="Category", font=("arial", 16), bg="#f8f8f2")
  pr_label.place(x=1099,y=70)

  def pro_fil(event):
    pro_f = dro.get()
    for record in treeproducts.get_children():
      treeproducts.delete(record)

    sql = "select * from Productservice where category = %s"
    val = (pro_f,)
    fbcursor.execute(sql, val)
    product_fil = fbcursor.fetchall()
    
    countp = 0
    for i in product_fil:
      if i[6] == '1':
        acti = 'Active'
      else:
        acti = 'Inactive' 
      if i[13] > i[14]:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4] , i[7], i[13], i[15],i[17]),tags=('green',))
        countp += 1
      elif (i[12] =="0") == (i[13] <= i[14]):
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4] , i[7], i[13], i[15],i[17]),tags=('red',))
        countp += 1
      elif i[12] == '1':
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4] , i[7], i[13], i[15],i[17]),tags=('blue',))
        countp += 1
      else:
        pass

  sql = "SELECT DISTINCT category FROM Productservice"
  fbcursor.execute(sql,)
  lic = fbcursor.fetchall()
  dro = ttk.Combobox(mainFrame,)
  dro.pack(side="right", padx=(0,10))
  dro['values'] = lic
  dro.bind("<<ComboboxSelected>>", pro_fil)

  pro_label = Label(mainFrame, text="Right click on datagrid row for more options.",  bg="#f8f8f2")
  pro_label.pack(side="right", padx=(0,260))


  sql = 'select * from Productservice'
  fbcursor.execute(sql)
  pandsdata = fbcursor.fetchall()

  treeproducts=ttk.Treeview(tab8,selectmode='browse')
  treeproducts.place(x=8,y=100,height=580)
  vertical_bar=ttk.Scrollbar(tab8,orient="vertical")
  vertical_bar.place(x=1083,y=101,height=580)

  treeproducts["columns"]=("1","2","3","4","5","6","7","8","9")
  treeproducts["show"]='headings'
  treeproducts.column("1",width=0,anchor='c', stretch=False)
  treeproducts.column("2",width=160,anchor='c')
  treeproducts.column("3",width=190,anchor='c')
  treeproducts.column("4",width=120,anchor='c')
  treeproducts.column("5",width=120,anchor='c')
  treeproducts.column("6",width=120,anchor='c')
  treeproducts.column("7",width=130,anchor='c')
  treeproducts.column("8",width=120,anchor='c')
  treeproducts.column("9",width=112,anchor='c')
  treeproducts.heading("1",text="")
  treeproducts.heading("2",text="Product/Service ID")
  treeproducts.heading("3",text="Category")
  treeproducts.heading("4",text="Status")
  treeproducts.heading("5",text="Name")
  treeproducts.heading("6",text="Price")
  treeproducts.heading("7",text="Stock")
  treeproducts.heading("8",text="Location/warehouse")
  treeproducts.heading("9",text="Image")
  treeproducts.bind('<Double-Button-1>' , psfile_image)
  treeproducts.tag_configure('green', foreground='green')
  treeproducts.tag_configure('red', foreground='red')
  treeproducts.tag_configure('blue', foreground='blue')
  countp = 0
  for i in pandsdata:
    if i[6] == '1':
      acti = 'Active'
    else:
      acti = 'Inactive'
    sql = "select currencysign,currsignplace from company"
    fbcursor.execute(sql)
    currsymb = fbcursor.fetchone()
    if not currsymb: 
      if i[13] > i[14]:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
        countp += 1              
      elif i[12] == '1':
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
        countp += 1
      else:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
        countp += 1
              
    elif currsymb[1] == "before amount":
      if (i[13]) > (i[14]):
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
        countp += 1
      elif i[12] == '1':
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
        countp += 1
      else:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
        countp += 1

    elif currsymb[1] == "before amount with space":
      if i[13] > i[14]:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
        countp += 1
      elif i[12] == '1':
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
        countp += 1
      else:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
        countp += 1

    elif currsymb[1] == "after amount":
      if i[13] > i[14]:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
        countp += 1
      elif i[12] == '1':
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
        countp += 1
      else:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
        countp += 1

    elif currsymb[1] == "after amount with space":
      if i[13] > i[14]:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
        countp += 1
      elif i[12] == '1':
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
        countp += 1
      else:
        treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
        countp += 1


  treeproducts.place(height=580, width=1070, x=10, y=101)

  ######side_Listbox##############

  treeps=ttk.Treeview(tab8,selectmode='browse')
  treeps.place(height=580,width=254,
                        x=1099,y=101
                        )
  treeps["columns"]=("1")
  treeps["show"]='headings'
  treeps.column("1",width=254,anchor='c')
  treeps.heading("1",text="View filter by category")

  def items_selected(event):
    selected_indices = listbox.curselection()
    selected_filter = ",".join([listbox.get(i) for i in selected_indices])

    sql = 'select * from Productservice'
    fbcursor.execute(sql)
    pandsdata = fbcursor.fetchall()
    psql = "select * from Productservice where serviceornot=%s"
    val = ('0', )
    fbcursor.execute(psql, val)
    pdata = fbcursor.fetchall()

    ssql = "select * from Productservice where serviceornot=%s"
    val = ('1', )
    fbcursor.execute(ssql, val)
    sdata = fbcursor.fetchall()

    # pssql = "select * from Productservice where category=%s"
    # psval = (selected_filter, )
    # fbcursor.execute(pssql, psval)
    # pssdata = fbcursor.fetchall()
    if selected_filter == "View all records":
      for record in treeproducts.get_children():
        treeproducts.delete(record)
      countp = 0
      for i in pandsdata:
        if i[6] == '1':
          acti = 'Active'
        else:
          acti = 'Inactive' 
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if not currsymb: 
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1              
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1
              
        elif currsymb[1] == "before amount":
          if (i[13]) > (i[14]):
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "before amount with space":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "after amount":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "after amount with space":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
            countp += 1

    elif selected_filter == "View all products":
      for record in treeproducts.get_children():
        treeproducts.delete(record)
      countp = 0
      for i in pdata:
        if i[6] == '1':
          acti = 'Active'
        else:
          acti = 'Inactive' 
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if not currsymb: 
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1              
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1
              
        elif currsymb[1] == "before amount":
          if (i[13]) > (i[14]):
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "before amount with space":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "after amount":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "after amount with space":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
            countp += 1
    elif selected_filter == "View all services":
      for record in treeproducts.get_children():
        treeproducts.delete(record)
      countp = 0
      for i in sdata:
        if i[6] == '1':
          acti = 'Active'
        else:
          acti = 'Inactive' 
        sql = "select currencysign,currsignplace from company"
        fbcursor.execute(sql)
        currsymb = fbcursor.fetchone()
        if not currsymb: 
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1              
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1
              
        elif currsymb[1] == "before amount":
          if (i[13]) > (i[14]):
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0]+i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "before amount with space":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], currsymb[0] +" "+i[7], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "after amount":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+currsymb[0], i[13], i[15],i[17]),tags=('red',))
            countp += 1

        elif currsymb[1] == "after amount with space":
          if i[13] > i[14]:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('green',))
            countp += 1
          elif i[12] == '1':
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('blue',))
            countp += 1
          else:
            treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[3], acti, i[4], i[7]+" "+currsymb[0], i[13], i[15],i[17]),tags=('red',))
            countp += 1
  
  listbox = Listbox(tab8,height = 8,  
                        width = 29,  
                        bg = "white",
                        activestyle = 'dotbox',  
                        fg = "black",
                        highlightbackground="white")  
  listbox.insert(0, "View all records")
  listbox.insert(1, "View all products")
  listbox.insert(2, "View all services")
 

  listbox.place(x=1099,y=118,height=564,width=255)

  listbox.bind('<<ListboxSelect>>', items_selected)
  
  stockok = Label(tab8,text="Green: Stock is Ok",foreground="green",background="white").place(x =1110,y =580)
  stocko = Label(tab8,text="Red: Limit <= Low Stock Limit",foreground="red",background="white").place(x =1110,y =600)
  stock = Label(tab8,text="Blue: Service,no Stock Control",foreground="blue",background="white").place(x =1110,y =620)
  
############################  END PRODUCT SERVICES  ############################
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
  exctree.column("#0",width=0,anchor='c', stretch=False)
  exctree.column('1',width=378,anchor='c')
  exctree.place(x=15,y=200,height=115,width=380)
  exctree.bind('<Double-Button-1>' , edit_valueexc)
  sql = 'select * from extra_cost_name'
  fbcursor.execute(sql)
  setexctree = fbcursor.fetchall()
  countp = 0
  for i in setexctree:
      print(i[2])
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
      print(i,idgettingextracnid)
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
    print(itemid)
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
    print(usna)
    sql='SELECT * FROM users WHERE username=%s'
    val=(usna,)
    fbcursor.execute(sql,val)
    chpass = fbcursor.fetchone()
    print(chpass)
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
  print(sectab)
  
  
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
  
  
  exd = DateEntry(secondtab)
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
        print(whuser[0])
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
    print(sixtabdataback)
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

