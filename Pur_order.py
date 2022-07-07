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
from tkinter import font,colorchooser
from tkinter import font as tkFont
from _tkinter import TclError
from tkinter.scrolledtext import ScrolledText
##########################saiju##############
import matplotlib.pyplot as plt
from pylab import plot, show, xlabel, ylabel
from matplotlib.widgets import Cursor
from dateutil.relativedelta import relativedelta
import pendulum
import tkinter as tk

from pathlib import Path
import pandas as pd
from tkinter import messagebox
from tkinter import *
# from docx import Document
# from fpdf import FPDF
import os
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
import pdfkit
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email import encoders

import win32api
import win32print
from tkinter import filedialog
from pyautogui import alert
import os
import tempfile

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tkinter import font as tkFont
from tkinter import TclError
from textwrap import wrap
import PIL.Image
from PIL import ImageGrab
from PIL import ImageTk, Image, ImageFile
import PIL.Image
from datetime import date,datetime, timedelta
import re
import datetime as dt


fbilldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="fbillingsintgrtd", port="3306"
)
fbcursor = fbilldb.cursor(buffered=True)

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
  root.geometry("500x200+450+250")
  root.resizable(False, False)
  Label(text='Wellocome to F-Billing Revolution 2022',font='arial 13 bold').place(x=100,y=40)
  submitbtn1=Button(text='OPEN NOW', width=20,height=2,command=lo,activeforeground="white",activebackground="black",font='arial 8 bold').place(x=165,y=100)             
else:
    root=Tk()
    root.geometry("500x200+450+250")
    root.resizable(False, False)
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
color = PhotoImage(file="images/font_color.png")
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
color = PhotoImage(file="images/font_color.png") 

################ expenses button images ####################

imgr1 =PIL.Image.open("images/refresh.png")
exprefreshIcon=ImageTk.PhotoImage(imgr1)
imgr2 = PIL.Image.open("images/search-icon.png")
expsearchIcon=ImageTk.PhotoImage(imgr2)
imgr3 = PIL.Image.open("images/delete.png")
expdeleteIcon=ImageTk.PhotoImage(imgr3)

imgr4 = PIL.Image.open("images/edit.png")
expeditIcon=ImageTk.PhotoImage(imgr4)

imgr5 = PIL.Image.open("images/plus.png")
expenseIcon=ImageTk.PhotoImage(imgr5)

################ Product service button images ####################
imgr6 = PIL.Image.open("images/refresh.png")
prorefreshIcon=ImageTk.PhotoImage(imgr6)

imgr7 = PIL.Image.open("images/export-file.png")
proexportIcon=ImageTk.PhotoImage(imgr7)

imgr8 = PIL.Image.open("images/import.png")
proimportIcon=ImageTk.PhotoImage(imgr8)

imgr9= PIL.Image.open("images/research.png")
prosearchIcon=ImageTk.PhotoImage(imgr9)

imgr10 = PIL.Image.open("images/delete.png")
prodeleteIcon=ImageTk.PhotoImage(imgr10)

imgr11 = PIL.Image.open("images/plus.png")
productIcon=ImageTk.PhotoImage(imgr11)

imgr12 = PIL.Image.open("images/edit.png")
proeditIcon=ImageTk.PhotoImage(imgr12)
# customer Module Image
ad_usr = PIL.Image.open("images/user_add.png")
cus_addcustomerIcon=ImageTk.PhotoImage(ad_usr)

usr_edit = PIL.Image.open("images/user_edit.png")
cus_editcustomerIcon=ImageTk.PhotoImage(usr_edit)

usr_del = PIL.Image.open("images/user_delete.png")
cus_deletecustomerIcon=ImageTk.PhotoImage(usr_del)

usr_pre = PIL.Image.open("images/priewok.png")
cus_previewinvoiceIcon=ImageTk.PhotoImage(usr_pre)

usr_print = PIL.Image.open("images/printer.png")
cus_printinvoiceIcon=ImageTk.PhotoImage(usr_print)

usr_em = PIL.Image.open("images/gmail.png")
cus_emailinviceIcon=ImageTk.PhotoImage(usr_em)

usr_sms = PIL.Image.open("images/text-message.png")
cus_smsIcon=ImageTk.PhotoImage(usr_sms)

usr_imp = PIL.Image.open("images/import.png")
cus_importcustomerIcon=ImageTk.PhotoImage(usr_imp)

usr_exp = PIL.Image.open("images/export.png")
cus_exportcustomerIcon=ImageTk.PhotoImage(usr_exp)

usr_srh = PIL.Image.open("images/search-icon.png")
cus_customersearchIcon=ImageTk.PhotoImage(usr_srh)

usr_rfs= PIL.Image.open("images/refresh.png")
cus_refreshcustomerIcon=ImageTk.PhotoImage(usr_rfs)




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

  def create_purchase():
    pop1=Toplevel(pur_midFrame)
    pop1.title("Orders")
    pop1.geometry("950x690+150+0")


    #select vendor
    def pur_create_customer():
      cuselection=Toplevel()
      cuselection.title("Select Customer")
      cuselection.geometry("930x650+240+10")
      cuselection.resizable(False, False)


      #add new customer
      def p_add_customer():
        def cus_add_cst():
          cst_id=b1sd.get()#id
          cus_bs_nm=bnm_cus.get()
          if cst_id=="" or cus_bs_nm=="" :
                
            messagebox.showerror("Empty Field", "Customer ID field and Business Name field is Required!")

          else:
            
            #bs name
            # cmp_id=
            cus_bs_ad_cus=bdfdsfsd2.get("1.0",END)#bs ad name
            
            cus_bs_cnt=bs_cnt.get()#Contact person
            cus_bs_em=bs_em.get()#email bs
            cus_bs_tel=bs_tel.get()#bs tel
            cus_bs_fax=bs_fax.get()#bs fax
            cus_bs_mob=bs_mobi.get()#bs mob
            cus_bs_pymcheck=cus_ds_chk.get()# discount checkboc
            cus_bs_spc_tax=blsr.get()# specific tax
            cus_bs_spc_tax2=bdsfd14.get()# specific tax
            cus_bs_dis=b1f2.get()# discount
            cus_bs_ctr=bs_cus_ct.get()# customer category

            # ship 
            cus_shp_cat=cus_catg.get()# category
            cus_shp_st=cus_st.get()# status Checkbox
            cus_shp_cnt_pr=cus_sh_nam.get()#contact person
            cus_shp_adr=b2sds1.get("1.0",END)#contact address
            cus_shp_cnt=bs_sh_cnt.get()#Contact person
            cus_shp_em=bs_sh_em.get()#email bs
            cus_shp_tel=bs_sh_tel.get()#bs tel
            cus_shp_fax=bs_sh_fax.get()#bs fax
            cus_shp_cntry=cus_sh_coun.get()#contry
            cus_shp_city=cus_sh_cty.get()#city
            cus_shp_nte=scll.get("1.0", END)

            cus_ed_tbles="select customerno from customer where customerno=%s"
            cus_ed_tbles_valuz=(cst_id,)
            fbcursor.execute(cus_ed_tbles,cus_ed_tbles_valuz)
            cus_ins_val=fbcursor.fetchone()

            cus_ed_tbless="select businessname from customer where businessname=%s"
            cus_ed_tbless_valuz=(cus_bs_nm,)
            fbcursor.execute(cus_ed_tbless,cus_ed_tbless_valuz)
            cus_ins_valse=fbcursor.fetchone()
        
            if cus_ins_val is None:
              if cus_ins_valse is None:
                cus_tbl_add="INSERT INTO customer(customerno,category,status,businessname,businessaddress,shipname,shipaddress,contactperson,cpemail,cptelno,cpfax,cpmobileforsms,shipcontactperson,shipcpemail,shipcptelno,shipcpfax,taxexempt,specifictax1,discount,country,city,customertype,notes,specifictax2)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
                cus_tbl_add_val=(cst_id,cus_shp_cat,cus_shp_st,cus_bs_nm,cus_bs_ad_cus,cus_shp_cnt_pr,cus_shp_adr,cus_bs_cnt,cus_bs_em,cus_bs_tel,cus_bs_fax,cus_bs_mob,cus_shp_cnt,cus_shp_em,cus_shp_tel,cus_shp_fax,cus_bs_pymcheck,cus_bs_spc_tax,cus_bs_dis,cus_shp_cntry,cus_shp_city,cus_bs_ctr,cus_shp_nte,cus_bs_spc_tax2)
                fbcursor.execute(cus_tbl_add,cus_tbl_add_val)
                fbilldb.commit()
                for record in pur_customertree.get_children():
                  pur_customertree.delete(record)
                fbcursor.execute('SELECT * FROM Customer;') 
                j = 0
                for i in fbcursor:
                  pur_customertree.insert(parent='', index='end', iid=i, text='', values=(i[24],i[4],i[10],i[8]))
                  j += 1
                add_customer.destroy()
              else:
                messagebox.showerror("Already Exists", "Customer ID value already exists. Duplicate value not allowed")
            else:
                messagebox.showerror("Already Exists", "Business name is already exists. Duplicate value not allowed")
        
        def top_btn():
            cus_bs_nm=bnm_cus.get()
            cus_bs_ad_cus=bdfdsfsd2.get("1.0",END)#bs ad name
            b1fr1.delete(0,'end')
            b1fr1.insert(0,cus_bs_nm)
            b2sds1.delete(1.0,'end')
            b2sds1.insert(1.0,cus_bs_ad_cus)

        def btm_btn():
            cus_bs_cnt=bs_cnt.get()#Contact person
            cus_bs_em=bs_em.get()#email bs
            cus_bs_tel=bs_tel.get()#bs tel
            cus_bs_fax=bs_fax.get()#bs fax
            b141sd.insert(0,cus_bs_cnt)
            b21vcvc1.delete(0,'end')
            b21vcvc1.insert(0,cus_bs_em)
            b3zx1.delete(0,'end')
            b3zx1.insert(0,cus_bs_tel)
            b4x141.delete(0,'end')
            b4x141.insert(0,cus_bs_fax)



        add_customer = Toplevel()  
        add_customer.title("Add new Customer ")
        p2 = PhotoImage(file = "images/fbicon.png")
        add_customer.iconphoto(False, p2)
        add_customer.geometry("775x580+300+100")
        Labelframe1=LabelFrame(add_customer,text="Customer")
        Labelframe1.place(x=10,y=10,width=755,height=525)
        a1=Label(Labelframe1,text="Customer ID:",fg="Blue")
        a2=Label(Labelframe1,text="Category:")
        a3=Label(Labelframe1,text="Status :")
        a3.place(x=620,y=7)
        cu_idr=IntVar() 
        b1sd=Entry(Labelframe1)
        cus_catg=StringVar() 
        b2=ttk.Combobox(Labelframe1,textvariable = cus_catg)    
        sql_cust_dt='SELECT DISTINCT category from customer'
        fbcursor.execute(sql_cust_dt)
        catgry=fbcursor.fetchall()
        b2['values'] = catgry 
        b2.place(x=390,y=220) 
        b2.current(0)
        a1.place(x=10,y=7)
        a2.place(x=330,y=7)   
        b1sd.place(x=120,y=7,width=200)
        b2.place(x=390,y=7,width=220)
        cus_st = IntVar()
        chkbtn1 = Checkbutton(Labelframe1, text = "Active", variable = cus_st, onvalue = 1, offvalue = 0)
        chkbtn1.select()
        chkbtn1.place(x=670,y=6)


        Labelframe2=LabelFrame(Labelframe1,text="Invoice to (appears on invoice)")
        Labelframe2.place(x=10,y=35,width=340,height=125)
        a1=Label(Labelframe2,text="Business Name:",fg="Blue").place(x=10,y=10)
        a2=Label(Labelframe2,text="Address:",fg="Blue").place(x=10,y=35)
        bnm_cus=StringVar()
        bs_adr_cus=StringVar()
        
        

        b1=Entry(Labelframe2, textvariable=bnm_cus)
        # b1.config(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
        b1.place(x=110,y=10,width=210)

        bdfdsfsd2=scrolledtext.ScrolledText(Labelframe2)
        bdfdsfsd2.place(x=110,y=35,width=210,height=63)  
        btn110=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>", command=lambda:top_btn()).place(x=359,y=85,height=20)


        Labelframe3=LabelFrame(Labelframe1,text="Ship to (appears on invoice)")
        Labelframe3.place(x=400,y=35,width=340,height=125)
        a11=Label(Labelframe3,text="Ship to Name:").place(x=10,y=10)
        a21=Label(Labelframe3,text="Address:").place(x=10,y=35)
        cus_sh_nam=StringVar()
        cus_sh_adr=StringVar()
        b1fr1=Entry(Labelframe3, textvariable=cus_sh_nam)
        b1fr1.place(x=110,y=10,width=210)
        b2sds1=scrolledtext.ScrolledText(Labelframe3)
        b2sds1.place(x=110,y=35,width=210,height=63)


        Labelframe4=LabelFrame(Labelframe1,text="Contact")
        Labelframe4.place(x=10,y=170,width=340,height=137)
        a11=Label(Labelframe4,text="Contact Person:").place(x=10,y=10)
        a21=Label(Labelframe4,text="Email Address:",fg="Blue").place(x=10,y=35)
        a31=Label(Labelframe4,text="Tel. No:").place(x=10,y=60)
        a41=Label(Labelframe4,text="Fax:").place(x=200,y=60)
        a51=Label(Labelframe4,text="Mobile number for SMS notification:").place(x=10,y=85)
        bs_cnt=StringVar()
        bs_em=StringVar()
        bs_tel=StringVar()
        bs_fax=StringVar()
        bs_mobi=StringVar()
        b11=Entry(Labelframe4, textvariable=bs_cnt).place(x=110,y=10,width=210)

        #-------------------------------------------------------------------------------------------Email Validation
        b21=Entry(Labelframe4,textvariable=bs_em)
        

        def validate(value):
              
              """
              Validat the email entry
              :param value:
              :return:
              """
              pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
              if re.fullmatch(pattern, value) is None:
                  
                  return False

              b21.config(fg="black")
              return True

        def on_invalid():
              b21.config(fg="red")
              
        vcmd = (Labelframe2.register(validate), '%P')
        ivcmd = (Labelframe2.register(on_invalid),)

        b21.config(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
        
        b21.place(x=110,y=35,width=210)

        b311=Entry(Labelframe4,textvariable=bs_tel)
        def validate_tel(value):
              
              """
              Validat the email entry
              :param value:
              :return:
              """
              pattern = r'^[0-9]\d{9,10}$'
              if re.fullmatch(pattern, value) is None:
                  
                  return False
              b311.config(fg="black")
              return True

        def on_invalid_tel():
              b311.config(fg="red")
              
        v_tel_cmd = (Labelframe2.register(validate_tel), '%P')
        iv_tel_cmd = (Labelframe2.register(on_invalid_tel),)
        
        
        b311.config(validate='focusout', validatecommand=v_tel_cmd, invalidcommand=iv_tel_cmd)
        b311.place(x=110,y=60,width=90)

        b4126=Entry(Labelframe4,textvariable=bs_fax)
        def validate_telb4126(value):
              
              """
              Validat the email entry
              :param value:
              :return:
              """
              pattern = r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
              if re.fullmatch(pattern, value) is None:
                  
                  return False
              b4126.config(fg="black")
              return True

        def on_invalid_telb4126():
              b4126.config(fg="red")
              
        v_tel_cmdb4126 = (Labelframe2.register(validate_telb4126), '%P')
        iv_tel_cmdb4126 = (Labelframe2.register(on_invalid_telb4126),)
        b4126.config(validate='focusout', validatecommand=v_tel_cmdb4126, invalidcommand=iv_tel_cmdb4126)
        b4126.place(x=230,y=60,width=90)
        
        b51=Entry(Labelframe4,textvariable=bs_mobi)
        def validate_telb51(value):
              
              """
              Validat the email entry
              :param value:
              :return:
              """
              pattern = r'^[0-9]\d{9}$'
              if re.fullmatch(pattern, value) is None:
                  
                  return False
              b51.config(fg="black")
              return True

        def on_invalid_telb51():
              b51.config(fg="red")
              
        v_tel_cmdb51 = (Labelframe2.register(validate_telb51), '%P')
        iv_tel_cmdb51 = (Labelframe2.register(on_invalid_telb51),)
        b51.config(validate='focusout', validatecommand=v_tel_cmdb51, invalidcommand=iv_tel_cmdb51)
        b51.place(x=215,y=85,width=105)
        btn111=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>", command=lambda:btm_btn()).place(x=359,y=220,height=20)

        bs_sh_cnt=StringVar()
        bs_sh_em=StringVar()
        bs_sh_tel=StringVar()
        bs_sh_fax=StringVar()

        Labelframe5=LabelFrame(Labelframe1,text="Ship To Contact")
        Labelframe5.place(x=400,y=170,width=340,height=108)
        a11=Label(Labelframe5,text="Contact Person:").place(x=10,y=10)
        a21=Label(Labelframe5,text="Email Address:").place(x=10,y=35)
        a31=Label(Labelframe5,text="Tel. No:").place(x=10,y=60)
        a41=Label(Labelframe5,text="Fax:").place(x=200,y=60)
      
        b141sd=Entry(Labelframe5, textvariable=bs_sh_cnt)
        b141sd.place(x=110,y=10,width=210)
        
        b21vcvc1=Entry(Labelframe5,textvariable=bs_sh_em)
        def validateb211(value):
              
              """
              Validat the email entry
              :param value:
              :return:
              """
              pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
              if re.fullmatch(pattern, value) is None:
                  
                  return False

              b21vcvc1.config(fg="black")
              return True

        def on_invalidb211():
              b21vcvc1.config(fg="red")
              
        vcmdb211 = (Labelframe2.register(validateb211), '%P')
        ivcmdb211 = (Labelframe2.register(on_invalidb211),)

        b21vcvc1.config(validate='focusout', validatecommand=vcmdb211, invalidcommand=ivcmdb211)
        b21vcvc1.place(x=110,y=35,width=210)
        
        b3zx1=Entry(Labelframe5,textvariable=bs_sh_tel)
        def validate_telb31(value):
              
              """
              Validat the email entry
              :param value:
              :return:
              """
              pattern = r'^[0-9]\d{9,10}$'
              if re.fullmatch(pattern, value) is None:
                  
                  return False
              b3zx1.config(fg="black")
              return True

        def on_invalid_telb31():
              b3zx1.config(fg="red")
              
        v_tel_cmdb31 = (Labelframe2.register(validate_telb31), '%P')
        iv_tel_cmdb31 = (Labelframe2.register(on_invalid_telb31),)
        b3zx1.config(validate='focusout', validatecommand=v_tel_cmdb31, invalidcommand=iv_tel_cmdb31)
        b3zx1.place(x=110,y=60,width=90)

        b4x141=Entry(Labelframe5,textvariable=bs_sh_fax)
        def validate_telb4141(value):
              
              """
              Validat the email entry
              :param value:
              :return:
              """
              pattern = r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
              if re.fullmatch(pattern, value) is None:
                  
                  return False
              b4x141.config(fg="black")
              return True

        def on_invalid_telb4141():
              b4x141.config(fg="red")
              
        v_tel_cmdb4141 = (Labelframe2.register(validate_telb4141), '%P')
        iv_tel_cmdb4141 = (Labelframe2.register(on_invalid_telb4141),)
        b4x141.config(validate='focusout', validatecommand=v_tel_cmdb4141, invalidcommand=iv_tel_cmdb4141)
        b4x141.place(x=230,y=60,width=90)


        Labelframe6=LabelFrame(Labelframe1,text="Payment Option")
        Labelframe6.place(x=10,y=317,width=340,height=80)
        cus_ds_chk = StringVar()
        cus_sp_tx=IntVar()
        cus_sp_tx2=IntVar()
        cus_sp_disc=IntVar()
        chkbtn1 = Checkbutton(Labelframe6, text = "Tax Exempt", variable = cus_ds_chk, onvalue = 1, offvalue = 0, font=("arial", 8))
        chkbtn1.place(x=10,y=6)
        chkbtn1.select()

        
        a12=Label(Labelframe6,text="Discount%:").place(x=10,y=30)
        
        cus_sp_disc = IntVar(Labelframe6)
        
        
        #-----------------------------------------------------------------------------------------------tax2
        swt='select taxtype from company'
        fbcursor.execute(swt)
        fdt=fbcursor.fetchone()
        def tax_frt(S,d):
            if d=='1':
              if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
                return False
              return True
              
            if d.isdigit():
              return True


        edt_lty=(Labelframe6.register(tax_frt), '%S','%d')
        blsr=Entry(Labelframe6, textvariable=cus_sp_tx)
        bdsfd14=Entry(Labelframe6)
        if fdt[0]=='3':
          a11=Label(Labelframe6,text="Specific Tax1%:").place(x=150,y=7)
          blsr=Entry(Labelframe6, )
          
          # edt_ltyr=(Labelframe6.register(tax_frtinv),)
          blsr.config(validate='key',validatecommand=(edt_lty))
          blsr.place(x=250,y=7,width=70)
          
          bdsfd14.config(validate='key',validatecommand=(edt_lty))
          bdsfd14.place(x=250,y=30,width=70)
          a16=Label(Labelframe6,text="Specific Tax2%::").place(x=150,y=30)
        elif fdt[0]=='2':
          a11=Label(Labelframe6,text="Specific Tax1%:").place(x=150,y=7)
          
          blsr.config(validate='key',validatecommand=(edt_lty))
          blsr.place(x=250,y=7,width=70)
        elif fdt[0]=='1':
          pass
        b1f2=Entry(Labelframe6)
        b1f2.config(validate='key',validatecommand=(edt_lty))
        b1f2.place(x=80,y=30,width=70)

        Labelframe7=LabelFrame(Labelframe1,text="Customer type")
        Labelframe7.place(x=10,y=405,width=340,height=90)
        bs_cus_ct=StringVar()
        r1=Radiobutton(Labelframe7, text = "Client", variable = bs_cus_ct, value ="Client")
        r1.select()
        r1.place(x=5,y=15)
        
        r2=Radiobutton(Labelframe7, text = "Vender", variable = bs_cus_ct, value = "Vender")
        r2.deselect()
        r2.place(x=90,y=15)
        r3=Radiobutton(Labelframe7, text = "Both(Client/Vender)", variable = bs_cus_ct, value = "Both(Client/Vender)")
        r3.deselect()
        r3.place(x=180,y=15)


        Labelframe8=LabelFrame(Labelframe1,text="Additional Info")
        Labelframe8.place(x=400,y=288,width=340,height=80)
        a11=Label(Labelframe8,text="Country:").place(x=10,y=5)
        a12=Label(Labelframe8,text="City:").place(x=10,y=30)
        cus_sh_coun=StringVar() 
        cus_sh_cty=StringVar() 

        b11=ttk.Combobox(Labelframe8,textvariable=cus_sh_coun)
        b11.place(x=110,y=5,width=210)
        b11['values'] = ('India','America')    
        
        b11.place(x=110,y=5) 
        b12=Entry(Labelframe8,textvariable=cus_sh_cty).place(x=110,y=30,width=210)
        Labelframe9=LabelFrame(Labelframe1,text="Notes")
        Labelframe9.place(x=400,y=380,width=340,height=115)
        '''scrollbar = Scrollbar(Labelframe9)
              scrollbar.place(x=300,y=10)
              b12=Entry(Labelframe9,yscrollcommand=scrollbar.set).place(x=10,y=10,width=290,height=70)
              yscrollcommand.config(command=b12.yview)'''
        cus_nt=StringVar()
        global scll
        scll=scrolledtext.ScrolledText(Labelframe9)
        scll.place(x=20,y=10,width=295,height=70)
        # scrollbar_cus_nt = Scrollbar(Labelframe9)
        # scrollbar_cus_nt.place(x=295,y=10)

        btn1=Button(add_customer,width=50,compound = LEFT,image=tick ,command=lambda:cus_add_cst(),text="  OK").place(x=20, y=545)
        btn2=Button(add_customer,width=80,compound = LEFT,image=cancel,text="  Cancel",command=add_customer.destroy).place(x=665, y=545)

      def p_edit_customer():
        try:
          cus_id=pur_customertree.item(pur_customertree.focus())["values"][0]
          
          cus_ed_tbles="select * from customer where customerno=%s"
          cus_ed_tbles_valuz=(cus_id,)
          fbcursor.execute(cus_ed_tbles,cus_ed_tbles_valuz)
          cus_ins_val=fbcursor.fetchone()

          def cus_edit_cst():
            
                  cst_id=b1s.get()#id
                
                  cus_bs_nm=bnm_cus.get()#bs name

                  cus_bs_ad_cus=bnjh2.get('1.0',END)#bs ad name
                  cus_bs_cnt=bs_cnt.get()#Contact person
                  cus_bs_em=bs_em.get()#email bs
                  cus_bs_tel=bs_tel.get()#bs tel
                  cus_bs_fax=bs_fax.get()#bs fax
                  cus_bs_mob=bs_mobi.get()#bs mob
                  cus_bs_pymcheck=cus_ds_chk.get()# discount checkboc
                  cus_bs_spc_tax=cus_sp_tx.get()# specific tax
                  cus_bs_spc_tax2=cus_sp_tx2.get()
                  cus_bs_dis=cus_sp_disc.get()# discount
                  cus_bs_ctr=bs_cus_ct.get()# customer category

                  # ship 
                  cus_shp_cat=cus_catg.get()# category
                  cus_shp_st=cus_st.get()# status Checkbox
                  cus_shp_cnt_pr=cus_sh_nam.get()#contact person
                  cus_shp_adr=b2vxcvcxbc1.get("1.0",END)#contact address
                  cus_shp_cnt=bs_sh_cnt.get()#Contact person
                  cus_shp_em=bs_sh_em.get()#email bs
                  cus_shp_tel=bs_sh_tel.get()#bs tel
                  cus_shp_fax=bs_sh_fax.get()#bs fax
                  cus_shp_cntry=cus_sh_coun.get()#contry
                  cus_shp_city=cus_sh_cty.get()#city
                  cus_shp_ntre=cfgd.get("1.0", END) 
                  
                  cus_ed_tbless="select businessname from customer where businessname=%s"
                  cus_ed_tbless_valuz=(cus_bs_nm,)
                  fbcursor.execute(cus_ed_tbless,cus_ed_tbless_valuz)
                  cus_ins_valse=fbcursor.fetchone()
                
                  cus_tbl_edit="update customer set customerno=%s,category=%s,status=%s,businessname=%s,businessaddress=%s,shipname=%s,shipaddress=%s,contactperson=%s,cpemail=%s,cptelno=%s,cpfax=%s,cpmobileforsms=%s,shipcontactperson=%s,shipcpemail=%s,shipcptelno=%s,shipcpfax=%s,taxexempt=%s,specifictax1=%s,discount=%s,country=%s,city=%s,customertype=%s,notes=%s, specifictax2=%s where customerno = %s" #adding values into db
                  cus_tbl_edit_val=(cst_id,cus_shp_cat,cus_shp_st,cus_bs_nm,cus_bs_ad_cus,cus_shp_cnt_pr,cus_shp_adr,cus_bs_cnt,cus_bs_em,cus_bs_tel,cus_bs_fax,cus_bs_mob,cus_shp_cnt,cus_shp_em,cus_shp_tel,cus_shp_fax,cus_bs_pymcheck,cus_bs_spc_tax,cus_bs_dis,cus_shp_cntry,cus_shp_city,cus_bs_ctr,cus_shp_ntre,cus_bs_spc_tax2,cus_id,)
                  fbcursor.execute(cus_tbl_edit,cus_tbl_edit_val)
                  fbilldb.commit()
                  cus_main_s=ttk.Style()
                  for record in pur_customertree.get_children():
                    pur_customertree.delete(record)
                  fbcursor.execute('SELECT * FROM Customer;') 
                  j = 0
                  for i in fbcursor:
                    pur_customertree.insert(parent='', index='end', iid=i, text='', values=(i[24],i[4],i[10],i[8]))
                    j += 1
                  edit_customer.destroy()
                    

          def top_SHP_btn():
            cus_bs_nm=bnm_cus.get()#bs name
            # cmp_id=
            cus_bs_ad_cus=bnjh2.get("1.0",END)#bs ad name
            b1fdgfg1.delete(0,'end')
            b1fdgfg1.insert(0,cus_bs_nm)
            b2vxcvcxbc1.delete(1.0,'end')
            b2vxcvcxbc1.insert(1.0,cus_bs_ad_cus)

          def btm_shp_btn():
              
              cus_bs_cnt=bs_cnt.get()#Contact person
              cus_bs_em=bs_em.get()#email bs
              cus_bs_tel=bs_tel.get()#bs tel
              cus_bs_fax=bs_fax.get()#bs fax
              b1dsf1.delete(0,'end')
              b1dsf1.insert(0,cus_bs_cnt)
              b21cd1.delete(0,'end')
              b21cd1.insert(0,cus_bs_em)
              b311.delete(0,'end')
              b311.insert(0,cus_bs_tel)
              b414.delete(0,'end')
              b414.insert(0,cus_bs_fax)
          edit_customer = Toplevel()  
          edit_customer.title("Add new Customer ")
          p2 = PhotoImage(file = "images/fbicon.png")
          edit_customer.iconphoto(False, p2)
          edit_customer.geometry("775x580+300+100")
          Labelframe1=LabelFrame(edit_customer,text="Customer")
          Labelframe1.place(x=10,y=10,width=755,height=525)
          a1=Label(Labelframe1,text="Customer ID:",fg="Blue")
          a2=Label(Labelframe1,text="Category:")
          a3=Label(Labelframe1,text="Status :")
          a3.place(x=620,y=7)
        
          b1s=Entry(Labelframe1)
          
          b1s.insert(0,cus_ins_val[24])
          b1s.config(state=DISABLED,disabledbackground="white",disabledforeground="black")
          cus_catg=StringVar() 
          b2=ttk.Combobox(Labelframe1,textvariable = cus_catg) 
          sql_cust_dt='SELECT DISTINCT category from customer'
          fbcursor.execute(sql_cust_dt)
          catgry=fbcursor.fetchall()    
          b2['values'] = catgry  
          b2.place(x=390,y=220) 
          b2.current(cus_ins_val[3])
          a1.place(x=10,y=7)
          a2.place(x=330,y=7)   
          b1s.place(x=120,y=7,width=200)
          b2.place(x=390,y=7,width=220)
          cus_st = IntVar()
          chkbtn1 = Checkbutton(Labelframe1, text = "Active", variable = cus_st, onvalue = 1, offvalue = 0)
          if cus_ins_val[3]=="0":
            chkbtn1.deselect()
          else:
            chkbtn1.select()
          chkbtn1.place(x=670,y=6)

          Labelframe2=LabelFrame(Labelframe1,text="Invoice to (appears on invoice)")
          Labelframe2.place(x=10,y=35,width=340,height=125)
          a1=Label(Labelframe2,text="Business Name:",fg="Blue").place(x=10,y=10)
          a2=Label(Labelframe2,text="Address:",fg="Blue").place(x=10,y=35)
          bnm_cus=StringVar()
          bs_adr_cus=StringVar()
          b1=Entry(Labelframe2, textvariable=bnm_cus)
          b1.insert(0,cus_ins_val[4])
          b1.place(x=110,y=10,width=210)
          bnjh2=scrolledtext.ScrolledText(Labelframe2) 
          
          bnjh2.insert(1.0,cus_ins_val[5])
          bnjh2.place(x=110,y=35,width=210,height=63) 
          # b1.place(x=359,y=85,height=20)
          btn110=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>", command=lambda:top_SHP_btn()).place(x=359,y=85,height=20)


          Labelframe3=LabelFrame(Labelframe1,text="Ship to (appears on invoice)")
          Labelframe3.place(x=400,y=35,width=340,height=125)
          a11=Label(Labelframe3,text="Ship to Name:").place(x=10,y=10)
          a21=Label(Labelframe3,text="Address:").place(x=10,y=35)
          cus_sh_nam=StringVar()
          cus_sh_adr=StringVar()
          b1fdgfg1=Entry(Labelframe3, textvariable=cus_sh_nam)
          b1fdgfg1.insert(0,str(cus_ins_val[6]))
          b1fdgfg1.place(x=110,y=10,width=210)
          b2vxcvcxbc1=scrolledtext.ScrolledText(Labelframe3)
          b2vxcvcxbc1.delete(1.0,'end')
          b2vxcvcxbc1.insert(1.0,str(cus_ins_val[7]))
          b2vxcvcxbc1.place(x=110,y=35,width=210,height=63)
          


          Labelframe4=LabelFrame(Labelframe1,text="Contact")
          Labelframe4.place(x=10,y=170,width=340,height=137)
          a11=Label(Labelframe4,text="Contact Person:").place(x=10,y=10)
          
          a21=Label(Labelframe4,text="Email Address:",fg="Blue").place(x=10,y=35)
          a31=Label(Labelframe4,text="Tel. No:").place(x=10,y=60)
          a41=Label(Labelframe4,text="Fax:").place(x=200,y=60)
          a51=Label(Labelframe4,text="Mobile number for SMS notification:").place(x=10,y=85)
          
          bs_cnt=StringVar()
          bs_em=StringVar()
          bs_tel=StringVar()
          bs_fax=StringVar()
          
          b11=Entry(Labelframe4, textvariable=bs_cnt)
          b11.insert(0,str(cus_ins_val[8]))
          b11.place(x=110,y=10,width=210)
          
          b21=Entry(Labelframe4,textvariable=bs_em)
          def validate(value):
                
                """
                Validat the email entry
                :param value:
                :return:
                """
                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                if re.fullmatch(pattern, value) is None:
                    
                    return False
                b21.config(fg="black")
                return True

          def on_invalid():
                b21.config(fg="red")
                
          vcmd = (Labelframe4.register(validate), '%P')
          ivcmd = (Labelframe4.register(on_invalid),)

          
          
          b21.insert(0,str(cus_ins_val[9]))
          b21.config(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
          b21.place(x=110,y=35,width=210)
          
          def validate_tel(value):
                
                """
                Validat the email entry
                :param value:
                :return:
                """
                pattern = r'^[0-9]\d{9,10}$'
                if re.fullmatch(pattern, value) is None:
                    return False
                    
                b31.config(fg="black")
                return True

          def on_invalid_tel():
              b31.config(fg="red")
          
              
          v_tel_cmd = (Labelframe4.register(validate_tel), '%P')
          iv_tel_cmd = (Labelframe4.register(on_invalid_tel),)

          b31=Entry(Labelframe4,textvariable=bs_tel)
          b31.config(validate='focusout', validatecommand=v_tel_cmd, invalidcommand=iv_tel_cmd)
          b31.insert(0,str(cus_ins_val[10]))

          b31.place(x=110,y=60,width=90)
          b4126=Entry(Labelframe4,textvariable=bs_fax)
          def validate_telb4126(value):
                
                """
                Validat the email entry
                :param value:
                :return:
                """
                pattern = r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
                if re.fullmatch(pattern, value) is None:
                    
                    return False
                b4126.config(fg="black")
                return True

          def on_invalid_telb4126():
                b4126.config(fg="red")
                
          v_tel_cmdb4126 = (Labelframe4.register(validate_telb4126), '%P')
          iv_tel_cmdb4126 = (Labelframe4.register(on_invalid_telb4126),)
          b4126.config(validate='focusout', validatecommand=v_tel_cmdb4126, invalidcommand=iv_tel_cmdb4126)
          b4126.insert(0,str(cus_ins_val[11]))
          b4126.place(x=230,y=60,width=90)
          bs_mobi=StringVar()
          b5fd1=Entry(Labelframe4,textvariable=bs_mobi)
          def validate_tel3(value):
                
                """
                Validat the email entry
                :param value:
                :return:
                """
                pattern = r'^[0-9]\d{9}$'
                if re.fullmatch(pattern, value) is None:
                    return False
                    
                b5fd1.config(fg="black")
                return True

          def on_invalid_tel3():
              b5fd1.config(fg="red")
          
          v_tel_cmd3 = (Labelframe4.register(validate_tel3), '%P')
          iv_tel_cmd3 = (Labelframe4.register(on_invalid_tel3),)
          b5fd1.insert(0,str(cus_ins_val[12]))
          b5fd1.config(validate='focusout', validatecommand=v_tel_cmd3, invalidcommand=iv_tel_cmd3)
        
          b5fd1.place(x=215,y=85,width=105)
          btn111=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>",command=lambda:btm_shp_btn())
          btn111.place(x=359,y=220,height=20)
        
          bs_sh_cnt=StringVar()
          bs_sh_em=StringVar()
          bs_sh_tel=StringVar()
          bs_sh_fax=StringVar()
      
          Labelframe5=LabelFrame(Labelframe1,text="Ship To Contact")
          Labelframe5.place(x=400,y=170,width=340,height=108)
          a11=Label(Labelframe5,text="Contact Person:").place(x=10,y=10)
          a21=Label(Labelframe5,text="Email Address:").place(x=10,y=35)
          a31=Label(Labelframe5,text="Tel. No:").place(x=10,y=60)
          a41=Label(Labelframe5,text="Fax:").place(x=200,y=60)
          
          b1dsf1=Entry(Labelframe5, textvariable=bs_sh_cnt)
          b1dsf1.insert(0,str(cus_ins_val[13]))
          b1dsf1.place(x=110,y=10,width=210)
          b21cd1=Entry(Labelframe5,textvariable=bs_sh_em)
          

          def validateb21(value):
                
                """
                Validat the email entry
                :param value:
                :return:
                """
                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                if re.fullmatch(pattern, value) is None:
                    
                    return False

              
                b21cd1.config(fg="black")
                return True

          def on_invalidb21():
                b21cd1.config(fg="red")
                
          vcmdb21 = (Labelframe5.register(validateb21), '%P')
          ivcmdb21 = (Labelframe5.register(on_invalidb21),)
          
          b21cd1.config(validate='focusout', validatecommand=vcmdb21, invalidcommand=ivcmdb21)
          b21cd1.insert(0,str(cus_ins_val[14]))
          b21cd1.place(x=110,y=35,width=210)
          b311=Entry(Labelframe5,textvariable=bs_sh_tel)
          def validate_telb311(value):
                
                """
                Validat the email entry
                :param value:
                :return:
                """
                pattern = r'^[0-9]\d{9,10}$'
                if re.fullmatch(pattern, value) is None:
                    return False
                    
                b311.config(fg="black")
                return True

          def on_invalid_telb311():
              b311.config(fg="red")
          v_tel_cmdb311 = (Labelframe5.register(validate_telb311), '%P')
          iv_tel_cmdb311 = (Labelframe5.register(on_invalid_telb311),)

          b311.insert(0,str(cus_ins_val[15]))
          b311.config(validate='focusout', validatecommand=v_tel_cmdb311, invalidcommand=iv_tel_cmdb311)
          b311.place(x=110,y=60,width=90)

          b414=Entry(Labelframe5,textvariable=bs_sh_fax)
          def validate_telb414(value):
                
                """
                Validat the email entry
                :param value:
                :return:
                """
                pattern = r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
                if re.fullmatch(pattern, value) is None:
                    
                    return False
                b414.config(fg="black")
                return True

          def on_invalid_telb414():
                b414.config(fg="red")
                
          v_tel_cmdb414 = (Labelframe5.register(validate_telb414), '%P')
          iv_tel_cmdb414 = (Labelframe5.register(on_invalid_telb414),)
          b414.config(validate='focusout', validatecommand=v_tel_cmdb414, invalidcommand=iv_tel_cmdb414)

          b414.insert(0,str(cus_ins_val[16]))
          b414.place(x=230,y=60,width=90)


          Labelframe6=LabelFrame(Labelframe1,text="Payment Option")
          Labelframe6.place(x=10,y=317,width=340,height=80)
          cus_ds_chk = StringVar()
          cus_sp_tx=IntVar()
          cus_sp_tx2=IntVar()
          cus_sp_disc=IntVar()
          chkbtn1 = Checkbutton(Labelframe6, text = "Tax Exempt", variable = cus_ds_chk, onvalue = 1, offvalue = 0, font=("arial", 8))
          if cus_ins_val[17]=="0":
            chkbtn1.deselect()
          else:
            chkbtn1.select()
          chkbtn1.place(x=10,y=6)

          
          a12=Label(Labelframe6,text="Discount%:").place(x=10,y=30)
          cus_sp_disc = IntVar(Labelframe6)

          cus_sp_disc=Entry(Labelframe6)
          
            # edt_ltyr=(Labelframe6.register(tax_frtinv),)
          def tax_frt(S,d):
              if d=='1':
                if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
                  return False
                return True
                
              if d.isdigit():
                return True


          edt_lty=(Labelframe6.register(tax_frt), '%S','%d')

          cus_sp_disc.insert(0,str(cus_ins_val[19]))
          cus_sp_disc.config(validate='key',validatecommand=(edt_lty))
          cus_sp_disc.place(x=80,y=30,width=70)

          swt='select taxtype from company'
          fbcursor.execute(swt)
          fdt=fbcursor.fetchone()
          print(fdt[0])
          cus_sp_tx=Entry(Labelframe6)
          cus_sp_tx2=Entry(Labelframe6)
          cus_sp_tx=Entry(Labelframe6)
          if fdt[0]=='3':

            a11=Label(Labelframe6,text="Specific Tax1%:").place(x=150,y=7)
            
            cus_sp_tx.insert(0,str(cus_ins_val[18]))
            cus_sp_tx.config(validate='key',validatecommand=(edt_lty))
            cus_sp_tx.place(x=250,y=7,width=70)
            
            cus_sp_tx2.insert(0,str(cus_ins_val[25]))
            cus_sp_tx2.config(validate='key',validatecommand=(edt_lty))
            cus_sp_tx2.place(x=250,y=30,width=70)
            
            a16=Label(Labelframe6,text="Specific Tax2%::").place(x=150,y=30)
          elif fdt[0]=='2':
            a11=Label(Labelframe6,text="Specific Tax1%:").place(x=150,y=7)
            
            cus_sp_tx.insert(0,str(cus_ins_val[18]))
            cus_sp_tx.config(validate='key',validatecommand=(edt_lty))
            cus_sp_tx.place(x=250,y=7,width=70)
          elif fdt[0]=='1':
            pass

          Labelframe7=LabelFrame(Labelframe1,text="Customer type")
          Labelframe7.place(x=10,y=405,width=340,height=90)
          bs_cus_ct=StringVar()
          r1=Radiobutton(Labelframe7, text = "Client", variable = bs_cus_ct, value ="Client")
          r2=Radiobutton(Labelframe7, text = "Vender", variable = bs_cus_ct, value = "Vender")
          r3=Radiobutton(Labelframe7, text = "Both(Client/Vender)", variable = bs_cus_ct, value = "Both(Client/Vender)")
          if cus_ins_val[22]=="Client":
            r1.select()
            r2.deselect()
            r3.deselect()
          elif cus_ins_val[22]=="Vender":
            r1.deselect()
            r2.select()
            r3.deselect()
          else:
            r1.deselect()
            r2.deselect()
            r3.select()
          r1.place(x=5,y=15)
          r2.place(x=90,y=15)
          r3.place(x=180,y=15)

          Labelframe8=LabelFrame(Labelframe1,text="Additional Info")
          Labelframe8.place(x=400,y=288,width=340,height=80)
          a11=Label(Labelframe8,text="Country:").place(x=10,y=5)
          a12=Label(Labelframe8,text="City:").place(x=10,y=30)
          cus_sh_coun=StringVar() 
          cus_sh_cty=StringVar() 

          b11=ttk.Combobox(Labelframe8,textvariable=cus_sh_coun)
          b11.place(x=110,y=5,width=210)
          b11['values'] = ('India','America')  
          b11.insert(0,str(cus_ins_val[20]))  
          b11.place(x=110,y=5) 
          b12=Entry(Labelframe8,textvariable=cus_sh_cty)
          b12.insert(0,str(cus_ins_val[21]))  
          b12.place(x=110,y=30,width=210)
          Labelframe9=LabelFrame(Labelframe1,text="Notes")
          Labelframe9.place(x=400,y=380,width=340,height=115)
          '''scrollbar = Scrollbar(Labelframe9)
                scrollbar.place(x=300,y=10)
                b12=Entry(Labelframe9,yscrollcommand=scrollbar.set).place(x=10,y=10,width=290,height=70)
                yscrollcommand.config(command=b12.yview)'''
          cus_nt=StringVar()
          global cfgd
          cfgd=scrolledtext.ScrolledText(Labelframe9)
          cfgd.insert(1.0,str(str(cus_ins_val[23])))
          cfgd.place(x=20,y=10,width=295,height=70)
          # scrollbar_cus_nt = Scrollbar(Labelframe9)
          # scrollbar_cus_nt.place(x=295,y=10)

          btn1=Button(edit_customer,width=50,compound = LEFT,image=tick ,command=lambda:cus_edit_cst(),text="  OK").place(x=20, y=545)
          btn2=Button(edit_customer,width=80,compound = LEFT,image=cancel,text="  Cancel", command=edit_customer.destroy).place(x=665, y=545)
          edit_customer.mainloop()
        except:
          pass
          
                 

      enter=Label(cuselection, text="Enter filter text").place(x=5, y=10)
      e1=Entry(cuselection, width=20).place(x=110, y=10)
      text=Label(cuselection, text="Filtered column").place(x=340, y=10)
      e2=Entry(cuselection, width=20).place(x=450, y=10)

      pur_customertree=ttk.Treeview(cuselection, height=27)
      pur_customertree["columns"]=["1","2","3", "4"]
      pur_customertree.column("#0", width=35)
      pur_customertree.column("1", width=160)
      pur_customertree.column("2", width=160)
      pur_customertree.column("3", width=140)
      pur_customertree.column("4", width=140)
      pur_customertree.heading("#0",text="")
      pur_customertree.heading("1",text="Customer/Ventor ID")
      pur_customertree.heading("2",text="Customer/Ventor Name")
      pur_customertree.heading("3",text="Tel.")
      pur_customertree.heading("4",text="Contact Person")
      pur_customertree.place(x=5, y=45)

      fbcursor.execute('SELECT * FROM Customer;') 
      j = 0
      for i in fbcursor:
        pur_customertree.insert(parent='', index='end', iid=i, text='', values=(i[24],i[4],i[10],i[8]))
        j += 1

      ctegorytree=ttk.Treeview(cuselection, height=27)
      ctegorytree["columns"]=["1"]
      ctegorytree.column("#0", width=35, minwidth=20)
      ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      ctegorytree.heading("#0",text="", anchor=W)
      ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      ctegorytree.place(x=660, y=45)

      def pur_cus_filter(event):
        selected_indices = pur_cus_listbox.curselection()
        if str(selected_indices)=="(0,)":
          for record in pur_customertree.get_children():
            pur_customertree.delete(record)
          cus_main_table_sql="select * from customer"
          fbcursor.execute(cus_main_table_sql)
          main_tb_val=fbcursor.fetchall()
          
          count_cus=0

          for i in main_tb_val:
            pur_customertree.insert(parent='', index='end', iid=i, text='', values=(i[24],i[4],i[10],i[8]))
            
            count_cus +=1
        elif str(selected_indices)=="(1,)":
          for record in pur_customertree.get_children():
            pur_customertree.delete(record)
          cus_main_table_sql="select * from customer where customertype='Both(Client/Vender)'"
          fbcursor.execute(cus_main_table_sql)
          main_tb_val=fbcursor.fetchall()
          
          count_cus=0

          for i in main_tb_val:
            pur_customertree.insert(parent='', index='end', iid=i, text='', values=(i[24],i[4],i[10],i[8]))
            
            count_cus +=1
        elif str(selected_indices)=="(2,)":
          for record in pur_customertree.get_children():
            pur_customertree.delete(record)
          cus_main_table_sql="select * from customer where customertype='Client'"
          fbcursor.execute(cus_main_table_sql)
          main_tb_val=fbcursor.fetchall()
          
          count_cus=0

          for i in main_tb_val:
            pur_customertree.insert(parent='', index='end', iid=i, text='', values=(i[24],i[4],i[10],i[8]))
            
            count_cus +=1
        elif str(selected_indices)=="(3,)":
          for record in pur_customertree.get_children():
            pur_customertree.delete(record)
          cus_main_table_sql="select * from customer where customertype='Vender'"
          fbcursor.execute(cus_main_table_sql)
          main_tb_val=fbcursor.fetchall()
          
          count_cus=0

          for i in main_tb_val:
            pur_customertree.insert(parent='', index='end', iid=i, text='', values=(i[24],i[4],i[10],i[8]))
            
            count_cus +=1
        else:
          pass

      pur_cus_listbox = Listbox(cuselection,height =8,  
                        width = 29,  
                        bg = "white",
                        activestyle = 'dotbox',  
                        fg = "black",
                        highlightbackground="white")  
      pur_cus_listbox.insert(0, "  View all records")
      pur_cus_listbox.insert(1, "  View only Client/Vendor Type")
      pur_cus_listbox.insert(2, "  View only Client Type")
      pur_cus_listbox.insert(3, "  View only Vendor Type")
    
      pur_cus_listbox.place(x=660,y=60,height=545,width=242)
      pur_cus_listbox.bind('<<ListboxSelect>>', pur_cus_filter)

      scrollbar = Scrollbar(cuselection)
      scrollbar.place(x=640, y=45, height=560)
      scrollbar.config( command=pur_customertree.yview )

      btn1=Button(cuselection,compound = LEFT,image=tick, text="ok", width=60).place(x=15, y=610)
      btn1=Button(cuselection,compound = LEFT,image=tick, text="Edit selected customer", width=150,command=p_edit_customer).place(x=250, y=610)
      btn1=Button(cuselection,compound = LEFT,image=tick,text="Add new customer", width=150,command=p_add_customer).place(x=435, y=610)
      btn1=Button(cuselection,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=740, y=610)   
    
    
    #add new line item
    def pur_create_newlineproduct():
      if pur_name.get() == '':
        messagebox.showwarning("F-billing", "Customer is required, please select customer\nbefore adding line item to order")
      else:
        newselection=Toplevel()
        newselection.title("Select Customer")
        newselection.geometry("930x650+240+10")
        newselection.resizable(False, False)

        #add new product
        def pur_create_product():
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
            
            def ord_edit_addproupload_file():
              global filename,img, b2
              f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
              filename = filedialog.askopenfilename(filetypes=f_types)
              shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
              image = Image.open(filename)
              resize_image = image.resize((350, 350))
              img = ImageTk.PhotoImage(resize_image)
              b2 = Button(imageFrame,image=img)
              b2.place(x=130, y=80)
            
            def ord_edit_addproducts():
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
                for record in pur_seleproducttree.get_children():
                  pur_seleproducttree.delete(record)
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
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
                      countp += 1              
                    elif i[12] == '1':
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
                      countp += 1
                    else:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
                      countp += 1
                          
                  elif currsymb[1] == "before amount":
                    if (i[13]) > (i[14]):
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('green',))
                      countp += 1
                    elif i[12] == '1':
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('blue',))
                      countp += 1
                    else:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('red',))
                      countp += 1

                  elif currsymb[1] == "before amount with space":
                    if i[13] > i[14]:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
                      countp += 1
                    elif i[12] == '1':
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
                      countp += 1
                    else:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
                      countp += 1

                  elif currsymb[1] == "after amount":
                    if i[13] > i[14]:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('green',))
                      countp += 1
                    elif i[12] == '1':
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('blue',))
                      countp += 1
                    else:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('red',))
                      countp += 1

                  elif currsymb[1] == "after amount with space":
                    if i[13] > i[14]:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('green',))
                      countp += 1
                    elif i[12] == '1':
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('blue',))
                      countp += 1
                    else:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('red',))
                      countp += 1 

                top.destroy()
              else:
                messagebox.showinfo("Alert", "Fields name and SKU should not be empty.\nFill out required fields and try again")
                       
            code1=Label(Customerlabelframe,text="Code or SKU* :",fg="blue",pady=10,padx=10)
            code1.place(x=20,y=0)
            codeentry = Entry(Customerlabelframe,width=35)
            codeentry.place(x=110,y=8)
           
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
            Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,command=switch, 
                              text="This is a service(no stock control)", 
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
            
            okButton = Button(innerFrame, text ="Ok",image=tick,width=70,compound = LEFT, command=ord_edit_addproducts)
            okButton.pack(side=LEFT, padx=(10, 0), pady=(5, 10))
            
            def closetab():
              top.destroy()

            cancelButton = Button(innerFrame,image=cancel,text="Cancel",width=70,compound = LEFT, command=closetab)
            cancelButton.pack(side=RIGHT, padx=(0, 10), pady=(5, 10))

            imageFrame = Frame(tab2, relief=GROOVE,height=580)
            imageFrame.pack(side="top",fill=BOTH)

            
              
            browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
            browseimg.place(x=30,y=35)
              
            browsebutton=Button(imageFrame,text = 'Browse',command=ord_edit_addproupload_file)
            browsebutton.place(x=485,y=30,height=30,width=50)

            removeButton = Button(imageFrame,image=cancel,text="Remove Product Image",width=150,compound = LEFT, command=lambda: b2.destroy())
            removeButton.place(x=410,y=460)

        def pur_edit_product():
          try:
            itemid = pur_seleproducttree.item(pur_seleproducttree.focus())["values"][0]
            
            global filename
            filename = ""
            
            def ord_edit_update_upload_file():
              global filename,img, b2
              f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
              filename = filedialog.askopenfilename(filetypes=f_types)
              shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
              image = Image.open(filename)
              resize_image = image.resize((350, 350))
              img = ImageTk.PhotoImage(resize_image)
              b2 = Button(imageFrame,image=img)
              b2.place(x=130, y=80)
            
            def ord_edit_updateproducts():
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
                  sql = "update Productservice set sku=%s, category=%s, name=%s, description=%s, status=%s, unitprice=%s, peices=%s, cost=%s, taxable=%s, priceminuscost=%s, serviceornot=%s, stock=%s, stocklimit=%s, warehouse=%s, privatenote=%s,tax2=%s where sku = %s"
                  val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, pnotes,tax2, itemid)
                  fbcursor.execute(sql, val)
                  fbilldb.commit()
                else:
                  file = shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
                  sql = "update Productservice set category=%s, name=%s, description=%s, status=%s, unitprice=%s, peices=%s, cost=%s, taxable=%s, priceminuscost=%s, serviceornot=%s, stock=%s, stocklimit=%s, warehouse=%s, image=%s, privatenote=%s,tax2=%s where sku = %s"
                  val = (catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse,filename.split('/')[-1], pnotes,tax2, itemid)
                  fbcursor.execute(sql, val)
                  fbilldb.commit()
                  
                for record in pur_seleproducttree.get_children():
                  pur_seleproducttree.delete(record)
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
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
                      countp += 1              
                    elif i[12] == '1':
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
                      countp += 1
                    else:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
                      countp += 1
                          
                  elif currsymb[1] == "before amount":
                    if (i[13]) > (i[14]):
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('green',))
                      countp += 1
                    elif i[12] == '1':
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('blue',))
                      countp += 1
                    else:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('red',))
                      countp += 1

                  elif currsymb[1] == "before amount with space":
                    if i[13] > i[14]:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
                      countp += 1
                    elif i[12] == '1':
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
                      countp += 1
                    else:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
                      countp += 1

                  elif currsymb[1] == "after amount":
                    if i[13] > i[14]:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('green',))
                      countp += 1
                    elif i[12] == '1':
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('blue',))
                      countp += 1
                    else:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('red',))
                      countp += 1

                  elif currsymb[1] == "after amount with space":
                    if i[13] > i[14]:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('green',))
                      countp += 1
                    elif i[12] == '1':
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('blue',))
                      countp += 1
                    else:
                      pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('red',))
                      countp += 1 
                top.destroy()
              else:
                messagebox.showinfo("F-Billing Revolution", "Fields name or SKU entered is already in database.")
                top.destroy()
              
              
            sql = "select * from Productservice where sku = %s"
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

            okButton = Button(innerFrame, text ="Ok",image=tick,width=70,compound = LEFT,command=ord_edit_updateproducts)
            okButton.pack(side=LEFT, padx=(10, 0))

            cancelButton = Button(innerFrame,image=cancel,text="Cancel",width=70,compound = LEFT, command=lambda :top.destroy())
            cancelButton.pack(side=RIGHT, padx=(0, 10))
            
            
            imageFrame = Frame(tabb, relief=GROOVE,height=580)
            imageFrame.pack(side="top",fill=BOTH)

            browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320pixels) ",bg='#f5f3f2')
            browseimg.place(x=15,y=35)

            browsebutton=Button(imageFrame,text = 'Browse', command=ord_edit_update_upload_file)
            browsebutton.place(x=470,y=30,height=30,width=50)

            try:
              image = Image.open("images/"+psdata[17])
              resize_image = image.resize((350, 350))
              image = ImageTk.PhotoImage(resize_image)
              b2 = Label(imageFrame,image=image,width=350,height=350)
              b2.photo = image
              b2.place(x=130, y=80)
          
            except:
              pass

            removeButton = Button(imageFrame,image=cancel,text="Remove Product Image",width=150,compound = LEFT)
            removeButton.place(x=410,y=460)
          except:
            try:
              top.destroy()
            except:
              pass
            pass

            
          
                        
        enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
        e1=Entry(newselection, width=20).place(x=110, y=10)
        text=Label(newselection, text="Filtered column").place(x=340, y=10)
        e2=Entry(newselection, width=20).place(x=450, y=10)

        pur_seleproducttree=ttk.Treeview(newselection, height=27)
        pur_seleproducttree["columns"]=["1","2","3", "4","5"]
        pur_seleproducttree.column("#0", width=35)
        pur_seleproducttree.column("1", width=160)
        pur_seleproducttree.column("2", width=160)
        pur_seleproducttree.column("3", width=140)
        pur_seleproducttree.column("4", width=70)
        pur_seleproducttree.column("5", width=70)
        pur_seleproducttree.heading("#0",text="")
        pur_seleproducttree.heading("1",text="ID/SKU")
        pur_seleproducttree.heading("2",text="Product/Service Name")
        pur_seleproducttree.heading("3",text="Unit price")
        pur_seleproducttree.heading("4",text="Service")
        pur_seleproducttree.heading("5",text="Stock")
        pur_seleproducttree.tag_configure('green', foreground='green')
        pur_seleproducttree.tag_configure('red', foreground='red')
        pur_seleproducttree.tag_configure('blue', foreground='blue')
        pur_seleproducttree.place(x=5, y=45)

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
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
              countp += 1              
            elif i[12] == '1':
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
              countp += 1
            else:
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
              countp += 1
                  
          elif currsymb[1] == "before amount":
            if (i[13]) > (i[14]):
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('blue',))
              countp += 1
            else:
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('red',))
              countp += 1

          elif currsymb[1] == "before amount with space":
            if i[13] > i[14]:
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
              countp += 1
            else:
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
              countp += 1

          elif currsymb[1] == "after amount":
            if i[13] > i[14]:
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('blue',))
              countp += 1
            else:
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('red',))
              countp += 1

          elif currsymb[1] == "after amount with space":
            if i[13] > i[14]:
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('green',))
              countp += 1
            elif i[12] == '1':
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('blue',))
              countp += 1
            else:
              pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('red',))
              countp += 1 


        ctegorytree=ttk.Treeview(newselection, height=27)
        ctegorytree["columns"]=["1"]
        ctegorytree.column("#0", width=35, minwidth=20)
        ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
        ctegorytree.heading("#0",text="", anchor=W)
        ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
        ctegorytree.place(x=660, y=45)
        def pur_pro_items_selected(event):
          selected_indices = pur_pro_listbox.curselection()
          selected_filter = ",".join([pur_pro_listbox.get(i) for i in selected_indices])

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


          if selected_filter == "          View all records":
              for record in pur_seleproducttree.get_children():
                pur_seleproducttree.delete(record)
              countp = 0
              for i in pandsdata:
                if i[12] == '1':
                  servi = '🗹'
                else:
                  servi = ''
                sql = "select currencysign,currsignplace from company"
                fbcursor.execute(sql)
                currsymb = fbcursor.fetchone()
                if not currsymb: 
                  if i[13] > i[14]:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
                    countp += 1              
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
                    countp += 1
                        
                elif currsymb[1] == "before amount":
                  if (i[13]) > (i[14]):
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('red',))
                    countp += 1

                elif currsymb[1] == "before amount with space":
                  if i[13] > i[14]:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
                    countp += 1

                elif currsymb[1] == "after amount":
                  if i[13] > i[14]:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('red',))
                    countp += 1

                elif currsymb[1] == "after amount with space":
                  if i[13] > i[14]:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('red',))
                    countp += 1 
            
              
          elif selected_filter == "          View all products":
              for record in pur_seleproducttree.get_children():
                pur_seleproducttree.delete(record)
              countp = 0
              for i in pdata:
                if i[12] == '1':
                  servi = '🗹'
                else:
                  servi = ''
                sql = "select currencysign,currsignplace from company"
                fbcursor.execute(sql)
                currsymb = fbcursor.fetchone()
                if not currsymb: 
                  if i[13] > i[14]:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
                    countp += 1              
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
                    countp += 1
                        
                elif currsymb[1] == "before amount":
                  if (i[13]) > (i[14]):
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('red',))
                    countp += 1

                elif currsymb[1] == "before amount with space":
                  if i[13] > i[14]:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
                    countp += 1

                elif currsymb[1] == "after amount":
                  if i[13] > i[14]:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('red',))
                    countp += 1

                elif currsymb[1] == "after amount with space":
                  if i[13] > i[14]:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('red',))
                    countp += 1


          elif selected_filter == "          View all services":
              for record in pur_seleproducttree.get_children():
                pur_seleproducttree.delete(record)
              countp = 0
              for i in sdata:
                if i[12] == '1':
                  servi = '🗹'
                else:
                  servi = ''
                sql = "select currencysign,currsignplace from company"
                fbcursor.execute(sql)
                currsymb = fbcursor.fetchone()
                if not currsymb: 
                  if i[13] > i[14]:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('green',))
                    countp += 1              
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7],servi,i[13]),tags=('red',))
                    countp += 1
                        
                elif currsymb[1] == "before amount":
                  if (i[13]) > (i[14]):
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0]+i[7],servi,i[13]),tags=('red',))
                    countp += 1

                elif currsymb[1] == "before amount with space":
                  if i[13] > i[14]:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],currsymb[0] +" "+i[7],servi,i[13]),tags=('red',))
                    countp += 1

                elif currsymb[1] == "after amount":
                  if i[13] > i[14]:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='', values=(i[2],i[4],i[7]+currsymb[0],servi,i[13]),tags=('red',))
                    countp += 1

                elif currsymb[1] == "after amount with space":
                  if i[13] > i[14]:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('green',))
                    countp += 1
                  elif i[12] == '1':
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('blue',))
                    countp += 1
                  else:
                    pur_seleproducttree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[4],i[7]+" "+currsymb[0],servi,i[13]),tags=('red',))
                    countp += 1

        pur_pro_listbox = Listbox(newselection,height = 8,  
                          width = 29,  
                          bg = "white",
                          activestyle = 'dotbox',  
                          fg = "black",
                          bd=0,
                          highlightbackground="white")  
        pur_pro_listbox.insert(0, "          View all records")
        pur_pro_listbox.insert(1, "          View all products")
        pur_pro_listbox.insert(2, "          View all services")
  

        pur_pro_listbox.place(x=660,y=75,height=530,width=240)
        pur_pro_listbox.bind('<<ListboxSelect>>', pur_pro_items_selected)

        scrollbar = Scrollbar(newselection)
        scrollbar.place(x=640, y=45, height=560)
        scrollbar.config( command=pur_seleproducttree.yview )
      

        btn1=Button(newselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
        btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=pur_edit_product).place(x=250, y=610)
        btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=pur_create_product).place(x=435, y=610)
        btn1=Button(newselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)





    #preview new line
    def pur_create_previewline1():
      messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")



    #sms notification
    def smspurch():
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
    def pur_create_delete():
      messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item.")



    #finalize
    def pur_create_finalize():  
      messagebox.askyesno("Finalize purchase order", "Would you like to mark this purchase order as completed ?All product will be added in to stock and purchase order will be closed")


    firFrame1=Frame(pop1, bg="#f5f3f2", height=60)
    firFrame1.pack(side="top", fill=X)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    create = Button(firFrame1,compound="top", text="Select\nVendor",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=pur_create_customer)
    create.pack(side="left", pady=3, ipadx=4)


    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    add= Button(firFrame1,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=pur_create_newlineproduct)
    add.pack(side="left", pady=3, ipadx=4)

    dele= Button(firFrame1,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=pur_create_delete)
    dele.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    prev= Button(firFrame1,compound="top", text="Preview\nP.Order",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=pur_create_previewline1)
    prev.pack(side="left", pady=3, ipadx=4)

    prin= Button(firFrame1,compound="top", text="Print \nP.Order",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printsele1)
    prin.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    mail= Button(firFrame1,compound="top", text="Email\nP.Order",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command="email_invoice_recurring")
    mail.pack(side="left", pady=3, ipadx=4)

    sms1= Button(firFrame1,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=smspurch)
    sms1.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    finalize= Button(firFrame1,compound="top", text="Finalize\nP.Order",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=pur_create_finalize)
    finalize.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)


    calc= Button(firFrame1,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
    calc.pack(side="left", pady=3, ipadx=4)

    fir1Frame=Frame(pop1, height=180,bg="#f5f3f2")
    fir1Frame.pack(side="top", fill=X)

    labelframe1 = LabelFrame(fir1Frame,text=" Vendor")
    labelframe1.place(x=10,y=5,width=640,height=160)
    order = Label(labelframe1, text="Vendor to").place(x=10,y=5)
    pur_name = ttk.Combobox(labelframe1, value="Hello",width=28)
    pur_name.place(x=80,y=5)
    address=Label(labelframe1,text="Address").place(x=10,y=30)
    pur_addr=Text(labelframe1,width=23)
    pur_addr.place(x=80,y=30,height=70)
    ship=Label(labelframe1,text="Delivery to").place(x=342,y=5)
    pur_delivery=Entry(labelframe1,width=30)
    pur_delivery.place(x=402,y=3)
    address1=Label(labelframe1,text="Address").place(x=340,y=30)
    pur_deliaddr=Text(labelframe1,width=23)
    pur_deliaddr.place(x=402,y=30,height=70)

    
    labelframe2 = LabelFrame(fir1Frame,text="")
    labelframe2.place(x=10,y=130,width=640,height=42)
    email=Label(labelframe2,text="Email").place(x=10,y=5)
    pur_email=Entry(labelframe2,width=30)
    pur_email.place(x=80,y=5)
    sms=Label(labelframe2,text="SMS Number").place(x=327,y=5)
    pur_sms=Entry(labelframe2,width=28)
    pur_sms.place(x=402,y=3)

    labelframe = LabelFrame(fir1Frame,text="Purchase Order")
    labelframe.place(x=652,y=5,width=290,height=170)
    order=Label(labelframe,text="P.Order#").place(x=5,y=5)
    pur_orderid=Entry(labelframe,width=27)
    pur_orderid.place(x=100,y=5,)
    orderdate=Label(labelframe,text="P.Order date").place(x=5,y=33)
    pur_date=Entry(labelframe,width=20)
    pur_date.place(x=150,y=33)
    checkvarStatus5=IntVar()
    pur_duedate_check=Checkbutton(labelframe,variable = checkvarStatus5,text="P.Due date",onvalue =0 ,offvalue = 1)
    pur_duedate_check.place(x=5,y=62)
    pur_duedate=Entry(labelframe,width=20)
    pur_duedate.place(x=150,y=62)
    terms=Label(labelframe,text="Terms").place(x=5,y=92)
    pur_terms=ttk.Combobox(labelframe, value="",width=25)
    pur_terms.place(x=100,y=92)
    ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
    pur_ref=Entry(labelframe,width=27)
    pur_ref.place(x=100,y=118)

    fir2Frame=Frame(pop1, height=150,width=100,bg="#f5f3f2")
    fir2Frame.pack(side="top", fill=X)
    listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
    
    pur_create_tree=ttk.Treeview(listFrame)
    pur_create_tree["columns"]=["1","2","3","4","5","6","7","8"]

    pur_create_tree.column("#0", width=40)
    pur_create_tree.column("1", width=80)
    pur_create_tree.column("2", width=190)
    pur_create_tree.column("3", width=190)
    pur_create_tree.column("4", width=80)
    pur_create_tree.column("5", width=60)
    pur_create_tree.column("6", width=60)
    pur_create_tree.column("7", width=60)
    pur_create_tree.column("8", width=80)
 
    pur_create_tree.heading("#0")
    pur_create_tree.heading("1",text="ID/SKU")
    pur_create_tree.heading("2",text="Product/Service")
    pur_create_tree.heading("3",text="Description")
    pur_create_tree.heading("4",text="Unit Price")
    pur_create_tree.heading("5",text="Quality")
    pur_create_tree.heading("6",text="Pcs/Weight")
    pur_create_tree.heading("7",text="Tax1")
    pur_create_tree.heading("8",text="Price")

    pur_create_tree.pack(fill="both", expand=1)
    listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    fir3Frame=Frame(pop1,height=200,width=700,bg="#f5f3f2")
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
    
    myNotebook.add(orderFrame,compound="left", text="Purchase Order")
    myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
    myNotebook.add(commentFrame,compound="left",  text="Comments")
    myNotebook.add(termsFrame,compound="left", text="Terms")
    myNotebook.add(noteFrame,compound="left",  text="Private notes")
    myNotebook.add(documentFrame,compound="left",  text="Documents")
    myNotebook.pack(expand = 1, fill ="both")

    labelframe1 = LabelFrame(orderFrame,text="",font=("arial",15))
    labelframe1.place(x=1,y=1,width=800,height=170)
    cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
    pur_extracostname=ttk.Combobox(labelframe1, value="",width=20)
    pur_extracostname.place(x=115,y=5)
    rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
    pur_disrate=Entry(labelframe1,width=6)
    pur_disrate.place(x=460,y=5)
    cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
    pur_extracost=Entry(labelframe1,width=10)
    pur_extracost.place(x=115,y=35)
    tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
    pur_tax1=Entry(labelframe1,width=7)
    pur_tax1.place(x=460,y=35)
    template=Label(labelframe1,text="Template").place(x=37,y=70)
    pur_templates=ttk.Combobox(labelframe1, value="",width=25)
    pur_templates.place(x=115,y=70)
    sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
    pur_salesper=Entry(labelframe1,width=18)
    pur_salesper.place(x=115,y=100)
    category=Label(labelframe1,text="Category").place(x=300,y=100)
    pur_cat=Entry(labelframe1,width=22)
    pur_cat.place(x=370,y=100)

    statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
    statusfrme.place(x=540,y=0,width=160,height=160)
    draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
    on1=Label(statusfrme, text="Emailed on:").place( y=50)
    nev1=Label(statusfrme, text="Never").place(x=100,y=50)
    on2=Label(statusfrme, text="Printed on:").place( y=90)
    nev2=Label(statusfrme, text="Never").place(x=100,y=90)

    text1=Label(headerFrame,text="Title text").place(x=50,y=5)
    pur_titltetext=ttk.Combobox(headerFrame, value="",width=60)
    pur_titltetext.place(x=125,y=5)
    text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
    pur_header=ttk.Combobox(headerFrame, value="",width=60)
    pur_header.place(x=125,y=45)
    text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
    pur_footer=ttk.Combobox(headerFrame, value="",width=60)
    pur_footer.place(x=125,y=85)

    text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
    pur_pravatenote=Text(noteFrame,width=100,height=7)
    pur_pravatenote.place(x=10,y=32)

    pur_termsnotes=Text(termsFrame,width=100,height=9)
    pur_termsnotes.place(x=10,y=10)

    pur_comments=Text(commentFrame,width=100,height=9)
    pur_comments.place(x=10,y=10)

    btn1=Button(documentFrame,height=2,width=3,text="+").place(x=5,y=10)
    btn2=Button(documentFrame,height=2,width=3,text="-").place(x=5,y=50)
    text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
    pur_create_doc=ttk.Treeview(documentFrame, height=5)
    pur_create_doc["columns"]=["1","2","3"]
    pur_create_doc.column("#0", width=20)
    pur_create_doc.column("1", width=250)
    pur_create_doc.column("2", width=250)
    pur_create_doc.column("2", width=200)
    pur_create_doc.heading("#0",text="", anchor=W)
    pur_create_doc.heading("1",text="Attach to Email")
    pur_create_doc.heading("2",text="Filename")
    pur_create_doc.heading("3",text="Filesize")  
    pur_create_doc.place(x=50, y=45)

    fir4Frame=Frame(pop1,height=190,width=210,bg="#f5f3f2")
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
    order=Label(summaryfrme, text="P.Order total").place(x=0 ,y=84)
    order1=Label(summaryfrme, text="$0.00").place(x=130 ,y=84)

    fir5Frame=Frame(pop1,height=38,width=210)
    fir5Frame.place(x=735,y=485)
    btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
    btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)

  
  #______________________ Edit Purchase Order _______________________________#
  def edit_purchase():
    pop1=Toplevel(pur_midFrame)
    pop1.title("Orders")
    pop1.geometry("950x690+150+0")


    #select vendor
    def purch_edit_purchase():
      cuselection=Toplevel()
      cuselection.title("Select Customer")
      cuselection.geometry("930x650+240+10")
      cuselection.resizable(False, False)


      #add new customer
      def addedit():
        ven=Toplevel(pur_midFrame)
        ven.title("Add new vendor")
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

        labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2",)
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

        btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick,text="OK").place(x=20, y=615)
        btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
          
                 

      enter=Label(cuselection, text="Enter filter text").place(x=5, y=10)
      e1=Entry(cuselection, width=20).place(x=110, y=10)
      text=Label(cuselection, text="Filtered column").place(x=340, y=10)
      e2=Entry(cuselection, width=20).place(x=450, y=10)

      purch_edit_customer=ttk.Treeview(cuselection, height=27)
      purch_edit_customer["columns"]=["1","2","3", "4"]
      purch_edit_customer.column("#0", width=35)
      purch_edit_customer.column("1", width=160)
      purch_edit_customer.column("2", width=160)
      purch_edit_customer.column("3", width=140)
      purch_edit_customer.column("4", width=140)
      purch_edit_customer.heading("#0",text="")
      purch_edit_customer.heading("1",text="Customer/Ventor ID")
      purch_edit_customer.heading("2",text="Customer/Ventor Name")
      purch_edit_customer.heading("3",text="Tel.")
      purch_edit_customer.heading("4",text="Contact Person")
      purch_edit_customer.place(x=5, y=45)

      ctegorytree=ttk.Treeview(cuselection, height=27)
      ctegorytree["columns"]=["1"]
      ctegorytree.column("#0", width=35, minwidth=20)
      ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      ctegorytree.heading("#0",text="", anchor=W)
      ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      ctegorytree.place(x=660, y=45)

      scrollbar = Scrollbar(cuselection)
      scrollbar.place(x=640, y=45, height=560)
      scrollbar.config( command=purch_edit_customer.yview )

      btn1=Button(cuselection,compound = LEFT,image=tick, text="ok", width=60).place(x=15, y=610)
      btn1=Button(cuselection,compound = LEFT,image=tick, text="Edit selected customer", width=150,command=addedit).place(x=250, y=610)
      btn1=Button(cuselection,compound = LEFT,image=tick,text="Add new customer", width=150,command=addedit).place(x=435, y=610)
      btn1=Button(cuselection,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=740, y=610)   



    #add new line item
    def puch_edit_newlineproduct():
      newselection=Toplevel()
      newselection.title("Select Customer")
      newselection.geometry("930x650+240+10")
      newselection.resizable(False, False)

      #add new product
      def product():  
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

      purch_seleproducttree=ttk.Treeview(newselection, height=27)
      purch_seleproducttree["columns"]=["1","2","3", "4","5"]
      purch_seleproducttree.column("#0", width=35)
      purch_seleproducttree.column("1", width=160)
      purch_seleproducttree.column("2", width=160)
      purch_seleproducttree.column("3", width=140)
      purch_seleproducttree.column("4", width=70)
      purch_seleproducttree.column("5", width=70)
      purch_seleproducttree.heading("#0",text="")
      purch_seleproducttree.heading("1",text="ID/SKU")
      purch_seleproducttree.heading("2",text="Product/Service Name")
      purch_seleproducttree.heading("3",text="Unit price")
      purch_seleproducttree.heading("4",text="Service")
      purch_seleproducttree.heading("5",text="Stock")
      purch_seleproducttree.place(x=5, y=45)

      ctegorytree=ttk.Treeview(newselection, height=27)
      ctegorytree["columns"]=["1"]
      ctegorytree.column("#0", width=35, minwidth=20)
      ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      ctegorytree.heading("#0",text="", anchor=W)
      ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      ctegorytree.place(x=660, y=45)


      scrollbar = Scrollbar(newselection)
      scrollbar.place(x=640, y=45, height=560)
      scrollbar.config( command=purch_seleproducttree.yview )
     

      btn1=Button(newselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
      btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=product).place(x=250, y=610)
      btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=product).place(x=435, y=610)
      btn1=Button(newselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)





    #preview new line
    def purch_edit_previewline1():
      messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")



    #sms notification
    def smspurch():
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
    def purch_edit_delete():
      messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item.")



    #finalize
    def puch_edit_finalize():  
      messagebox.askyesno("Finalize purchase order", "Would you like to mark this purchase order as completed ?All product will be added in to stock and purchase order will be closed")


    firFrame1=Frame(pop1, bg="#f5f3f2", height=60)
    firFrame1.pack(side="top", fill=X)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    create = Button(firFrame1,compound="top", text="Select\nVendor",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=purch_edit_purchase)
    create.pack(side="left", pady=3, ipadx=4)


    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    add= Button(firFrame1,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=puch_edit_newlineproduct)
    add.pack(side="left", pady=3, ipadx=4)

    dele= Button(firFrame1,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=purch_edit_delete)
    dele.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    prev= Button(firFrame1,compound="top", text="Preview\nP.Order",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=purch_edit_previewline1)
    prev.pack(side="left", pady=3, ipadx=4)

    prin= Button(firFrame1,compound="top", text="Print \nP.Order",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printsele1)
    prin.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    mail= Button(firFrame1,compound="top", text="Email\nP.Order",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command="email_invoice_recurring")
    mail.pack(side="left", pady=3, ipadx=4)

    sms1= Button(firFrame1,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=smspurch)
    sms1.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    finalize= Button(firFrame1,compound="top", text="Finalize\nP.Order",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=puch_edit_finalize)
    finalize.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)


    calc= Button(firFrame1,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
    calc.pack(side="left", pady=3, ipadx=4)

    fir1Frame=Frame(pop1, height=180,bg="#f5f3f2")
    fir1Frame.pack(side="top", fill=X)

    labelframe1 = LabelFrame(fir1Frame,text=" Vendor")
    labelframe1.place(x=10,y=5,width=640,height=160)
    order = Label(labelframe1, text="Vendor to").place(x=10,y=5)
    purch_name = ttk.Combobox(labelframe1, value="Hello",width=28)
    purch_name.place(x=80,y=5)
    address=Label(labelframe1,text="Address").place(x=10,y=30)
    purch_addr=Text(labelframe1,width=23)
    purch_addr.place(x=80,y=30,height=70)
    ship=Label(labelframe1,text="Delivery to").place(x=342,y=5)
    purch_deli=Entry(labelframe1,width=30)
    purch_deli.place(x=402,y=3)
    address1=Label(labelframe1,text="Address").place(x=340,y=30)
    purch_deliaddr=Text(labelframe1,width=23)
    purch_deliaddr.place(x=402,y=30,height=70)

    
    labelframe2 = LabelFrame(fir1Frame,text="")
    labelframe2.place(x=10,y=130,width=640,height=42)
    email=Label(labelframe2,text="Email").place(x=10,y=5)
    purch_email=Entry(labelframe2,width=30)
    purch_email.place(x=80,y=5)
    sms=Label(labelframe2,text="SMS Number").place(x=327,y=5)
    purch_sms=Entry(labelframe2,width=28)
    purch_sms.place(x=402,y=3)

    labelframe = LabelFrame(fir1Frame,text="Purchase Order")
    labelframe.place(x=652,y=5,width=290,height=170)
    order=Label(labelframe,text="P.Order#").place(x=5,y=5)
    purch_orderid=Entry(labelframe,width=27)
    purch_orderid.place(x=100,y=5,)
    orderdate=Label(labelframe,text="P.Order date").place(x=5,y=33)
    purch_date=Entry(labelframe,width=20)
    purch_date.place(x=150,y=33)
    checkvarStatus5=IntVar()
    purch_duedate_check=Checkbutton(labelframe,variable = checkvarStatus5,text="P.Due date",onvalue =0 ,offvalue = 1)
    purch_duedate_check.place(x=5,y=62)
    purch_duedate=Entry(labelframe,width=20)
    purch_duedate.place(x=150,y=62)
    terms=Label(labelframe,text="Terms").place(x=5,y=92)
    purch_terms=ttk.Combobox(labelframe, value="",width=25)
    purch_terms.place(x=100,y=92)
    ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
    purch_ref=Entry(labelframe,width=27)
    purch_ref.place(x=100,y=118)

    fir2Frame=Frame(pop1, height=150,width=100,bg="#f5f3f2")
    fir2Frame.pack(side="top", fill=X)
    listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
    
    purch_edit_tree=ttk.Treeview(listFrame)
    purch_edit_tree["columns"]=["1","2","3","4","5","6","7","8"]

    purch_edit_tree.column("#0", width=40)
    purch_edit_tree.column("1", width=80)
    purch_edit_tree.column("2", width=190)
    purch_edit_tree.column("3", width=190)
    purch_edit_tree.column("4", width=80)
    purch_edit_tree.column("5", width=60)
    purch_edit_tree.column("6", width=60)
    purch_edit_tree.column("7", width=60)
    purch_edit_tree.column("8", width=80)

    purch_edit_tree.heading("#0")
    purch_edit_tree.heading("1",text="ID/SKU")
    purch_edit_tree.heading("2",text="Product/Service")
    purch_edit_tree.heading("3",text="Description")
    purch_edit_tree.heading("4",text="Unit Price")
    purch_edit_tree.heading("5",text="Quality")
    purch_edit_tree.heading("6",text="Pcs/Weight")
    purch_edit_tree.heading("7",text="Tax1")
    purch_edit_tree.heading("8",text="Price")

    purch_edit_tree.pack(fill="both", expand=1)
    listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    fir3Frame=Frame(pop1,height=200,width=700,bg="#f5f3f2")
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
    
    myNotebook.add(orderFrame,compound="left", text="Purchase Order")
    myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
    myNotebook.add(commentFrame,compound="left",  text="Comments")
    myNotebook.add(termsFrame,compound="left", text="Terms")
    myNotebook.add(noteFrame,compound="left",  text="Private notes")
    myNotebook.add(documentFrame,compound="left",  text="Documents")
    myNotebook.pack(expand = 1, fill ="both")

    labelframe1 = LabelFrame(orderFrame,text="",font=("arial",15))
    labelframe1.place(x=1,y=1,width=800,height=170)
    cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
    purch_extracostname=ttk.Combobox(labelframe1, value="",width=20)
    purch_extracostname.place(x=115,y=5)
    rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
    purch_disrate=Entry(labelframe1,width=6)
    purch_disrate.place(x=460,y=5)
    cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
    purch_extracost=Entry(labelframe1,width=10)
    purch_extracost.place(x=115,y=35)
    tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
    purch_tax1=Entry(labelframe1,width=7)
    purch_tax1.place(x=460,y=35)
    template=Label(labelframe1,text="Template").place(x=37,y=70)
    purch_template=ttk.Combobox(labelframe1, value="",width=25)
    purch_template.place(x=115,y=70)
    sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
    purch_salesper=Entry(labelframe1,width=18)
    purch_salesper.place(x=115,y=100)
    category=Label(labelframe1,text="Category").place(x=300,y=100)
    purch_cat=Entry(labelframe1,width=22)
    purch_cat.place(x=370,y=100)

    statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
    statusfrme.place(x=540,y=0,width=160,height=160)
    draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
    on1=Label(statusfrme, text="Emailed on:").place( y=50)
    nev1=Label(statusfrme, text="Never").place(x=100,y=50)
    on2=Label(statusfrme, text="Printed on:").place( y=90)
    nev2=Label(statusfrme, text="Never").place(x=100,y=90)

    text1=Label(headerFrame,text="Title text").place(x=50,y=5)
    purch_titletext=ttk.Combobox(headerFrame, value="",width=60)
    purch_titletext.place(x=125,y=5)
    text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
    purch_headertext=ttk.Combobox(headerFrame, value="",width=60)
    purch_headertext.place(x=125,y=45)
    text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
    purch_footer=ttk.Combobox(headerFrame, value="",width=60)
    purch_footer.place(x=125,y=85)

    text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
    purch_privatenotes=Text(noteFrame,width=100,height=7).place(x=10,y=32)

    purchterms=Text(termsFrame,width=100,height=9)
    purchterms.place(x=10,y=10)

    purch_comments=Text(commentFrame,width=100,height=9)
    purch_comments.place(x=10,y=10)

    btn1=Button(documentFrame,height=2,width=3,text="+").place(x=5,y=10)
    btn2=Button(documentFrame,height=2,width=3,text="-").place(x=5,y=50)
    text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
    purch_edit_tree=ttk.Treeview(documentFrame, height=5)
    purch_edit_tree["columns"]=["1","2","3"]
    purch_edit_tree.column("#0", width=20)
    purch_edit_tree.column("1", width=250)
    purch_edit_tree.column("2", width=250)
    purch_edit_tree.column("2", width=200)
    purch_edit_tree.heading("#0",text="", anchor=W)
    purch_edit_tree.heading("1",text="Attach to Email")
    purch_edit_tree.heading("2",text="Filename")
    purch_edit_tree.heading("3",text="Filesize")  
    purch_edit_tree.place(x=50, y=45)

    fir4Frame=Frame(pop1,height=190,width=210,bg="#f5f3f2")
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
    order=Label(summaryfrme, text="P.Order total").place(x=0 ,y=84)
    order1=Label(summaryfrme, text="$0.00").place(x=130 ,y=84)

    fir5Frame=Frame(pop1,height=38,width=210)
    fir5Frame.place(x=735,y=485)
    btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
    btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)



  # print preview purchase order
  def purchase_printpreview1():
    messagebox.showerror("F-Billing Revolution","Customer is required,please select customer for this order before printing.")




  #delete purchase order
  def purchase_dele1():  
    messagebox.askyesno("Delete order", "Are you sure to delete this order? All products will be placed back into stock")
      


  #search in purchase order
  def search1():  
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




  #print selectede purchase order
  def printsele1():

    def proper1():
      propert=Toplevel()
      propert.title("Microsoft Print To PDF Advanced Document Settings")
      propert.geometry("670x500+240+150")

      def proper2():
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
      style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
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

      btn=Button(property_Frame, text="Advanced",command=proper2).place(x=550, y=380)
      btn=Button(property_Frame,compound = LEFT,image=tick, text="OK", width=60,).place(x=430, y=420)
      btn=Button(property_Frame,compound = LEFT,image=tick, text="Cancel", width=60,).place(x=550, y=420)     

        
    
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
        btn=Button(printerframe, text="Properties", width=10,command=proper1).place(x=540, y=5)

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

        okbtn=Button(print1,compound = LEFT,image=tick,text="Ok", width=60).place(x=460, y=370)
        canbtn=Button(print1,compound = LEFT,image=tick, text="Cancel", width=60).place(x=570, y=370)
        




  pur_mainFrame=Frame(tab5, relief=GROOVE, bg="#f8f8f2")
  pur_mainFrame.pack(side="top", fill=BOTH)

  pur_midFrame=Frame(pur_mainFrame, bg="#f5f3f2", height=60)
  pur_midFrame.pack(side="top", fill=X)

  w = Canvas(pur_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=(5, 2))
  w = Canvas(pur_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=(0, 5))

  invoice1Label = Button(pur_midFrame,compound="top", text="Create new\nP.Order",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=create_purchase)
  invoice1Label.pack(side="left", pady=3, ipadx=4)

  order1Label = Button(pur_midFrame,compound="top", text="View/Edit\nP.Orders",relief=RAISED, image=photo1,bg="#f8f8f2",fg="black", height=55, bd=1, width=55,command=edit_purchase)
  order1Label.pack(side="left")

  estimate1Label = Button(pur_midFrame,compound="top", text="Delete\nSelected",relief=RAISED, image=photo2,bg="#f8f8f2",fg="black", height=55, bd=1, width=55,command=purchase_dele1)
  estimate1Label.pack(side="left")

  w = Canvas(pur_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  preview1Label = Button(pur_midFrame,compound="top", text="Print\nPreview",relief=RAISED, image=photo4,bg="#f8f8f2",fg="black", height=55, bd=1, width=55,command=purchase_printpreview1)
  preview1Label.pack(side="left")

  purchase1Label = Button(pur_midFrame,compound="top", text="Print\nSelected",relief=RAISED, image=photo5,bg="#f8f8f2",fg="black", height=55, bd=1, width=55,command=printsele1)
  purchase1Label.pack(side="left")

  w = Canvas(pur_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  expense1Label = Button(pur_midFrame,compound="top", text=" E-mail \nP.Order",relief=RAISED, image=photo6,bg="#f8f8f2",fg="black", height=55, bd=1, width=55,command="email_invoice_recurring")
  expense1Label.pack(side="left")

  sms1Label = Button(pur_midFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command="smspurch")
  sms1Label.pack(side="left")

  w = Canvas(pur_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  product1Label = Button(pur_midFrame,compound="top", text="Search\nP.Orders",relief=RAISED, image=photo7,bg="#f8f8f2",fg="black", height=55, bd=1, width=55,command=search1)
  product1Label.pack(side="left")

  pur_lb1frame = LabelFrame(pur_midFrame, height=60, width=200, bg="#f8f8f2")
  pur_lb1frame.pack(side="left", padx=10, pady=0)
  lbl1_invdt = Label(pur_lb1frame, text="Porder date from : ", bg="#f8f8f2")
  lbl1_invdt.grid(row=0, column=0, pady=5, padx=(5, 0))
  lbl1_invdtt = Label(pur_lb1frame, text="Porder date to  :  ", bg="#f8f8f2")
  lbl1_invdtt.grid(row=1, column=0, pady=5, padx=(5, 0))
  invdt1 = Entry(pur_lb1frame, width=15)
  invdt1.grid(row=0, column=1)
  invdtt1 = Entry(pur_lb1frame, width=15)
  invdtt1.grid(row=1, column=1)
  check1var1 = IntVar()
  chk1btn1 = Checkbutton(pur_lb1frame, text = "Apply filter", variable = check1var1, onvalue = 1, offvalue = 0, height =2, width = 8, bg="#f8f8f2")
  chk1btn1.grid(row=0, column=2, rowspan=2, padx=(5,5))

  product1Label = Button(pur_midFrame,compound="top", text="Refresh\nP.Orders list",relief=RAISED, image=photo8,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  product1Label.pack(side="left")

  w = Canvas(pur_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  product1Label = Button(pur_midFrame,compound="top", text="Hide totals\nSum",relief=RAISED, image=photo9,bg="#f8f8f2",fg="black", height=55, bd=1, width=55)
  product1Label.pack(side="left")


  invoi1label = Label(pur_mainFrame, text="Purchase Orders(All)", font=("arial", 18), bg="#f8f8f2")
  invoi1label.pack(side="left", padx=(20,0))
  drop1 = ttk.Combobox(pur_mainFrame, value="Hello")
  drop1.pack(side="right", padx=(0,10))
  invoi1label = Label(pur_mainFrame, text="Category filter", font=("arial", 15), bg="#f8f8f2")
  invoi1label.pack(side="right", padx=(0,10))

  class MyApp1:
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

      
      tree = ttk.Treeview(self.left_frame, columns = (1,2,3,4,5,6,7,8,9,10), height = 15, show = "headings")
      tree.pack(side = 'top')
      tree.heading(1)
      tree.heading(2, text="P.Order#")
      tree.heading(3, text="Porder date")
      tree.heading(4, text="Due date")
      tree.heading(5, text="Customer Name")
      tree.heading(6, text="Status")
      tree.heading(7, text="Emailed on")
      tree.heading(8, text="Printed on")
      tree.heading(9, text="SMS on")
      tree.heading(10, text="Porder Total")   
      tree.column(1, width = 40)
      tree.column(2, width = 145)
      tree.column(3, width = 140)
      tree.column(4, width = 140)
      tree.column(5, width = 200)
      tree.column(6, width = 140)
      tree.column(7, width = 150)
      tree.column(8, width = 130)
      tree.column(9, width = 130)
      tree.column(10, width = 130)

      scrollbar = Scrollbar(self.left_frame)
      scrollbar.place(x=990+345, y=0, height=300+20)
      scrollbar.config( command=tree.yview )

      tabControl = ttk.Notebook(self.left_frame,width=1)
      tab1 = ttk.Frame(tabControl)
      tab2 = ttk.Frame(tabControl)
      tab3=  ttk.Frame(tabControl)
      tab4 = ttk.Frame(tabControl)
      tabControl.add(tab1,image=invoices,compound = LEFT, text ='P.Order Items')
      tabControl.add(tab2,image=photo11,compound = LEFT, text ='Invoice Private Notes')
      tabControl.add(tab3,image=smslog,compound = LEFT, text ='SMS log')
      tabControl.add(tab4,image=photo11,compound = LEFT, text ='Documents')
      tabControl.pack(expand = 1, fill ="both")
      
      tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8,), height = 15, show = "headings")
      tree.pack(side = 'top')
      tree.heading(1)
      tree.heading(2, text="Product/Service ID",)
      tree.heading(3, text="Name")
      tree.heading(4, text="Description")
      tree.heading(5, text="Price")
      tree.heading(6, text="QTY")
      tree.heading(7, text="Tax1")
      tree.heading(8, text="Line Total")   
      tree.column(1, width = 40)
      tree.column(2, width = 260)
      tree.column(3, width = 260)
      tree.column(4, width = 300)
      tree.column(5, width = 130)
      tree.column(6, width = 100)
      tree.column(7, width = 100)
      tree.column(8, width = 150)

      note1=Text(tab2, width=170,height=10).place(x=10, y=10)

      note1=Text(tab3, width=170,height=10).place(x=10, y=10)

      tree = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
      tree.pack(side = 'top')
      tree.heading(1)
      tree.heading(2, text="Attach to Email",)
      tree.heading(3, text="Filename")
      tree.column(1, width = 50)
      tree.column(2, width = 250)
      tree.column(3, width = 1000)

      scrollbar = Scrollbar(self.left_frame)
      scrollbar.place(x=990+340, y=360, height=190)
      scrollbar.config( command=tree.yview )
         
  myapp = MyApp1(tab5)

######################## FRONT PAGE OF Settings module #######################################################
  
      
  settingsframe=Frame(tab10, relief=GROOVE, bg="#f8f8f2")
  settingsframe.pack(side="top", fill=BOTH)
  
  settframe=Frame(settingsframe, bg="#f5f3f2", height=60)
  settframe.pack(side="top", fill=X)
  
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(5, 2))
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))

  global filename
  filename = ""
  def save_company():
    #save date tab 04,03------------------------------------------------------------------------------
    sql_03_tb='select * from invoice_settings'
    fbcursor.execute(sql_03_tb)
    mt_tb=fbcursor.fetchone()

    if mt_tb is None:
        
        stt_tbl_add="INSERT INTO invoice_settings(invoice_prefix,starting_invoice_number,bgcolour,invoice,invoice2,invoice_date,order_ref,terms,invoice_to,ship_to,id_sku,product_service,quantity,	description,	unit_price,price,subtotal,discount,	discount_rate,tax1,invoice_total,total_paid,balance,	terms_conditions,	tax_exempted,page,of,terms_notes)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
        stt_tbl_add_val=(inv_tp_lf.get(),inv_spn_bx.get(),invset_bg_var.get(),inv_lst_bx1.get(1.0,END),inv_lst_bx2.get(1.0,END),inv_lst_bx3.get(1.0,END),inv_lst_bx4.get(1.0,END),inv_lst_bx5.get(1.0,END),inv_lst_bx6.get(1.0,END),inv_lst_bx7.get(1.0,END),inv_lst_bx8.get(1.0,END),inv_lst_bx9.get(1.0,END),inv_lst_bx10.get(1.0,END),inv_lst_bx11.get(1.0,END),inv_lst_bx12.get(1.0,END),inv_lst_bx13.get(1.0,END),inv_lst_bx14.get(1.0,END),inv_lst_bx15.get(1.0,END),inv_lst_bx16.get(1.0,END),inv_lst_bx17.get(1.0,END),inv_lst_bx18.get(1.0,END),inv_lst_bx19.get(1.0,END),inv_lst_bx20.get(1.0,END),inv_lst_bx21.get(1.0,END),inv_lst_bx22.get(1.0,END),inv_lst_bx23.get(1.0,END),inv_lst_bx24.get(1.0,END),inv_txt.get("1.0",END))
        fbcursor.execute(stt_tbl_add,stt_tbl_add_val)
        fbilldb.commit()
    else:
        stt_tbl_updt="update invoice_settings set invoice_prefix=%s,starting_invoice_number=%s,bgcolour=%s,invoice=%s,invoice2=%s,invoice_date=%s,order_ref=%s,terms=%s,invoice_to=%s,ship_to=%s,id_sku=%s,product_service=%s,quantity=%s,	description=%s,	unit_price=%s,price=%s,subtotal=%s,discount=%s,	discount_rate=%s,tax1=%s,invoice_total=%s,total_paid=%s,balance=%s,	terms_conditions=%s,tax_exempted=%s,page=%s,of=%s,terms_notes=%s" #adding values into db
        stt_tbl_updt_val=(inv_tp_lf.get(),inv_spn_bx.get(),invset_bg_var.get(),inv_lst_bx1.get(1.0,END),inv_lst_bx2.get(1.0,END),inv_lst_bx3.get(1.0,END),inv_lst_bx4.get(1.0,END),inv_lst_bx5.get(1.0,END),inv_lst_bx6.get(1.0,END),inv_lst_bx7.get(1.0,END),inv_lst_bx8.get(1.0,END),inv_lst_bx9.get(1.0,END),inv_lst_bx10.get(1.0,END),inv_lst_bx11.get(1.0,END),inv_lst_bx12.get(1.0,END),inv_lst_bx13.get(1.0,END),inv_lst_bx14.get(1.0,END),inv_lst_bx15.get(1.0,END),inv_lst_bx16.get(1.0,END),inv_lst_bx17.get(1.0,END),inv_lst_bx18.get(1.0,END),inv_lst_bx19.get(1.0,END),inv_lst_bx20.get(1.0,END),inv_lst_bx21.get(1.0,END),inv_lst_bx22.get(1.0,END),inv_lst_bx23.get(1.0,END),inv_lst_bx24.get(1.0,END),inv_txt.get("1.0",END))
        fbcursor.execute(stt_tbl_updt,stt_tbl_updt_val)
        fbilldb.commit()
    #------------------------------------------------------------------------------------------order settings
    sq_tab4='select * from order_settings'
    fbcursor.execute(sq_tab4)
    mt_tb=fbcursor.fetchone()
    if mt_tb is None:
        stt_04_add="INSERT INTO order_settings(order_prefix,	starting_order_number,	bgcolour,	orders,	order2,order_date,	due_date,order_to,order_total,footer_note)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
        stt_04_add_val=(ord_lft_tp.get(),ord_spn_bx.get(),ord_man_var.get(),ord_lft_tp1.get(1.0,END),ord_lft_tp2.get(1.0,END),ord_lft_tp3.get(1.0,END),ord_lft_tp4.get(1.0,END),ord_lft_tp5.get(1.0,END),ord_lft_tp6.get(1.0,END),ord_scrl_txt.get("1.0",END))
        fbcursor.execute(stt_04_add,stt_04_add_val)
        fbilldb.commit()
    else:
        stt_04_updt="update order_settings set order_prefix=%s,starting_order_number=%s,bgcolour=%s,orders=%s,order2=%s,order_date=%s,due_date=%s,order_to=%s,order_total=%s,footer_note=%s" #adding values into db
        stt_04_updt_val=(ord_lft_tp.get(),ord_spn_bx.get(),ord_man_var.get(),ord_lft_tp1.get(1.0,END),ord_lft_tp2.get(1.0,END),ord_lft_tp3.get(1.0,END),ord_lft_tp4.get(1.0,END),ord_lft_tp5.get(1.0,END),ord_lft_tp6.get(1.0,END),ord_scrl_txt.get("1.0",END))
        fbcursor.execute(stt_04_updt,stt_04_updt_val)
        fbilldb.commit()
        
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
    # child = exctree.get_children()
    est_prefix = est_str.get()
    est_header = win_menu1.get()
    est_text1 = est_str1.get()
    est_text2 = est_str2.get()
    est_text3 = est_str3.get()
    est_text4 = est_str4.get()
    est_text5 = est_str5.get()
    est_text6 = est_str6.get()
    est_predefined = est_str7.get(1.0,END)
    est_default = win_menu2.get()
    est_spin1 = spin1.get()
    adv_default = adv_win_menu8.get()
    pord_prefix = prefix_str.get()
    pord_spin = pspin2.get()
    pord_header = pwin_menu.get()
    pord_text1 = pord_str1.get()
    pord_text2 = pord_str2.get()
    pord_text3 = pord_str3.get()
    pord_text4 = pord_str4.get()
    pord_text5 = pord_str5.get()
    pord_text6 = pord_str6.get()
    pord_text7 = pord_str7.get()
    pord_predefind = pord_str8.get(1.0,END)
    combo = em_menu.get()
    textfld = memaiframe.get(1.0,END) 
    sql = "select image from company"
    fbcursor.execute(sql)
    im = fbcursor.fetchone()
    sql = "select * from company"
    fbcursor.execute(sql)
    i = fbcursor.fetchall()
    if not i:
      if filename == "":
        
        sql = 'insert into company(name, address, email,salestaxno,currency,currencysign,currsignplace,  decimalseperator,excurrency,dateformat,exdate,taxtype,printimageornot,tax1name,tax1rate,printtax1,  tax2name,tax2rate,printtax2,attachment_file_type,miscellanoustab_cbutton1,miscellanoustab_cbutton2,miscellanoustab_cbutton3,miscellanoustab_cbutton4,miscellanoustab_cbutton5,miscellanoustab_cbutton6,Estimate_prefix,Customizeestimatetextlabels,Customizeestimatetextlabels1,Customizeestimatetextlabels2,Customizeestimatetextlabels3,Customizeestimatetextlabels4,Customizeestimatetextlabels5,Defaultestimatetemplate,Startingestimatenumber,Predefinedtextforestimates,adv_Selectedtemplatepreview,est_Headerboxbackgroundcolor,porder_prefix,headrebox_color,starting_porderno,text_label1,text_label2,text_label3,text_label4,text_label5,text_label6,text_label7,predefindterms_porder,email_template,text_field) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header,pord_prefix,pord_spin,pord_header,pord_text1,pord_text2,pord_text3,pord_text4,pord_text5,pord_text6,pord_text7,pord_predefind,combo,textfld)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        sql = 'insert into company(name, address, email,salestaxno,currency,currencysign,currsignplace,  decimalseperator,excurrency,dateformat,exdate,taxtype,printimageornot,tax1name,tax1rate,printtax1,  tax2name,tax2rate,printtax2,image,attachment_file_type,miscellanoustab_cbutton1,miscellanoustab_cbutton2,miscellanoustab_cbutton3,miscellanoustab_cbutton4,miscellanoustab_cbutton5,miscellanoustab_cbutton6,Estimate_prefix,Customizeestimatetextlabels,Customizeestimatetextlabels1,Customizeestimatetextlabels2,Customizeestimatetextlabels3,Customizeestimatetextlabels4,Customizeestimatetextlabels5,Defaultestimatetemplate,Startingestimatenumber,Predefinedtextforestimates,adv_Selectedtemplatepreview,est_Headerboxbackgroundcolor,porder_prefix,headrebox_color,starting_porderno,text_label1,text_label2,text_label3,text_label4,text_label5,text_label6,text_label7,predefindterms_porder,email_template,text_field) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,filename.split('/')[-1],radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header,pord_prefix,pord_spin,pord_header,pord_text1,pord_text2,pord_text3,pord_text4,pord_text5,pord_text6,pord_text7,pord_predefind,combo,textfld)
        fbcursor.execute(sql, val)
        fbilldb.commit()
    else:
      if filename == "":
        sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,currency=%s,currencysign=%s,  currsignplace=%s,decimalseperator=%s,excurrency=%s,dateformat=%s,exdate=%s,taxtype=%s,  printimageornot=%s,tax1name=%s,tax1rate=%s,printtax1=%s,tax2name=%s,tax2rate=%s,printtax2=%s,attachment_file_type=%s,miscellanoustab_cbutton1=%s,miscellanoustab_cbutton2=%s,miscellanoustab_cbutton3=%s,miscellanoustab_cbutton4=%s,miscellanoustab_cbutton5=%s,miscellanoustab_cbutton6=%s,Estimate_prefix=%s,Customizeestimatetextlabels=%s,Customizeestimatetextlabels1=%s,Customizeestimatetextlabels2=%s,Customizeestimatetextlabels3=%s,Customizeestimatetextlabels4=%s,Customizeestimatetextlabels5=%s,Defaultestimatetemplate=%s,Startingestimatenumber=%s,Predefinedtextforestimates=%s,adv_Selectedtemplatepreview=%s,est_Headerboxbackgroundcolor=%s,porder_prefix=%s,headrebox_color=%s,starting_porderno=%s,text_label1=%s,text_label2=%s,text_label3=%s,text_label4=%s,text_label5=%s,text_label6=%s,text_label7=%s,predefindterms_porder=%s,email_template=%s,text_field=%s"
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header,pord_prefix,pord_spin,pord_header,pord_text1,pord_text2,pord_text3,pord_text4,pord_text5,pord_text6,pord_text7,pord_predefind,combo,textfld)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,currency=%s,currencysign=%s,  currsignplace=%s,decimalseperator=%s,excurrency=%s,dateformat=%s,exdate=%s,taxtype=%s,  printimageornot=%s,tax1name=%s,tax1rate=%s,printtax1=%s,tax2name=%s,tax2rate=%s,printtax2=%s,image=%s,attachment_file_type=%s,miscellanoustab_cbutton1=%s,miscellanoustab_cbutton2=%s,miscellanoustab_cbutton3=%s,miscellanoustab_cbutton4=%s,miscellanoustab_cbutton5=%s,miscellanoustab_cbutton6=%s,Estimate_prefix=%s,Customizeestimatetextlabels=%s,Customizeestimatetextlabels1=%s,Customizeestimatetextlabels2=%s,Customizeestimatetextlabels3=%s,Customizeestimatetextlabels4=%s,Customizeestimatetextlabels5=%s,Defaultestimatetemplate=%s,Startingestimatenumber=%s,Predefinedtextforestimates=%s,adv_Selectedtemplatepreview=%s,est_Headerboxbackgroundcolor=%s,porder_prefix=%s,headrebox_color=%s,starting_porderno=%s,text_label1=%s,text_label2=%s,text_label3=%s,text_label4=%s,text_label5=%s,text_label6=%s,text_label7=%s,predefindterms_porder=%s,email_template=%s,text_field=%s"
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,filename.split('/')[-1],radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header,pord_prefix,pord_spin,pord_header,pord_text1,pord_text2,pord_text3,pord_text4,pord_text5,pord_text6,pord_text7,pord_predefind,combo,textfld)
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
        
        exclistbox.delete(0,END)
        fbcursor.execute("select extra_cost_name  from extra_cost_name")
        pandsdata = fbcursor.fetchall()
        excvalues = []
        for i in pandsdata:
          excvalues.append(i[0])
        for records in excvalues:
          exclistbox.insert(0,records)
  # new_value = String
        
        
  
  def edit_valueexc(event):
    itemexc = exclistbox.get(ACTIVE)
    entryexc.delete(0, END)
    entryexc.insert(0, itemexc)
  
  def save_valueexc():
    i = entryexc.get()
    if i == "":
      pass
    else:
      itemexc = exclistbox.get(ACTIVE)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      companyid = com[0]
      if not com:
        pass
      else:
        sql = 'update extra_cost_name set extra_cost_name=%s where extra_cost_name=%s'
        val = (i,itemexc)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        entryexc.delete(0, END)
        
        exclistbox.delete(0,END)
        fbcursor.execute("select extra_cost_name  from extra_cost_name")
        pandsdata = fbcursor.fetchall()
        excvalues = []
        for i in pandsdata:
          excvalues.append(i[0])
        for records in excvalues:
          exclistbox.insert(0,records)
    
    
  
  def del_valueexc():
    itemexc = exclistbox.get(ACTIVE)
    print(itemexc)
    sql = "delete from extra_cost_name where extra_cost_name = %s"
    val = (itemexc, )
    fbcursor.execute(sql, val)
    fbilldb.commit()
    
    exclistbox.delete(0,END)
    fbcursor.execute("select extra_cost_name  from extra_cost_name")
    pandsdata = fbcursor.fetchall()
    excvalues = []
    for i in pandsdata:
      excvalues.append(i[0])
    for records in excvalues:
      exclistbox.insert(0,records)
      
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  exclistbox = Listbox(firsttab, width=43, bg="white",bd=0,
                  activestyle = 'dotbox')
  exclistbox.place(x=15,y=200,height=115,width=380)
  fbcursor.execute("select extra_cost_name  from extra_cost_name")
  pandsdata = fbcursor.fetchall()
  excvalues = []
  for i in pandsdata:
    excvalues.append(i[0])
  for records in excvalues:
    exclistbox.insert(0,records)
  exclistbox.bind('<Double-1>',edit_valueexc)

  scrollbary.config(command=exclistbox.yview)
  scrollbary.place(x=394,y=200,height=125)
  scrollbarx.config(command=exclistbox.xview)
  scrollbarx.place(x=15,y=313, width=380)
  
 
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
        prelistbox.delete(0, END)
        sql = 'select headerandfooter from header_and_footer'
        fbcursor.execute(sql)
        foothead = fbcursor.fetchall()
        prevalues = []
        for i in foothead:
          prevalues.append(i[0])
        for records in prevalues:
          prelistbox.insert(0,records)
  # new_value = String
        
        
  
  def edit_valuepre(event):
    selected_item = prelistbox.get(ACTIVE)
    entrypre.delete(0, END)
    entrypre.insert(0, selected_item)
  
  def save_valuepre():
    i = prestr.get()
    if i == "":
      pass
    else:
      selected_item = prelistbox.get(ACTIVE)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      companyid = com[0]
      if not com:
        pass
      else:
        sql = 'update header_and_footer set headerandfooter=%s where headerandfooter=%s'
        val = (i,selected_item)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        prelistbox.delete(0, END)
        sql = 'select headerandfooter from header_and_footer'
        fbcursor.execute(sql)
        foothead = fbcursor.fetchall()
        prevalues = []
        for i in foothead:
          prevalues.append(i[0])
        for records in prevalues:
          prelistbox.insert(0,records)
    
    
  
  def del_valuepre():
    itempre = prelistbox.get(ACTIVE)
    sql = "delete from header_and_footer where headerandfooter = %s"
    val = (itempre,)
    fbcursor.execute(sql, val)
    fbilldb.commit()
    prelistbox.delete(0, END)
    sql = 'select headerandfooter from header_and_footer'
    fbcursor.execute(sql)
    foothead = fbcursor.fetchall()
    prevalues = []
    for i in foothead:
      prevalues.append(i[0])
    for records in prevalues:
      prelistbox.insert(0,records)
    
      
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  prelistbox = Listbox(firsttab, width=43, bg="white",bd=0,
                  activestyle = 'dotbox')
  prelistbox.place(x=15,y=400,height=115,width=380)
  scrollbary.config(command=prelistbox.yview)
  scrollbary.place(x=395,y=400,height=115)
  scrollbarx.config(command=prelistbox.xview)
  scrollbarx.place(x=15,y=510, width=380)

  sql = 'select headerandfooter from header_and_footer'
  fbcursor.execute(sql)
  foothead = fbcursor.fetchall()
  prevalues = []
  for i in foothead:
    prevalues.append(i[0])
  for records in prevalues:
    prelistbox.insert(0,records)
  prelistbox.bind('<Double-1>',edit_valuepre)
  
  
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
    if sectab[10] == "Default":
      setdateex = 'mm-dd-yyyy'
    elif dafget == "mm-dd-yyyy":
      setdateex = 'mm-dd-yyyy'
    elif dafget == "dd-mm-yyyy":
      setdateex = 'dd-mm-yyyy'
    elif dafget == "yyyy.mm.dd":
      setdateex = 'yyyy.mm.dd'
    elif dafget == "mm/dd/yyyy":
      setdateex = "mm/dd/yyyy"
    elif dafget == "dd/mm/yyyy":
      setdateex = "dd/mm/yyyy"
    elif dafget == "dd.mm.yyyy":
      setdateex = "dd.mm.yyyy"
    elif dafget == "yyyy/mm/dd":
      setdateex = "yyyy/mm/dd"
    else:
      setdateex = "yyyy/mm/dd"
    exd = DateEntry(secondtab,date_pattern=setdateex)
    exd.place(x=280,y=380)
  
  comdaf = StringVar()
  daf = ttk.Combobox(secondtab,textvariable=comdaf)
  daf["values"] = ("Default",'mm-dd-yyyy','dd-mm-yyyy','yyyy.mm.dd','mm/dd/yyyy','dd/mm/yyyy','dd.mm.yyyy','yyyy/mm/dd')
  daf.bind("<<ComboboxSelected>>",daffun)
  if not sectab:
    pass
  elif sectab[10]:
    daf.insert(0, sectab[10])
  daf.place(x=60,y=380)
  

  if not sectab:
    setdateex = 'mm-dd-yyyy'
  elif sectab[10] == "Default":
    setdateex = 'mm-dd-yyyy'
  elif sectab[10] == "mm-dd-yyyy":
    setdateex = 'mm-dd-yyyy'
  elif sectab[10] == "dd-mm-yyyy":
    setdateex = 'dd-mm-yyyy'
  elif sectab[10] == "yyyy.mm.dd":
    setdateex = 'yyyy.mm.dd'
  elif sectab[10] == "mm/dd/yyyy":
    setdateex = "mm/dd/yyyy"
  elif sectab[10] == "dd/mm/yyyy":
    setdateex = "dd/mm/yyyy"
  elif sectab[10] == "dd.mm.yyyy":
    setdateex = "dd.mm.yyyy"
  elif sectab[10] == "yyyy/mm/dd":
    setdateex = "yyyy/mm/dd"

  exd = DateEntry(secondtab,date_pattern=setdateex)
  exd.place(x=280,y=380)
  
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

  ################### tab03 ###################################################################### ###settings-saiju
  Invoice_setting_frame=Frame(tab03, relief=GROOVE, bg="#f8f8f2")
  Invoice_setting_frame.pack(side="top", fill=BOTH)

  Invoice_setting_frame_cpy=Frame(Invoice_setting_frame, bg="#f5f3f2", height=700)
  Invoice_setting_frame_cpy.pack(side="top", fill=BOTH)
  ver = Label(Invoice_setting_frame_cpy,text="Invoice# prefix")
  ver.place(x=5,y=20)

  sql_tb03_qry="select * from invoice_settings"
  fbcursor.execute(sql_tb03_qry)
  tab03_valzs=fbcursor.fetchone()

  inv_tp_lf =Entry(Invoice_setting_frame)
  if tab03_valzs is None:
    inv_tp_lf.insert(0, "INV")
  else:
    inv_tp_lf.delete(0,'end')
    inv_tp_lf.insert(END,tab03_valzs[0])
  inv_tp_lf.place(x=100,y=20)

  invset_ver = Label(Invoice_setting_frame_cpy,text="Starting Invoice number")
  invset_ver.place(x=25,y=50)

  def spin_valss_tab03(S,d):
    if d=='1':
      if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
        return False
      return True
          
    if d.isdigit():
      return True


  valdity_tab03=(Invoice_setting_frame_cpy.register(spin_valss_tab03), '%S','%d')
  inv_spn_bx = Spinbox(Invoice_setting_frame_cpy,from_=1,to=1000000,width=15,justify=RIGHT)
  
  if tab03_valzs is None:
    pass
  else:
    inv_spn_bx.delete(0,"end")
    inv_spn_bx.insert(0,int(tab03_valzs[1]))
  inv_spn_bx.config(validate='key',validatecommand=(valdity_tab03))
  inv_spn_bx.place(x=50,y=80)

  inv_lbl2 = Label(Invoice_setting_frame_cpy,text="Header box background color")
  inv_lbl2.place(x=5,y=100)
  


  invset_bg_var = StringVar()
  invset_bg_list = ttk.Combobox(Invoice_setting_frame_cpy,textvariable=invset_bg_var)
  
  invset_bg_list['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
  if tab03_valzs is None:
    invset_bg_list.current(0)
  else:
    invset_bg_list.insert(0,tab03_valzs[2])
  invset_bg_list.place(x=6 ,y=120)

  inv_lb22 = Label(Invoice_setting_frame_cpy,text="Customize Invoice text labels")
  inv_lb22.place(x=5,y=140)

  def lst_bx1(event):
    pass
  def restore_dfilt():
    inv_lst_bx1.delete(1.0,'end')
    inv_lst_bx1.insert(END, "Invoice")
    inv_lst_bx2.delete(1.0,'end')
    inv_lst_bx2.insert(END, "Invoice#")
    inv_lst_bx3.delete(1.0,'end')
    inv_lst_bx3.insert(END, "Invoice date")
    inv_lst_bx4.delete(1.0,'end')
    inv_lst_bx4.insert(END, "Order ref.#")
    inv_lst_bx5.delete(1.0,'end')
    inv_lst_bx5.insert(END, "Terms")
    inv_lst_bx6.delete(1.0,'end')
    inv_lst_bx6.insert(END, "Invoice to")
    inv_lst_bx7.delete(1.0,'end')
    inv_lst_bx7.insert(END, "Ship to")
    inv_lst_bx8.delete(1.0,'end')
    inv_lst_bx8.insert(END, "ID/SKU")
    inv_lst_bx9.delete(1.0,'end')
    inv_lst_bx9.insert(END, "Product/Service")
    inv_lst_bx10.delete(1.0,'end')
    inv_lst_bx10.insert(END, "Quantity")
    inv_lst_bx11.delete(1.0,'end')
    inv_lst_bx11.insert(END, "Description")
    inv_lst_bx12.delete(1.0,'end')
    inv_lst_bx12.insert(END, "Unit Price")
    inv_lst_bx13.delete(1.0,'end')
    inv_lst_bx13.insert(END, "Price")
    inv_lst_bx14.delete(1.0,'end')
    inv_lst_bx14.insert(END, "Subtotal")
    inv_lst_bx15.delete(1.0,'end')
    inv_lst_bx15.insert(END, "Discount")
    inv_lst_bx16.delete(1.0,'end')
    inv_lst_bx16.insert(END, "Discount rate")
    inv_lst_bx17.delete(1.0,'end')
    inv_lst_bx17.insert(END, "TAX1")
    inv_lst_bx18.delete(1.0,'end')
    inv_lst_bx18.insert(END, "Invoice Total")
    inv_lst_bx19.delete(1.0,'end')
 
    inv_lst_bx19.insert(END, "Total Paid")
    inv_lst_bx20.delete(1.0,'end')
    inv_lst_bx20.insert(END, "Balance")
    inv_lst_bx21.delete(1.0,'end')
    inv_lst_bx21.insert(END, "Terms and Conditions")
    inv_lst_bx22.delete(1.0,'end')
    inv_lst_bx22.insert(END, "Tax Exempted")
    inv_lst_bx23.delete(1.0,'end')
    inv_lst_bx23.insert(END, "Page")
    inv_lst_bx24.delete(1.0,'end')
    inv_lst_bx24.insert(END, "of")
 

    
  inv_lst_bx1 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx1.insert(END, "Invoice")
  else:
    inv_lst_bx1.delete(1.0,"end")
    inv_lst_bx1.insert(1.0,tab03_valzs[3])

  inv_lst_bx1.place(x=5,y=160)
  inv_lst_bx2 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx2.insert(END, "Invoice#")
  else:
    inv_lst_bx2.delete(1.0,"end")
    inv_lst_bx2.insert(1.0,tab03_valzs[4])

  
  inv_lst_bx2.place(x=5,y=180)
  inv_lst_bx3 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx3.insert(END, "Invoice date")
  else:
    inv_lst_bx3.delete(1.0,"end")
    inv_lst_bx3.insert(1.0,tab03_valzs[5])
  
  inv_lst_bx3.place(x=5,y=200)
  inv_lst_bx4 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx4.insert(END, "Order ref.#")
  else:
    inv_lst_bx4.delete(1.0,"end")
    inv_lst_bx4.insert(1.0,tab03_valzs[6])
  
  inv_lst_bx4.place(x=5,y=220)
  inv_lst_bx5 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx5.insert(END, "Terms")
  else:
    inv_lst_bx5.delete(1.0,"end")
    inv_lst_bx5.insert(1.0,tab03_valzs[7])
  
  inv_lst_bx5.place(x=5,y=240)
  inv_lst_bx6 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx6.insert(END, "Invoice to")
  else:
    inv_lst_bx6.delete(1.0,"end")
    inv_lst_bx6.insert(1.0,tab03_valzs[8])
  
  inv_lst_bx6.place(x=5,y=260)
  inv_lst_bx7 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx7.insert(END, "Ship to")
  else:
    inv_lst_bx7.delete(1.0,"end")
    inv_lst_bx7.insert(1.0,tab03_valzs[9])
  
  inv_lst_bx7.place(x=5,y=280)
  inv_lst_bx8 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx8.insert(END, "ID/SKU")
  else:
    inv_lst_bx8.delete(1.0,"end")
    inv_lst_bx8.insert(1.0,tab03_valzs[10])
  
  inv_lst_bx8.place(x=5,y=300)
  inv_lst_bx9 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx9.insert(END, "Product/Service")
  else:
    inv_lst_bx9.delete(1.0,"end")
    inv_lst_bx9.insert(1.0,tab03_valzs[11])
  
  inv_lst_bx9.place(x=5,y=320)
  inv_lst_bx10 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx10.insert(END, "Quantity")
  else:
    inv_lst_bx10.delete(1.0,"end")
    inv_lst_bx10.insert(1.0,tab03_valzs[12])
  
  inv_lst_bx10.place(x=5,y=340)
  inv_lst_bx11 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx11.insert(END, "Description")
  else:
    inv_lst_bx11.delete(1.0,"end")
    inv_lst_bx11.insert(1.0,tab03_valzs[13])
  
  inv_lst_bx11.place(x=5,y=360)
  inv_lst_bx12 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx12.insert(END, "Unit Price")
  else:
    inv_lst_bx12.delete(1.0,"end")
    inv_lst_bx12.insert(1.0,tab03_valzs[14])
  
  inv_lst_bx12.place(x=5,y=380)
  inv_lst_bx13 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx13.insert(END, "Price")
  else:
    inv_lst_bx13.delete(1.0,"end")
    inv_lst_bx13.insert(1.0,tab03_valzs[15])
  
  inv_lst_bx13.place(x=5,y=400)
  inv_lst_bx14 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx14.insert(END, "Subtotal")
  else:
    inv_lst_bx14.delete(1.0,"end")
    inv_lst_bx14.insert(1.0,tab03_valzs[16])
  
  inv_lst_bx14.place(x=5,y=420)
  inv_lst_bx15 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx15.insert(END, "Discount")
  else:
    inv_lst_bx15.delete(1.0,"end")
    inv_lst_bx15.insert(1.0,tab03_valzs[17])
  
  inv_lst_bx15.place(x=5,y=440)
  inv_lst_bx16 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx16.insert(END, "Discount rate")
  else:
    inv_lst_bx16.delete(1.0,"end")
    inv_lst_bx16.insert(1.0,tab03_valzs[18])
  
  inv_lst_bx16.place(x=5,y=460)
  inv_lst_bx17 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx17.insert(END, "TAX1")
  else:
    inv_lst_bx17.delete(1.0,"end")
    inv_lst_bx17.insert(1.0,tab03_valzs[19])
  
  inv_lst_bx17.place(x=200,y=520)
  inv_lst_bx18 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx18.insert(END, "Invoice Total")
  else:
    inv_lst_bx18.delete(1.0,"end")
    inv_lst_bx18.insert(1.0,tab03_valzs[20])
  
  inv_lst_bx18.place(x=400,y=520)
  inv_lst_bx19 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx19.insert(END, "Total Paid")
  else:
    inv_lst_bx19.delete(1.0,"end")
    inv_lst_bx19.insert(1.0,tab03_valzs[21])
  
  inv_lst_bx19.place(x=600,y=520)
  inv_lst_bx20 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx20.insert(END, "Balance")
  else:
    inv_lst_bx20.delete(1.0,"end")
    inv_lst_bx20.insert(1.0,tab03_valzs[22])
  
  inv_lst_bx20.place(x=800,y=520)
  inv_lst_bx21 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx21.insert(END, "Terms and Conditions")
  else:
    inv_lst_bx21.delete(1.0,"end")
    inv_lst_bx21.insert(1.0,tab03_valzs[23])
  
  inv_lst_bx21.place(x=1000,y=520)
  inv_lst_bx22 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx22.insert(END, "Tax Exempted")
  else:
    inv_lst_bx22.delete(1.0,"end")
    inv_lst_bx22.insert(1.0,tab03_valzs[24])
  
  inv_lst_bx22.place(x=5,y=480)
  inv_lst_bx23 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx23.insert(END, "Page")
  else:
    inv_lst_bx23.delete(1.0,"end")
    inv_lst_bx23.insert(1.0,tab03_valzs[25])
  
  inv_lst_bx23.place(x=5,y=500)
  inv_lst_bx24 = Text(Invoice_setting_frame, height=1, width=25, font=('Calibri 10'))
  if tab03_valzs is None:
    inv_lst_bx24.insert(END, "of")
  else:
    inv_lst_bx24.delete(1.0,"end")
    inv_lst_bx24.insert(1.0,tab03_valzs[26])
  
  inv_lst_bx24.place(x=5,y=520)

  



  invset_s1 = StringVar(Invoice_setting_frame, "Invoice")


  invset_ver = Label(Invoice_setting_frame_cpy,text="Default Invoice template(example,click on preview for mouse scrolling)")
  invset_ver.place(x=248,y=55 )

  invset_ver = Label(Invoice_setting_frame_cpy,text="Default Invoice template")
  invset_ver.place(x=619,y=40)

  #data=StringVar()

  invset_messagelbframe=LabelFrame(Invoice_setting_frame_cpy,text="Predefined terms and conditions text for Invoice", height=100, width=980)
  invset_messagelbframe.place(x=248, y=400)

  inv_txt = scrolledtext.ScrolledText(Invoice_setting_frame_cpy, undo=True,width=115,height=4)
  if tab03_valzs is None:
    inv_txt.insert(1.0,"Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods, and agrees to be bound to these contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller.")
  else:
    inv_txt.insert(1.0,tab03_valzs[27])
  inv_txt.place(x=260,y=425)

  inv_rst_btn = Button(Invoice_setting_frame_cpy,text="Restore defaults",command=lambda:restore_dfilt())
  inv_rst_btn.place(x=1200,y=515)

  #------------Professional 1 (logo on left side)-------------
  def styl_can_def(event):
      menuvar_lst=logo_just_var.get()
    
      por_sql_st='select * from company'
      fbcursor.execute(por_sql_st)
      cmpy_dtl=fbcursor.fetchone()
      if menuvar_lst == 'Professional 1 (logo on left side)':

        if cmpy_dtl[1] is not None:
          sql='select dateformat from company'
          fbcursor.execute(sql)
          date_frmat=fbcursor.fetchone()
          
          if not date_frmat:
            ft_fr='%Y-%m-%d'
        
          elif date_frmat[0]=="mm-dd-yyyy":
            ft_fr='%m-%d-%Y'

          elif date_frmat[0]=="dd-mm-yyyy":
              ft_fr='%d-%m-%Y'
                      
          elif date_frmat[0]=="yyy.mm.dd":
              ft_fr='%Y.%m.%d'
                          
          elif date_frmat[0]=="mm/dd/yyyy":
              ft_fr='%m/%d/%Y'
                          
          elif date_frmat[0]=="dd/mm/yyyy":
              ft_fr='%d/%m/%Y'
                                  
          elif date_frmat[0]=="dd.mm.yyyy":
              ft_fr='%d.%m.%Y'
                                  
          elif date_frmat[0]=="yyyy/  mm/dd":
              ft_fr='%Y/%m/%d'

          else:
              ft_fr='%Y-%m-%d'
          td_date=date.today()
          date_tdy=td_date.strftime(ft_fr)  
          frame_pro1 = Frame(Invoice_setting_frame_cpy, width=953, height=300)
          frame_pro1.pack(expand=True, fill=BOTH)
          frame_pro1.place(x=247,y=90)
          inv_pro1_canvas=Canvas(frame_pro1, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(frame_pro1, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=inv_pro1_canvas.yview)
          
          inv_pro1_canvas.config(width=953,height=300)
          inv_pro1_canvas.config(yscrollcommand=vertibar.set)
          inv_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          inv_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          inv_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            inv_image = Image.open("images/"+cmpy_dtl[13])
            inv_resize_image = inv_image.resize((200,75))
            inv_image = ImageTk.PhotoImage(inv_resize_image)
          
            inv_logo = Label(inv_pro1_canvas,width=200,height=75, bg="white",image = inv_image) 
            inv_window_image = inv_pro1_canvas.create_window(150, 50, anchor="nw", window=inv_logo)
            inv_logo.photo = inv_image
          except:
            inv_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          
          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx2.get(1.0, END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Invoice#
          win_inv1 = inv_pro1_canvas.create_window(175, 140, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx3.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1 )#Invoicedate
          win_inv1 = inv_pro1_canvas.create_window(175, 160, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(inv_pro1_canvas,text="Due Date", bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Due date
          win_inv1 = inv_pro1_canvas.create_window(175, 180, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx5.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Terms
          win_inv1 = inv_pro1_canvas.create_window(175, 200, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx4.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = inv_pro1_canvas.create_window(175, 220, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_pro1_canvas,text=str(inv_tp_lf.get())+"1/2022", bg="white",anchor="nw",font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = inv_pro1_canvas.create_window(310, 140, anchor="nw", window=lb_inv1)
          inv_pro1_canvas.create_text(350, 170, text=date_tdy,justify=LEFT, fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(350, 190, text=date_tdy,justify=LEFT, fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(340, 210, text="NET 15",justify=LEFT, fill="black", font=('Helvetica 11'))   
          
          labelcmp=Label(inv_pro1_canvas,text=cmpy_dtl[1], bg="white",anchor="e",font=("Helvetica", 12), width=40, height=1)
          window = inv_pro1_canvas.create_window(430,80, anchor="nw", window=labelcmp)

          labelcmpl=Label(inv_pro1_canvas,text=cmpy_dtl[2],justify=RIGHT, bg="white",font=("Helvetica", 9),anchor="ne", width=50, height=4)
          windowl = inv_pro1_canvas.create_window(440,110, anchor="nw", window=labelcmpl)

          
          inv_pro1_canvas.create_text(745, 185, text=cmpy_dtl[4], fill="black", font=('Helvetica 10'))

          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx1.get(1.0,END), bg="white",anchor="ne",font=('Helvetica 14 bold'),height=1)#invoice
          win_inv1 = inv_pro1_canvas.create_window(800, 200, anchor="ne", window=lb_inv1)

          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx22.get(1.0,END), bg="white",justify=LEFT,font=("Helvetica 10" ),height=2)#TAX EXEMPTED
          win_inv1 = inv_pro1_canvas.create_window(800, 225, anchor="ne", window=lb_inv1)

          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx6.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline" ),height=1)#Invoice to
          win_inv1 = inv_pro1_canvas.create_window(175, 250, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx7.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline"),height=1)#Ship to
          win_inv1 = inv_pro1_canvas.create_window(525, 250, anchor="nw", window=lb_inv1)

          
          # inv_pro1_canvas.create_text(765, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))
          # inv_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
          # inv_pro1_canvas.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
          inv_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          inv_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
          # inv_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          inv_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          inv_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
          fgth = ttk.Style()
          fgth.configure('mystyle101.Treeview.Heading', background=''+ invset_bg_var.get(),State='DISABLE')

          tree=ttk.Treeview(inv_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle101.Treeview')

          tree.column("# 1", anchor=E, stretch=NO, width=100)
          tree.heading("# 1", text=inv_lst_bx8.get(1.0,END))#"ID/SKU"
          tree.column("# 2", anchor=E, stretch=NO, width=350)
          tree.heading("# 2", text=inv_lst_bx9.get(1.0,END))#Product/Service - Description
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text=inv_lst_bx10.get(1.0,END))#"Quantity"
          tree.column("# 4", anchor=E, stretch=NO, width=90)  
          tree.heading("# 4", text=inv_lst_bx12.get(1.0,END))#"Unit Price"
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text=inv_lst_bx13.get(1.0,END))#"Price"
          
          window = inv_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)
          squl_qry='select * from company'
          fbcursor.execute(squl_qry)
          cmpy_tax=fbcursor.fetchone()

          inv_pro1_canvas.create_line(120, 390, 820, 390 )
          inv_pro1_canvas.create_line(120, 340, 120, 365 )
          inv_pro1_canvas.create_line(120, 365, 120, 390 )
          inv_pro1_canvas.create_line(820, 340, 820, 540 )
          inv_pro1_canvas.create_line(740, 340, 740, 540 )
          inv_pro1_canvas.create_line(570, 340, 570, 540 )
          inv_pro1_canvas.create_line(570, 415, 820, 415 )
          inv_pro1_canvas.create_line(570, 440, 820, 440 )
          inv_pro1_canvas.create_line(570, 465, 820, 465 )
          inv_pro1_canvas.create_line(570, 490, 820, 490 )
          inv_pro1_canvas.create_line(570, 515, 820, 515 )
          inv_pro1_canvas.create_line(650, 340, 650, 390 )
          inv_pro1_canvas.create_line(220, 340, 220, 390 )
          inv_pro1_canvas.create_line(570, 540, 820, 540 )

          sqlr= 'select currencysign from company'
          fbcursor.execute(sqlr)
          crncy=fbcursor.fetchone()
          crcy_type=crncy[0]
          sqlrt= 'select currsignplace from company'
          fbcursor.execute(sqlrt)
          post_rp=fbcursor.fetchone()
          cry_plcy=post_rp[0]
          if cry_plcy=="before amount": 
            inv_pro1_canvas.create_text(710, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 404, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 428, text=str(crcy_type)+"18.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 502, text=str(crcy_type)+"100.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 526, text=str(crcy_type)+"138.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 454, text=str(crcy_type)+"20.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 479, text=str(crcy_type)+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount":
            inv_pro1_canvas.create_text(710, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 404, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 428, text="18.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 502, text="100.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 526, text="138.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 454, text="20.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 479, text="238.00"+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="before amount with space": 
            inv_pro1_canvas.create_text(710, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 404, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 428, text=str(crcy_type)+" "+"18.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 502, text=str(crcy_type)+" "+"100.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 526, text=str(crcy_type)+" "+"138.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 454, text=str(crcy_type)+" "+"20.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 479, text=str(crcy_type)+" "+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount with space":
            inv_pro1_canvas.create_text(710, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 404, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 428, text="18.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 502, text="100.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 526, text="138.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 454, text="20.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 479, text="238.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          else:
            pass

          inv_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
          
            

          lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
          win_inv2 = inv_pro1_canvas.create_window(630,392, anchor="nw", window=lbx_inv)

          lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
          win_inv2 = inv_pro1_canvas.create_window(635,418, anchor="nw", window=lbx_inv)

          lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
          win_inv2 = inv_pro1_canvas.create_window(630, 492,anchor="nw", window=lbx_inv)

          lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
          win_inv2 = inv_pro1_canvas.create_window(635, 518, anchor="nw", window=lbx_inv)

          
          lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx18.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#Order Total"
          win_inv2 = inv_pro1_canvas.create_window(625, 468, anchor="nw", window=lbx_inv)
          lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx21.get(1.0,END), bg="white",anchor="n",font=("Helvetica 10 "),height=1)#"Terms and Conditions"
          win_inv2 = inv_pro1_canvas.create_window(420, 570, anchor="nw", window=lbx_inv)
        
          inv_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

 
      
          # if int(cmpy_tax[12])==3:
          #   inv_pro1_canvas.create_line(120, 390, 820, 390 )
          #   inv_pro1_canvas.create_line(120, 340, 120, 365 )
          #   inv_pro1_canvas.create_line(120, 365, 120, 390 )
          #   inv_pro1_canvas.create_line(820, 360, 820, 565 )
          #   inv_pro1_canvas.create_line(740, 340, 740, 565 )
          #   inv_pro1_canvas.create_line(570, 340, 570, 565 )
          #   inv_pro1_canvas.create_line(570, 415, 820, 415 )
          #   inv_pro1_canvas.create_line(570, 440, 820, 440 )
          #   inv_pro1_canvas.create_line(570, 465, 820, 465 )
          #   inv_pro1_canvas.create_line(570, 490, 820, 490 )
          #   inv_pro1_canvas.create_line(570, 515, 820, 515 )
          #   inv_pro1_canvas.create_line(650, 340, 650, 390 )
          #   inv_pro1_canvas.create_line(220, 340, 220, 390 )
          #   inv_pro1_canvas.create_line(570, 540, 820, 540 )
          #   inv_pro1_canvas.create_line(570, 565, 820, 565 )

          #   inv_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
          #   inv_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          #   inv_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
          #   inv_pro1_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
          #   inv_pro1_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))
            

          #   lbx_inv=Label(inv_pro1_canvas,text="Subtotal", bg="white",anchor="nw",font=("Helvetica 10"))
          #   win_inv2 = inv_pro1_canvas.create_window(635, 393, anchor="nw", window=lbx_inv)

          #   lbx_inv=Label(inv_pro1_canvas,text="TAX1", bg="white",anchor="nw",font=("Helvetica 10"))
          #   win_inv2 = inv_pro1_canvas.create_window(635, 418, anchor="nw", window=lbx_inv)

          #   lbx_inv=Label(inv_pro1_canvas,text="TAX2", bg="white",anchor="nw",font=("Helvetica 10"))
          #   win_inv2 = inv_pro1_canvas.create_window(635, 443, anchor="nw", window=lbx_inv)

          #   lbx_inv=Label(inv_pro1_canvas,text="Total Paid", bg="white",anchor="nw",font=("Helvetica 10 "))
          #   win_inv2 = inv_pro1_canvas.create_window(630, 518,anchor="nw", window=lbx_inv)

          #   lbx_inv=Label(inv_pro1_canvas,text="Balance", bg="white",anchor="nw",font=("Helvetica 10 "))
          #   win_inv2 = inv_pro1_canvas.create_window(635, 543, anchor="nw", window=lbx_inv)
            
            

          #   # inv_pro1_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
          #   inv_pro1_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

          #   inv_pro1_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

          #   inv_pro1_canvas.create_text(792, 455, text="$18.00", fill="black", font=('Helvetica 10'))

          #   inv_pro1_canvas.create_text(650, 480, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          #   inv_pro1_canvas.create_text(792, 480, text="$20.00", fill="black", font=('Helvetica 10'))

          #   inv_pro1_canvas.create_text(790, 505, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          #   inv_pro1_canvas.create_text(655, 505, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

          #   inv_pro1_canvas.create_text(790, 530, text="$100.00", fill="black", font=('Helvetica 10'))
        

          #   inv_pro1_canvas.create_text(790, 553, text="$138.00", fill="black", font=('Helvetica 10'))

          # elif int(cmpy_tax[12])==2:
          #   inv_pro1_canvas.create_line(120, 390, 820, 390 )
          #   inv_pro1_canvas.create_line(120, 340, 120, 365 )
          #   inv_pro1_canvas.create_line(120, 365, 120, 390 )
          #   inv_pro1_canvas.create_line(820, 340, 820, 540 )
          #   inv_pro1_canvas.create_line(740, 340, 740, 540 )
          #   inv_pro1_canvas.create_line(570, 340, 570, 540 )
          #   inv_pro1_canvas.create_line(570, 415, 820, 415 )
          #   inv_pro1_canvas.create_line(570, 440, 820, 440 )
          #   inv_pro1_canvas.create_line(570, 465, 820, 465 )
          #   inv_pro1_canvas.create_line(570, 490, 820, 490 )
          #   inv_pro1_canvas.create_line(570, 515, 820, 515 )
          #   inv_pro1_canvas.create_line(650, 340, 650, 390 )
          #   inv_pro1_canvas.create_line(220, 340, 220, 390 )
          #   inv_pro1_canvas.create_line(570, 540, 820, 540 )

          #   inv_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
          #   inv_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          #   inv_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
          #   inv_pro1_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
          #   inv_pro1_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))
            

          #   lbx_inv=Label(inv_pro1_canvas,text="Subtotal", bg="white",anchor="nw",font=("Helvetica 10"))
          #   win_inv2 = inv_pro1_canvas.create_window(630,392, anchor="nw", window=lbx_inv)

          #   lbx_inv=Label(inv_pro1_canvas,text="TAX1", bg="white",anchor="nw",font=("Helvetica 10 "))
          #   win_inv2 = inv_pro1_canvas.create_window(635,418, anchor="nw", window=lbx_inv)

          #   lbx_inv=Label(inv_pro1_canvas,text="Total Paid", bg="red",anchor="nw",font=("Helvetica 10 "))
          #   win_inv2 = inv_pro1_canvas.create_window(630, 492,anchor="nw", window=lbx_inv)

          #   lbx_inv=Label(inv_pro1_canvas,text="Balance", bg="white",anchor="nw",font=("Helvetica 10 "))
          #   win_inv2 = inv_pro1_canvas.create_window(635, 518, anchor="nw", window=lbx_inv)
            

          #   # inv_pro1_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
          #   inv_pro1_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))


          #   inv_pro1_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

          #   inv_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          #   inv_pro1_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

          #   inv_pro1_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          #   inv_pro1_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

          #   inv_pro1_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))


          #   inv_pro1_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))

          # elif cmpy_tax[12]==1:
          #   pass
          
          

          inv_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
        
          inv_pro1_canvas.create_line(150, 600, 795, 600)
          text=inv_txt.get('1.0',END)
          wraped_text="\n".join(wrap(text,130))
    
        
          lbx_inv=Label(inv_pro1_canvas,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
          win_inv2 = inv_pro1_canvas.create_window(150, 603,anchor="nw", window=lbx_inv)

          inv_pro1_canvas.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    

          inv_pro1_canvas.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
        else:
          frame_pro1 = Frame(Invoice_setting_frame_cpy, width=953, height=300)
          frame_pro1.pack(expand=True, fill=BOTH)
          frame_pro1.place(x=247,y=90)
          inv_pro1_canvas=Canvas(frame_pro1, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(frame_pro1, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=inv_pro1_canvas.yview)
          
          inv_pro1_canvas.config(width=953,height=300)
          inv_pro1_canvas.config(yscrollcommand=vertibar.set)
          inv_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          inv_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          inv_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          
          inv_pro1_canvas.create_text(195, 150, text="Invoice#", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(205, 170, text="Invoicedate", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(205, 230, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(350, 150, text="INV1/2022", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(350, 170, text="03-05-2022", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(350, 190, text="18-05-2022", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))   
          
          inv_pro1_canvas.create_text(720, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))

          inv_pro1_canvas.create_text(750, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(750, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(750, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(750, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(745, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(745, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(750, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))
          inv_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
          inv_pro1_canvas.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
          inv_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          inv_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          inv_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          inv_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
          s = ttk.Style()
          s.configure('Treeview.Heading', background=''+ invset_bg_var.get(),State='DISABLE')

          tree=ttk.Treeview(inv_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')

          tree.column("# 1", anchor=E, stretch=NO, width=100)
          tree.heading("# 1", text="ID/SKU")
          tree.column("# 2", anchor=E, stretch=NO, width=350)
          tree.heading("# 2", text="Product/Service - Description")
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text="Quantity")
          tree.column("# 4", anchor=E, stretch=NO, width=90)
          tree.heading("# 4", text="Unit Price")
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text="Price")
          
          window = inv_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)

          inv_pro1_canvas.create_line(120, 390, 820, 390 )
          inv_pro1_canvas.create_line(120, 340, 120, 365 )
          inv_pro1_canvas.create_line(120, 365, 120, 390 )
          inv_pro1_canvas.create_line(820, 340, 820, 540 )
          inv_pro1_canvas.create_line(740, 340, 740, 540 )
          inv_pro1_canvas.create_line(570, 340, 570, 540 )
          inv_pro1_canvas.create_line(570, 415, 820, 415 )
          inv_pro1_canvas.create_line(570, 440, 820, 440 )
          inv_pro1_canvas.create_line(570, 465, 820, 465 )
          inv_pro1_canvas.create_line(570, 490, 820, 490 )
          inv_pro1_canvas.create_line(570, 515, 820, 515 )
          inv_pro1_canvas.create_line(650, 340, 650, 390 )
          inv_pro1_canvas.create_line(220, 340, 220, 390 )
          inv_pro1_canvas.create_line(570, 540, 820, 540 )

          inv_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(610, 372, text="0", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(710, 372, text="0", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(790, 372, text="0", fill="black", font=('Helvetica 10'))

          inv_pro1_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(790, 404, text="0", fill="black", font=('Helvetica 10'))

          inv_pro1_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(792, 428, text="0", fill="black", font=('Helvetica 10'))

          inv_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(792, 454, text="0", fill="black", font=('Helvetica 10'))

          inv_pro1_canvas.create_text(790, 479, text="0", fill="black", font=('Helvetica 10 bold'))
          inv_pro1_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

          inv_pro1_canvas.create_text(790, 502, text="0", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

          inv_pro1_canvas.create_text(790, 526, text="0", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

          inv_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
          inv_pro1_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_line(150, 620, 795, 620)
          

          inv_pro1_canvas.create_text(280, 640, text= "", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
        

    #----------------Professional 2 (logo on right side)------------------
      elif menuvar_lst == 'Professional 2 (logo on right side)':
        if cmpy_dtl[1] is not None:
          sql='select dateformat from company'
          fbcursor.execute(sql)
          date_frmat=fbcursor.fetchone()
          
          if not date_frmat:
            ft_fr='%Y-%m-%d'
        
          elif date_frmat[0]=="mm-dd-yyyy":
            ft_fr='%m-%d-%Y'

          elif date_frmat[0]=="dd-mm-yyyy":
              ft_fr='%d-%m-%Y'
                      
          elif date_frmat[0]=="yyy.mm.dd":
              ft_fr='%Y.%m.%d'
                          
          elif date_frmat[0]=="mm/dd/yyyy":
              ft_fr='%m/%d/%Y'
                          
          elif date_frmat[0]=="dd/mm/yyyy":
              ft_fr='%d/%m/%Y'
                                  
          elif date_frmat[0]=="dd.mm.yyyy":
              ft_fr='%d.%m.%Y'
                                  
          elif date_frmat[0]=="yyyy/  mm/dd":
              ft_fr='%Y/%m/%d'

          else:
              ft_fr='%Y-%m-%d'
          td_date=date.today()
          date_tdy=td_date.strftime(ft_fr)  
          frame_inv_pro2 = Frame(Invoice_setting_frame_cpy, width=953, height=300)
          frame_inv_pro2.pack(expand=True, fill=BOTH)
          frame_inv_pro2.place(x=247,y=90)
          
          canvas_pro2=Canvas(frame_inv_pro2, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(frame_inv_pro2, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas_pro2.yview)
          canvas_pro2.config(width=953,height=300)
          
          canvas_pro2.config(yscrollcommand=vertibar.set)
          canvas_pro2.pack(expand=True,side=LEFT,fill=BOTH)
          canvas_pro2.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          canvas_pro2.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            inv_image = Image.open("images/"+cmpy_dtl[13])
            inv_resize_image = inv_image.resize((200,75))
            inv_image = ImageTk.PhotoImage(inv_resize_image)
          
            inv_logo = Label(canvas_pro2,width=200,height=75, bg="white",image = inv_image) 
            inv_window_image = canvas_pro2.create_window(800, 60, anchor="ne", window=inv_logo)
            inv_logo.photo = inv_image
          except:
            canvas_pro2.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          labelcmp=Label(canvas_pro2,text=cmpy_dtl[1],justify=LEFT, bg="white",anchor="nw",font=("Helvetica", 12), width=40, height=1)
          window = canvas_pro2.create_window(150,80, anchor="nw", window=labelcmp)

          labelcmpl=Label(canvas_pro2,text=cmpy_dtl[2],justify=LEFT, bg="white",font=("Helvetica", 9),anchor="nw", width=40, height=4)
          windowl = canvas_pro2.create_window(155 ,110, anchor="nw", window=labelcmpl)
          
          lb_inv1=Label(canvas_pro2,text=inv_lst_bx2.get(1.0, END), bg="white",anchor="ne",font=("Helvetica", 11),height=1)#Invoice#
          win_inv1 = canvas_pro2.create_window(550, 140, anchor="nw", window=lb_inv1)

          lb_inv1=Label(canvas_pro2,text=inv_lst_bx3.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", 11),height=1 )#Invoicedate
          win_inv1 = canvas_pro2.create_window(550, 160, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(canvas_pro2,text="Due Date", bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Due date
          win_inv1 = canvas_pro2.create_window(550, 180, anchor="nw", window=lb_inv1)

          lb_inv1=Label(canvas_pro2,text=inv_lst_bx5.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", 11),height=1)#Terms
          win_inv1 = canvas_pro2.create_window(550, 200, anchor="nw", window=lb_inv1)

          lb_inv1=Label(canvas_pro2,text=inv_lst_bx4.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = canvas_pro2.create_window(550, 220, anchor="nw", window=lb_inv1)

          canvas_pro2.create_text(210, 185, text=cmpy_dtl[4],justify=LEFT, fill="black", font=('Helvetica 9'))
        
          lb_inv1=Label(canvas_pro2,text=str(inv_tp_lf.get())+"1/2022", bg="white",justify=LEFT,font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = canvas_pro2.create_window(790, 140, anchor="ne", window=lb_inv1)
          canvas_pro2.create_text(750, 170, text=date_tdy, fill="black", font=('Helvetica 11'))
          canvas_pro2.create_text(750, 190, text=date_tdy, fill="black", font=('Helvetica 11'))
          canvas_pro2.create_text(740, 210, text="NET 15", fill="black", font=('Helvetica 11'))  
            

          # lb_inv1=Label(canvas_pro2,text=inv_lst_bx1.get(1.0,END), bg="white",anchor="e",font=('Helvetica 14 bold'),height=2)#invoice
          # win_inv1 = canvas_pro2.create_window(155, 200, anchor="nw", window=lb_inv1)
          lb_inv1=Label(canvas_pro2,text=inv_lst_bx1.get(1.0,END), bg="white",anchor="ne",font=('Helvetica 14 bold'),height=1)#invoice
          win_inv1 = canvas_pro2.create_window(155, 200, anchor="nw", window=lb_inv1)


          lb_inv1=Label(canvas_pro2,text=inv_lst_bx6.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline" ),height=1)#Invoice to
          win_inv1 = canvas_pro2.create_window(175, 250, anchor="nw", window=lb_inv1)

          lb_inv1=Label(canvas_pro2,text=inv_lst_bx7.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline"),height=1)#Ship to
          win_inv1 = canvas_pro2.create_window(525, 250, anchor="nw", window=lb_inv1)

        
          canvas_pro2.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas_pro2.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))

          canvas_pro2.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas_pro2.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

          fgth = ttk.Style()
          fgth.configure('mystyle102.Treeview.Heading', background=''+ invset_bg_var.get(),State='DISABLE')

          tree=ttk.Treeview(canvas_pro2, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle102.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=100)
          tree.heading("# 1", text=inv_lst_bx8.get(1.0,END))
          tree.column("# 2", anchor=E, stretch=NO, width=350)
          tree.heading("# 2", text=inv_lst_bx9.get(1.0,END))
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text=inv_lst_bx10.get(1.0,END))
          tree.column("# 4", anchor=E, stretch=NO, width=90)
          tree.heading("# 4", text=inv_lst_bx13.get(1.0,END))
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text="Price")
          
          window = canvas_pro2.create_window(120, 340, anchor="nw", window=tree)

          canvas_pro2.create_line(120, 390, 820, 390 )
          canvas_pro2.create_line(120, 340, 120, 365 )
          canvas_pro2.create_line(120, 365, 120, 390 )
          canvas_pro2.create_line(820, 340, 820, 540 )
          canvas_pro2.create_line(740, 340, 740, 540 )
          canvas_pro2.create_line(570, 340, 570, 540 )
          canvas_pro2.create_line(570, 415, 820, 415 )
          canvas_pro2.create_line(570, 440, 820, 440 )
          canvas_pro2.create_line(570, 465, 820, 465 )
          canvas_pro2.create_line(570, 490, 820, 490 )
          canvas_pro2.create_line(570, 515, 820, 515 )
          canvas_pro2.create_line(650, 340, 650, 390 )
          canvas_pro2.create_line(220, 340, 220, 390 )
          canvas_pro2.create_line(570, 540, 820, 540 )

          sqlr= 'select currencysign from company'
          fbcursor.execute(sqlr)
          crncy=fbcursor.fetchone()
          crcy_type=crncy[0]
          sqlrt= 'select currsignplace from company'
          fbcursor.execute(sqlrt)
          post_rp=fbcursor.fetchone()
          cry_plcy=post_rp[0]
          if cry_plcy=="before amount": 
            canvas_pro2.create_text(710, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 404, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(792, 428, text=str(crcy_type)+"18.00", fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 502, text=str(crcy_type)+"100.00", fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 526, text=str(crcy_type)+"138.00", fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(792, 454, text=str(crcy_type)+"20.00", fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 479, text=str(crcy_type)+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount":
            canvas_pro2.create_text(710, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 404, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(792, 428, text="18.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 502, text="100.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 526, text="138.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(792, 454, text="20.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 479, text="238.00"+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="before amount with space": 
            canvas_pro2.create_text(710, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 404, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(792, 428, text=str(crcy_type)+" "+"18.00", fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 502, text=str(crcy_type)+" "+"100.00", fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 526, text=str(crcy_type)+" "+"138.00", fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(792, 454, text=str(crcy_type)+" "+"20.00", fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 479, text=str(crcy_type)+" "+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount with space":
            canvas_pro2.create_text(710, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 404, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(792, 428, text="18.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 502, text="100.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 526, text="138.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(792, 454, text="20.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            canvas_pro2.create_text(790, 479, text="238.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          else:
            pass


          canvas_pro2.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
          

          lbx_inv=Label(canvas_pro2,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
          win_inv2 = canvas_pro2.create_window(630,392, anchor="nw", window=lbx_inv)

          lbx_inv=Label(canvas_pro2,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
          win_inv2 = canvas_pro2.create_window(635,418, anchor="nw", window=lbx_inv)

          lbx_inv=Label(canvas_pro2,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
          win_inv2 = canvas_pro2.create_window(630, 492,anchor="nw", window=lbx_inv)

          lbx_inv=Label(canvas_pro2,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
          win_inv2 = canvas_pro2.create_window(635, 518, anchor="nw", window=lbx_inv)
            

        
          canvas_pro2.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

          lbx_inv=Label(canvas_pro2,text=inv_lst_bx18.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#Order Total"
          win_inv2 = canvas_pro2.create_window(625, 468, anchor="nw", window=lbx_inv)
          lbx_inv=Label(canvas_pro2,text=inv_lst_bx21.get(1.0,END), bg="white",anchor="n",font=("Helvetica 10 "),height=1)#"Terms and Conditions"
          win_inv2 = canvas_pro2.create_window(420, 570, anchor="nw", window=lbx_inv)
        
          canvas_pro2.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        

          canvas_pro2.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
          
          canvas_pro2.create_line(150, 600, 795, 600)
          text=inv_txt.get('1.0',END)
          wraped_text="\n".join(wrap(text,130))
    
        
          lbx_inv=Label(canvas_pro2,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
          win_inv2 = canvas_pro2.create_window(150, 603,anchor="nw", window=lbx_inv)

          canvas_pro2.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    

          canvas_pro2.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
        else:

          frame_inv_pro2 = Frame(Invoice_setting_frame_cpy, width=953, height=300)
          frame_inv_pro2.pack(expand=True, fill=BOTH)
          frame_inv_pro2.place(x=247,y=90)
          
          canvas_pro2=Canvas(frame_inv_pro2, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(frame_inv_pro2, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas_pro2.yview)
          canvas_pro2.config(width=953,height=300)
          
          canvas_pro2.config(yscrollcommand=vertibar.set)
          canvas_pro2.pack(expand=True,side=LEFT,fill=BOTH)
          canvas_pro2.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          canvas_pro2.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          
          canvas_pro2.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          
          canvas_pro2.create_text(250, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
          canvas_pro2.create_text(225, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(225, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(225, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(225, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(234, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(234, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(225, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))
          canvas_pro2.create_text(232, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
          canvas_pro2.create_text(502, 150, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas_pro2.create_text(515, 170, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas_pro2.create_text(500, 190, text="Due date", fill="black", font=('Helvetica 11'))
          canvas_pro2.create_text(491, 210, text="Terms", fill="black", font=('Helvetica 11'))
          canvas_pro2.create_text(505, 230, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
          canvas_pro2.create_text(680, 150, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas_pro2.create_text(680, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
          canvas_pro2.create_text(680, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
          canvas_pro2.create_text(670, 210, text="NET 15", fill="black", font=('Helvetica 11'))  
            
          canvas_pro2.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
          canvas_pro2.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas_pro2.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas_pro2.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas_pro2.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

          tree=ttk.Treeview(canvas_pro2, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=100)
          tree.heading("# 1", text="ID/SKU")
          tree.column("# 2", anchor=E, stretch=NO, width=350)
          tree.heading("# 2", text="Product/Service - Description")
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text="Quantity")
          tree.column("# 4", anchor=E, stretch=NO, width=90)
          tree.heading("# 4", text="Unit Price")
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text="Price")
          
          window = canvas_pro2.create_window(120, 340, anchor="nw", window=tree)

          canvas_pro2.create_line(120, 390, 820, 390 )
          canvas_pro2.create_line(120, 340, 120, 365 )
          canvas_pro2.create_line(120, 365, 120, 390 )
          canvas_pro2.create_line(820, 340, 820, 540 )
          canvas_pro2.create_line(740, 340, 740, 540 )
          canvas_pro2.create_line(570, 340, 570, 540 )
          canvas_pro2.create_line(570, 415, 820, 415 )
          canvas_pro2.create_line(570, 440, 820, 440 )
          canvas_pro2.create_line(570, 465, 820, 465 )
          canvas_pro2.create_line(570, 490, 820, 490 )
          canvas_pro2.create_line(570, 515, 820, 515 )
          canvas_pro2.create_line(650, 340, 650, 390 )
          canvas_pro2.create_line(220, 340, 220, 390 )
          canvas_pro2.create_line(570, 540, 820, 540 )

          canvas_pro2.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas_pro2.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas_pro2.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

          canvas_pro2.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

          canvas_pro2.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          canvas_pro2.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

          canvas_pro2.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

          canvas_pro2.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

          canvas_pro2.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

          canvas_pro2.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_line(150, 620, 795, 620)
          canvas_pro2.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas_pro2.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


    #----------------Simplified 1 (logo on left side)------------------ 
      elif menuvar_lst == 'Simplified 1 (logo on left side)':
        if cmpy_dtl[1] is not None:
          sql='select dateformat from company'
          fbcursor.execute(sql)
          date_frmat=fbcursor.fetchone()
          
          if not date_frmat:
            ft_fr='%Y-%m-%d'
        
          elif date_frmat[0]=="mm-dd-yyyy":
            ft_fr='%m-%d-%Y'

          elif date_frmat[0]=="dd-mm-yyyy":
              ft_fr='%d-%m-%Y'
                      
          elif date_frmat[0]=="yyy.mm.dd":
              ft_fr='%Y.%m.%d'
                          
          elif date_frmat[0]=="mm/dd/yyyy":
              ft_fr='%m/%d/%Y'
                          
          elif date_frmat[0]=="dd/mm/yyyy":
              ft_fr='%d/%m/%Y'
                                  
          elif date_frmat[0]=="dd.mm.yyyy":
              ft_fr='%d.%m.%Y'
                                  
          elif date_frmat[0]=="yyyy/  mm/dd":
              ft_fr='%Y/%m/%d'

          else:
              ft_fr='%Y-%m-%d'
          td_date=date.today()
          date_tdy=td_date.strftime(ft_fr)
          smply_frame = Frame(Invoice_setting_frame_cpy, width=953, height=300)
          smply_frame.pack(expand=True, fill=BOTH)
          smply_frame.place(x=247,y=90)
          inv_smply_canvas=Canvas(smply_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(smply_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=inv_smply_canvas.yview)
          inv_smply_canvas.config(width=953,height=300)

          inv_smply_canvas.config(yscrollcommand=vertibar.set)
          inv_smply_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          inv_smply_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          inv_smply_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            inv_image = Image.open("images/"+cmpy_dtl[13])
            inv_resize_image = inv_image.resize((200,75))
            inv_image = ImageTk.PhotoImage(inv_resize_image)
          
            inv_logo = Label(inv_smply_canvas,width=200,height=75, bg="white",image = inv_image) 
            inv_window_image = inv_smply_canvas.create_window(150, 50, anchor="nw", window=inv_logo)
            inv_logo.photo = inv_image
          except:
            inv_smply_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          lb_inv1=Label(inv_smply_canvas,text=inv_lst_bx2.get(1.0, END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Invoice#
          win_inv1 = inv_smply_canvas.create_window(175, 140, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_smply_canvas,text=inv_lst_bx3.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1 )#Invoicedate
          win_inv1 = inv_smply_canvas.create_window(175, 160, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(inv_smply_canvas,text="Due Date", bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Due date
          win_inv1 = inv_smply_canvas.create_window(175, 180, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_smply_canvas,text=inv_lst_bx5.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Terms
          win_inv1 = inv_smply_canvas.create_window(175, 200, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_smply_canvas,text=inv_lst_bx4.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = inv_smply_canvas.create_window(175, 220, anchor="nw", window=lb_inv1)

          win_inv1 = inv_smply_canvas.create_window(175, 220, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_smply_canvas,text=str(inv_tp_lf.get())+"1/2022", bg="white",anchor="nw",font=("Helvetica", ),height=1)
          win_inv1 = inv_smply_canvas.create_window(310, 140, anchor="nw", window=lb_inv1)
          inv_smply_canvas.create_text(350, 170, text=date_tdy, fill="black", font=('Helvetica 11'))
          inv_smply_canvas.create_text(350, 190, text=date_tdy, fill="black", font=('Helvetica 11'))
          inv_smply_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

          labelcmp=Label(inv_smply_canvas,text=cmpy_dtl[1], bg="white",anchor="e",font=("Helvetica", 12), width=40, height=1)
          window = inv_smply_canvas.create_window(430,80, anchor="nw", window=labelcmp)

          labelcmpl=Label(inv_smply_canvas,text=cmpy_dtl[2],justify=RIGHT, bg="white",font=("Helvetica", 9),anchor="ne", width=50, height=4)
          windowl = inv_smply_canvas.create_window(440,110, anchor="nw", window=labelcmpl)

          
          inv_smply_canvas.create_text(745, 185, text=cmpy_dtl[4], fill="black", font=('Helvetica 9'))

          lb_inv1=Label(inv_smply_canvas,text=inv_lst_bx1.get(1.0,END), bg="white",anchor="ne",font=('Helvetica 14 bold'),height=1)#invoice
          win_inv1 = inv_smply_canvas.create_window(800, 200, anchor="ne", window=lb_inv1)

          

          lb_inv1=Label(inv_smply_canvas,text=inv_lst_bx6.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline" ),height=1)#Invoice to
          win_inv1 = inv_smply_canvas.create_window(175, 250, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_smply_canvas,text=inv_lst_bx7.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline"),height=1)#Ship to
          win_inv1 = inv_smply_canvas.create_window(525, 250, anchor="nw", window=lb_inv1)

          # inv_smply_canvas.create_text(765, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          
          # inv_smply_canvas.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
          inv_smply_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          inv_smply_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
          # inv_smply_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          inv_smply_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          inv_smply_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
          fgth = ttk.Style()
          fgth.configure('mystyle103.Treeview.Heading', background=''+ invset_bg_var.get(),State='DISABLE')
          tree=ttk.Treeview(inv_smply_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle103.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=530)
          tree.heading("# 1", text=inv_lst_bx9.get(1.0,END))
          tree.column("# 2", anchor=E, stretch=NO, width=90)
          tree.heading("# 2", text=inv_lst_bx10.get(1.0,END))
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text=inv_lst_bx13.get(1.0,END))
          
          window = inv_smply_canvas.create_window(120, 340, anchor="nw", window=tree)

          inv_smply_canvas.create_line(120, 390, 820, 390 )
          inv_smply_canvas.create_line(120, 340, 120, 365 )
          inv_smply_canvas.create_line(120, 365, 120, 390 )
          inv_smply_canvas.create_line(820, 340, 820, 540 )
          inv_smply_canvas.create_line(740, 340, 740, 540 )
          inv_smply_canvas.create_line(570, 390, 570, 540 )
          inv_smply_canvas.create_line(570, 415, 820, 415 )
          inv_smply_canvas.create_line(570, 440, 820, 440 )
          inv_smply_canvas.create_line(570, 465, 820, 465 )
          inv_smply_canvas.create_line(570, 490, 820, 490 )
          inv_smply_canvas.create_line(570, 515, 820, 515 )
          inv_smply_canvas.create_line(650, 340, 650, 390 )
          inv_smply_canvas.create_line(570, 540, 820, 540 )
          sqlr= 'select currencysign from company'
          fbcursor.execute(sqlr)
          crncy=fbcursor.fetchone()
          crcy_type=crncy[0]
          sqlrt= 'select currsignplace from company'
          fbcursor.execute(sqlrt)
          post_rp=fbcursor.fetchone()
          cry_plcy=post_rp[0]
          if cry_plcy=="before amount": 
            inv_smply_canvas.create_text(710, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 404, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(792, 428, text=str(crcy_type)+"18.00", fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 502, text=str(crcy_type)+"100.00", fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 526, text=str(crcy_type)+"138.00", fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(792, 454, text=str(crcy_type)+"20.00", fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 479, text=str(crcy_type)+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount":
            inv_smply_canvas.create_text(710, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 404, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(792, 428, text="18.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 502, text="100.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 526, text="138.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(792, 454, text="20.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 479, text="238.00"+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="before amount with space": 
            inv_smply_canvas.create_text(710, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 404, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(792, 428, text=str(crcy_type)+" "+"18.00", fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 502, text=str(crcy_type)+" "+"100.00", fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 526, text=str(crcy_type)+" "+"138.00", fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(792, 454, text=str(crcy_type)+" "+"20.00", fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 479, text=str(crcy_type)+" "+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount with space":
            inv_smply_canvas.create_text(710, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 404, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(792, 428, text="18.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 502, text="100.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 526, text="138.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(792, 454, text="20.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_smply_canvas.create_text(790, 479, text="238.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          else:
            pass
            

          
          inv_smply_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))


          lbx_inv=Label(inv_smply_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
          win_inv2 = inv_smply_canvas.create_window(630,392, anchor="nw", window=lbx_inv)

          lbx_inv=Label(inv_smply_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
          win_inv2 = inv_smply_canvas.create_window(635,418, anchor="nw", window=lbx_inv)

          lbx_inv=Label(inv_smply_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
          win_inv2 = inv_smply_canvas.create_window(630, 492,anchor="nw", window=lbx_inv)

          lbx_inv=Label(inv_smply_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
          win_inv2 = inv_smply_canvas.create_window(635, 518, anchor="nw", window=lbx_inv)
            

        
        
          inv_smply_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

          lbx_inv=Label(inv_smply_canvas,text=inv_lst_bx18.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#Order Total"
          win_inv2 = inv_smply_canvas.create_window(625, 468, anchor="nw", window=lbx_inv)
          lbx_inv=Label(inv_smply_canvas,text=inv_lst_bx21.get(1.0,END), bg="white",anchor="n",font=("Helvetica 10 "),height=1)#"Terms and Conditions"
          win_inv2 = inv_smply_canvas.create_window(420, 570, anchor="nw", window=lbx_inv)

          inv_smply_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
    
          inv_smply_canvas.create_line(150, 600, 795, 600)
          text=inv_txt.get('1.0',END)
          wraped_text="\n".join(wrap(text,130))
    
        
          lbx_inv=Label(inv_smply_canvas,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
          win_inv2 = inv_smply_canvas.create_window(150, 603,anchor="nw", window=lbx_inv)

          inv_smply_canvas.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    

          inv_smply_canvas.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
        else:
          smply_frame = Frame(Invoice_setting_frame_cpy, width=953, height=300)
          smply_frame.pack(expand=True, fill=BOTH)
          smply_frame.place(x=247,y=90)
          inv_smply_canvas=Canvas(smply_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(smply_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=inv_smply_canvas.yview)
          inv_smply_canvas.config(width=953,height=300)

          inv_smply_canvas.config(yscrollcommand=vertibar.set)
          inv_smply_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          inv_smply_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          inv_smply_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          inv_smply_canvas.create_text(202, 150, text="Invoice#", fill="black", font=('Helvetica 11'))
          inv_smply_canvas.create_text(215, 170, text="Invoice date", fill="black", font=('Helvetica 11'))
          inv_smply_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
          inv_smply_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
          inv_smply_canvas.create_text(205, 230, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
          inv_smply_canvas.create_text(350, 150, text="INV1/2022", fill="black", font=('Helvetica 11'))
          inv_smply_canvas.create_text(350, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
          inv_smply_canvas.create_text(350, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
          inv_smply_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

          inv_smply_canvas.create_text(720, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
          inv_smply_canvas.create_text(750, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(750, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(750, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(750, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(745, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(745, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(750, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))
          
          inv_smply_canvas.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
          inv_smply_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          inv_smply_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          inv_smply_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          inv_smply_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

          tree=ttk.Treeview(inv_smply_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=530)
          tree.heading("# 1", text="Product/Service - Description")
          tree.column("# 2", anchor=E, stretch=NO, width=90)
          tree.heading("# 2", text="Quantity")
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text="Price")
          
          window = inv_smply_canvas.create_window(120, 340, anchor="nw", window=tree)

          inv_smply_canvas.create_line(120, 390, 820, 390 )
          inv_smply_canvas.create_line(120, 340, 120, 365 )
          inv_smply_canvas.create_line(120, 365, 120, 390 )
          inv_smply_canvas.create_line(820, 340, 820, 540 )
          inv_smply_canvas.create_line(740, 340, 740, 540 )
          inv_smply_canvas.create_line(570, 390, 570, 540 )
          inv_smply_canvas.create_line(570, 415, 820, 415 )
          inv_smply_canvas.create_line(570, 440, 820, 440 )
          inv_smply_canvas.create_line(570, 465, 820, 465 )
          inv_smply_canvas.create_line(570, 490, 820, 490 )
          inv_smply_canvas.create_line(570, 515, 820, 515 )
          inv_smply_canvas.create_line(650, 340, 650, 390 )
          inv_smply_canvas.create_line(570, 540, 820, 540 )

          
          inv_smply_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

          inv_smply_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

          inv_smply_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

          inv_smply_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

          inv_smply_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          inv_smply_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

          inv_smply_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

          inv_smply_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

          inv_smply_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

          inv_smply_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_line(150, 620, 795, 620)
          inv_smply_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          inv_smply_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

    #----------------Simplified 2 (logo on right side)------------------ 
      elif menuvar_lst == 'Simplified 2 (logo on right side)': 
        if cmpy_dtl[1] is not None:
          sql='select dateformat from company'
          fbcursor.execute(sql)
          date_frmat=fbcursor.fetchone()
          
          if not date_frmat:
            ft_fr='%Y-%m-%d'
        
          elif date_frmat[0]=="mm-dd-yyyy":
            ft_fr='%m-%d-%Y'

          elif date_frmat[0]=="dd-mm-yyyy":
              ft_fr='%d-%m-%Y'
                      
          elif date_frmat[0]=="yyy.mm.dd":
              ft_fr='%Y.%m.%d'
                          
          elif date_frmat[0]=="mm/dd/yyyy":
              ft_fr='%m/%d/%Y'
                          
          elif date_frmat[0]=="dd/mm/yyyy":
              ft_fr='%d/%m/%Y'
                                  
          elif date_frmat[0]=="dd.mm.yyyy":
              ft_fr='%d.%m.%Y'
                                  
          elif date_frmat[0]=="yyyy/  mm/dd":
              ft_fr='%Y/%m/%d'

          else:
              ft_fr='%Y-%m-%d'
          td_date=date.today()
          date_tdy=td_date.strftime(ft_fr)
          smply2_frame = Frame(Invoice_setting_frame_cpy, width=953, height=300)
          smply2_frame.pack(expand=True, fill=BOTH)
          smply2_frame.place(x=247,y=90)

          smply2_canvas=Canvas(smply2_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(smply2_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=smply2_canvas.yview)
          smply2_canvas.config(width=953,height=300)

          smply2_canvas.config(yscrollcommand=vertibar.set)
          smply2_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          smply2_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          smply2_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            inv_image = Image.open("images/"+cmpy_dtl[13])
            inv_resize_image = inv_image.resize((200,75))
            inv_image = ImageTk.PhotoImage(inv_resize_image)
          
            inv_logo = Label(smply2_canvas,width=200,height=75, bg="white",image = inv_image) 
            inv_window_image = smply2_canvas.create_window(800, 60, anchor="ne", window=inv_logo)
            inv_logo.photo = inv_image
          except:
            smply2_canvas.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          labelcmp=Label(smply2_canvas,text=cmpy_dtl[1],justify=LEFT, bg="white",anchor="nw",font=("Helvetica", 12), width=40, height=1)
          window = smply2_canvas.create_window(150,80, anchor="nw", window=labelcmp)

          labelcmpl=Label(smply2_canvas,text=cmpy_dtl[2],justify=LEFT, bg="white",font=("Helvetica", 9),anchor="nw", width=40, height=4)
          windowl = smply2_canvas.create_window(155 ,110, anchor="nw", window=labelcmpl)
          
          lb_inv1=Label(smply2_canvas,text=inv_lst_bx2.get(1.0, END), bg="white",anchor="ne",font=("Helvetica", 11),height=1)#Invoice#
          win_inv1 = smply2_canvas.create_window(550, 140, anchor="nw", window=lb_inv1)

          lb_inv1=Label(smply2_canvas,text=inv_lst_bx3.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", 11),height=1 )#Invoicedate
          win_inv1 = smply2_canvas.create_window(550, 160, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(smply2_canvas,text="Due Date", bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Due date
          win_inv1 = smply2_canvas.create_window(550, 180, anchor="nw", window=lb_inv1)

          lb_inv1=Label(smply2_canvas,text=inv_lst_bx5.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", 11),height=1)#Terms
          win_inv1 = smply2_canvas.create_window(550, 200, anchor="nw", window=lb_inv1)

          lb_inv1=Label(smply2_canvas,text=inv_lst_bx4.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = smply2_canvas.create_window(550, 220, anchor="nw", window=lb_inv1)

          smply2_canvas.create_text(210, 185, text=cmpy_dtl[4],justify=LEFT, fill="black", font=('Helvetica 9'))
          lb_inv1=Label(smply2_canvas,text=inv_lst_bx1.get(1.0,END), bg="white",anchor="ne",font=('Helvetica 14 bold'),height=1)#invoice
          win_inv1 = smply2_canvas.create_window(155, 200, anchor="nw", window=lb_inv1)


          lb_inv1=Label(smply2_canvas,text=inv_lst_bx6.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline" ),height=1)#Invoice to
          win_inv1 = smply2_canvas.create_window(175, 250, anchor="nw", window=lb_inv1)

          lb_inv1=Label(smply2_canvas,text=inv_lst_bx7.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline"),height=1)#Ship to
          win_inv1 = smply2_canvas.create_window(525, 250, anchor="nw", window=lb_inv1)
    
          lb_inv1=Label(smply2_canvas,text=str(inv_tp_lf.get())+"1/2022", bg="white",justify=LEFT,font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = smply2_canvas.create_window(790, 140, anchor="ne", window=lb_inv1)

          smply2_canvas.create_text(750, 170, text=date_tdy, fill="black", font=('Helvetica 11'))
          smply2_canvas.create_text(750, 190, text=date_tdy, fill="black", font=('Helvetica 11'))
          smply2_canvas.create_text(740, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

        
          smply2_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          smply2_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))

          smply2_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          smply2_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

          fgth = ttk.Style()
          fgth.configure('mystyle104.Treeview.Heading', background=''+ invset_bg_var.get(),State='DISABLE')
          tree=ttk.Treeview(smply2_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle104.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=530)
          tree.heading("# 1", text=inv_lst_bx9.get(1.0,END))
          tree.column("# 2", anchor=E, stretch=NO, width=90)
          tree.heading("# 2", text=inv_lst_bx10.get(1.0,END))
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text=inv_lst_bx13.get(1.0,END))
          
          window = smply2_canvas.create_window(120, 340, anchor="nw", window=tree)

          smply2_canvas.create_line(120, 390, 820, 390 )
          smply2_canvas.create_line(120, 340, 120, 365 )
          smply2_canvas.create_line(120, 365, 120, 390 )
          smply2_canvas.create_line(820, 340, 820, 540 )
          smply2_canvas.create_line(740, 340, 740, 540 )
          smply2_canvas.create_line(570, 390, 570, 540 )
          smply2_canvas.create_line(570, 415, 820, 415 )
          smply2_canvas.create_line(570, 440, 820, 440 )
          smply2_canvas.create_line(570, 465, 820, 465 )
          smply2_canvas.create_line(570, 490, 820, 490 )
          smply2_canvas.create_line(570, 515, 820, 515 )
          smply2_canvas.create_line(650, 340, 650, 390 )
          smply2_canvas.create_line(570, 540, 820, 540 )

          sqlr= 'select currencysign from company'
          fbcursor.execute(sqlr)
          crncy=fbcursor.fetchone()
          crcy_type=crncy[0]
          sqlrt= 'select currsignplace from company'
          fbcursor.execute(sqlrt)
          post_rp=fbcursor.fetchone()
          cry_plcy=post_rp[0]
          if cry_plcy=="before amount": 
            smply2_canvas.create_text(710, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 404, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(792, 428, text=str(crcy_type)+"18.00", fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 502, text=str(crcy_type)+"100.00", fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 526, text=str(crcy_type)+"138.00", fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(792, 454, text=str(crcy_type)+"20.00", fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 479, text=str(crcy_type)+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount":
            smply2_canvas.create_text(710, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 404, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(792, 428, text="18.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 502, text="100.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 526, text="138.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(792, 454, text="20.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 479, text="238.00"+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="before amount with space": 
            smply2_canvas.create_text(710, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 404, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(792, 428, text=str(crcy_type)+" "+"18.00", fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 502, text=str(crcy_type)+" "+"100.00", fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 526, text=str(crcy_type)+" "+"138.00", fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(792, 454, text=str(crcy_type)+" "+"20.00", fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 479, text=str(crcy_type)+" "+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount with space":
            smply2_canvas.create_text(710, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 404, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(792, 428, text="18.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 502, text="100.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 526, text="138.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(792, 454, text="20.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            smply2_canvas.create_text(790, 479, text="238.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          else:
            pass
          
          smply2_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))
          

          lbx_inv=Label(smply2_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
          win_inv2 = smply2_canvas.create_window(630,392, anchor="nw", window=lbx_inv)

          lbx_inv=Label(smply2_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
          win_inv2 = smply2_canvas.create_window(635,418, anchor="nw", window=lbx_inv)

          lbx_inv=Label(smply2_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
          win_inv2 = smply2_canvas.create_window(630, 492,anchor="nw", window=lbx_inv)

          lbx_inv=Label(smply2_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
          win_inv2 = smply2_canvas.create_window(635, 518, anchor="nw", window=lbx_inv)
            

        

          smply2_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        
          lbx_inv=Label(smply2_canvas,text=inv_lst_bx18.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#Order Total"
          win_inv2 = smply2_canvas.create_window(625, 468, anchor="nw", window=lbx_inv)
          lbx_inv=Label(smply2_canvas,text=inv_lst_bx21.get(1.0,END), bg="white",anchor="n",font=("Helvetica 10 "),height=1)#"Terms and Conditions"
          win_inv2 = smply2_canvas.create_window(420, 570, anchor="nw", window=lbx_inv)


          smply2_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
      
          smply2_canvas.create_line(150, 600, 795, 600)
          text=inv_txt.get('1.0',END)
          wraped_text="\n".join(wrap(text,130))
    
        
          lbx_inv=Label(smply2_canvas,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
          win_inv2 = smply2_canvas.create_window(150, 603,anchor="nw", window=lbx_inv)

          smply2_canvas.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    

          smply2_canvas.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
        else:
          smply2_frame = Frame(Invoice_setting_frame_cpy, width=953, height=300)
          smply2_frame.pack(expand=True, fill=BOTH)
          smply2_frame.place(x=247,y=90)

          smply2_canvas=Canvas(smply2_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(smply2_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=smply2_canvas.yview)
          smply2_canvas.config(width=953,height=300)

          smply2_canvas.config(yscrollcommand=vertibar.set)
          smply2_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          smply2_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          smply2_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          smply2_canvas.create_text(250, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
          smply2_canvas.create_text(225, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(225, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(225, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(225, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(234, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(234, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(225, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          smply2_canvas.create_text(502, 150, text="Invoice#", fill="black", font=('Helvetica 11'))
          smply2_canvas.create_text(515, 170, text="Invoice date", fill="black", font=('Helvetica 11'))
          smply2_canvas.create_text(500, 190, text="Due date", fill="black", font=('Helvetica 11'))
          smply2_canvas.create_text(491, 210, text="Terms", fill="black", font=('Helvetica 11'))
          smply2_canvas.create_text(505, 230, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
          smply2_canvas.create_text(680, 150, text="INV1/2022", fill="black", font=('Helvetica 11'))
          smply2_canvas.create_text(680, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
          smply2_canvas.create_text(680, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
          smply2_canvas.create_text(670, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

          smply2_canvas.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
          smply2_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          smply2_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          smply2_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          smply2_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

          tree=ttk.Treeview(smply2_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=530)
          tree.heading("# 1", text="Product/Service - Description")
          tree.column("# 2", anchor=E, stretch=NO, width=90)
          tree.heading("# 2", text="Quantity")
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text="Price")
          
          window = smply2_canvas.create_window(120, 340, anchor="nw", window=tree)

          smply2_canvas.create_line(120, 390, 820, 390 )
          smply2_canvas.create_line(120, 340, 120, 365 )
          smply2_canvas.create_line(120, 365, 120, 390 )
          smply2_canvas.create_line(820, 340, 820, 540 )
          smply2_canvas.create_line(740, 340, 740, 540 )
          smply2_canvas.create_line(570, 390, 570, 540 )
          smply2_canvas.create_line(570, 415, 820, 415 )
          smply2_canvas.create_line(570, 440, 820, 440 )
          smply2_canvas.create_line(570, 465, 820, 465 )
          smply2_canvas.create_line(570, 490, 820, 490 )
          smply2_canvas.create_line(570, 515, 820, 515 )
          smply2_canvas.create_line(650, 340, 650, 390 )
          smply2_canvas.create_line(570, 540, 820, 540 )

          
          smply2_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

          smply2_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

          smply2_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

          smply2_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

          smply2_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          smply2_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

          smply2_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

          smply2_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

          smply2_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

          smply2_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_line(150, 620, 795, 620)
          smply2_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          smply2_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

    #----------------Business Classic------------------ 
      elif menuvar_lst == 'Business Classic':
        if cmpy_dtl[1] is not None:
          sql='select dateformat from company'
          fbcursor.execute(sql)
          date_frmat=fbcursor.fetchone()
          
          if not date_frmat:
            ft_fr='%Y-%m-%d'
        
          elif date_frmat[0]=="mm-dd-yyyy":
            ft_fr='%m-%d-%Y'

          elif date_frmat[0]=="dd-mm-yyyy":
              ft_fr='%d-%m-%Y'
                      
          elif date_frmat[0]=="yyy.mm.dd":
              ft_fr='%Y.%m.%d'
                          
          elif date_frmat[0]=="mm/dd/yyyy":
              ft_fr='%m/%d/%Y'
                          
          elif date_frmat[0]=="dd/mm/yyyy":
              ft_fr='%d/%m/%Y'
                                  
          elif date_frmat[0]=="dd.mm.yyyy":
              ft_fr='%d.%m.%Y'
                                  
          elif date_frmat[0]=="yyyy/  mm/dd":
              ft_fr='%Y/%m/%d'

          else:
              ft_fr='%Y-%m-%d'
          td_date=date.today()
          date_tdy=td_date.strftime(ft_fr)
          bsn_frame = Frame(Invoice_setting_frame_cpy, width=953, height=300)
          bsn_frame.pack(expand=True, fill=BOTH)
          bsn_frame.place(x=247,y=90)
          
          bsn_canvas=Canvas(bsn_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(bsn_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=bsn_canvas.yview)
          bsn_canvas.config(width=953,height=300)
          
          bsn_canvas.config(yscrollcommand=vertibar.set)
          bsn_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          bsn_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          bsn_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_line(150, 70, 800, 70, fill='orange')
          try:
            inv_image = Image.open("images/"+cmpy_dtl[13])
            inv_resize_image = inv_image.resize((200,75))
            inv_image = ImageTk.PhotoImage(inv_resize_image)
          
            inv_logo = Label(bsn_canvas,width=200,height=75, bg="white",image = inv_image) 
            inv_window_image = bsn_canvas.create_window(140, 125, anchor="nw", window=inv_logo)
            inv_logo.photo = inv_image
          except:
            bsn_canvas.create_text(300, 150, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          labelcmp=Label(bsn_canvas,text=cmpy_dtl[1],justify=LEFT, bg="white",anchor="nw",font=("Helvetica", 12), width=30, height=1)
          window = bsn_canvas.create_window(345,100, anchor="nw", window=labelcmp)

          labelcmpl=Label(bsn_canvas,text=cmpy_dtl[2],justify=LEFT, bg="white",font=("Helvetica", 9),anchor="nw", width=40, height=4)
          windowl = bsn_canvas.create_window(350 ,130, anchor="nw", window=labelcmpl)
          
          bsn_canvas.create_text(405, 210, text=cmpy_dtl[4],justify=LEFT, fill="black", font=('Helvetica 9'))

          # bsn_canvas.create_text(500, 115, text="Your Company Name", fill="black", font=('Helvetica 12 '))
          # bsn_canvas.create_text(525, 140, text="Address line 1", fill="black", font=('Helvetica 10'))
          # bsn_canvas.create_text(525, 155, text="Address line 2", fill="black", font=('Helvetica 10'))
          # bsn_canvas.create_text(525, 170, text="Address line 3", fill="black", font=('Helvetica 10'))
          # bsn_canvas.create_text(525, 185, text="Address line 4", fill="black", font=('Helvetica 10'))
          # bsn_canvas.create_text(534, 200, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # bsn_canvas.create_text(534, 215, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))

          
          
          bsn_canvas.create_text(720, 130, text="John Doe\n381 South Beadford Road\nBedford Corner,NY10549\nUnited States", fill="black", font=('Helvetica 11'))

          lb_inv1=Label(bsn_canvas,text=inv_lst_bx1.get(1.0, END), bg="white",anchor="ne",font=("Helvetica", 11),height=1)#Invoice#
          win_inv1 = bsn_canvas.create_window(575, 170, anchor="nw", window=lb_inv1)

          lb_inv1=Label(bsn_canvas,text=inv_lst_bx3.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", 11),height=1 )#Invoicedate
          win_inv1 = bsn_canvas.create_window(575, 200, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(bsn_canvas,text="Due Date", bg="white",anchor="ne",font=("Helvetica", 11),height=1)#Due date
          win_inv1 = bsn_canvas.create_window(575, 230, anchor="nw", window=lb_inv1)

          lb_inv1=Label(bsn_canvas,text=str(inv_tp_lf.get())+"1/2022", bg="white",justify=LEFT,font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = bsn_canvas.create_window(815, 170, anchor="ne", window=lb_inv1)

          # bsn_canvas.create_text(776, 180, text="INV1/2022", fill="black", font=('Helvetica 11'))
          bsn_canvas.create_text(776, 210, text=date_tdy, fill="black", font=('Helvetica 11'))
          bsn_canvas.create_text(776, 240, text=date_tdy, fill="black", font=('Helvetica 11'))

          fgth = ttk.Style()
          fgth.configure('mystyle105.Treeview.Heading', background=''+ invset_bg_var.get(),State='DISABLE')

          tree=ttk.Treeview(bsn_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle105.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=200)
          tree.heading("# 1", text=inv_lst_bx9.get(1.0,END))
          tree.column("# 2", anchor=E, stretch=NO, width=250)
          tree.heading("# 2", text=inv_lst_bx11.get(1.0,END))
          tree.column("# 3", anchor=E, stretch=NO, width=90)
          tree.heading("# 3", text=inv_lst_bx12.get(1.0,END))
          tree.column("# 4", anchor=E, stretch=NO, width=80)
          tree.heading("# 4", text=inv_lst_bx10.get(1.0,END))
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text=inv_lst_bx13.get(1.0,END))
          
          window = bsn_canvas.create_window(120, 255, anchor="nw", window=tree)
          
          bsn_canvas.create_line(120, 295, 820, 295 )
          bsn_canvas.create_line(120, 255, 120, 295 )
          bsn_canvas.create_line(320, 255, 320, 295 )
          
          bsn_canvas.create_line(740, 255, 740, 445 )
          bsn_canvas.create_line(570, 255, 570, 445 )
          bsn_canvas.create_line(570, 255, 570, 295 )
          bsn_canvas.create_line(660, 255, 660, 295 )
          bsn_canvas.create_line(740, 255, 740, 295 )
          bsn_canvas.create_line(820, 255, 820, 445 )
          bsn_canvas.create_line(570, 320, 820, 320 )
          bsn_canvas.create_line(570, 345, 820, 345 )
          bsn_canvas.create_line(570, 370, 820, 370 )
          bsn_canvas.create_line(570, 395, 820, 395 )
          bsn_canvas.create_line(570, 420, 820, 420 )
          bsn_canvas.create_line(570, 445, 820, 445 )
          
          sqlr= 'select currencysign from company'
          fbcursor.execute(sqlr)
          crncy=fbcursor.fetchone()
          crcy_type=crncy[0]
          sqlrt= 'select currsignplace from company'
          fbcursor.execute(sqlrt)
          post_rp=fbcursor.fetchone()
          cry_plcy=post_rp[0]
          if cry_plcy=="before amount": 
            bsn_canvas.create_text(630, 285, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 285, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 310, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(795, 335, text=str(crcy_type)+"18.00", fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(795, 360, text=str(crcy_type)+"20.00", fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 385, text=str(crcy_type)+"238.00", fill="black", font=('Helvetica 10 bold'))
            bsn_canvas.create_text(790, 410, text=str(crcy_type)+"100.00", fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 435, text=str(crcy_type)+"138.00", fill="black", font=('Helvetica 10'))
          elif cry_plcy=="after amount":
            bsn_canvas.create_text(630, 285, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 285, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 310, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(795, 335, text="18.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(795, 360, text="20.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 385, text="238.00"+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
            bsn_canvas.create_text(790, 410, text="100.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 435, text="138.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
          elif cry_plcy=="before amount with space":
            bsn_canvas.create_text(630, 285, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 285, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 310, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(795, 335, text=str(crcy_type)+" "+"18.00", fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(795, 360, text=str(crcy_type)+" "+"20.00", fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 385, text=str(crcy_type)+" "+"238.00", fill="black", font=('Helvetica 10 bold'))
            bsn_canvas.create_text(790, 410, text=str(crcy_type)+" "+"100.00", fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 435, text=str(crcy_type)+" "+"138.00", fill="black", font=('Helvetica 10')) 
          elif cry_plcy=="after amount with space":
            bsn_canvas.create_text(630, 285, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 285, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 310, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(795, 335, text="18.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(795, 360, text="20.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 385, text="238.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
            bsn_canvas.create_text(790, 410, text="100.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            bsn_canvas.create_text(790, 435, text="138.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
          else:
            pass
          bsn_canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
      
          bsn_canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
          

          

          lbx_inv=Label(bsn_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
          win_inv2 = bsn_canvas.create_window(630,298, anchor="nw", window=lbx_inv)

          lbx_inv=Label(bsn_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
          win_inv2 = bsn_canvas.create_window(635,323, anchor="nw", window=lbx_inv)

          lbx_inv=Label(bsn_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
          win_inv2 = bsn_canvas.create_window(630, 398,anchor="nw", window=lbx_inv)

          lbx_inv=Label(bsn_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
          win_inv2 = bsn_canvas.create_window(635, 423, anchor="nw", window=lbx_inv)

      
          bsn_canvas.create_text(655, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          lbx_inv=Label(bsn_canvas,text=inv_lst_bx18.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#Order Total"
          win_inv2 = bsn_canvas.create_window(630, 373, anchor="nw", window=lbx_inv)
          lbx_inv=Label(bsn_canvas,text=inv_lst_bx21.get(1.0,END), bg="white",anchor="n",font=("Helvetica 10 "),height=1)#"Terms and Conditions"
          win_inv2 = bsn_canvas.create_window(420, 570, anchor="nw", window=lbx_inv)
      

          bsn_canvas.create_line(150, 470, 800, 470, fill='orange')
          bsn_canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
          


          bsn_canvas.create_line(150, 600, 795, 600)
          text=inv_txt.get('1.0',END)
          wraped_text="\n".join(wrap(text,130))
    
        
          lbx_inv=Label(bsn_canvas,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
          win_inv2 = bsn_canvas.create_window(150, 603,anchor="nw", window=lbx_inv)

          bsn_canvas.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    

          bsn_canvas.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
        else:

          bsn_frame = Frame(Invoice_setting_frame_cpy, width=953, height=300)
          bsn_frame.pack(expand=True, fill=BOTH)
          bsn_frame.place(x=247,y=90)
          
          bsn_canvas=Canvas(bsn_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(bsn_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=bsn_canvas.yview)
          bsn_canvas.config(width=953,height=300)
          
          bsn_canvas.config(yscrollcommand=vertibar.set)
          bsn_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          bsn_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          bsn_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_line(150, 70, 800, 70, fill='orange')
          bsn_canvas.create_text(300, 150, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          bsn_canvas.create_text(500, 115, text="Your Company Name", fill="black", font=('Helvetica 12 '))
          bsn_canvas.create_text(525, 140, text="Address line 1", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(525, 155, text="Address line 2", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(525, 170, text="Address line 3", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(525, 185, text="Address line 4", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(534, 200, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(534, 215, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))

          
          

          bsn_canvas.create_text(659, 180, text="Invoice", fill="black", font=('Helvetica 11'))
          bsn_canvas.create_text(675, 210, text="Invoice date", fill="black", font=('Helvetica 11'))
          bsn_canvas.create_text(659, 240, text="Due date", fill="black", font=('Helvetica 11'))

          bsn_canvas.create_text(776, 180, text="INV1/2022", fill="black", font=('Helvetica 11'))
          bsn_canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
          bsn_canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))
          tree=ttk.Treeview(bsn_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=200)
          tree.heading("# 1", text="Product/Service")
          tree.column("# 2", anchor=E, stretch=NO, width=250)
          tree.heading("# 2", text="Description")
          tree.column("# 3", anchor=E, stretch=NO, width=90)
          tree.heading("# 3", text="Unit Price")
          tree.column("# 4", anchor=E, stretch=NO, width=80)
          tree.heading("# 4", text="Quantity")
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text="Price")
          
          window = bsn_canvas.create_window(120, 255, anchor="nw", window=tree)

          bsn_canvas.create_line(120, 295, 820, 295 )
          bsn_canvas.create_line(120, 255, 120, 295 )
          bsn_canvas.create_line(320, 255, 320, 295 )
          bsn_canvas.create_line(570, 255, 570, 295 )
          bsn_canvas.create_line(660, 255, 660, 295 )
          bsn_canvas.create_line(740, 255, 740, 295 )
          bsn_canvas.create_line(820, 255, 820, 445 )
          bsn_canvas.create_line(570, 320, 820, 320 )
          bsn_canvas.create_line(570, 345, 820, 345 )
          bsn_canvas.create_line(570, 370, 820, 370 )
          bsn_canvas.create_line(570, 395, 820, 395 )
          bsn_canvas.create_line(570, 420, 820, 420 )
          bsn_canvas.create_line(570, 445, 820, 445 )
          
          bsn_canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(630, 285, text="$200.00", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(790, 285, text="$200.00", fill="black", font=('Helvetica 10'))

          bsn_canvas.create_text(790, 310, text="$200.00", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(795, 335, text="$18.00", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(795, 360, text="$20.00", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(790, 385, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          bsn_canvas.create_text(790, 410, text="$100.00", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(790, 435, text="$138.00", fill="black", font=('Helvetica 10'))

          bsn_canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(615, 385, text="Estimate total", fill="black", font=('Helvetica 10 bold'))
          bsn_canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

          bsn_canvas.create_line(150, 470, 800, 470, fill='orange')
          bsn_canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
          
          bsn_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_line(150, 620, 795, 620, fill='orange')
          bsn_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          bsn_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      
  logo_just_var = StringVar()
  inv_cn_stl = ttk.Combobox(Invoice_setting_frame_cpy,textvariable=logo_just_var)
  inv_cn_stl.place(x=770 ,y=40, width=220)
  inv_cn_stl.bind("<<ComboboxSelected>>", styl_can_def)
  inv_cn_stl["values"] = ("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
  inv_cn_stl.current(0)
  por_sql_st='select * from company'
  fbcursor.execute(por_sql_st)
  cmpy_dtl=fbcursor.fetchone()
  if cmpy_dtl is not None:   
          sql='select dateformat from company'
          fbcursor.execute(sql)
          date_frmat=fbcursor.fetchone()
          
          if not date_frmat:
            ft_fr='%Y-%m-%d'
        
          elif date_frmat[0]=="mm-dd-yyyy":
            ft_fr='%m-%d-%Y'

          elif date_frmat[0]=="dd-mm-yyyy":
              ft_fr='%d-%m-%Y'
                      
          elif date_frmat[0]=="yyy.mm.dd":
              ft_fr='%Y.%m.%d'
                          
          elif date_frmat[0]=="mm/dd/yyyy":
              ft_fr='%m/%d/%Y'
                          
          elif date_frmat[0]=="dd/mm/yyyy":
              ft_fr='%d/%m/%Y'
                                  
          elif date_frmat[0]=="dd.mm.yyyy":
              ft_fr='%d.%m.%Y'
                                  
          elif date_frmat[0]=="yyyy/  mm/dd":
              ft_fr='%Y/%m/%d'

          else:
              ft_fr='%Y-%m-%d'
          td_date=date.today()
          date_tdy=td_date.strftime(ft_fr)   
          frame_pro1 = Frame(Invoice_setting_frame_cpy, width=953, height=300)
          frame_pro1.pack(expand=True, fill=BOTH)
          frame_pro1.place(x=247,y=90)
          inv_pro1_canvas=Canvas(frame_pro1, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(frame_pro1, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=inv_pro1_canvas.yview)
          
          inv_pro1_canvas.config(width=953,height=300)
          inv_pro1_canvas.config(yscrollcommand=vertibar.set)
          inv_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          inv_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          inv_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            inv_image = Image.open("images/"+cmpy_dtl[13])
            inv_resize_image = inv_image.resize((200,75))
            inv_image = ImageTk.PhotoImage(inv_resize_image)
          
            inv_logo = Label(inv_pro1_canvas,width=200,height=75, bg="white",image = inv_image) 
            inv_window_image = inv_pro1_canvas.create_window(150, 50, anchor="nw", window=inv_logo)
            inv_logo.photo = inv_image
          except:
            inv_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          
          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx2.get(1.0, END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Invoice#
          win_inv1 = inv_pro1_canvas.create_window(175, 140, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx3.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1 )#Invoicedate
          win_inv1 = inv_pro1_canvas.create_window(175, 160, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(inv_pro1_canvas,text="Due date", bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Due date
          win_inv1 = inv_pro1_canvas.create_window(175, 180, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx5.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Terms
          win_inv1 = inv_pro1_canvas.create_window(175, 200, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx4.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = inv_pro1_canvas.create_window(175, 220, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_pro1_canvas,text=str(inv_tp_lf.get())+"1/2022", bg="white",anchor="nw",font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = inv_pro1_canvas.create_window(310, 140, anchor="nw", window=lb_inv1)

          inv_pro1_canvas.create_text(350, 150, text="INV1/2022",justify=LEFT, fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(350, 170, text=date_tdy,justify=LEFT, fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(350, 190, text=date_tdy,justify=LEFT, fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(340, 210, text="NET 15",justify=LEFT, fill="black", font=('Helvetica 11'))   
          
          labelcmp=Label(inv_pro1_canvas,text=cmpy_dtl[1], bg="white",anchor="e",font=("Helvetica", 12), width=40, height=1)
          window = inv_pro1_canvas.create_window(430,80, anchor="nw", window=labelcmp)

          labelcmpl=Label(inv_pro1_canvas,text=cmpy_dtl[2],justify=RIGHT, bg="white",font=("Helvetica", 9),anchor="ne", width=50, height=4)
          windowl = inv_pro1_canvas.create_window(440,110, anchor="nw", window=labelcmpl)

          
          inv_pro1_canvas.create_text(745, 185, text=cmpy_dtl[4], fill="black", font=('Helvetica 10'))

          # lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx1.get(1.0,END), bg="white",anchor="ne",font=('Helvetica 14 bold'),height=1)#invoice
          # win_inv1 = inv_pro1_canvas.create_window(725, 200, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx1.get(1.0,END), bg="white",anchor="ne",font=('Helvetica 14 bold'),height=1)#invoice
          win_inv1 = inv_pro1_canvas.create_window(800, 200, anchor="ne", window=lb_inv1)


          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx22.get(1.0,END), bg="white",anchor="ne",font=("Helvetica 10" ),height=1)#TAX EXEMPTED
          win_inv1 = inv_pro1_canvas.create_window(705, 225, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx6.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline" ),height=1)#Invoice to
          win_inv1 = inv_pro1_canvas.create_window(175, 250, anchor="nw", window=lb_inv1)

          lb_inv1=Label(inv_pro1_canvas,text=inv_lst_bx7.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline"),height=1)#Ship to
          win_inv1 = inv_pro1_canvas.create_window(525, 250, anchor="nw", window=lb_inv1)

          
          # inv_pro1_canvas.create_text(765, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))
          # inv_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
          # inv_pro1_canvas.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
          inv_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          inv_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
          # inv_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          inv_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          inv_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
          fgth = ttk.Style()
          fgth.configure('mystyle106.Treeview.Heading', background=''+ invset_bg_var.get(),State='DISABLE')

          tree=ttk.Treeview(inv_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle106.Treeview')

          tree.column("# 1", anchor=E, stretch=NO, width=100)
          tree.heading("# 1", text=inv_lst_bx8.get(1.0,END))#"ID/SKU"
          tree.column("# 2", anchor=E, stretch=NO, width=350)
          tree.heading("# 2", text=inv_lst_bx9.get(1.0,END))#Product/Service - Description
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text=inv_lst_bx10.get(1.0,END))#"Quantity"
          tree.column("# 4", anchor=E, stretch=NO, width=90)
          tree.heading("# 4", text=inv_lst_bx12.get(1.0,END))#"Unit Price"
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text=inv_lst_bx13.get(1.0,END))#"Price"
          
          window = inv_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)
          squl_qry='select * from company'
          fbcursor.execute(squl_qry)
          cmpy_tax=fbcursor.fetchone()

          inv_pro1_canvas.create_line(120, 390, 820, 390 )
          inv_pro1_canvas.create_line(120, 340, 120, 365 )
          inv_pro1_canvas.create_line(120, 365, 120, 390 )
          inv_pro1_canvas.create_line(820, 340, 820, 540 )
          inv_pro1_canvas.create_line(740, 340, 740, 540 )
          inv_pro1_canvas.create_line(570, 340, 570, 540 )
          inv_pro1_canvas.create_line(570, 415, 820, 415 )
          inv_pro1_canvas.create_line(570, 440, 820, 440 )
          inv_pro1_canvas.create_line(570, 465, 820, 465 )
          inv_pro1_canvas.create_line(570, 490, 820, 490 )
          inv_pro1_canvas.create_line(570, 515, 820, 515 )
          inv_pro1_canvas.create_line(650, 340, 650, 390 )
          inv_pro1_canvas.create_line(220, 340, 220, 390 )
          inv_pro1_canvas.create_line(570, 540, 820, 540 )

          inv_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
          
            

          lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
          win_inv2 = inv_pro1_canvas.create_window(630,392, anchor="nw", window=lbx_inv)

          lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
          win_inv2 = inv_pro1_canvas.create_window(635,418, anchor="nw", window=lbx_inv)

          lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
          win_inv2 = inv_pro1_canvas.create_window(630, 492,anchor="nw", window=lbx_inv)

          lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
          win_inv2 = inv_pro1_canvas.create_window(635, 518, anchor="nw", window=lbx_inv)
            
          sqlr= 'select currencysign from company'
          fbcursor.execute(sqlr)
          crncy=fbcursor.fetchone()
          crcy_type=crncy[0]
          sqlrt= 'select currsignplace from company'
          fbcursor.execute(sqlrt)
          post_rp=fbcursor.fetchone()
          cry_plcy=post_rp[0]
          if cry_plcy=="before amount": 
            inv_pro1_canvas.create_text(710, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 404, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 428, text=str(crcy_type)+"18.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 502, text=str(crcy_type)+"100.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 526, text=str(crcy_type)+"138.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 454, text=str(crcy_type)+"20.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 479, text=str(crcy_type)+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount":
            inv_pro1_canvas.create_text(710, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 404, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 428, text="18.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 502, text="100.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 526, text="138.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 454, text="20.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 479, text="238.00"+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="before amount with space": 
            inv_pro1_canvas.create_text(710, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 404, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 428, text=str(crcy_type)+" "+"18.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 502, text=str(crcy_type)+" "+"100.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 526, text=str(crcy_type)+" "+"138.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 454, text=str(crcy_type)+" "+"20.00", fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 479, text=str(crcy_type)+" "+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount with space":
            inv_pro1_canvas.create_text(710, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 404, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 428, text="18.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 502, text="100.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 526, text="138.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(792, 454, text="20.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            inv_pro1_canvas.create_text(790, 479, text="238.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          else:
            pass
          
          inv_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          
          lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx18.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#Order Total"
          win_inv2 = inv_pro1_canvas.create_window(625, 468, anchor="nw", window=lbx_inv)
          
        
          inv_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
          lbx_inv=Label(inv_pro1_canvas,text=inv_lst_bx21.get(1.0,END), bg="white",anchor="n",font=("Helvetica 10 "),height=1)#"Terms and Conditions"
          win_inv2 = inv_pro1_canvas.create_window(420, 570, anchor="nw", window=lbx_inv)

          # inv_pro1_canvas.create_text(500, 620, text=inv_lst_bx21.get(1.0,END), fill="black", font=('Helvetica 10'))#"Terms and Conditions"
          inv_pro1_canvas.create_line(150, 600, 795, 600)
          text=inv_txt.get('1.0',END)
          wraped_text="\n".join(wrap(text,130))
    
        
          lbx_inv=Label(inv_pro1_canvas,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
          win_inv2 = inv_pro1_canvas.create_window(150, 603,anchor="nw", window=lbx_inv)

          inv_pro1_canvas.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    

          inv_pro1_canvas.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  else:
          frame_pro1 = Frame(Invoice_setting_frame_cpy, width=953, height=300)
          frame_pro1.pack(expand=True, fill=BOTH)
          frame_pro1.place(x=247,y=90)
          inv_pro1_canvas=Canvas(frame_pro1, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(frame_pro1, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=inv_pro1_canvas.yview)
          
          inv_pro1_canvas.config(width=953,height=300)
          inv_pro1_canvas.config(yscrollcommand=vertibar.set)
          inv_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          inv_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          inv_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          
          inv_pro1_canvas.create_text(195, 150, text="Invoice#", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(205, 170, text="Invoicedate", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(205, 230, text="Invoice ref.#", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(350, 150, text="INV1/2022", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(350, 170, text="03-05-2022", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(350, 190, text="18-05-2022", fill="black", font=('Helvetica 11'))
          inv_pro1_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))   
          
          inv_pro1_canvas.create_text(720, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))

          inv_pro1_canvas.create_text(750, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(750, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(750, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(750, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(745, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(745, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(750, 205, text="Invoice", fill="black", font=('Helvetica 14 bold'))
          inv_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
          inv_pro1_canvas.create_text(210, 260, text="Invoice to", fill="black", font=('Helvetica 10 underline'))
          inv_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          inv_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          inv_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          inv_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
          s = ttk.Style()
          s.configure('Treeview.Heading', background=''+ invset_bg_var.get(),State='DISABLE')

          tree=ttk.Treeview(inv_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')

          tree.column("# 1", anchor=E, stretch=NO, width=100)
          tree.heading("# 1", text="ID/SKU")
          tree.column("# 2", anchor=E, stretch=NO, width=350)
          tree.heading("# 2", text="Product/Service - Description")
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text="Quantity")
          tree.column("# 4", anchor=E, stretch=NO, width=90)
          tree.heading("# 4", text="Unit Price")
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text="Price")
          
          window = inv_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)

          inv_pro1_canvas.create_line(120, 390, 820, 390 )
          inv_pro1_canvas.create_line(120, 340, 120, 365 )
          inv_pro1_canvas.create_line(120, 365, 120, 390 )
          inv_pro1_canvas.create_line(820, 340, 820, 540 )
          inv_pro1_canvas.create_line(740, 340, 740, 540 )
          inv_pro1_canvas.create_line(570, 340, 570, 540 )
          inv_pro1_canvas.create_line(570, 415, 820, 415 )
          inv_pro1_canvas.create_line(570, 440, 820, 440 )
          inv_pro1_canvas.create_line(570, 465, 820, 465 )
          inv_pro1_canvas.create_line(570, 490, 820, 490 )
          inv_pro1_canvas.create_line(570, 515, 820, 515 )
          inv_pro1_canvas.create_line(650, 340, 650, 390 )
          inv_pro1_canvas.create_line(220, 340, 220, 390 )
          inv_pro1_canvas.create_line(570, 540, 820, 540 )

          inv_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(610, 372, text="0", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(710, 372, text="0", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(790, 372, text="0", fill="black", font=('Helvetica 10'))

          inv_pro1_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(790, 404, text="0", fill="black", font=('Helvetica 10'))

          inv_pro1_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(792, 428, text="0", fill="black", font=('Helvetica 10'))

          inv_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(792, 454, text="0", fill="black", font=('Helvetica 10'))

          inv_pro1_canvas.create_text(790, 479, text="0", fill="black", font=('Helvetica 10 bold'))
          inv_pro1_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

          inv_pro1_canvas.create_text(790, 502, text="0", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

          inv_pro1_canvas.create_text(790, 526, text="0", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

          inv_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
          inv_pro1_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_line(150, 620, 795, 620)
          

          inv_pro1_canvas.create_text(280, 640, text= "", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          inv_pro1_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


  ######################################################################################tab 04 Orders
  ord_set_frm=Frame(tab04, relief=GROOVE, bg="#f8f8f2")
  ord_set_frm.pack(side="top", fill=BOTH)

  ord_set_frm_cpy=Frame(ord_set_frm, bg="#f5f3f2", height=700)
  ord_set_frm_cpy.pack(side="top", fill=BOTH)
  ord_ver = Label(ord_set_frm_cpy,text="Order# prefix")
  ord_ver.place(x=5,y=40)

  sql_ord_ist="select * from order_settings"
  fbcursor.execute(sql_ord_ist)
  inst_dtl_ord=fbcursor.fetchone()


  ord_lft_tp = Entry(ord_set_frm)
  if inst_dtl_ord is None:
    ord_lft_tp.insert(0, "ORD")
  else:
    ord_lft_tp.delete(0,'end')
    ord_lft_tp.insert(0, inst_dtl_ord[0])
  
  ord_lft_tp.place(x=100,y=40)

  ordset_ver = Label(ord_set_frm_cpy,text="Starting estimate number")
  ordset_ver.place(x=25,y=80)
  my_var_sprn= StringVar(ord_set_frm_cpy)
  
  

  def spin_valss(S,d):
    if d=='1':
      if not S in ['.','0','1','2','3','4','5','6','7','8','9']:
        return False
      return True
          
    if d.isdigit():
      return True


  valditysss=(ord_set_frm_cpy.register(spin_valss), '%S','%d')
  ord_spn_bx = Spinbox(ord_set_frm_cpy,from_=1,to=1000000,width=15,justify=RIGHT)

  if inst_dtl_ord is None:
    pass
  else:
    ord_spn_bx.delete(0,"end")
    ord_spn_bx.insert(0,int(inst_dtl_ord[1]))
  ord_spn_bx.config(validate='key',validatecommand=(valditysss))
  ord_spn_bx.place(x=50,y=100)

  ordset_ver = Label(ord_set_frm_cpy,text="Header box background color")
  ordset_ver.place(x=5,y=140)



  ord_man_var = StringVar()
  ord_cmb_bx = ttk.Combobox(ord_set_frm_cpy,textvariable=ord_man_var)
  
  ord_cmb_bx['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
  if inst_dtl_ord is None:
    ord_cmb_bx.current(0)
  else:
    ord_cmb_bx.insert(0, inst_dtl_ord[2])
  ord_cmb_bx.place(x=6 ,y=160)

  

  ordset_ver = Label(ord_set_frm_cpy,text="Customize Estimate text labels")
  ordset_ver.place(x=5,y=190)

  def rstr_ord_tab04():
    ord_lft_tp1.delete(1.0,'end')
    ord_lft_tp1.insert(END, "Order")
    ord_lft_tp2.delete(1.0,'end')
    ord_lft_tp2.insert(1.0, "Order#")
    ord_lft_tp3.delete(1.0,'end')
    ord_lft_tp3.insert(1.0, "Order date")
    ord_lft_tp4.delete(1.0,'end')
    ord_lft_tp4.insert(END, "Due date")
    ord_lft_tp5.delete(1.0,'end')
    ord_lft_tp5.insert(END, "Order to")
    ord_lft_tp6.delete(1.0,'end')
    ord_lft_tp6.insert(1.0, "Order total")

  ord_lft_tp1 = Text(ord_set_frm, height=1, width=25, font=('Calibri 10'))
  if inst_dtl_ord is None:
    ord_lft_tp1.delete(1.0,'end')
    ord_lft_tp1.insert(END, "Order")
  else:
    ord_lft_tp1.delete(1.0,'end')
    ord_lft_tp1.insert(1.0, inst_dtl_ord[3])
  ord_lft_tp1.place(x=5,y=220)
  ord_lft_tp2 = Text(ord_set_frm,height=1, width=25, font=('Calibri 10'))
  if inst_dtl_ord is None:
    ord_lft_tp2.delete(1.0,'end')
    ord_lft_tp2.insert(1.0, "Order#")
  else:
    ord_lft_tp2.delete(1.0,'end')
    ord_lft_tp2.insert(1.0, inst_dtl_ord[4])
  
  ord_lft_tp2.place(x=5,y=240)
  ord_lft_tp3 = Text(ord_set_frm,height=1, width=25, font=('Calibri 10'))
  if inst_dtl_ord is None:
    ord_lft_tp3.delete(1.0,'end')
    ord_lft_tp3.insert(1.0, "Order date")
  else:
    ord_lft_tp3.delete(1.0,'end')
    ord_lft_tp3.insert(1.0, inst_dtl_ord[5])
  
  ord_lft_tp3.place(x=5,y=260) 

  
  ord_lft_tp4 = Text(ord_set_frm,height=1, width=25, font=('Calibri 10'))
  if inst_dtl_ord is None:
    ord_lft_tp4.delete(1.0,'end')
    ord_lft_tp4.insert(END, "Due date")
  else:
    ord_lft_tp4.delete(1.0,'end')
    ord_lft_tp4.insert(1.0, inst_dtl_ord[6])

  ord_lft_tp4.place(x=5,y=280)
  # vght=ord_lft_tp4
  ord_lft_tp5 = Text(ord_set_frm,height=1, width=25, font=('Calibri 10'))
  if inst_dtl_ord is None:
    ord_lft_tp5.delete(1.0,'end')
    ord_lft_tp5.insert(END, "Order to")
  else:
    ord_lft_tp5.delete(1.0,'end')
    ord_lft_tp5.insert(1.0, inst_dtl_ord[7])
  
  ord_lft_tp5.place(x=5,y=300)
  ord_lft_tp6 = Text(ord_set_frm, height=1,width=25, font=('Calibri 10'))
  if inst_dtl_ord is None:
    ord_lft_tp6.delete(1.0,'end')
    ord_lft_tp6.insert(1.0, "Order total")
  else:
    ord_lft_tp6.delete(1.0,'end')
    ord_lft_tp6.insert(1.0, inst_dtl_ord[8])
  
  ord_lft_tp6.place(x=5,y=320)



  ord_s1 = StringVar(ord_set_frm, "Order")


  ordset_ver = Label(ord_set_frm_cpy,text="Default Order template(example,click on preview for mouse scrolling)")
  ordset_ver.place(x=248,y=55 )

  ordset_ver = Label(ord_set_frm_cpy,text="Default Order template")
  ordset_ver.place(x=619,y=40)



  ordset_messagelbframe=LabelFrame(ord_set_frm_cpy,text="Predefined terms and conditions text for estimates", height=100, width=980)
  ordset_messagelbframe.place(x=248, y=400)

  ord_scrl_txt = scrolledtext.ScrolledText(ord_set_frm_cpy, undo=True,width=115,height=4)
  if inst_dtl_ord is None:
    ord_scrl_txt.insert(1.0,"Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods, and agrees to be bound to these contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller.")
  else:
    ord_scrl_txt.insert(1.0, inst_dtl_ord[9])

  
  ord_scrl_txt.place(x=260,y=425)



  ordset_bttermadd = Button(ord_set_frm_cpy,text="Restore defaults", command=lambda:rstr_ord_tab04())
  ordset_bttermadd.place(x=32,y=450)
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~order drop
  def ord_main_mn(event):
      cmp_mn_var=ord_main_var.get()
      por_sql_st='select * from company'
      fbcursor.execute(por_sql_st)
      cmpy_dtls=fbcursor.fetchone()

      if cmp_mn_var == 'Professional 1 (logo on left side)':
        if cmpy_dtls is not None:
          sql='select dateformat from company'
          fbcursor.execute(sql)
          date_frmat=fbcursor.fetchone()
          
          if not date_frmat:
            ft_fr='%Y-%m-%d'
        
          elif date_frmat[0]=="mm-dd-yyyy":
            ft_fr='%m-%d-%Y'

          elif date_frmat[0]=="dd-mm-yyyy":
              ft_fr='%d-%m-%Y'
                      
          elif date_frmat[0]=="yyy.mm.dd":
              ft_fr='%Y.%m.%d'
                          
          elif date_frmat[0]=="mm/dd/yyyy":
              ft_fr='%m/%d/%Y'
                          
          elif date_frmat[0]=="dd/mm/yyyy":
              ft_fr='%d/%m/%Y'
                                  
          elif date_frmat[0]=="dd.mm.yyyy":
              ft_fr='%d.%m.%Y'
                                  
          elif date_frmat[0]=="yyyy/  mm/dd":
              ft_fr='%Y/%m/%d'

          else:
              ft_fr='%Y-%m-%d'
          td_date=date.today()
          date_tdy=td_date.strftime(ft_fr)
          ord_pro1_frame = Frame(ord_set_frm_cpy, width=953, height=300)
          ord_pro1_frame.pack(expand=True, fill=BOTH)
          ord_pro1_frame.place(x=247,y=90)
          ord_pro1_canvas=Canvas(ord_pro1_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(ord_pro1_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=ord_pro1_canvas.yview)
          
          ord_pro1_canvas.config(width=953,height=300)
          ord_pro1_canvas.config(yscrollcommand=vertibar.set)
          ord_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          ord_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          ord_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            inv_image = Image.open("images/"+cmpy_dtl[13])
            inv_resize_image = inv_image.resize((200,75))
            inv_image = ImageTk.PhotoImage(inv_resize_image)
          
            inv_logo = Label(ord_pro1_canvas,width=200,height=75, bg="white",image = inv_image) 
            inv_window_image = ord_pro1_canvas.create_window(150, 50, anchor="nw", window=inv_logo)
            inv_logo.photo = inv_image
          except:
            ord_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          
          lb_inv1=Label(ord_pro1_canvas,text=ord_lft_tp2.get(1.0, END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Order#"
          win_inv1 = ord_pro1_canvas.create_window(175, 140, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_pro1_canvas,text=ord_lft_tp3.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1 )#Order date
          win_inv1 = ord_pro1_canvas.create_window(175, 160, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(ord_pro1_canvas,text=ord_lft_tp4.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Due date
          win_inv1 = ord_pro1_canvas.create_window(175, 180, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_pro1_canvas,text=inv_lst_bx5.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Terms
          win_inv1 = ord_pro1_canvas.create_window(175, 200, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_pro1_canvas,text=inv_lst_bx4.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", ),height=1)#Order ref.#
          win_inv1 = ord_pro1_canvas.create_window(175, 220, anchor="nw", window=lb_inv1)

          # ord_pro1_canvas.create_text(195, 150, text="Order#", fill="black", font=('Helvetica 11'))
          # ord_pro1_canvas.create_text(205, 170, text="Order date", fill="black", font=('Helvetica 11'))
          # ord_pro1_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
          # ord_pro1_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
          # ord_pro1_canvas.create_text(205, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
          lb_inv1=Label(ord_pro1_canvas,text=str(ord_lft_tp.get())+"1/2022", bg="white",anchor="nw",font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = ord_pro1_canvas.create_window(310, 140, anchor="nw", window=lb_inv1)
          ord_pro1_canvas.create_text(350, 170, text=date_tdy, fill="black", font=('Helvetica 11'))
          ord_pro1_canvas.create_text(350, 190, text=date_tdy, fill="black", font=('Helvetica 11'))
          ord_pro1_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

          labelcmp=Label(ord_pro1_canvas,text=cmpy_dtl[1], bg="white",anchor="e",font=("Helvetica", 12), width=40, height=1)
          window = ord_pro1_canvas.create_window(430,80, anchor="nw", window=labelcmp)

          labelcmpl=Label(ord_pro1_canvas,text=cmpy_dtl[2],justify=RIGHT, bg="white",font=("Helvetica", 9),anchor="ne", width=50, height=4)
          windowl = ord_pro1_canvas.create_window(440,110, anchor="nw", window=labelcmpl)

          
          ord_pro1_canvas.create_text(745, 185, text=cmpy_dtl[4], fill="black", font=('Helvetica 10'))
          lb_inv1=Label(ord_pro1_canvas,text=ord_lft_tp1.get(1.0,END), bg="white",anchor="ne",font=('Helvetica 14 bold'),height=1)#Order
          win_inv1 = ord_pro1_canvas.create_window(800, 200, anchor="ne", window=lb_inv1)

          lb_inv1=Label(ord_pro1_canvas,text=inv_lst_bx22.get(1.0,END), bg="white",justify=LEFT,font=("Helvetica 10" ),height=2)#TAX EXEMPTED
          win_inv1 = ord_pro1_canvas.create_window(800, 225, anchor="ne", window=lb_inv1)

          lb_inv1=Label(ord_pro1_canvas,text=ord_lft_tp5.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline" ),height=1)#Order to
          win_inv1 = ord_pro1_canvas.create_window(175, 250, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_pro1_canvas,text=inv_lst_bx7.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline"),height=1)#Ship to
          win_inv1 = ord_pro1_canvas.create_window(525, 250, anchor="nw", window=lb_inv1)

          # ord_pro1_canvas.create_text(770, 205, text="Order", fill="black", font=('Helvetica 14 bold'))
      
          # ord_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
            
          # ord_pro1_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
          ord_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
          # ord_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          ord_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
          phf = ttk.Style()
          phf.configure('mystyle122.Treeview.Heading', background=''+ ord_man_var.get(),State='DISABLE')

          tree=ttk.Treeview(ord_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle122.Treeview')

          tree.column("# 1", anchor=E, stretch=NO, width=100)
          tree.heading("# 1", text=inv_lst_bx8.get(1.0,END))
          tree.column("# 2", anchor=E, stretch=NO, width=350)
          tree.heading("# 2", text=inv_lst_bx9.get(1.0,END))
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text=inv_lst_bx10.get(1.0,END))
          tree.column("# 4", anchor=E, stretch=NO, width=90)
          tree.heading("# 4", text=inv_lst_bx12.get(1.0,END))
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text=inv_lst_bx13.get(1.0,END))
          
          window = ord_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)

          ord_pro1_canvas.create_line(120, 390, 820, 390 )
          ord_pro1_canvas.create_line(120, 340, 120, 365 )
          ord_pro1_canvas.create_line(120, 365, 120, 390 )
          ord_pro1_canvas.create_line(820, 340, 820, 540 )
          ord_pro1_canvas.create_line(740, 340, 740, 540 )
          ord_pro1_canvas.create_line(570, 340, 570, 540 )
          ord_pro1_canvas.create_line(570, 415, 820, 415 )
          ord_pro1_canvas.create_line(570, 440, 820, 440 )
          ord_pro1_canvas.create_line(570, 465, 820, 465 )
          ord_pro1_canvas.create_line(570, 490, 820, 490 )
          ord_pro1_canvas.create_line(570, 515, 820, 515 )
          ord_pro1_canvas.create_line(650, 340, 650, 390 )
          ord_pro1_canvas.create_line(220, 340, 220, 390 )
          ord_pro1_canvas.create_line(570, 540, 820, 540 )

          lbx_inv=Label(ord_pro1_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
          win_inv2 = ord_pro1_canvas.create_window(630,392, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_pro1_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
          win_inv2 = ord_pro1_canvas.create_window(635,418, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_pro1_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
          win_inv2 = ord_pro1_canvas.create_window(630, 492,anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_pro1_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
          win_inv2 = ord_pro1_canvas.create_window(635, 518, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_pro1_canvas,text=ord_lft_tp6.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#Order Total"
          win_inv2 = ord_pro1_canvas.create_window(630, 468, anchor="nw", window=lbx_inv)
          

          sqlr= 'select currencysign from company'
          fbcursor.execute(sqlr)
          crncy=fbcursor.fetchone()
          crcy_type=crncy[0]
          sqlrt= 'select currsignplace from company'
          fbcursor.execute(sqlrt)
          post_rp=fbcursor.fetchone()
          cry_plcy=post_rp[0]
          if cry_plcy=="before amount": 
            ord_pro1_canvas.create_text(710, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 404, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 428, text=str(crcy_type)+"18.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 502, text=str(crcy_type)+"100.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 526, text=str(crcy_type)+"138.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 454, text=str(crcy_type)+"20.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 479, text=str(crcy_type)+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount":
            ord_pro1_canvas.create_text(710, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 404, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 428, text="18.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 502, text="100.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 526, text="138.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 454, text="20.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 479, text="238.00"+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="before amount with space": 
            ord_pro1_canvas.create_text(710, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 404, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 428, text=str(crcy_type)+" "+"18.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 502, text=str(crcy_type)+" "+"100.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 526, text=str(crcy_type)+" "+"138.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 454, text=str(crcy_type)+" "+"20.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 479, text=str(crcy_type)+" "+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount with space":
            ord_pro1_canvas.create_text(710, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 404, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 428, text="18.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 502, text="100.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 526, text="138.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 454, text="20.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 479, text="238.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          else:
            pass


          ord_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
  
          ord_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10')) 
          ord_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
          lbx_inv=Label(ord_pro1_canvas,text=inv_lst_bx21.get(1.0,END), bg="white",anchor="n",font=("Helvetica 10 "),height=1)#"Terms and Conditions"
          win_inv2 = ord_pro1_canvas.create_window(420, 570, anchor="nw", window=lbx_inv)
          ord_pro1_canvas.create_line(150, 600, 795, 600)
          text=ord_scrl_txt.get('1.0',END)
          wraped_text="\n".join(wrap(text,130))
    
        
          lbx_inv=Label(ord_pro1_canvas,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
          win_inv2 = ord_pro1_canvas.create_window(150, 603,anchor="nw", window=lbx_inv)

          ord_pro1_canvas.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    

          ord_pro1_canvas.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
        else:
          ord_pro1_frame = Frame(ord_set_frm_cpy, width=953, height=300)
          ord_pro1_frame.pack(expand=True, fill=BOTH)
          ord_pro1_frame.place(x=247,y=90)
          ord_pro1_canvas=Canvas(ord_pro1_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(ord_pro1_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=ord_pro1_canvas.yview)
          
          ord_pro1_canvas.config(width=953,height=300)
          ord_pro1_canvas.config(yscrollcommand=vertibar.set)
          ord_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          ord_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          ord_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          
          ord_pro1_canvas.create_text(195, 150, text="Order#", fill="black", font=('Helvetica 11'))
          ord_pro1_canvas.create_text(205, 170, text="Order date", fill="black", font=('Helvetica 11'))
          ord_pro1_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
          ord_pro1_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
          ord_pro1_canvas.create_text(205, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
          ord_pro1_canvas.create_text(350, 150, text="ORD1/2022", fill="black", font=('Helvetica 11'))
          ord_pro1_canvas.create_text(350, 170, text="03-05-2022", fill="black", font=('Helvetica 11'))
          ord_pro1_canvas.create_text(350, 190, text="18-05-2022", fill="black", font=('Helvetica 11'))
          ord_pro1_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

          ord_pro1_canvas.create_text(720, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
          ord_pro1_canvas.create_text(750, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(750, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(750, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(750, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(745, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(745, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(750, 205, text="Order", fill="black", font=('Helvetica 14 bold'))
          ord_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
            
          ord_pro1_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
          ord_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          ord_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
          s = ttk.Style()
          s.configure('Treeview.Heading', background=''+ ordset_win_menu1.get(),State='DISABLE')

          tree=ttk.Treeview(ord_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')

          tree.column("# 1", anchor=E, stretch=NO, width=100)
          tree.heading("# 1", text="ID/SKU")
          tree.column("# 2", anchor=E, stretch=NO, width=350)
          tree.heading("# 2", text="Product/Service - Description")
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text="Quantity")
          tree.column("# 4", anchor=E, stretch=NO, width=90)
          tree.heading("# 4", text="Unit Price")
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text="Price")
          
          window = ord_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)

          ord_pro1_canvas.create_line(120, 390, 820, 390 )
          ord_pro1_canvas.create_line(120, 340, 120, 365 )
          ord_pro1_canvas.create_line(120, 365, 120, 390 )
          ord_pro1_canvas.create_line(820, 340, 820, 540 )
          ord_pro1_canvas.create_line(740, 340, 740, 540 )
          ord_pro1_canvas.create_line(570, 340, 570, 540 )
          ord_pro1_canvas.create_line(570, 415, 820, 415 )
          ord_pro1_canvas.create_line(570, 440, 820, 440 )
          ord_pro1_canvas.create_line(570, 465, 820, 465 )
          ord_pro1_canvas.create_line(570, 490, 820, 490 )
          ord_pro1_canvas.create_line(570, 515, 820, 515 )
          ord_pro1_canvas.create_line(650, 340, 650, 390 )
          ord_pro1_canvas.create_line(220, 340, 220, 390 )
          ord_pro1_canvas.create_line(570, 540, 820, 540 )

          ord_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

          ord_pro1_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

          ord_pro1_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

          ord_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

          ord_pro1_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          ord_pro1_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

          ord_pro1_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

          ord_pro1_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

          ord_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
          ord_pro1_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_line(150, 620, 795, 620)
          

          ord_pro1_canvas.create_text(280, 640, text= "", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


    #-----------------------------------------------------------------------Professional 2 (logo on right side)
      elif cmp_mn_var == 'Professional 2 (logo on right side)':
        if cmpy_dtls is not None:
          sql='select dateformat from company'
          fbcursor.execute(sql)
          date_frmat=fbcursor.fetchone()
          
          if not date_frmat:
            ft_fr='%Y-%m-%d'
        
          elif date_frmat[0]=="mm-dd-yyyy":
            ft_fr='%m-%d-%Y'

          elif date_frmat[0]=="dd-mm-yyyy":
              ft_fr='%d-%m-%Y'
                      
          elif date_frmat[0]=="yyy.mm.dd":
              ft_fr='%Y.%m.%d'
                          
          elif date_frmat[0]=="mm/dd/yyyy":
              ft_fr='%m/%d/%Y'
                          
          elif date_frmat[0]=="dd/mm/yyyy":
              ft_fr='%d/%m/%Y'
                                  
          elif date_frmat[0]=="dd.mm.yyyy":
              ft_fr='%d.%m.%Y'
                                  
          elif date_frmat[0]=="yyyy/  mm/dd":
              ft_fr='%Y/%m/%d'

          else:
              ft_fr='%Y-%m-%d'
          td_date=date.today()
          date_tdy=td_date.strftime(ft_fr)
          ord_pro2_frame = Frame(ord_set_frm_cpy, width=953, height=300)
          ord_pro2_frame.pack(expand=True, fill=BOTH)
          ord_pro2_frame.place(x=247,y=90)
          
          ord_pro2_canvas=Canvas(ord_pro2_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(ord_pro2_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=ord_pro2_canvas.yview)
          ord_pro2_canvas.config(width=953,height=300)
          
          ord_pro2_canvas.config(yscrollcommand=vertibar.set)
          ord_pro2_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          ord_pro2_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          ord_pro2_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            inv_image = Image.open("images/"+cmpy_dtl[13])
            inv_resize_image = inv_image.resize((200,75))
            inv_image = ImageTk.PhotoImage(inv_resize_image)
          
            inv_logo = Label(ord_pro2_canvas,width=200,height=75, bg="white",image = inv_image) 
            inv_window_image = ord_pro2_canvas.create_window(800, 60, anchor="ne", window=inv_logo)
            inv_logo.photo = inv_image
          except:
            ord_pro2_canvas.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          labelcmp=Label(ord_pro2_canvas,text=cmpy_dtl[1],justify=LEFT, bg="white",anchor="nw",font=("Helvetica", 12), width=40, height=1)
          window = ord_pro2_canvas.create_window(150,80, anchor="nw", window=labelcmp)

          labelcmpl=Label(ord_pro2_canvas,text=cmpy_dtl[2],justify=LEFT, bg="white",font=("Helvetica", 9),anchor="nw", width=40, height=4)
          windowl = ord_pro2_canvas.create_window(155 ,110, anchor="nw", window=labelcmpl)
          
          ord_pro2_canvas.create_text(210, 185, text=cmpy_dtl[4],justify=LEFT, fill="black", font=('Helvetica 9'))

          lb_inv1=Label(ord_pro2_canvas,text=ord_lft_tp2.get(1.0, END), bg="white",anchor="ne",font=("Helvetica", 11),height=1)#Order#"
          win_inv1 = ord_pro2_canvas.create_window(550, 140, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_pro2_canvas,text=ord_lft_tp3.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", 11),height=1 )#Invoicedate
          win_inv1 = ord_pro2_canvas.create_window(550, 160, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(ord_pro2_canvas,text=ord_lft_tp4.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Due date
          win_inv1 = ord_pro2_canvas.create_window(550, 180, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_pro2_canvas,text=inv_lst_bx5.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", 11),height=1)#Terms
          win_inv1 = ord_pro2_canvas.create_window(550, 200, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_pro2_canvas,text=inv_lst_bx4.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = ord_pro2_canvas.create_window(550, 220, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(ord_pro2_canvas,text=ord_lft_tp1.get(1.0,END), bg="white",anchor="ne",font=('Helvetica 14 bold'),height=1)#invoice
          win_inv1 = ord_pro2_canvas.create_window(155, 200, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_pro2_canvas,text=ord_lft_tp5.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline" ),height=1)#Order to
          win_inv1 = ord_pro2_canvas.create_window(175, 250, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_pro2_canvas,text=inv_lst_bx7.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline"),height=1)#Ship to
          win_inv1 = ord_pro2_canvas.create_window(525, 250, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_pro2_canvas,text=str(ord_lft_tp.get())+"1/2022", bg="white",justify=LEFT,font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = ord_pro2_canvas.create_window(790, 140, anchor="ne", window=lb_inv1)

          
          ord_pro2_canvas.create_text(750, 170, text=date_tdy, fill="black", font=('Helvetica 11'))
          ord_pro2_canvas.create_text(750, 190, text=date_tdy, fill="black", font=('Helvetica 11'))
          ord_pro2_canvas.create_text(740, 210, text="NET 15", fill="black", font=('Helvetica 11'))  
            
        
          ord_pro2_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_pro2_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))

          ord_pro2_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_pro2_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

          phf = ttk.Style()
          phf.configure('mystyle123.Treeview.Heading', background=''+ ord_man_var.get(),State='DISABLE')
          tree=ttk.Treeview(ord_pro2_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle123.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=100)
          tree.heading("# 1", text=inv_lst_bx8.get(1.0,END))
          tree.column("# 2", anchor=E, stretch=NO, width=350)
          tree.heading("# 2", text=inv_lst_bx9.get(1.0,END))
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text=inv_lst_bx10.get(1.0,END))
          tree.column("# 4", anchor=E, stretch=NO, width=90)
          tree.heading("# 4", text=inv_lst_bx12.get(1.0,END))
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text=inv_lst_bx13.get(1.0,END))
          
          window = ord_pro2_canvas.create_window(120, 340, anchor="nw", window=tree)

          ord_pro2_canvas.create_line(120, 390, 820, 390 )
          ord_pro2_canvas.create_line(120, 340, 120, 365 )
          ord_pro2_canvas.create_line(120, 365, 120, 390 )
          ord_pro2_canvas.create_line(820, 340, 820, 540 )
          ord_pro2_canvas.create_line(740, 340, 740, 540 )
          ord_pro2_canvas.create_line(570, 340, 570, 540 )
          ord_pro2_canvas.create_line(570, 415, 820, 415 )
          ord_pro2_canvas.create_line(570, 440, 820, 440 )
          ord_pro2_canvas.create_line(570, 465, 820, 465 )
          ord_pro2_canvas.create_line(570, 490, 820, 490 )
          ord_pro2_canvas.create_line(570, 515, 820, 515 )
          ord_pro2_canvas.create_line(650, 340, 650, 390 )
          ord_pro2_canvas.create_line(220, 340, 220, 390 )
          ord_pro2_canvas.create_line(570, 540, 820, 540 )

          sqlr= 'select currencysign from company'
          fbcursor.execute(sqlr)
          crncy=fbcursor.fetchone()
          crcy_type=crncy[0]
          sqlrt= 'select currsignplace from company'
          fbcursor.execute(sqlrt)
          post_rp=fbcursor.fetchone()
          cry_plcy=post_rp[0]
          if cry_plcy=="before amount": 
            ord_pro2_canvas.create_text(710, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 404, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(792, 428, text=str(crcy_type)+"18.00", fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 502, text=str(crcy_type)+"100.00", fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 526, text=str(crcy_type)+"138.00", fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(792, 454, text=str(crcy_type)+"20.00", fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 479, text=str(crcy_type)+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount":
            ord_pro2_canvas.create_text(710, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 404, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(792, 428, text="18.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 502, text="100.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 526, text="138.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(792, 454, text="20.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 479, text="238.00"+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="before amount with space": 
            ord_pro2_canvas.create_text(710, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 404, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(792, 428, text=str(crcy_type)+" "+"18.00", fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 502, text=str(crcy_type)+" "+"100.00", fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 526, text=str(crcy_type)+" "+"138.00", fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(792, 454, text=str(crcy_type)+" "+"20.00", fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 479, text=str(crcy_type)+" "+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount with space":
            ord_pro2_canvas.create_text(710, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 404, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(792, 428, text="18.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 502, text="100.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 526, text="138.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(792, 454, text="20.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro2_canvas.create_text(790, 479, text="238.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          else:
            pass

          ord_pro2_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
      
          ord_pro2_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
      
        

          lbx_inv=Label(ord_pro2_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
          win_inv2 = ord_pro2_canvas.create_window(630,392, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_pro2_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
          win_inv2 = ord_pro2_canvas.create_window(635,418, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_pro2_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
          win_inv2 = ord_pro2_canvas.create_window(630, 492,anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_pro2_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
          win_inv2 = ord_pro2_canvas.create_window(635, 518, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_pro2_canvas,text=ord_lft_tp6.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#Order Total"
          win_inv2 = ord_pro2_canvas.create_window(630, 468, anchor="nw", window=lbx_inv)
          
          ord_pro2_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
          lbx_inv=Label(ord_pro2_canvas,text=inv_lst_bx21.get(1.0,END), bg="white",anchor="n",font=("Helvetica 10 "),height=1)#"Terms and Conditions"
          win_inv2 = ord_pro2_canvas.create_window(420, 570, anchor="nw", window=lbx_inv)
          ord_pro2_canvas.create_line(150, 600, 795, 600)
          text=ord_scrl_txt.get('1.0',END)
          wraped_text="\n".join(wrap(text,130))
    
        
          lbx_inv=Label(ord_pro2_canvas,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
          win_inv2 = ord_pro2_canvas.create_window(150, 603,anchor="nw", window=lbx_inv)

          ord_pro2_canvas.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    

          ord_pro2_canvas.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
        else:
          ord_pro2_frame = Frame(ord_set_frm_cpy, width=953, height=300)
          ord_pro2_frame.pack(expand=True, fill=BOTH)
          ord_pro2_frame.place(x=247,y=90)
          
          ord_pro2_canvas=Canvas(ord_pro2_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(ord_pro2_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=ord_pro2_canvas.yview)
          ord_pro2_canvas.config(width=953,height=300)
          
          ord_pro2_canvas.config(yscrollcommand=vertibar.set)
          ord_pro2_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          ord_pro2_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          ord_pro2_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          
          ord_pro2_canvas.create_text(250, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
          ord_pro2_canvas.create_text(225, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(225, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(225, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(225, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(234, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(234, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(225, 205, text="Order", fill="black", font=('Helvetica 14 bold'))
          ord_pro2_canvas.create_text(232, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
          ord_pro2_canvas.create_text(502, 150, text="Order#", fill="black", font=('Helvetica 11'))
          ord_pro2_canvas.create_text(515, 170, text="Order date", fill="black", font=('Helvetica 11'))
          ord_pro2_canvas.create_text(500, 190, text="Due date", fill="black", font=('Helvetica 11'))
          ord_pro2_canvas.create_text(491, 210, text="Terms", fill="black", font=('Helvetica 11'))
          ord_pro2_canvas.create_text(505, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
          ord_pro2_canvas.create_text(680, 150, text="ORD1/2022", fill="black", font=('Helvetica 11'))
          ord_pro2_canvas.create_text(680, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
          ord_pro2_canvas.create_text(680, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
          ord_pro2_canvas.create_text(670, 210, text="NET 15", fill="black", font=('Helvetica 11'))  
            
          ord_pro2_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
          ord_pro2_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_pro2_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          ord_pro2_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_pro2_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

          tree=ttk.Treeview(ord_pro2_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=100)
          tree.heading("# 1", text="ID/SKU")
          tree.column("# 2", anchor=E, stretch=NO, width=350)
          tree.heading("# 2", text="Product/Service - Description")
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text="Quantity")
          tree.column("# 4", anchor=E, stretch=NO, width=90)
          tree.heading("# 4", text="Unit Price")
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text="Price")
          
          window = ord_pro2_canvas.create_window(120, 340, anchor="nw", window=tree)

          ord_pro2_canvas.create_line(120, 390, 820, 390 )
          ord_pro2_canvas.create_line(120, 340, 120, 365 )
          ord_pro2_canvas.create_line(120, 365, 120, 390 )
          ord_pro2_canvas.create_line(820, 340, 820, 540 )
          ord_pro2_canvas.create_line(740, 340, 740, 540 )
          ord_pro2_canvas.create_line(570, 340, 570, 540 )
          ord_pro2_canvas.create_line(570, 415, 820, 415 )
          ord_pro2_canvas.create_line(570, 440, 820, 440 )
          ord_pro2_canvas.create_line(570, 465, 820, 465 )
          ord_pro2_canvas.create_line(570, 490, 820, 490 )
          ord_pro2_canvas.create_line(570, 515, 820, 515 )
          ord_pro2_canvas.create_line(650, 340, 650, 390 )
          ord_pro2_canvas.create_line(220, 340, 220, 390 )
          ord_pro2_canvas.create_line(570, 540, 820, 540 )

          ord_pro2_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

          ord_pro2_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

          ord_pro2_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

          ord_pro2_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

          ord_pro2_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          ord_pro2_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

          ord_pro2_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

          ord_pro2_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

          ord_pro2_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

          ord_pro2_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_line(150, 620, 795, 620)
          ord_pro2_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          ord_pro2_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


    #----------------------------------------------------------------------Simplified 1 (logo on left side)
      elif cmp_mn_var == 'Simplified 1 (logo on left side)':
        if cmpy_dtls is not None:
          sql='select dateformat from company'
          fbcursor.execute(sql)
          date_frmat=fbcursor.fetchone()
          
          if not date_frmat:
            ft_fr='%Y-%m-%d'
        
          elif date_frmat[0]=="mm-dd-yyyy":
            ft_fr='%m-%d-%Y'

          elif date_frmat[0]=="dd-mm-yyyy":
              ft_fr='%d-%m-%Y'
                      
          elif date_frmat[0]=="yyy.mm.dd":
              ft_fr='%Y.%m.%d'
                          
          elif date_frmat[0]=="mm/dd/yyyy":
              ft_fr='%m/%d/%Y'
                          
          elif date_frmat[0]=="dd/mm/yyyy":
              ft_fr='%d/%m/%Y'
                                  
          elif date_frmat[0]=="dd.mm.yyyy":
              ft_fr='%d.%m.%Y'
                                  
          elif date_frmat[0]=="yyyy/  mm/dd":
              ft_fr='%Y/%m/%d'

          else:
              ft_fr='%Y-%m-%d'
          td_date=date.today()
          date_tdy=td_date.strftime(ft_fr)
          ord_smply_frame = Frame(ord_set_frm_cpy, width=953, height=300)
          ord_smply_frame.pack(expand=True, fill=BOTH)
          ord_smply_frame.place(x=247,y=90)
          ord_smply_canvas=Canvas(ord_smply_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(ord_smply_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=ord_smply_canvas.yview)
          ord_smply_canvas.config(width=953,height=300)

          ord_smply_canvas.config(yscrollcommand=vertibar.set)
          ord_smply_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          ord_smply_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          ord_smply_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            inv_image = Image.open("images/"+cmpy_dtl[13])
            inv_resize_image = inv_image.resize((200,75))
            inv_image = ImageTk.PhotoImage(inv_resize_image)
          
            inv_logo = Label(ord_smply_canvas,width=200,height=75, bg="white",image = inv_image) 
            inv_window_image = ord_smply_canvas.create_window(150, 50, anchor="nw", window=inv_logo)
            inv_logo.photo = inv_image
          except:
            ord_smply_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          
          lb_inv1=Label(ord_smply_canvas,text=ord_lft_tp1.get(1.0,END), bg="white",anchor="ne",font=('Helvetica 14 bold'),height=1)#Order
          win_inv1 = ord_smply_canvas.create_window(800, 200, anchor="ne", window=lb_inv1)

    

          lb_inv1=Label(ord_smply_canvas,text=ord_lft_tp5.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline" ),height=1)#Order to
          win_inv1 = ord_smply_canvas.create_window(175, 250, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_smply_canvas,text=inv_lst_bx7.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline"),height=1)#Ship to
          win_inv1 = ord_smply_canvas.create_window(525, 250, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_smply_canvas,text=ord_lft_tp2.get(1.0, END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Order#"
          win_inv1 = ord_smply_canvas.create_window(175, 140, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_smply_canvas,text=ord_lft_tp3.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1 )#Order date
          win_inv1 = ord_smply_canvas.create_window(175, 160, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(ord_smply_canvas,text=ord_lft_tp4.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Due date
          win_inv1 = ord_smply_canvas.create_window(175, 180, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_smply_canvas,text=inv_lst_bx5.get(1.0,END), bg="white",justify=LEFT,font=("Helvetica", 11),height=2)#Terms
          win_inv1 = ord_smply_canvas.create_window(175, 200, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_smply_canvas,text=inv_lst_bx4.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", ),height=1)#Order ref.#
          win_inv1 = ord_smply_canvas.create_window(175, 220, anchor="nw", window=lb_inv1)


        

        
          lb_inv1=Label(ord_smply_canvas,text=str(ord_lft_tp.get())+"1/2022", bg="white",anchor="nw",font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = ord_smply_canvas.create_window(310, 140, anchor="nw", window=lb_inv1)

          ord_smply_canvas.create_text(350, 170, text=date_tdy, fill="black", font=('Helvetica 11'))
          ord_smply_canvas.create_text(350, 190, text=date_tdy, fill="black", font=('Helvetica 11'))
          ord_smply_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

          labelcmp=Label(ord_smply_canvas,text=cmpy_dtl[1], bg="white",anchor="e",font=("Helvetica", 12), width=40, height=1)
          window = ord_smply_canvas.create_window(430,80, anchor="nw", window=labelcmp)

          labelcmpl=Label(ord_smply_canvas,text=cmpy_dtl[2],justify=RIGHT, bg="white",font=("Helvetica", 9),anchor="ne", width=50, height=4)
          windowl = ord_smply_canvas.create_window(440,110, anchor="nw", window=labelcmpl)

          
          ord_smply_canvas.create_text(740, 185, text=cmpy_dtl[4], fill="black", font=('Helvetica 9'))
        

          
    
          ord_smply_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_smply_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    
          ord_smply_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_smply_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
          phf = ttk.Style()
          phf.configure('mystyle124.Treeview.Heading', background=''+ ord_man_var.get(),State='DISABLE')
          tree=ttk.Treeview(ord_smply_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle124.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=530)
          tree.heading("# 1", text=inv_lst_bx9.get(1.0,END))
          tree.column("# 2", anchor=E, stretch=NO, width=90)
          tree.heading("# 2", text=inv_lst_bx10.get(1.0,END))
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text=inv_lst_bx13.get(1.0,END))
          
          window = ord_smply_canvas.create_window(120, 340, anchor="nw", window=tree)

          ord_smply_canvas.create_line(120, 390, 820, 390 )
          ord_smply_canvas.create_line(120, 340, 120, 365 )
          ord_smply_canvas.create_line(120, 365, 120, 390 )
          ord_smply_canvas.create_line(820, 340, 820, 540 )
          ord_smply_canvas.create_line(740, 340, 740, 540 )
          ord_smply_canvas.create_line(570, 390, 570, 540 )
          ord_smply_canvas.create_line(570, 415, 820, 415 )
          ord_smply_canvas.create_line(570, 440, 820, 440 )
          ord_smply_canvas.create_line(570, 465, 820, 465 )
          ord_smply_canvas.create_line(570, 490, 820, 490 )
          ord_smply_canvas.create_line(570, 515, 820, 515 )
          ord_smply_canvas.create_line(650, 340, 650, 390 )
          ord_smply_canvas.create_line(570, 540, 820, 540 )

          lbx_inv=Label(ord_smply_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
          win_inv2 = ord_smply_canvas.create_window(630,392, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_smply_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
          win_inv2 = ord_smply_canvas.create_window(635,418, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_smply_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
          win_inv2 = ord_smply_canvas.create_window(630, 492,anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_smply_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
          win_inv2 = ord_smply_canvas.create_window(635, 518, anchor="nw", window=lbx_inv)

          lb_inv1=Label(ord_smply_canvas,text=ord_lft_tp5.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline" ),height=1)#Order to
          win_inv1 = ord_smply_canvas.create_window(175, 250, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_smply_canvas,text=inv_lst_bx7.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline"),height=1)#Ship to
          win_inv1 = ord_smply_canvas.create_window(525, 250, anchor="nw", window=lb_inv1)

          lbx_inv=Label(ord_smply_canvas,text=ord_lft_tp6.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#Order Total"
          win_inv2 = ord_smply_canvas.create_window(630, 468, anchor="nw", window=lbx_inv)

          sqlr= 'select currencysign from company'
          fbcursor.execute(sqlr)
          crncy=fbcursor.fetchone()
          crcy_type=crncy[0]
          sqlrt= 'select currsignplace from company'
          fbcursor.execute(sqlrt)
          post_rp=fbcursor.fetchone()
          cry_plcy=post_rp[0]
          if cry_plcy=="before amount": 
            ord_smply_canvas.create_text(710, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 404, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(792, 428, text=str(crcy_type)+"18.00", fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 502, text=str(crcy_type)+"100.00", fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 526, text=str(crcy_type)+"138.00", fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(792, 454, text=str(crcy_type)+"20.00", fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 479, text=str(crcy_type)+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount":
            ord_smply_canvas.create_text(710, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 404, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(792, 428, text="18.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 502, text="100.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 526, text="138.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(792, 454, text="20.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 479, text="238.00"+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="before amount with space": 
            ord_smply_canvas.create_text(710, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 404, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(792, 428, text=str(crcy_type)+" "+"18.00", fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 502, text=str(crcy_type)+" "+"100.00", fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 526, text=str(crcy_type)+" "+"138.00", fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(792, 454, text=str(crcy_type)+" "+"20.00", fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 479, text=str(crcy_type)+" "+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount with space":
            ord_smply_canvas.create_text(710, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 404, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(792, 428, text="18.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 502, text="100.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 526, text="138.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(792, 454, text="20.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply_canvas.create_text(790, 479, text="238.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          else:
            pass



          ord_smply_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

          

          ord_smply_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        

          ord_smply_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
          lbx_inv=Label(ord_smply_canvas,text=inv_lst_bx21.get(1.0,END), bg="white",anchor="n",font=("Helvetica 10 "),height=1)#"Terms and Conditions"
          win_inv2 = ord_smply_canvas.create_window(420, 570, anchor="nw", window=lbx_inv)
          ord_smply_canvas.create_line(150, 600, 795, 600)
          text=ord_scrl_txt.get('1.0',END)
          wraped_text="\n".join(wrap(text,130))
    
        
          lbx_inv=Label(ord_smply_canvas,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
          win_inv2 = ord_smply_canvas.create_window(150, 603,anchor="nw", window=lbx_inv)

          ord_smply_canvas.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    

          ord_smply_canvas.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
        else:

          ord_smply_frame = Frame(ord_set_frm_cpy, width=953, height=300)
          ord_smply_frame.pack(expand=True, fill=BOTH)
          ord_smply_frame.place(x=247,y=90)
          ord_smply_canvas=Canvas(ord_smply_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(ord_smply_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=ord_smply_canvas.yview)
          ord_smply_canvas.config(width=953,height=300)

          ord_smply_canvas.config(yscrollcommand=vertibar.set)
          ord_smply_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          ord_smply_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          ord_smply_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          ord_smply_canvas.create_text(202, 150, text="Order#", fill="black", font=('Helvetica 11'))
          ord_smply_canvas.create_text(215, 170, text="Order date", fill="black", font=('Helvetica 11'))
          ord_smply_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
          ord_smply_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
          ord_smply_canvas.create_text(205, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
          ord_smply_canvas.create_text(350, 150, text="EST1/2022", fill="black", font=('Helvetica 11'))
          ord_smply_canvas.create_text(350, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
          ord_smply_canvas.create_text(350, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
          ord_smply_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

          ord_smply_canvas.create_text(720, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
          ord_smply_canvas.create_text(750, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(750, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(750, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(750, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(745, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(745, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(750, 205, text="Order", fill="black", font=('Helvetica 14 bold'))
          
          ord_smply_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
          ord_smply_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_smply_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          ord_smply_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_smply_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

          tree=ttk.Treeview(ord_smply_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=530)
          tree.heading("# 1", text="Product/Service - Description")
          tree.column("# 2", anchor=E, stretch=NO, width=90)
          tree.heading("# 2", text="Quantity")
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text="Price")
          
          window = ord_smply_canvas.create_window(120, 340, anchor="nw", window=tree)

          ord_smply_canvas.create_line(120, 390, 820, 390 )
          ord_smply_canvas.create_line(120, 340, 120, 365 )
          ord_smply_canvas.create_line(120, 365, 120, 390 )
          ord_smply_canvas.create_line(820, 340, 820, 540 )
          ord_smply_canvas.create_line(740, 340, 740, 540 )
          ord_smply_canvas.create_line(570, 390, 570, 540 )
          ord_smply_canvas.create_line(570, 415, 820, 415 )
          ord_smply_canvas.create_line(570, 440, 820, 440 )
          ord_smply_canvas.create_line(570, 465, 820, 465 )
          ord_smply_canvas.create_line(570, 490, 820, 490 )
          ord_smply_canvas.create_line(570, 515, 820, 515 )
          ord_smply_canvas.create_line(650, 340, 650, 390 )
          ord_smply_canvas.create_line(570, 540, 820, 540 )

          
          ord_smply_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

          ord_smply_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

          ord_smply_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

          ord_smply_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

          ord_smply_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          ord_smply_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

          ord_smply_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

          ord_smply_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

          ord_smply_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

          ord_smply_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_line(150, 620, 795, 620)
          ord_smply_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          ord_smply_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

    #-------------------------------------------------------------------------------Simplified 2 (logo on right side)
      elif cmp_mn_var == 'Simplified 2 (logo on right side)':
        if cmpy_dtls is not None:
          sql='select dateformat from company'
          fbcursor.execute(sql)
          date_frmat=fbcursor.fetchone()
          
          if not date_frmat:
            ft_fr='%Y-%m-%d'
        
          elif date_frmat[0]=="mm-dd-yyyy":
            ft_fr='%m-%d-%Y'

          elif date_frmat[0]=="dd-mm-yyyy":
              ft_fr='%d-%m-%Y'
                      
          elif date_frmat[0]=="yyy.mm.dd":
              ft_fr='%Y.%m.%d'
                          
          elif date_frmat[0]=="mm/dd/yyyy":
              ft_fr='%m/%d/%Y'
                          
          elif date_frmat[0]=="dd/mm/yyyy":
              ft_fr='%d/%m/%Y'
                                  
          elif date_frmat[0]=="dd.mm.yyyy":
              ft_fr='%d.%m.%Y'
                                  
          elif date_frmat[0]=="yyyy/  mm/dd":
              ft_fr='%Y/%m/%d'

          else:
              ft_fr='%Y-%m-%d'
          td_date=date.today()
          date_tdy=td_date.strftime(ft_fr)
          ord_smply2_frame = Frame(ord_set_frm_cpy, width=953, height=300)
          ord_smply2_frame.pack(expand=True, fill=BOTH)
          ord_smply2_frame.place(x=247,y=90)

          ord_smply2_canvas=Canvas(ord_smply2_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(ord_smply2_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=ord_smply2_canvas.yview)
          ord_smply2_canvas.config(width=953,height=300)

          ord_smply2_canvas.config(yscrollcommand=vertibar.set)
          ord_smply2_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          ord_smply2_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          ord_smply2_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            inv_image = Image.open("images/"+cmpy_dtl[13])
            inv_resize_image = inv_image.resize((200,75))
            inv_image = ImageTk.PhotoImage(inv_resize_image)
          
            inv_logo = Label(ord_smply2_canvas,width=200,height=75, bg="white",image = inv_image) 
            inv_window_image = ord_smply2_canvas.create_window(800, 60, anchor="ne", window=inv_logo)
            inv_logo.photo = inv_image
          except:
            ord_smply2_canvas.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          labelcmp=Label(ord_smply2_canvas,text=cmpy_dtl[1],justify=LEFT, bg="white",anchor="nw",font=("Helvetica", 12), width=40, height=1)
          window = ord_smply2_canvas.create_window(150,80, anchor="nw", window=labelcmp)

          labelcmpl=Label(ord_smply2_canvas,text=cmpy_dtl[2],justify=LEFT, bg="white",font=("Helvetica", 9),anchor="nw", width=40, height=4)
          windowl = ord_smply2_canvas.create_window(155 ,110, anchor="nw", window=labelcmpl)
          
          ord_smply2_canvas.create_text(210, 185, text=cmpy_dtl[4],justify=LEFT, fill="black", font=('Helvetica 9'))
          lb_inv1=Label(ord_smply2_canvas,text=ord_lft_tp2.get(1.0, END), bg="white",anchor="ne",font=("Helvetica", 11),height=1)#Order#"
          win_inv1 = ord_smply2_canvas.create_window(550, 140, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_smply2_canvas,text=ord_lft_tp3.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", 11),height=1 )#Invoicedate
          win_inv1 = ord_smply2_canvas.create_window(550, 160, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(ord_smply2_canvas,text=ord_lft_tp4.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Due date
          win_inv1 = ord_smply2_canvas.create_window(550, 180, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_smply2_canvas,text=inv_lst_bx5.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", 11),height=1)#Terms
          win_inv1 = ord_smply2_canvas.create_window(550, 200, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_smply2_canvas,text=inv_lst_bx4.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = ord_smply2_canvas.create_window(550, 220, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(ord_smply2_canvas,text=ord_lft_tp1.get(1.0,END), bg="white",anchor="ne",font=('Helvetica 14 bold'),height=1)#invoice
          win_inv1 = ord_smply2_canvas.create_window(155, 200, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_smply2_canvas,text=ord_lft_tp5.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline" ),height=1)#Order to
          win_inv1 = ord_smply2_canvas.create_window(175, 250, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_smply2_canvas,text=inv_lst_bx7.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline"),height=1)#Ship to
          win_inv1 = ord_smply2_canvas.create_window(525, 250, anchor="nw", window=lb_inv1)


          lb_inv1=Label(ord_smply2_canvas,text=str(ord_lft_tp.get())+"1/2022", bg="white",anchor="nw",font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = ord_smply2_canvas.create_window(640, 140, anchor="nw", window=lb_inv1)
          ord_smply2_canvas.create_text(680, 170, text=date_tdy, fill="black", font=('Helvetica 11'))
          ord_smply2_canvas.create_text(680, 190, text=date_tdy, fill="black", font=('Helvetica 11'))
          ord_smply2_canvas.create_text(670, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

          
          ord_smply2_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_smply2_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))

          ord_smply2_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_smply2_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

          phf = ttk.Style()
          phf.configure('mystyle125.Treeview.Heading', background=''+ ord_man_var.get(),State='DISABLE')

          tree=ttk.Treeview(ord_smply2_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle125.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=530)
          tree.heading("# 1", text=inv_lst_bx9.get(1.0,END))
          tree.column("# 2", anchor=E, stretch=NO, width=90)
          tree.heading("# 2", text=inv_lst_bx10.get(1.0,END))
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text=inv_lst_bx13.get(1.0,END))
          
          window = ord_smply2_canvas.create_window(120, 340, anchor="nw", window=tree)

          ord_smply2_canvas.create_line(120, 390, 820, 390 )
          ord_smply2_canvas.create_line(120, 340, 120, 365 )
          ord_smply2_canvas.create_line(120, 365, 120, 390 )
          ord_smply2_canvas.create_line(820, 340, 820, 540 )
          ord_smply2_canvas.create_line(740, 340, 740, 540 )
          ord_smply2_canvas.create_line(570, 390, 570, 540 )
          ord_smply2_canvas.create_line(570, 415, 820, 415 )
          ord_smply2_canvas.create_line(570, 440, 820, 440 )
          ord_smply2_canvas.create_line(570, 465, 820, 465 )
          ord_smply2_canvas.create_line(570, 490, 820, 490 )
          ord_smply2_canvas.create_line(570, 515, 820, 515 )
          ord_smply2_canvas.create_line(650, 340, 650, 390 )
          ord_smply2_canvas.create_line(570, 540, 820, 540 )

          sqlr= 'select currencysign from company'
          fbcursor.execute(sqlr)
          crncy=fbcursor.fetchone()
          crcy_type=crncy[0]
          sqlrt= 'select currsignplace from company'
          fbcursor.execute(sqlrt)
          post_rp=fbcursor.fetchone()
          cry_plcy=post_rp[0]
          if cry_plcy=="before amount": 
            ord_smply2_canvas.create_text(710, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 404, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(792, 428, text=str(crcy_type)+"18.00", fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 502, text=str(crcy_type)+"100.00", fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 526, text=str(crcy_type)+"138.00", fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(792, 454, text=str(crcy_type)+"20.00", fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 479, text=str(crcy_type)+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount":
            ord_smply2_canvas.create_text(710, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 404, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(792, 428, text="18.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 502, text="100.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 526, text="138.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(792, 454, text="20.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 479, text="238.00"+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="before amount with space": 
            ord_smply2_canvas.create_text(710, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 404, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(792, 428, text=str(crcy_type)+" "+"18.00", fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 502, text=str(crcy_type)+" "+"100.00", fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 526, text=str(crcy_type)+" "+"138.00", fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(792, 454, text=str(crcy_type)+" "+"20.00", fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 479, text=str(crcy_type)+" "+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount with space":
            ord_smply2_canvas.create_text(710, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 404, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(792, 428, text="18.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 502, text="100.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 526, text="138.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(792, 454, text="20.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_smply2_canvas.create_text(790, 479, text="238.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          else:
            pass


          
          ord_smply2_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))


          ord_smply2_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
      

          lbx_inv=Label(ord_smply2_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
          win_inv2 = ord_smply2_canvas.create_window(630,392, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_smply2_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
          win_inv2 = ord_smply2_canvas.create_window(635,418, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_smply2_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
          win_inv2 = ord_smply2_canvas.create_window(630, 492,anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_smply2_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
          win_inv2 = ord_smply2_canvas.create_window(635, 518, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_smply2_canvas,text=ord_lft_tp6.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#Order Total"
          win_inv2 = ord_smply2_canvas.create_window(630, 468, anchor="nw", window=lbx_inv)
          
          ord_smply2_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
          lbx_inv=Label(ord_smply2_canvas,text=inv_lst_bx21.get(1.0,END), bg="white",anchor="n",font=("Helvetica 10 "),height=1)#"Terms and Conditions"
          win_inv2 = ord_smply2_canvas.create_window(420, 570, anchor="nw", window=lbx_inv)
          ord_smply2_canvas.create_line(150, 600, 795, 600)
          text=ord_scrl_txt.get('1.0',END)
          wraped_text="\n".join(wrap(text,130))
    
        
          lbx_inv=Label(ord_smply2_canvas,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
          win_inv2 = ord_smply2_canvas.create_window(150, 603,anchor="nw", window=lbx_inv)

          ord_smply2_canvas.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    

          ord_smply2_canvas.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
        else:
          ord_smply2_frame = Frame(ord_set_frm_cpy, width=953, height=300)
          ord_smply2_frame.pack(expand=True, fill=BOTH)
          ord_smply2_frame.place(x=247,y=90)

          ord_smply2_canvas=Canvas(ord_smply2_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(ord_smply2_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=ord_smply2_canvas.yview)
          ord_smply2_canvas.config(width=953,height=300)

          ord_smply2_canvas.config(yscrollcommand=vertibar.set)
          ord_smply2_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          ord_smply2_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          ord_smply2_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(650, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          ord_smply2_canvas.create_text(250, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
          ord_smply2_canvas.create_text(225, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(225, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(225, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(225, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(234, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(234, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(225, 205, text="Order", fill="black", font=('Helvetica 14 bold'))

          ord_smply2_canvas.create_text(502, 150, text="Order#", fill="black", font=('Helvetica 11'))
          ord_smply2_canvas.create_text(515, 170, text="Order date", fill="black", font=('Helvetica 11'))
          ord_smply2_canvas.create_text(500, 190, text="Due date", fill="black", font=('Helvetica 11'))
          ord_smply2_canvas.create_text(491, 210, text="Terms", fill="black", font=('Helvetica 11'))
          ord_smply2_canvas.create_text(505, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
          ord_smply2_canvas.create_text(680, 150, text="EST1/2022", fill="black", font=('Helvetica 11'))
          ord_smply2_canvas.create_text(680, 170, text="05-05-2022", fill="black", font=('Helvetica 11'))
          ord_smply2_canvas.create_text(680, 190, text="20-05-2022", fill="black", font=('Helvetica 11'))
          ord_smply2_canvas.create_text(670, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

          ord_smply2_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
          ord_smply2_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_smply2_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          ord_smply2_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_smply2_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

          tree=ttk.Treeview(ord_smply2_canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=530)
          tree.heading("# 1", text="Product/Service - Description")
          tree.column("# 2", anchor=E, stretch=NO, width=90)
          tree.heading("# 2", text="Quantity")
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text="Price")
          
          window = ord_smply2_canvas.create_window(120, 340, anchor="nw", window=tree)

          ord_smply2_canvas.create_line(120, 390, 820, 390 )
          ord_smply2_canvas.create_line(120, 340, 120, 365 )
          ord_smply2_canvas.create_line(120, 365, 120, 390 )
          ord_smply2_canvas.create_line(820, 340, 820, 540 )
          ord_smply2_canvas.create_line(740, 340, 740, 540 )
          ord_smply2_canvas.create_line(570, 390, 570, 540 )
          ord_smply2_canvas.create_line(570, 415, 820, 415 )
          ord_smply2_canvas.create_line(570, 440, 820, 440 )
          ord_smply2_canvas.create_line(570, 465, 820, 465 )
          ord_smply2_canvas.create_line(570, 490, 820, 490 )
          ord_smply2_canvas.create_line(570, 515, 820, 515 )
          ord_smply2_canvas.create_line(650, 340, 650, 390 )
          ord_smply2_canvas.create_line(570, 540, 820, 540 )

          
          ord_smply2_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

          ord_smply2_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

          ord_smply2_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

          ord_smply2_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

          ord_smply2_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          ord_smply2_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

          ord_smply2_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

          ord_smply2_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

          ord_smply2_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

          ord_smply2_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_line(150, 620, 795, 620)
          ord_smply2_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          ord_smply2_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

    #-----------------------------------------------------------------------------------------------Business Classic-
      elif cmp_mn_var == 'Business Classic':
        if cmpy_dtls is not None:
          sql='select dateformat from company'
          fbcursor.execute(sql)
          date_frmat=fbcursor.fetchone()
          
          if not date_frmat:
            ft_fr='%Y-%m-%d'
        
          elif date_frmat[0]=="mm-dd-yyyy":
            ft_fr='%m-%d-%Y'

          elif date_frmat[0]=="dd-mm-yyyy":
              ft_fr='%d-%m-%Y'
                      
          elif date_frmat[0]=="yyy.mm.dd":
              ft_fr='%Y.%m.%d'
                          
          elif date_frmat[0]=="mm/dd/yyyy":
              ft_fr='%m/%d/%Y'
                          
          elif date_frmat[0]=="dd/mm/yyyy":
              ft_fr='%d/%m/%Y'
                                  
          elif date_frmat[0]=="dd.mm.yyyy":
              ft_fr='%d.%m.%Y'
                                  
          elif date_frmat[0]=="yyyy/  mm/dd":
              ft_fr='%Y/%m/%d'

          else:
              ft_fr='%Y-%m-%d'
          td_date=date.today()
          date_tdy=td_date.strftime(ft_fr)
          ord_bs_frame = Frame(ord_set_frm_cpy, width=953, height=300)
          ord_bs_frame.pack(expand=True, fill=BOTH)
          ord_bs_frame.place(x=247,y=90)
          
          ord_bs_canvas=Canvas(ord_bs_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(ord_bs_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=ord_bs_canvas.yview)
          ord_bs_canvas.config(width=953,height=300)
          
          ord_bs_canvas.config(yscrollcommand=vertibar.set)
          ord_bs_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          ord_bs_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          ord_bs_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_line(150, 70, 800, 70, fill='orange')
          try:
            inv_image = Image.open("images/"+cmpy_dtl[13])
            inv_resize_image = inv_image.resize((200,75))
            inv_image = ImageTk.PhotoImage(inv_resize_image)
          
            inv_logo = Label(ord_bs_canvas,width=200,height=75, bg="white",image = inv_image) 
            inv_window_image = ord_bs_canvas.create_window(140, 125, anchor="nw", window=inv_logo)
            inv_logo.photo = inv_image
          except:
            ord_bs_canvas.create_text(300, 150, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          labelcmp=Label(ord_bs_canvas,text=cmpy_dtl[1],justify=LEFT, bg="white",anchor="nw",font=("Helvetica", 12), width=30, height=1)
          window = ord_bs_canvas.create_window(345,100, anchor="nw", window=labelcmp)

          labelcmpl=Label(ord_bs_canvas,text=cmpy_dtl[2],justify=LEFT, bg="white",font=("Helvetica", 9),anchor="nw", width=40, height=4)
          windowl = ord_bs_canvas.create_window(350 ,130, anchor="nw", window=labelcmpl)
          
          ord_bs_canvas.create_text(405, 210, text=cmpy_dtl[4],justify=LEFT, fill="black", font=('Helvetica 9'))
          
          ord_bs_canvas.create_text(720, 130, text="John Doe\n381 South Beadford Road\nBedford Corner,NY10549\nUnited States", fill="black", font=('Helvetica 11'))

          lb_inv1=Label(ord_bs_canvas,text=ord_lft_tp2.get(1.0, END), bg="white",anchor="ne",font=("Helvetica", 11),height=1)#Invoice#
          win_inv1 = ord_bs_canvas.create_window(575, 170, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_bs_canvas,text=ord_lft_tp3.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", 11),height=1 )#Invoicedate
          win_inv1 = ord_bs_canvas.create_window(575, 200, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(ord_bs_canvas,text=ord_lft_tp4.get(1.0,END), bg="white",anchor="ne",font=("Helvetica", 11),height=1)#Due date
          win_inv1 = ord_bs_canvas.create_window(575, 230, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(ord_bs_canvas,text=str(ord_lft_tp.get())+"1/2022", bg="white",justify=LEFT,font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = ord_bs_canvas.create_window(815, 170, anchor="ne", window=lb_inv1)
          ord_bs_canvas.create_text(776, 210, text=date_tdy, fill="black", font=('Helvetica 11'))
          ord_bs_canvas.create_text(776, 240, text=date_tdy, fill="black", font=('Helvetica 11'))
          phf = ttk.Style()
          phf.configure('mystyle126.Treeview.Heading', background=''+ ord_man_var.get(),State='DISABLE')
          
          tree=ttk.Treeview(ord_bs_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle126.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=200)
          tree.heading("# 1", text=inv_lst_bx9.get(1.0,END))
          tree.column("# 2", anchor=E, stretch=NO, width=250)
          tree.heading("# 2", text=inv_lst_bx11.get(1.0,END))
          tree.column("# 3", anchor=E, stretch=NO, width=90)
          tree.heading("# 3", text=inv_lst_bx12.get(1.0,END))
          tree.column("# 4", anchor=E, stretch=NO, width=80)
          tree.heading("# 4", text=inv_lst_bx10.get(1.0,END))
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text=inv_lst_bx13.get(1.0,END))
          
          window = ord_bs_canvas.create_window(120, 255, anchor="nw", window=tree)

          ord_bs_canvas.create_line(120, 295, 820, 295 )
          ord_bs_canvas.create_line(120, 255, 120, 295 )
          ord_bs_canvas.create_line(320, 255, 320, 295 )
          
          ord_bs_canvas.create_line(740, 255, 740, 445 )
          ord_bs_canvas.create_line(570, 255, 570, 445 )
          ord_bs_canvas.create_line(570, 255, 570, 295 )
          ord_bs_canvas.create_line(660, 255, 660, 295 )
          ord_bs_canvas.create_line(740, 255, 740, 295 )
          ord_bs_canvas.create_line(820, 255, 820, 445 )
          ord_bs_canvas.create_line(570, 320, 820, 320 )
          ord_bs_canvas.create_line(570, 345, 820, 345 )
          ord_bs_canvas.create_line(570, 370, 820, 370 )
          ord_bs_canvas.create_line(570, 395, 820, 395 )
          ord_bs_canvas.create_line(570, 420, 820, 420 )
          ord_bs_canvas.create_line(570, 445, 820, 445 )
          
          
          lbx_inv=Label(ord_bs_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
          win_inv2 = ord_bs_canvas.create_window(630,298, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_bs_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
          win_inv2 = ord_bs_canvas.create_window(635,323, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_bs_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
          win_inv2 = ord_bs_canvas.create_window(630, 398,anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_bs_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
          win_inv2 = ord_bs_canvas.create_window(635, 423, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_bs_canvas,text=ord_lft_tp6.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#Order Total"
          win_inv2 = ord_bs_canvas.create_window(630, 373, anchor="nw", window=lbx_inv)

          sqlr= 'select currencysign from company'
          fbcursor.execute(sqlr)
          crncy=fbcursor.fetchone()
          crcy_type=crncy[0]
          sqlrt= 'select currsignplace from company'
          fbcursor.execute(sqlrt)
          post_rp=fbcursor.fetchone()
          cry_plcy=post_rp[0]
          if cry_plcy=="before amount": 
            ord_bs_canvas.create_text(630, 285, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 285, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 310, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(795, 335, text=str(crcy_type)+"18.00", fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(795, 360, text=str(crcy_type)+"20.00", fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 385, text=str(crcy_type)+"238.00", fill="black", font=('Helvetica 10 bold'))
            ord_bs_canvas.create_text(790, 410, text=str(crcy_type)+"100.00", fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 435, text=str(crcy_type)+"138.00", fill="black", font=('Helvetica 10'))
          elif cry_plcy=="after amount":
            ord_bs_canvas.create_text(630, 285, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 285, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 310, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(795, 335, text="18.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(795, 360, text="20.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 385, text="238.00"+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
            ord_bs_canvas.create_text(790, 410, text="100.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 435, text="138.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
          elif cry_plcy=="before amount with space":
            ord_bs_canvas.create_text(630, 285, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 285, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 310, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(795, 335, text=str(crcy_type)+" "+"18.00", fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(795, 360, text=str(crcy_type)+" "+"20.00", fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 385, text=str(crcy_type)+" "+"238.00", fill="black", font=('Helvetica 10 bold'))
            ord_bs_canvas.create_text(790, 410, text=str(crcy_type)+" "+"100.00", fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 435, text=str(crcy_type)+" "+"138.00", fill="black", font=('Helvetica 10')) 
          elif cry_plcy=="after amount with space":
            ord_bs_canvas.create_text(630, 285, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 285, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 310, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(795, 335, text="18.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(795, 360, text="20.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 385, text="238.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
            ord_bs_canvas.create_text(790, 410, text="100.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_bs_canvas.create_text(790, 435, text="138.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
          else:
            pass


          ord_bs_canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    
          ord_bs_canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
      

          ord_bs_canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))

          ord_bs_canvas.create_line(150, 470, 800, 470, fill='orange')

          ord_bs_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
          lbx_inv=Label(ord_bs_canvas,text=inv_lst_bx21.get(1.0,END), bg="white",anchor="n",font=("Helvetica 10 "),height=1)#"Terms and Conditions"
          win_inv2 = ord_bs_canvas.create_window(420, 570, anchor="nw", window=lbx_inv)
          ord_bs_canvas.create_line(150, 600, 795, 600)
          text=ord_scrl_txt.get('1.0',END)
          wraped_text="\n".join(wrap(text,130))
    
        
          lbx_inv=Label(ord_bs_canvas,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
          win_inv2 = ord_bs_canvas.create_window(150, 603,anchor="nw", window=lbx_inv)

          ord_bs_canvas.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    

          ord_bs_canvas.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
        else:
          ord_bs_frame = Frame(ord_set_frm_cpy, width=953, height=300)
          ord_bs_frame.pack(expand=True, fill=BOTH)
          ord_bs_frame.place(x=247,y=90)
          
          ord_bs_canvas=Canvas(ord_bs_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(ord_bs_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=ord_bs_canvas.yview)
          ord_bs_canvas.config(width=953,height=300)
          
          ord_bs_canvas.config(yscrollcommand=vertibar.set)
          ord_bs_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          ord_bs_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          ord_bs_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_line(150, 70, 800, 70, fill='orange')
          ord_bs_canvas.create_text(300, 150, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          ord_bs_canvas.create_text(500, 115, text="Your Company Name", fill="black", font=('Helvetica 12 '))
          ord_bs_canvas.create_text(525, 140, text="Address line 1", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(525, 155, text="Address line 2", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(525, 170, text="Address line 3", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(525, 185, text="Address line 4", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(534, 200, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(534, 215, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))

          

          ord_bs_canvas.create_text(659, 180, text="Order", fill="black", font=('Helvetica 11'))
          ord_bs_canvas.create_text(675, 210, text="Order date", fill="black", font=('Helvetica 11'))
          ord_bs_canvas.create_text(659, 240, text="Due date", fill="black", font=('Helvetica 11'))

          

          

          ord_bs_canvas.create_text(776, 180, text="ORD1/2022", fill="black", font=('Helvetica 11'))
          ord_bs_canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
          ord_bs_canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))
          tree=ttk.Treeview(ord_bs_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')
          
          tree.column("# 1", anchor=E, stretch=NO, width=200)
          tree.heading("# 1", text="Product/Service")
          tree.column("# 2", anchor=E, stretch=NO, width=250)
          tree.heading("# 2", text="Description")
          tree.column("# 3", anchor=E, stretch=NO, width=90)
          tree.heading("# 3", text="Unit Price")
          tree.column("# 4", anchor=E, stretch=NO, width=80)
          tree.heading("# 4", text="Quantity")
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text="Price")
          
          window = ord_bs_canvas.create_window(120, 255, anchor="nw", window=tree)

          ord_bs_canvas.create_line(120, 295, 820, 295 )
          ord_bs_canvas.create_line(120, 255, 120, 295 )
          ord_bs_canvas.create_line(320, 255, 320, 295 )
          ord_bs_canvas.create_line(570, 255, 570, 295 )
          ord_bs_canvas.create_line(660, 255, 660, 295 )
          ord_bs_canvas.create_line(740, 255, 740, 295 )
          ord_bs_canvas.create_line(820, 255, 820, 445 )
          ord_bs_canvas.create_line(570, 320, 820, 320 )
          ord_bs_canvas.create_line(570, 345, 820, 345 )
          ord_bs_canvas.create_line(570, 370, 820, 370 )
          ord_bs_canvas.create_line(570, 395, 820, 395 )
          ord_bs_canvas.create_line(570, 420, 820, 420 )
          ord_bs_canvas.create_line(570, 445, 820, 445 )
          
          ord_bs_canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(630, 285, text="$200.00", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(790, 285, text="$200.00", fill="black", font=('Helvetica 10'))

          ord_bs_canvas.create_text(790, 310, text="$200.00", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(795, 335, text="$18.00", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(795, 360, text="$20.00", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(790, 385, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          ord_bs_canvas.create_text(790, 410, text="$100.00", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(790, 435, text="$138.00", fill="black", font=('Helvetica 10'))

          ord_bs_canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(615, 385, text="Estimate total", fill="black", font=('Helvetica 10 bold'))
          ord_bs_canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

          ord_bs_canvas.create_line(150, 470, 800, 470, fill='orange')
          ord_bs_canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
          
          ord_bs_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_line(150, 620, 795, 620, fill='orange')
          ord_bs_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          ord_bs_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
          pass

  por_sql_st='select * from company'
  fbcursor.execute(por_sql_st)
  cmpy_dtls=fbcursor.fetchone()
  if cmpy_dtls is not None:
          sql='select dateformat from company'
          fbcursor.execute(sql)
          date_frmat=fbcursor.fetchone()
          
          if not date_frmat:
            ft_fr='%Y-%m-%d'
        
          elif date_frmat[0]=="mm-dd-yyyy":
            ft_fr='%m-%d-%Y'

          elif date_frmat[0]=="dd-mm-yyyy":
              ft_fr='%d-%m-%Y'
                      
          elif date_frmat[0]=="yyy.mm.dd":
              ft_fr='%Y.%m.%d'
                          
          elif date_frmat[0]=="mm/dd/yyyy":
              ft_fr='%m/%d/%Y'
                          
          elif date_frmat[0]=="dd/mm/yyyy":
              ft_fr='%d/%m/%Y'
                                  
          elif date_frmat[0]=="dd.mm.yyyy":
              ft_fr='%d.%m.%Y'
                                  
          elif date_frmat[0]=="yyyy/  mm/dd":
              ft_fr='%Y/%m/%d'

          else:
              ft_fr='%Y-%m-%d'
          td_date=date.today()
          date_tdy=td_date.strftime(ft_fr)
          ord_pro1_frame = Frame(ord_set_frm_cpy, width=953, height=300)
          ord_pro1_frame = Frame(ord_set_frm_cpy, width=953, height=300)
          ord_pro1_frame.pack(expand=True, fill=BOTH)
          ord_pro1_frame.place(x=247,y=90)
          ord_pro1_canvas=Canvas(ord_pro1_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
          vertibar=Scrollbar(ord_pro1_frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=ord_pro1_canvas.yview)
          
          ord_pro1_canvas.config(width=953,height=300)
          ord_pro1_canvas.config(yscrollcommand=vertibar.set)
          ord_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
          ord_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
          ord_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            inv_image = Image.open("images/"+cmpy_dtl[13])
            inv_resize_image = inv_image.resize((200,75))
            inv_image = ImageTk.PhotoImage(inv_resize_image)
          
            inv_logo = Label(ord_pro1_canvas,width=200,height=75, bg="white",image = inv_image) 
            inv_window_image = ord_pro1_canvas.create_window(150, 50, anchor="nw", window=inv_logo)
            inv_logo.photo = inv_image
          except:
            ord_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          
          lb_inv1=Label(ord_pro1_canvas,text=ord_lft_tp2.get(1.0, END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Order#"
          win_inv1 = ord_pro1_canvas.create_window(175, 140, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_pro1_canvas,text=ord_lft_tp3.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1 )#Order date
          win_inv1 = ord_pro1_canvas.create_window(175, 160, anchor="nw", window=lb_inv1)
          
          lb_inv1=Label(ord_pro1_canvas,text=ord_lft_tp4.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Due date
          win_inv1 = ord_pro1_canvas.create_window(175, 180, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_pro1_canvas,text=inv_lst_bx5.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", 11),height=1)#Terms
          win_inv1 = ord_pro1_canvas.create_window(175, 200, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_pro1_canvas,text=inv_lst_bx4.get(1.0,END), bg="white",anchor="nw",font=("Helvetica", ),height=1)#Order ref.#
          win_inv1 = ord_pro1_canvas.create_window(175, 220, anchor="nw", window=lb_inv1)

          # ord_pro1_canvas.create_text(195, 150, text="Order#", fill="black", font=('Helvetica 11'))
          # ord_pro1_canvas.create_text(205, 170, text="Order date", fill="black", font=('Helvetica 11'))
          # ord_pro1_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
          # ord_pro1_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
          # ord_pro1_canvas.create_text(205, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
          lb_inv1=Label(ord_pro1_canvas,text=str(ord_lft_tp.get())+"1/2022", bg="white",anchor="nw",font=("Helvetica", ),height=1)#Invoice ref.#
          win_inv1 = ord_pro1_canvas.create_window(310, 140, anchor="nw", window=lb_inv1)
          ord_pro1_canvas.create_text(350, 170, text=date_tdy, fill="black", font=('Helvetica 11'))
          ord_pro1_canvas.create_text(350, 190, text=date_tdy, fill="black", font=('Helvetica 11'))
          ord_pro1_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

          labelcmp=Label(ord_pro1_canvas,text=cmpy_dtl[1], bg="white",anchor="e",font=("Helvetica", 12), width=40, height=1)
          window = ord_pro1_canvas.create_window(430,80, anchor="nw", window=labelcmp)

          labelcmpl=Label(ord_pro1_canvas,text=cmpy_dtl[2],justify=RIGHT, bg="white",font=("Helvetica", 9),anchor="ne", width=50, height=4)
          windowl = ord_pro1_canvas.create_window(440,110, anchor="nw", window=labelcmpl)

          
          ord_pro1_canvas.create_text(745, 195, text=cmpy_dtl[4], fill="black", font=('Helvetica 10'))
          # lb_inv1=Label(ord_pro1_canvas,text=ord_lft_tp1.get(1.0,END), bg="white",justify=LEFT,font=('Helvetica 14 bold'),height=2)#Order
          # win_inv1 = ord_pro1_canvas.create_window(800, 250, anchor="ne", window=lb_inv1)

          lb_inv1=Label(ord_pro1_canvas,text=ord_lft_tp1.get(1.0,END), bg="white",anchor="ne",font=('Helvetica 14 bold'),height=1)#invoice
          win_inv1 = ord_pro1_canvas.create_window(800, 200, anchor="ne", window=lb_inv1)

          lb_inv1=Label(ord_pro1_canvas,text=inv_lst_bx22.get(1.0,END), bg="white",justify=LEFT,font=("Helvetica 10" ),height=2)#TAX EXEMPTED
          win_inv1 = ord_pro1_canvas.create_window(800, 225, anchor="ne", window=lb_inv1)

          lb_inv1=Label(ord_pro1_canvas,text=ord_lft_tp5.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline" ),height=1)#Order to
          win_inv1 = ord_pro1_canvas.create_window(175, 250, anchor="nw", window=lb_inv1)

          lb_inv1=Label(ord_pro1_canvas,text=inv_lst_bx7.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 underline"),height=1)#Ship to
          win_inv1 = ord_pro1_canvas.create_window(525, 250, anchor="nw", window=lb_inv1)

          # ord_pro1_canvas.create_text(770, 205, text="Order", fill="black", font=('Helvetica 14 bold'))
      
          # ord_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
            
          # ord_pro1_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
          ord_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
          # ord_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          ord_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
          ord_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
          phf = ttk.Style()
          phf.configure('mystyle126.Treeview.Heading', background=''+ ord_man_var.get(),State='DISABLE')

          tree=ttk.Treeview(ord_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle126.Treeview')

          tree.column("# 1", anchor=E, stretch=NO, width=100)
          tree.heading("# 1", text=inv_lst_bx8.get(1.0,END))
          tree.column("# 2", anchor=E, stretch=NO, width=350)
          tree.heading("# 2", text=inv_lst_bx9.get(1.0,END))
          tree.column("# 3", anchor=E, stretch=NO, width=80)
          tree.heading("# 3", text=inv_lst_bx10.get(1.0,END))
          tree.column("# 4", anchor=E, stretch=NO, width=90)
          tree.heading("# 4", text=inv_lst_bx12.get(1.0,END))
          tree.column("# 5", anchor=E, stretch=NO, width=80)
          tree.heading("# 5", text=inv_lst_bx13.get(1.0,END))
          
          window = ord_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)

          ord_pro1_canvas.create_line(120, 390, 820, 390 )
          ord_pro1_canvas.create_line(120, 340, 120, 365 )
          ord_pro1_canvas.create_line(120, 365, 120, 390 )
          ord_pro1_canvas.create_line(820, 340, 820, 540 )
          ord_pro1_canvas.create_line(740, 340, 740, 540 )
          ord_pro1_canvas.create_line(570, 340, 570, 540 )
          ord_pro1_canvas.create_line(570, 415, 820, 415 )
          ord_pro1_canvas.create_line(570, 440, 820, 440 )
          ord_pro1_canvas.create_line(570, 465, 820, 465 )
          ord_pro1_canvas.create_line(570, 490, 820, 490 )
          ord_pro1_canvas.create_line(570, 515, 820, 515 )
          ord_pro1_canvas.create_line(650, 340, 650, 390 )
          ord_pro1_canvas.create_line(220, 340, 220, 390 )
          ord_pro1_canvas.create_line(570, 540, 820, 540 )

          lbx_inv=Label(ord_pro1_canvas,text=inv_lst_bx14.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10"),height=1)#"Subtotal"
          win_inv2 = ord_pro1_canvas.create_window(630,392, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_pro1_canvas,text=inv_lst_bx17.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"TAX1"
          win_inv2 = ord_pro1_canvas.create_window(635,418, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_pro1_canvas,text=inv_lst_bx19.get(1.0,END), bg="White",anchor="nw",font=("Helvetica 10 "), height=1)#"Total Paid"
          win_inv2 = ord_pro1_canvas.create_window(630, 492,anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_pro1_canvas,text=inv_lst_bx20.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#"Balance"
          win_inv2 = ord_pro1_canvas.create_window(635, 518, anchor="nw", window=lbx_inv)

          lbx_inv=Label(ord_pro1_canvas,text=ord_lft_tp6.get(1.0,END), bg="white",anchor="nw",font=("Helvetica 10 "),height=1)#Order Total"
          win_inv2 = ord_pro1_canvas.create_window(630, 468, anchor="nw", window=lbx_inv)

          sqlr= 'select currencysign from company'
          fbcursor.execute(sqlr)
          crncy=fbcursor.fetchone()
          crcy_type=crncy[0]
          sqlrt= 'select currsignplace from company'
          fbcursor.execute(sqlrt)
          post_rp=fbcursor.fetchone()
          cry_plcy=post_rp[0]
          if cry_plcy=="before amount": 
            ord_pro1_canvas.create_text(710, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 372, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 404, text=str(crcy_type)+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 428, text=str(crcy_type)+"18.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 502, text=str(crcy_type)+"100.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 526, text=str(crcy_type)+"138.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 454, text=str(crcy_type)+"20.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 479, text=str(crcy_type)+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount":
            ord_pro1_canvas.create_text(710, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 372, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 404, text="200.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 428, text="18.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 502, text="100.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 526, text="138.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 454, text="20.00"+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 479, text="238.00"+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="before amount with space": 
            ord_pro1_canvas.create_text(710, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 372, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 404, text=str(crcy_type)+" "+"200.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 428, text=str(crcy_type)+" "+"18.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 502, text=str(crcy_type)+" "+"100.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 526, text=str(crcy_type)+" "+"138.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 454, text=str(crcy_type)+" "+"20.00", fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 479, text=str(crcy_type)+" "+"238.00", fill="black", font=('Helvetica 10 bold'))
          elif cry_plcy=="after amount with space":
            ord_pro1_canvas.create_text(710, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 372, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 404, text="200.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 428, text="18.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 502, text="100.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 526, text="138.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(792, 454, text="20.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10'))
            ord_pro1_canvas.create_text(790, 479, text="238.00"+" "+str(crcy_type), fill="black", font=('Helvetica 10 bold'))
          else:
            pass

          

          ord_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    
    

        

          ord_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
  

          
          ord_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
          ord_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
          lbx_inv=Label(ord_pro1_canvas,text=inv_lst_bx21.get(1.0,END), bg="white",anchor="n",font=("Helvetica 10 "),height=1)#"Terms and Conditions"
          win_inv2 = ord_pro1_canvas.create_window(420, 570, anchor="nw", window=lbx_inv)

          ord_pro1_canvas.create_line(150, 600, 795, 600)
          text=ord_scrl_txt.get('1.0',END)
          wraped_text="\n".join(wrap(text,130))
    
        
          lbx_inv=Label(ord_pro1_canvas,text=wraped_text, bg="white",anchor="nw",font=("Helvetica 8 "), justify=LEFT, height=3, width=107)
          win_inv2 = ord_pro1_canvas.create_window(150, 603,anchor="nw", window=lbx_inv)

          ord_pro1_canvas.create_text(280, 660, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    

          ord_pro1_canvas.create_text(720, 660, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  else:
    ord_pro1_frame = Frame(ord_set_frm_cpy, width=953, height=300)
    ord_pro1_frame.pack(expand=True, fill=BOTH)
    ord_pro1_frame.place(x=247,y=90)
    ord_pro1_canvas=Canvas(ord_pro1_frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
    vertibar=Scrollbar(ord_pro1_frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=ord_pro1_canvas.yview)
          
    ord_pro1_canvas.config(width=953,height=300)
    ord_pro1_canvas.config(yscrollcommand=vertibar.set)
    ord_pro1_canvas.pack(expand=True,side=LEFT,fill=BOTH)
    ord_pro1_canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    ord_pro1_canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          
    ord_pro1_canvas.create_text(195, 150, text="Order#", fill="black", font=('Helvetica 11'))
    ord_pro1_canvas.create_text(205, 170, text="Order date", fill="black", font=('Helvetica 11'))
    ord_pro1_canvas.create_text(200, 190, text="Due date", fill="black", font=('Helvetica 11'))
    ord_pro1_canvas.create_text(191, 210, text="Terms", fill="black", font=('Helvetica 11'))
    ord_pro1_canvas.create_text(205, 230, text="Order ref.#", fill="black", font=('Helvetica 11'))
    ord_pro1_canvas.create_text(350, 150, text="ORD1/2022", fill="black", font=('Helvetica 11'))
    ord_pro1_canvas.create_text(350, 170, text="03-05-2022", fill="black", font=('Helvetica 11'))
    ord_pro1_canvas.create_text(350, 190, text="18-05-2022", fill="black", font=('Helvetica 11'))
    ord_pro1_canvas.create_text(340, 210, text="NET 15", fill="black", font=('Helvetica 11'))      

    ord_pro1_canvas.create_text(720, 80, text="Your Company Name", fill="black", font=('Helvetica 12 '))
    ord_pro1_canvas.create_text(750, 110, text="Address line 1", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(750, 125, text="Address line 2", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(750, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(750, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(745, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(745, 185, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(750, 205, text="Order", fill="black", font=('Helvetica 14 bold'))
    ord_pro1_canvas.create_text(746, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
            
    ord_pro1_canvas.create_text(210, 260, text="Order to", fill="black", font=('Helvetica 10 underline'))
    ord_pro1_canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    ord_pro1_canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    ord_pro1_canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    ord_pro1_canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
    s = ttk.Style()
    s.configure('Treeview.Heading', background=''+ ord_man_var.get(),State='DISABLE')

    tree=ttk.Treeview(ord_pro1_canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')

    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
          
    window = ord_pro1_canvas.create_window(120, 340, anchor="nw", window=tree)

    ord_pro1_canvas.create_line(120, 390, 820, 390 )
    ord_pro1_canvas.create_line(120, 340, 120, 365 )
    ord_pro1_canvas.create_line(120, 365, 120, 390 )
    ord_pro1_canvas.create_line(820, 340, 820, 540 )
    ord_pro1_canvas.create_line(740, 340, 740, 540 )
    ord_pro1_canvas.create_line(570, 340, 570, 540 )
    ord_pro1_canvas.create_line(570, 415, 820, 415 )
    ord_pro1_canvas.create_line(570, 440, 820, 440 )
    ord_pro1_canvas.create_line(570, 465, 820, 465 )
    ord_pro1_canvas.create_line(570, 490, 820, 490 )
    ord_pro1_canvas.create_line(570, 515, 820, 515 )
    ord_pro1_canvas.create_line(650, 340, 650, 390 )
    ord_pro1_canvas.create_line(220, 340, 220, 390 )
    ord_pro1_canvas.create_line(570, 540, 820, 540 )

    ord_pro1_canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(710, 372, text="$200.00", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(790, 372, text="$200.00", fill="black", font=('Helvetica 10'))

    ord_pro1_canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(790, 404, text="$200.00", fill="black", font=('Helvetica 10'))

    ord_pro1_canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(792, 428, text="$18.00", fill="black", font=('Helvetica 10'))

    ord_pro1_canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(792, 454, text="$20.00", fill="black", font=('Helvetica 10'))

    ord_pro1_canvas.create_text(790, 479, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    ord_pro1_canvas.create_text(650, 479, text="Estimate total", fill="black", font=('Helvetica 10 bold'))

    ord_pro1_canvas.create_text(790, 502, text="$100.00", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

    ord_pro1_canvas.create_text(790, 526, text="$138.00", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    ord_pro1_canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
    ord_pro1_canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_line(150, 620, 795, 620)
          

    ord_pro1_canvas.create_text(280, 640, text= "", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(280, 655, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    ord_pro1_canvas.create_text(720, 655, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

  ord_main_var = StringVar()
  ord_cmb_bx_mn = ttk.Combobox(ord_set_frm_cpy,textvariable=ord_main_var)
  ord_cmb_bx_mn.place(x=770 ,y=40, width=220)
  ord_cmb_bx_mn.bind("<<ComboboxSelected>>", ord_main_mn)
  ord_cmb_bx_mn["values"] = ("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
  ord_cmb_bx_mn.current(0)
  
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

  ################### tab05 ###################################
  fifthtab1=Frame(tab05, relief=GROOVE, bg="#f8f8f2")
  fifthtab1.pack(side="top", fill=BOTH)

  fifthtab=Frame(fifthtab1, bg="#f5f3f2", height=700)
  fifthtab.pack(side="top", fill=BOTH)

  sql = "select * from company"
  fbcursor.execute(sql)
  estdata = fbcursor.fetchone()


  ver = Label(fifthtab,text="Estimate# prefix")
  ver.place(x=5,y=40)

  est_str = StringVar() 
  est_entry = Entry(fifthtab, textvariable=est_str)
  est_entry.place(x=100,y=40)
  if not estdata:
    est_str.set('EST')
  else:
    est_entry.insert(0, estdata[29])

  ver = Label(fifthtab,text="Starting estimate number")
  ver.place(x=25,y=80)

  def callback(input):
      
    if input.isdigit():
        return True
                          
    elif input is "":
        return True
  
    else:
        return False

  spin1 = Spinbox(fifthtab,from_=0,to=1000000,width=15)
  reg = fifthtab.register(callback)
  
  spin1.config(validate ="key", 
         validatecommand =(reg, '%S'))
  if not estdata:
    pass
  else:
    spin1.delete(0, END)
    spin1.insert(0,estdata[38])
  spin1.place(x=50,y=100)

  ver = Label(fifthtab,text="Header box background color")
  ver.place(x=5,y=140)

  win_menu1 = StringVar()
  winstyle1 = ttk.Combobox(fifthtab,textvariable=win_menu1)
  #est_win1 = win_menu1.get()
  winstyle1['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
  if not estdata:
    winstyle1.current(0)
  else:
    winstyle1.insert(0, estdata[30])
  winstyle1.place(x=6 ,y=160)
  #winstyle1.current(0)

  ver = Label(fifthtab,text="Customize Estimate text labels")
  ver.place(x=5,y=190)
  
  est_str1 = StringVar() 
  est_lbx1 = Entry(fifthtab, width=30,textvariable=est_str1)
  # est_str1.set('Estimate')
  if not estdata:
    est_str1.set('Estimate')
  else:
    est_lbx1.insert(0, estdata[31])
  est_lbx1.place(x=5,y=220)
  
  est_str2 = StringVar() 
  est_lbx2 = Entry(fifthtab, width=30,textvariable=est_str2)
  if not estdata:
    est_str2.set('Estimate#')
  else:
    est_lbx2.insert(0,estdata[33])
  est_lbx2.place(x=5,y=240)
  
  
  est_str3 = StringVar() 
  est_lbx3 = Entry(fifthtab,width=30,textvariable=est_str3)
  if not estdata:
    est_str3.set('Estimate date')
  else:
    est_lbx3.insert(0, estdata[34])
  est_lbx3.place(x=5,y=260) 

  est_str4 = StringVar() 
  est_lbx4 = Entry(fifthtab,width=30,textvariable=est_str4)
  if not estdata:
    est_str4.set('Due date')
  else:
    est_lbx4.insert(0, estdata[35])
  est_lbx4.place(x=5,y=280)

  est_str5 = StringVar() 
  est_lbx5 = Entry(fifthtab,width=30,textvariable=est_str5)
  if not estdata:
    est_str5.set('Estimate to')
  else:
    est_lbx5.insert(0, estdata[36])
  est_lbx5.place(x=5,y=300)

  est_str6 = StringVar() 
  est_lbx6 = Entry(fifthtab, width=30,textvariable=est_str6)
  if not estdata:
    est_str6.set('Estimate total')
  else:
    est_lbx6.insert(0, estdata[37])
  est_lbx6.place(x=5,y=320)


  ver = Label(fifthtab,text="Default Estimate template(example,click on preview for mouse scrolling)")
  ver.place(x=248,y=55 )

  ver = Label(fifthtab,text="Default Estimate template")
  ver.place(x=619,y=40)



  messagelbframe=LabelFrame(fifthtab,text="Predefined terms and conditions text for estimates", height=70, width=980)
  messagelbframe.place(x=248, y=396)

  
  # est_str7 = StringVar() 
  # entry1=Entry(fifthtab, width=155,textvariable=est_str7)
  # if not estdata:
  #   pass
  # else:
  #   entry1.insert(0, estdata[39])
  # entry1.place(x=260, y=415, height=36)
  
  est_str7 = scrolledtext.ScrolledText(fifthtab)
  if  not estdata:
    pass
  else:
    est_str7.insert('1.0', estdata[39])
  est_str7.place(x=260,y=415,height=38,width=950)


  def restore_defaulttt1():
        est_lbx1.delete(0, 'end')
        est_lbx1.insert(0, 'Estimate')
        est_lbx2.delete(0, 'end')
        est_lbx2.insert(0,'Estimate#')
        est_lbx3.delete(0, 'end')
        est_lbx3.insert(0, 'Estimate date')
        est_lbx4.delete(0, 'end')
        est_lbx4.insert(0, 'Due date')
        est_lbx5.delete(0, 'end')
        est_lbx5.insert(0, 'Estimate to')
        est_lbx6.delete(0, 'end')
        est_lbx6.insert(0, 'Estimate total')

  bttermadd_01 = Button(fifthtab,text="Restore defaults", command=restore_defaulttt1)
  bttermadd_01.place(x=32,y=430)


#------------Professional 1 (logo on left side)-------------
  def maindropmenu(event):
      menuvar=win_menu2.get()
      sql = "select * from company"
      fbcursor.execute(sql)
      estdata1 = fbcursor.fetchone()

      if menuvar == 'Professional 1 (logo on left side)':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
              
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
          
        canvas.config(width=953,height=300)
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
          
        canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)
        canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
        canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
      
        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

        tree.column("# 1", anchor=E, stretch=NO, width=100)
        tree.heading("# 1", text="ID/SKU")
        tree.column("# 2", anchor=E, stretch=NO, width=350)
        tree.heading("# 2", text="Product/Service - Description")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Quantity")
        tree.column("# 4", anchor=E, stretch=NO, width=90)
        tree.heading("# 4", text="Unit Price")
        tree.column("# 5", anchor=E, stretch=NO, width=80)
        tree.heading("# 5", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 340, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(220, 340, 220, 390 )
        canvas.create_line(570, 540, 820, 540 )

        canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    
        if comcursignpla.get() == "before amount":
          canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        else:
          pass
        # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        
        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
        
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)

        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
          

#----------------Professional 2 (logo on right side)------------------
      elif menuvar == 'Professional 2 (logo on right side)':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
      
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)
          
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(215, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
        #T_address_window = canvas.create_window(175, 80, anchor="nw", window=T_address)

        canvas.create_text(215, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
        canvas.create_text(232, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(690, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(690, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(690, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 220, text="NET 15", fill="black", font=('Helvetica 11'))      
          
        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=100)
        tree.heading("# 1", text="ID/SKU")
        tree.column("# 2", anchor=E, stretch=NO, width=350)
        tree.heading("# 2", text="Product/Service - Description")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Quantity")
        tree.column("# 4", anchor=E, stretch=NO, width=90)
        tree.heading("# 4", text="Unit Price")
        tree.column("# 5", anchor=E, stretch=NO, width=80)
        tree.heading("# 5", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 340, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(220, 340, 220, 390 )
        canvas.create_line(570, 540, 820, 540 )

        canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
        
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
#----------------Simplified 1 (logo on left side)------------------ 
      elif menuvar == 'Simplified 1 (logo on left side)':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)

        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

        canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        #canvas.create_text(710, 200, text=caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)

        canvas.create_text(708, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(710, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
          
        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 390, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(570, 540, 820, 540 )

      
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#----------------Simplified 2 (logo on right side)------------------ 
      elif menuvar == 'Simplified 2 (logo on right side)':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)

        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)

        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(224, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)

        canvas.create_text(224, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))

        canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(670, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 390, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(570, 540, 820, 540 )

          
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#----------------Business Classic------------------ 
      elif menuvar == 'Business Classic':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
          
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)
          
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 70, 800, 70, fill='orange')
        
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(140, 120, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  

        canvas.create_text(500, 90, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(485, 220, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=35, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
        
        canvas.create_text(480, 210, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))

        canvas.create_text(655, 100, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(696, 120, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(706, 135, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(665, 150, text="United States", fill="black", font=('Helvetica 10'))

        canvas.create_text(659, 180, text=""+est_str1.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(675, 210, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(659, 240, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))

        canvas.create_text(776, 180, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=200)
        tree.heading("# 1", text="Product/Service")
        tree.column("# 2", anchor=E, stretch=NO, width=250)
        tree.heading("# 2", text="Description")
        tree.column("# 3", anchor=E, stretch=NO, width=90)
        tree.heading("# 3", text="Unit Price")
        tree.column("# 4", anchor=E, stretch=NO, width=80)
        tree.heading("# 4", text="Quantity")
        tree.column("# 5", anchor=E, stretch=NO, width=80)
        tree.heading("# 5", text="Price")
      
        window = canvas.create_window(120, 255, anchor="nw", window=tree)

        canvas.create_line(120, 295, 820, 295 )
        canvas.create_line(120, 255, 120, 295 )
        canvas.create_line(320, 255, 320, 295 )
        canvas.create_line(570, 255, 570, 295 )
        canvas.create_line(660, 255, 660, 295 )
        canvas.create_line(740, 255, 740, 295 )
        canvas.create_line(820, 255, 820, 445 )
        canvas.create_line(570, 320, 820, 320 )
        canvas.create_line(570, 345, 820, 345 )
        canvas.create_line(570, 370, 820, 370 )
        canvas.create_line(570, 395, 820, 395 )
        canvas.create_line(570, 420, 820, 420 )
        canvas.create_line(570, 445, 820, 445 )
      
        canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(624, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 310, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(789, 335, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(789, 360, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 385, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 410, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 435, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
        canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
        canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        canvas.create_text(615, 385, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
        canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_line(150, 470, 800, 470, fill='orange')
        canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608, fill='orange')
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
        pass

  win_menu2 = StringVar()
  winstyle2 = ttk.Combobox(fifthtab,textvariable=win_menu2)
  winstyle2.bind("<<ComboboxSelected>>", maindropmenu)
  winstyle2["values"] = ("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
  if not estdata:
    winstyle2.current(0)
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
      
    canvas.config(width=953,height=300)
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  
    #canvas.create_image(120,0, anchor=NW, image=est_logo)  
    canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
      
    canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
      
    canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
    # T_address = Text(canvas, height=5, width=20 , font=('Helvetica 10'))
    # T_address.insert(END, estdata[2])
    # T_address_window = canvas.create_window(645, 80, anchor="nw", window=T_address)
    canvas.create_text(700, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
      
    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 340, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(220, 340, 220, 390 )
    canvas.create_line(570, 540, 820, 540 )

    canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    else:
      pass
    # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
    # T = Text(canvas, height=3, width=105, font=('Helvetica 10'))
    # T.insert(END, estdata[39])
    # T_window = canvas.create_window(105, 612, anchor="nw", window=T)


    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10')) 
  elif estdata[32] == 'Professional 1 (logo on left side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
      
    canvas.config(width=953,height=300)
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
      
    canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)
    canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
      
    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 340, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(220, 340, 220, 390 )
    canvas.create_line(570, 540, 820, 540 )

    canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    else:
      pass
    # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)

    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Professional 2 (logo on right side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
      
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
      
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)
      
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(225, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
    canvas.create_text(225, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(232, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(690, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(690, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(690, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 220, text="NET 15", fill="black", font=('Helvetica 11'))      
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 340, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(220, 340, 220, 390 )
    canvas.create_line(570, 540, 820, 540 )

    canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Simplified 1 (logo on left side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

    canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(710, 200, text=caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)

    canvas.create_text(708, 170, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(710, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=530)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=90)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 390, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(570, 540, 820, 540 )

      
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Simplified 2 (logo on right side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)

    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(224, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
    canvas.create_text(224, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(670, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=530)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=90)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 390, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(570, 540, 820, 540 )

      
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Business Classic':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
      
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
      
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)
      
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 70, 800, 70, fill='orange')
    
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(140, 120, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  

    canvas.create_text(500, 90, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(480, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=35, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
        
        
    canvas.create_text(480, 210, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))

    canvas.create_text(655, 100, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(696, 120, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(706, 135, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(665, 150, text="United States", fill="black", font=('Helvetica 10'))

    canvas.create_text(659, 180, text=""+est_str1.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(675, 210, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(659, 240, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))

    canvas.create_text(776, 180, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=200)
    tree.heading("# 1", text="Product/Service")
    tree.column("# 2", anchor=E, stretch=NO, width=250)
    tree.heading("# 2", text="Description")
    tree.column("# 3", anchor=E, stretch=NO, width=90)
    tree.heading("# 3", text="Unit Price")
    tree.column("# 4", anchor=E, stretch=NO, width=80)
    tree.heading("# 4", text="Quantity")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 255, anchor="nw", window=tree)

    canvas.create_line(120, 295, 820, 295 )
    canvas.create_line(120, 255, 120, 295 )
    canvas.create_line(320, 255, 320, 295 )
    canvas.create_line(570, 255, 570, 295 )
    canvas.create_line(660, 255, 660, 295 )
    canvas.create_line(740, 255, 740, 295 )
    canvas.create_line(820, 255, 820, 445 )
    canvas.create_line(570, 320, 820, 320 )
    canvas.create_line(570, 345, 820, 345 )
    canvas.create_line(570, 370, 820, 370 )
    canvas.create_line(570, 395, 820, 395 )
    canvas.create_line(570, 420, 820, 420 )
    canvas.create_line(570, 445, 820, 445 )
      
    canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(624, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 310, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(789, 335, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(789, 360, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 385, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 410, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 435, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
    canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
    canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    canvas.create_text(615, 385, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
    canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_line(150, 470, 800, 470, fill='orange')
    canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608, fill='orange')
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  else:
    pass
  winstyle2.place(x=770 ,y=40, width=220)
  #winstyle2.current(0)



################### tab07 ###################################
  seventhtab1=Frame(tab07, relief=GROOVE, bg="#f8f8f2")
  seventhtab1.pack(side="top", fill=BOTH)

  sql = "select * from company"
  fbcursor.execute(sql)
  advdata = fbcursor.fetchone()


  seventhtab=Frame(seventhtab1, bg="#f5f3f2", height=700)
  seventhtab.pack(side="top", fill=BOTH)

  adv_messagelbframe=LabelFrame(seventhtab,text="Template advanced settings", height=250, width=1150)
  adv_messagelbframe.place(x=2, y=10)

  adv_fbill = Label(seventhtab,text="Template",font="arial 10 bold").place(x=20,y=30)

  adv_ver = Label(seventhtab,text="Professional 1 (logo on left side)")
  adv_ver.place(x=20,y=60)

  adv_ver = Label(seventhtab,text="Professional 2 (logo on right side)")
  adv_ver.place(x=20,y=90)

  adv_ver = Label(seventhtab,text="Simplified 1 (logo on left side)")
  adv_ver.place(x=20,y=120)

  adv_ver = Label(seventhtab,text="Simplified 2 (logo on right side)")
  adv_ver.place(x=20,y=150)

  adv_ver = Label(seventhtab,text="Business Classic")
  adv_ver.place(x=20,y=180)

  adv_fbill = Label(seventhtab,text="Page size",font="arial 10 bold").place(x=255,y=30)

  adv_win_menu3 = StringVar()
  adv_winstyle3 = ttk.Combobox(seventhtab,textvariable=adv_win_menu3)
  adv_winstyle3['values'] = ('Letter','A4')
  adv_win_menu3.set('Letter')
  #adv_winstyle3.current(0)
  adv_winstyle3.place(x=225 ,y=60)
    
  
  adv_win_menu4 = StringVar()
  adv_winstyle4 = ttk.Combobox(seventhtab,textvariable=adv_win_menu4)
  adv_winstyle4.place(x=225,y=90)
  adv_winstyle4['values'] = ("Letter","A4")
  adv_winstyle4.set("Letter")
  adv_winstyle4.current(0)

  adv_win_menu5 = StringVar()
  adv_winstyle5 = ttk.Combobox(seventhtab,textvariable=adv_win_menu5)
  adv_winstyle5.place(x=225,y=120)
  adv_winstyle5['values'] = ("Letter","A4")
  adv_winstyle5.set("Letter")
  adv_winstyle5.current(0)

  adv_win_menu6 = StringVar()
  adv_winstyle6 = ttk.Combobox(seventhtab,textvariable=adv_win_menu6)
  adv_winstyle6.place(x=225,y=150)
  adv_winstyle6['values'] = ("Letter","A4")
  adv_winstyle6.set("Letter")
  adv_winstyle6.current(0)

  adv_win_menu7 = StringVar()
  adv_winstyle7 = ttk.Combobox(seventhtab,textvariable=adv_win_menu7)
  adv_winstyle7.place(x=225,y=180)
  adv_winstyle7['values'] = ("Letter","A4")
  adv_winstyle7.set("Letter")
  adv_winstyle7.current(0)

  adv_fbill = Label(seventhtab,text="Right Margin(mm)",font="arial 10 bold").place(x=450,y=30)

  adv_spin00 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin00.place(x=465,y=60)

  adv_spin01 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin01.place(x=465,y=90)

  adv_spin02 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin02.place(x=465,y=120)

  adv_spin03 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin03.place(x=465,y=150)

  adv_spin04 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin04.place(x=465,y=180)


  adv_fbill = Label(seventhtab,text="'Invoice to'block position shift(mm)",font="arial 10 bold").place(x=650,y=30)

  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=60)
  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=90)
  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=120)
  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=150)

  adv_spin10 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin10.place(x=685,y=60)

  adv_spin11 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin11.place(x=685,y=90)

  adv_spin12 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin12.place(x=685,y=120)

  adv_spin13 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin13.place(x=685,y=150)

  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=60)
  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=90)
  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=120)
  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=150)

  adv_spin20 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin20.place(x=820,y=60)

  adv_spin21 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin21.place(x=820,y=90)

  adv_spin22 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin22.place(x=820,y=120)

  adv_spin23 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin23.place(x=820,y=150)

  adv_bttermadd = Button(seventhtab,image=photo8,compound = LEFT,text="Refresh preview",width=115)
  adv_bttermadd.place(x=1000,y=50)

  adv_bttermadd = Button(seventhtab,image=saves,compound = LEFT,text="Save Settings",width=115)
  adv_bttermadd.place(x=1000,y=140)

  def adv_restore():
    adv_spin10.delete(0,'end')
    adv_spin10.insert(0,"0")
    adv_spin11.delete(0,'end')
    adv_spin11.insert(0,"0")
    adv_spin12.delete(0,'end')
    adv_spin12.insert(0,"0")
    adv_spin13.delete(0,'end')
    adv_spin13.insert(0,"0")
    adv_spin20.delete(0,'end')
    adv_spin20.insert(0,"0")
    adv_spin21.delete(0,'end')
    adv_spin21.insert(0,"0")
    adv_spin22.delete(0,'end')
    adv_spin22.insert(0,"0")
    adv_spin23.delete(0,'end')
    adv_spin23.insert(0,"0")
    adv_spin00.delete(0,'end')
    adv_spin00.insert(0,"10")
    adv_spin01.delete(0,'end')
    adv_spin01.insert(0,"10")
    adv_spin02.delete(0,'end')
    adv_spin02.insert(0,"10")
    adv_spin03.delete(0,'end')
    adv_spin03.insert(0,"10")
    adv_spin04.delete(0,'end')
    adv_spin04.insert(0,"10")
    adv_winstyle3.delete(0,'end')
    adv_winstyle3.insert(0,"Letter")
    adv_winstyle4.delete(0,'end')
    adv_winstyle4.insert(0,"Letter")
    adv_winstyle5.delete(0,'end')
    adv_winstyle5.insert(0,"Letter")
    adv_winstyle6.delete(0,'end')
    adv_winstyle6.insert(0,"Letter")
    adv_winstyle7.delete(0,'end')
    adv_winstyle7.insert(0,"Letter")

  adv_bttermadd = Button(seventhtab,text="Restore defaults",width=16, command=adv_restore)
  adv_bttermadd.place(x=1000,y=180)

  adv_ver = Label(seventhtab,text="By positioning 'Invoice to'block,the customer name/address can be displayed in right place in the windowed envelope. If you networking, you need to setup this on all computer.\nExample:(Left:20 and Top:10 means that shift 'Invoice to'block to right 20mm and shift down 10mm) Original position Left:0 Top:0")
  adv_ver.place(x=50,y=210)

  adv_ver = Label(seventhtab,text="Selected template preview (example, click on preview for mouse scrolling)")
  adv_ver.place(x=230,y=270)

#------------Professional 1 (logo on left side)------------- 
  def adv_maindropmenu(event):
      menuvar=adv_win_menu8.get()
      sql = "select * from company"
      fbcursor.execute(sql)
      advdata1 = fbcursor.fetchone()

      if menuvar == 'Professional 1 (logo on left side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

          canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))

          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(150, 30, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  

          canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
          canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
          canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
              
          tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
            
          tree.column("# 1", anchor=E, stretch=NO, width=150)
          tree.heading("# 1", text="ID/SKU")
          tree.column("# 2", anchor=E, stretch=NO, width=400)
          tree.heading("# 2", text="Product/Service - Description")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Quantity")
          tree.column("# 4", anchor=E, stretch=NO, width=150)
          tree.heading("# 4", text="Unit Price")
          tree.column("# 5", anchor=E, stretch=NO, width=150)
          tree.heading("# 5", text="Price")
            
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(270, 290, 270, 330 )
          canvas.create_line(670, 290, 670, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
          canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#------------Professional 2 (logo on right side)------------- 

      elif menuvar == 'Professional 2 (logo on right side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))

          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  

          # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(829, 110, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(841, 130, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(830, 150, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(820, 170, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(834, 190, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(1047, 110, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 130, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 150, text="21-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1040, 170, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(170, 65, text=""+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
          #T_address_window = canvas.create_window(95, 80, anchor="nw", window=T_address)
          canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
          tree.column("# 1", anchor=E, stretch=NO, width=150)
          tree.heading("# 1", text="ID/SKU")
          tree.column("# 2", anchor=E, stretch=NO, width=400)
          tree.heading("# 2", text="Product/Service - Description")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Quantity")
          tree.column("# 4", anchor=E, stretch=NO, width=150)
          tree.heading("# 4", text="Unit Price")
          tree.column("# 5", anchor=E, stretch=NO, width=150)
          tree.heading("# 5", text="Price")
      
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(270, 290, 270, 330 )
          canvas.create_line(670, 290, 670, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
          canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 320, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 345, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 370, text="$18.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 395, text="$20.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 445, text="$100.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 465, text="$138.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#------------Simplified 1 (logo on left side)------------- 

      elif menuvar == 'Simplified 1 (logo on left side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(150, 25, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  
          #canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
          canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
      
          tree.column("# 1", anchor=E, stretch=NO, width=700)
          tree.heading("# 1", text="Product/Service - Description")
          tree.column("# 2", anchor=E, stretch=NO, width=150)
          tree.heading("# 2", text="Quantity")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Price")
            
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


#------------Simplified 2 (logo on right side)-------------

      elif menuvar == 'Simplified 2 (logo on right side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  

          # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(829, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(841, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(830, 160, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(820, 180, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(834, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(1047, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1040, 180, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(170, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
          canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
              
          tree.column("# 1", anchor=E, stretch=NO, width=700)
          tree.heading("# 1", text="Product/Service - Description")
          tree.column("# 2", anchor=E, stretch=NO, width=150)
          tree.heading("# 2", text="Quantity")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Price")
        
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

  #------------Business Classic------------- 

      elif menuvar == 'Business Classic':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_line(100, 60, 1120, 60, fill="orange")
          #canvas.create_line(1000, 60, 600, 60, fill="grey")

          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,100))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=100,image = adv_image) 
            adv_window_image = canvas.create_window(140, 100, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  


          # canvas.create_text(250, 155, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(560, 85, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(535, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
          # adv_btlabel = Label(canvas,width=20,height=10,text=""+caddent.get('1.0', 'end-1c')) 
          # adv_window_label = canvas.create_window(530, 110, anchor="nw", window=adv_btlabel)
          canvas.create_text(530, 190, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(530, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(530, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(536, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(536, 190, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(524, 210, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(749, 95, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(791, 110, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(800, 125, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(760, 140, text="United States", fill="black", font=('Helvetica 10'))

          canvas.create_text(745, 160, text="Invoice", fill="black", font=('Helvetica 11'))
          canvas.create_text(760, 180, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(750, 200, text="Due date", fill="black", font=('Helvetica 11'))

          canvas.create_text(947, 160, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(950, 180, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(950, 200, text="21-05-2022", fill="black", font=('Helvetica 11'))
          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
        
          tree.column("# 1", anchor=E, stretch=NO, width=150)
          tree.heading("# 1", text="Product/Service")
          tree.column("# 2", anchor=E, stretch=NO, width=400)
          tree.heading("# 2", text="Description")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Unit Price")
          tree.column("# 4", anchor=E, stretch=NO, width=150)
          tree.heading("# 4", text="Quantity")
          tree.column("# 5", anchor=E, stretch=NO, width=150)
          tree.heading("# 5", text="Price")
              
          window = canvas.create_window(120, 230, anchor="nw", window=tree)

          canvas.create_line(120, 270, 1120, 270 )
          canvas.create_line(120, 230, 120, 270 )
          canvas.create_line(270, 230, 270, 270 )
          canvas.create_line(670, 230, 670, 270 )
          canvas.create_line(820, 230, 820, 270 )
          canvas.create_line(970, 230, 970, 270 )
          canvas.create_line(1120, 230, 1120, 270)
          canvas.create_line(1120, 270, 1120, 420)
          canvas.create_line(670, 295, 1120, 295)
          canvas.create_line(670, 320, 1120, 320)
          canvas.create_line(670, 345, 1120, 345)
          canvas.create_line(670, 370, 1120, 370)
          canvas.create_line(670, 395, 1120, 395)
          canvas.create_line(670, 420, 1120, 420)

          canvas.create_text(165, 260, text="PROD-0001", fill="black", font=('Helvetica 10'))
          canvas.create_text(400, 260, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(734, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(734, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(734, 260, text="$200.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(890, 260, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          # canvas.create_text(1080, 260, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(697, 285, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 285, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(692, 310, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 310, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 310, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 310, text="$18.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(737, 335, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 335, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 335, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 335, text="$20.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 360, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 360, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 360, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(715, 360, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 385, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 385, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 385, text="100.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(705, 385, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 410, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 410, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 410, text="$138.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(700, 410, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_line(100, 480, 1120, 480, fill="orange")
          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(100, 600, 1120, 600, fill="orange")
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
          pass

  adv_win_menu8 = StringVar()
  adv_winstyle8 = ttk.Combobox(seventhtab,textvariable=adv_win_menu8)
  adv_winstyle8.bind("<<ComboboxSelected>>", adv_maindropmenu)
  adv_winstyle8["values"] = ("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
  if not advdata:
    adv_winstyle8.current(0)
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

    canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))

    canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    # T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    # T_address.tag_configure('tag_name',justify='right')
    # T_address.insert('1.0', advdata[2])
    # T_address.tag_add('tag_name','1.0', 'end')
    # T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
    canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
        
    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(270, 290, 270, 330 )
    canvas.create_line(670, 290, 670, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Professional 1 (logo on left side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))

    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(150, 30, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  

    canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
        
    canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
        
    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(270, 290, 270, 330 )
    canvas.create_line(670, 290, 670, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Professional 2 (logo on right side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  
    #canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(829, 110, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(841, 130, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(830, 150, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(820, 170, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(834, 190, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(1047, 110, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 130, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 150, text="21-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1040, 170, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(170, 65, text=""+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
    canvas.create_text(125, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))
    
    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(270, 290, 270, 330 )
    canvas.create_line(670, 290, 670, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 320, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 345, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 370, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 395, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 445, text="$100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 465, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


  elif advdata[32] == 'Simplified 1 (logo on left side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(150, 25, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  
    #canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
    canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=700)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=150)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Simplified 2 (logo on right side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  

    # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(829, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(841, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(830, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(820, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(834, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(1047, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1040, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(170, 55, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(135, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
    canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
        
    tree.column("# 1", anchor=E, stretch=NO, width=700)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=150)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Price")
        
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Business Classic':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_line(100, 60, 1120, 60, fill="orange")
    #canvas.create_line(1000, 60, 600, 60, fill="grey")

    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,100))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=100,image = adv_image) 
      adv_window_image = canvas.create_window(140, 100, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  


    # canvas.create_text(250, 155, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(560, 85, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(535, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
    # adv_btlabel = Label(canvas,width=20,height=10,text=""+caddent.get('1.0', 'end-1c')) 
    # adv_window_label = canvas.create_window(530, 110, anchor="nw", window=adv_btlabel)
    canvas.create_text(530, 190, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(530, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(530, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(536, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(536, 190, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(524, 210, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(749, 95, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(791, 110, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(800, 125, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(760, 140, text="United States", fill="black", font=('Helvetica 10'))

    canvas.create_text(745, 160, text="Invoice", fill="black", font=('Helvetica 11'))
    canvas.create_text(760, 180, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(750, 200, text="Due date", fill="black", font=('Helvetica 11'))

    canvas.create_text(947, 160, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(950, 180, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(950, 200, text="21-05-2022", fill="black", font=('Helvetica 11'))
    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
        
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="Product/Service")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Unit Price")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Quantity")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
        
    window = canvas.create_window(120, 230, anchor="nw", window=tree)

    canvas.create_line(120, 270, 1120, 270 )
    canvas.create_line(120, 230, 120, 270 )
    canvas.create_line(270, 230, 270, 270 )
    canvas.create_line(670, 230, 670, 270 )
    canvas.create_line(820, 230, 820, 270 )
    canvas.create_line(970, 230, 970, 270 )
    canvas.create_line(1120, 230, 1120, 270)
    canvas.create_line(1120, 270, 1120, 420)
    canvas.create_line(670, 295, 1120, 295)
    canvas.create_line(670, 320, 1120, 320)
    canvas.create_line(670, 345, 1120, 345)
    canvas.create_line(670, 370, 1120, 370)
    canvas.create_line(670, 395, 1120, 395)
    canvas.create_line(670, 420, 1120, 420)

    canvas.create_text(165, 260, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 260, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(734, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(734, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(734, 260, text="$200.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(890, 260, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(1080, 260, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(697, 285, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 285, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(692, 310, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 310, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 310, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 310, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(737, 335, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 335, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 335, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 335, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 360, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 360, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 360, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(715, 360, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 385, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 385, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 385, text="100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(705, 385, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 410, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 410, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 410, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 410, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_line(100, 480, 1120, 480, fill="orange")
    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(100, 600, 1120, 600, fill="orange")
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  else:
    pass
  adv_winstyle8.place(x=2 ,y=270, width=220)
  #adv_winstyle8.current(0)



   ###################################tab08###########################

  eighttab1=Frame(tab08, relief=GROOVE, bg="#f8f8f2")
  eighttab1.pack(side="top", fill=BOTH)

  eighttab=Frame(eighttab1, bg="#f5f3f2", height=700)
  eighttab.pack(side="top", fill=BOTH)


  sql = "select * from company"
  fbcursor.execute(sql)
  emdata = fbcursor.fetchone()


  lbl01 = Label(eighttab,text="Purchase Order E-Mail Tmplate",font="TimesNewRoman 12 ")
  lbl01.place(x=2,y=20)

  def selected(event):
    paym=em_menu.get()
    lbl01.place_forget()
    memaiframe.delete("1.0",END) 
    if paym == "Purchase Order E-Mail Template":
      lb1 = Label(eighttab,text='Purchase Order E-Mail Template',font="TimesNewRoman 12 ")
      lb1.place(x=2,y=20)

      def select_list(event):
        memaiframe.insert('1.0',lbx.get(ANCHOR))
      lbx = Listbox(eighttab,  height=29, width=34)
      lbx.insert(END, "{{Company_Name}}")
      lbx.insert(END, "{{Company_Address}}")
      lbx.insert(END, "{{Company_Email1}}")
      lbx.insert(END, "{{Customer_Name}}")
      lbx.insert(END, "{{Customer_Address}}")
      lbx.insert(END, "{{Customer_Email}}")
      lbx.insert(END, "{{Purchase_Order_Number}}")
      lbx.insert(END, "{{Purchase_Order_Date}}")
      lbx.insert(END, "{{Purchase_Order_Total}}")
      lbx.insert(END, "{{Current_date}}")
      lbx.place(x=1090, y=46)
      lbx.bind('<Double-1>', select_list)
    

    elif paym == "Estimate E-Mail Template":
      lb4 = Label(eighttab,text='Estimate E-Mail Template  ',font="TimesNewRoman 12 ")
      lb4.place(x=2,y=20)

      def select_list(event):
        memaiframe.insert('1.0',lbx.get(ANCHOR))
      lbx = Listbox(eighttab,  height=29, width=34)
      lbx.insert(END, "{{Company_Name}}")
      lbx.insert(END, "{{Company_Address}}")
      lbx.insert(END, "{{Company_Email1}}")
      lbx.insert(END, "{{Customer_Name}}")
      lbx.insert(END, "{{Customer_Address}}")
      lbx.insert(END, "{{Customer_Email}}")
      lbx.insert(END, "{{Estimate_Number}}")
      lbx.insert(END, "{{Estimate_Date}}")  
      lbx.insert(END, "{{Estimate_Total}}")
      lbx.insert(END, "{{Estimate_Balance}}")
      lbx.insert(END, "{{Current_date}}")
      lbx.place(x=1090, y=46)
      lbx.bind('<Double-1>', select_list)



    
    elif paym == "Order E-Mail Template":

      lb2 = Label(eighttab,text='Order E-Mail Template      ',font="TimesNewRoman 13 ")
      lb2.place(x=2,y=20)

      def select_list(event):
        memaiframe.insert('1.0',lbx.get(ANCHOR))
      lbx = Listbox(eighttab,  height=29, width=34)
      lbx.insert(END, "{{Company_Name}}")
      lbx.insert(END, "{{Company_Address}}")
      lbx.insert(END, "{{Company_Email1}}")
      lbx.insert(END, "{{Customer_Name}}")
      lbx.insert(END, "{{Customer_Address}}")
      lbx.insert(END, "{{Customer_Email}}")
      lbx.insert(END, "{{Order_Number}}")
      lbx.insert(END, "{{Order_Date}}")
      lbx.insert(END, "{{Order_Total}}")
      lbx.insert(END, "{{Order_Balance}}")
      lbx.insert(END, "{{Current_date}}")
      lbx.place(x=1090, y=46)
      lbx.bind('<Double-1>', select_list)
      

      
    elif paym == "Invoice E-Mail Template":
      lb3 = Label(eighttab,text='Invoice E-Mail Template     ',font="TimesNewRoman 12 ")
      lb3.place(x=2,y=20)

      def select_list(event):
        memaiframe.insert('1.0',lbx.get(ANCHOR))
      lbx = Listbox(eighttab,  height=29, width=34)
      lbx.insert(END, "{{Company_Name}}")
      lbx.insert(END, "{{Company_Address}}")
      lbx.insert(END, "{{Company_Email1}}")
      lbx.insert(END, "{{Customer_Name}}")
      lbx.insert(END, "{{Customer_Address}}")
      lbx.insert(END, "{{Customer_Email}}")
      lbx.insert(END, "{{Invoice_Number}}")
      lbx.insert(END, "{{Invoice_Date}}")
      lbx.insert(END, "{{Invoice_Due_Date}}")
      lbx.insert(END, "{{Invoice_OrderRef}}")
      lbx.insert(END, "{{Invoice_Total}}")
      lbx.insert(END, "{{Invoice_TotalPaid}}")
      lbx.insert(END, "{{Invoice_Balance}}")
      lbx.insert(END, "{{Current_date}}")
      lbx.place(x=1090, y=46)
      lbx.bind('<Double-1>', select_list)
  
     
    elif paym == "Payment Receipt Template":
      lb5 = Label(eighttab,text='Payment Receipt Template',font="TimesNewRoman 12 ")
      lb5.place(x=2,y=20)

      def select_list(event):
        memaiframe.insert('1.0',lbx.get(ANCHOR))
      lbx = Listbox(eighttab,  height=29, width=34)
      lbx.insert(END, "{{Company_Name}}")
      lbx.insert(END, "{{Company_Address}}")
      lbx.insert(END, "{{Company_Email1}}")
      lbx.insert(END, "{{Customer_Name}}")
      lbx.insert(END, "{{Customer_Address}}")
      lbx.insert(END, "{{Customer_Email}}")
      lbx.insert(END, "{{Invoice_Number}}")
      lbx.insert(END, "{{Invoice_Date}}")
      lbx.insert(END, "{{Invoice_Due_Date}}")
      lbx.insert(END, "{{Invoice_OrderRef}}")
      lbx.insert(END, "{{Invoice_Total}}")
      lbx.insert(END, "{{Invoice_TotalPaid}}")
      lbx.insert(END, "{{Invoice_Balance}}")
      lbx.insert(END, "{{Current_date}}")
      lbx.insert(END, "{{Currency_Sign}}")
      lbx.insert(END, "{{Payment_Date}}")
      lbx.insert(END, "{{Payment_Amount}}")
      lbx.insert(END, "{{Payment_Mode}}")
      lbx.insert(END, "{{Payment_Description}}")
      lbx.insert(END, "{{Payment_ID}}")
      lbx.place(x=1090, y=46)
      lbx.bind('<Double-1>', select_list)
      memaiframe.insert('1.0','Dear {{Customer_Name}},\n\nThis message is to inform you that your payment of {{Currency_Sign}}{{Payment_Amount}} {{Currency}} for Invoice# {{Invoice_Number}} has been received."\n\nInvoice ID: {{Invoice_Number}}\nPayment Date: {{Payment_Date}}\nAmount: {{Currency_Sign}}{{Payment_Amount}} {{Currency}}\nPaid by: {{Payment_Mode}}\nDescription: {{Payment_Description}}\n\nThank you for your business.\n{{Company_Name}}')


  fontSize=12
  fontStyle='arial'
  def font_style(event):
    global fontStyle
    fontStyle=font_family__variable.get()
    memaiframe.config(font=(fontStyle,fontSize))

  def font_size(event):
    global fontSize
    fontSize=size_variable.get()
    memaiframe.config(font=(fontStyle,fontSize))

  def bold_text():
    bold_font = font.Font(memaiframe, memaiframe.cget("font"))
    bold_font.configure(weight="bold")
    memaiframe.tag_configure("bold", font=bold_font)
    current_tags = memaiframe.tag_names("sel.first")
    if "bold" in current_tags:
      memaiframe.tag_remove("bold", "sel.first", "sel.last")
    else:
      memaiframe.tag_add("bold", "sel.first", "sel.last")
   
  
  def italic_text():
    italic_font = font.Font(memaiframe, memaiframe.cget("font"))
    italic_font.configure(slant="italic")
    memaiframe.tag_configure("italic", font=italic_font)
    current_tags = memaiframe.tag_names("sel.first")
    if "italic" in current_tags:
      memaiframe.tag_remove("italic", "sel.first", "sel.last")
    else:
      memaiframe.tag_add("italic", "sel.first", "sel.last")


  def underline_text():
    try:
        if memaiframe.tag_nextrange('underline_selection', 'sel.first', 'sel.last') != ():
            memaiframe.tag_remove('underline_selection', 'sel.first', 'sel.last')
        else:
            memaiframe.tag_add('underline_selection', 'sel.first', 'sel.last')
            memaiframe.tag_configure('underline_selection', underline=True)
    except TclError:
        pass

  def color_select():
    color=colorchooser.askcolor()[1]
    if color:
      color_font = font.Font(memaiframe, memaiframe.cget("font"))
      memaiframe.tag_configure("colored", font=color_font, foreground=color)
      current_tags = memaiframe.tag_names("sel.first")
      if "colored" in current_tags:
        memaiframe.tag_remove("colored", "sel.first", "sel.last")
      else:
        memaiframe.tag_add("colored", "sel.first", "sel.last")

  def align_right():
    data=memaiframe.get(0.0,END)
    memaiframe.tag_config('right',justify=RIGHT)
    memaiframe.delete(0.0,END)
    memaiframe.insert(INSERT,data,'right')

  def align_left():
    data=memaiframe.get(0.0,END)
    memaiframe.tag_config('left',justify=LEFT)
    memaiframe.delete(0.0,END)
    memaiframe.insert(INSERT,data,'left')

  def align_center():
    data=memaiframe.get(0.0,END)
    memaiframe.tag_config('center',justify=CENTER)
    memaiframe.delete(0.0,END)
    memaiframe.insert(INSERT,data,'center')

  em_menu = StringVar()
  winstyle = ttk.Combobox(eighttab,textvariable=em_menu,width=28)
  winstyle['values'] = ('Invoice E-Mail Template','Order E-Mail Template','Estimate E-Mail Template','Payment Receipt Template','Purchase Order E-Mail template')
  winstyle.bind("<<ComboboxSelected>>",selected)
  if  not emdata:
    pass
  else:
    winstyle.insert(0, emdata[2])
  winstyle.place(x=280 ,y=20)
  winstyle.current(4)



  # savebtn=Button(eighttab,image=saves,text="Save Settings",compound = LEFT, height=15, width=100)
  # savebtn.place(x=500, y=20)


    
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=78, padding=10)
  mess_Notebook = ttk.Notebook(eighttab)
  emailmessage_Frame = Frame(mess_Notebook, height=430, width=1060)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.place(x=5, y=50)

  meframe = StringVar()
  memaiframe=Text(emailmessage_Frame,font=('arial 17'),undo=True,width=130,height=400)
  if not emdata:
    pass
  else:
    memaiframe.insert('1.0', emdata[53])
  memaiframe.pack(padx=0,pady=28,expand=False)


  scrollbar1 = Scrollbar(emailmessage_Frame,orient=VERTICAL)
  scrollbar2= Scrollbar(memaiframe,orient=HORIZONTAL,command=memaiframe.xview,width=0)
  scrollbar2.pack(fill=X,expand=True,side=BOTTOM,padx=502,pady=200)
  memaiframe.config(xscrollcommand=scrollbar2.set)
  memaiframe.config(yscrollcommand=scrollbar1.set)
  scrollbar1.config(command=memaiframe.yview)
  scrollbar1.place(x =1040  , y=0, height=432)
  scrollbar2.config(command=memaiframe.xview)


 
  

  btn1=Button(emailmessage_Frame,width=20,height=20,compound = LEFT,image=selectall,command=lambda :memaiframe.event_generate('<Control a>'))
  btn1.place(x=5, y=1)

        
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut,command=lambda :memaiframe.event_generate('<Control x>'))
  btn2.place(x=36, y=1)

  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy,command=lambda :memaiframe.event_generate('<Control c>'))
  btn3.place(x=73, y=1)

  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste,command=lambda :memaiframe.event_generate('<Control v>'))
  btn4.place(x=105, y=1)

  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo, command=lambda:memaiframe.event_generate("<<Undo>>"))
  btn5.place(x=140, y=1)

  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo, command=lambda:memaiframe.event_generate("<<Redo>>"))
  btn6.place(x=175, y=1)

  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold,command=bold_text)
  btn7.place(x=210, y=1)

  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics,command=italic_text)
  btn8.place(x=245, y=1)

  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline,command=underline_text)
  btn9.place(x=280, y=1)

  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left,command=align_left)
  btn10.place(x=315, y=1)

  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right,command=align_right)
  btn11.place(x=350, y=1)

  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center,command=align_center)
  btn12.place(x=385, y=1)

  # btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink,command=open)
  # btn13.place(x=420, y=1)
        
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove,command=lambda :memaiframe.delete(0.0,END))
  btn14.place(x=420, y=1)

  btn15=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=color,command=color_select)
  btn15.place(x=455, y=1)

  # btn16=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=save,command=save_file)
  # btn16.place(x=525, y=1)
 

  size_variable=IntVar()
  compo = ttk.Combobox(emailmessage_Frame, width=14,textvariable=size_variable,values=tuple(range(10,80)))
  compo['values'] =('11','12','13','14','15','16','17')
  compo.place(x=600, y=5)
  compo.current(4)

  compo.bind('<<ComboboxSelected>>',font_size)


  font_families=font.families()
  font_family__variable=StringVar()

  def select(event):
    memaiframe.insert('1.0',lbx01.get(ANCHOR))

  attachlbframe=LabelFrame(eighttab,text="placeholders(double click to insert)", height=500, width=233)
  attachlbframe.place(x=1080, y=22)

  lbx01 = Listbox(eighttab, height=28, width=34)
  lbx01.insert(END, "{{Company_Name}}")
  lbx01.insert(END, "{{Company_Address}}")
  lbx01.insert(END, "{{Company_Email1}}")
  lbx01.insert(END, "{{Customer_Name}}")
  lbx01.insert(END, "{{Customer_Address}}")
  lbx01.insert(END, "{{Customer_Email}}")
  lbx01.insert(END, "{{Purchase_Order_Number}}")
  lbx01.insert(END, "{{Purchase_Order_Date}}")
  lbx01.insert(END, "{{Purchase_Order_Total}}")
  lbx01.insert(END, "{{Current_date}}")
  lbx01.place(x=1090, y=46)
  lbx01.bind('<Double-1>', select)

     

################################### tab09 ###########################


  ninetab1=Frame(tab09, relief=GROOVE, bg="#f8f8f2")
  ninetab1.pack(side="top", fill=BOTH)
  ninetab=Frame(ninetab1, bg="#f5f3f2", height=700)
  ninetab.pack(side="top", fill=BOTH)

  global filename_btn,filename_logo

  filename_btn = ""
  filename_logo = ""
  def payments():
    checkbtn1 = showpaidbol.get()
    checkbtn2 = sendpaybol.get()                        
    checkbtn3 = insrtpaybol.get()
    checkbtn4 =attachupdbol.get()
    payrece = enterec.get()
    payin = enterin.get()
    amrece = camou.get()
    des = descr.get()
    paymentrece = payrec.get()
    receipt = paym.get()
    date = payd.get()
    pay_amount = payma.get()
    total = tota.get()
    total_paid = paid.get()
    balance_due = due.get()
    payment_prefix = receipt_prefix.get()

    sql = "select * from payments"
    fbcursor.execute(sql)
    i = fbcursor.fetchall()
    if not i:
      if filename_btn == "":
        sql = 'insert into payments(show_paid,send_payment,insert_paypal,attach_updated,payment_receipt,payment_invoice,amount_received,description,payment_received,payment_rece,payment_date,payment_amount,total_amount,total_paid,balance_due,prefix) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (checkbtn1,checkbtn2,checkbtn3,checkbtn4,payrece,payin,amrece,des,paymentrece,receipt,date,pay_amount,total,total_paid,balance_due,payment_prefix)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename_btn, os.getcwd()+'/images/'+filename_btn.split('/')[-1])
        sql = 'insert into payments(show_paid,send_payment,insert_paypal,attach_updated,payment_receipt,payment_invoice,amount_received,description,payment_received,payment_rece,payment_date,payment_amount,total_amount,total_paid,balance_due,prefix,load_button) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (checkbtn1,checkbtn2,checkbtn3,checkbtn4,payrece,payin,amrece,des,paymentrece,receipt,date,pay_amount,total,total_paid,balance_due,payment_prefix,filename_btn.split('/')[-1])
        fbcursor.execute(sql, val)
        fbilldb.commit()
        try:
          shutil.copyfile(filename_logo, os.getcwd()+'/images/'+filename_logo.split('/')[-1])
          sql = "update payments set show_paid=%s, send_payment=%s, insert_paypal=%s,attach_updated=%s,payment_receipt=%s,payment_invoice=%s,amount_received=%s,description=%s,payment_received=%s,payment_rece=%s,payment_date=%s,payment_amount=%s,total_amount=%s,total_paid=%s,balance_due=%s,prefix=%s,load_logo=%s"
          val = (checkbtn1,checkbtn2,checkbtn3,checkbtn4,payrece,payin,amrece,des,paymentrece,receipt,date,pay_amount,total,total_paid,balance_due,payment_prefix,filename_logo.split('/')[-1])
          fbcursor.execute(sql, val)
          fbilldb.commit()
        except:
          pass
    else:
      if filename_btn == "":
        sql = "update payments set show_paid=%s, send_payment=%s, insert_paypal=%s,attach_updated=%s,payment_receipt=%s,payment_invoice=%s,amount_received=%s,description=%s,payment_received=%s,payment_rece=%s,payment_date=%s,payment_amount=%s,total_amount=%s,total_paid=%s,balance_due=%s,prefix=%s"
        val = (checkbtn1,checkbtn2,checkbtn3,checkbtn4,payrece,payin,amrece,des,paymentrece,receipt,date,pay_amount,total,total_paid,balance_due,payment_prefix)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename_btn, os.getcwd()+'/images/'+filename_btn.split('/')[-1])
        sql = "update payments set show_paid=%s, send_payment=%s, insert_paypal=%s,attach_updated=%s,payment_receipt=%s,payment_invoice=%s,amount_received=%s,description=%s,payment_received=%s,payment_rece=%s,payment_date=%s,payment_amount=%s,total_amount=%s,total_paid=%s,balance_due=%s,prefix=%s,load_button=%s"
        val = (checkbtn1,checkbtn2,checkbtn3,checkbtn4,payrece,payin,amrece,des,paymentrece,receipt,date,pay_amount,total,total_paid,balance_due,payment_prefix,filename_btn.split('/')[-1])
        fbcursor.execute(sql, val)
        fbilldb.commit()
        try:
          shutil.copyfile(filename_logo, os.getcwd()+'/images/'+filename_logo.split('/')[-1])
          sql = "update payments set show_paid=%s, send_payment=%s, insert_paypal=%s,attach_updated=%s,payment_receipt=%s,payment_invoice=%s,amount_received=%s,description=%s,payment_received=%s,payment_rece=%s,payment_date=%s,payment_amount=%s,total_amount=%s,total_paid=%s,balance_due=%s,prefix=%s,load_logo=%s"
          val = (checkbtn1,checkbtn2,checkbtn3,checkbtn4,payrece,payin,amrece,des,paymentrece,receipt,date,pay_amount,total,total_paid,balance_due,payment_prefix,filename_logo.split('/')[-1])
          fbcursor.execute(sql, val)
          fbilldb.commit()
        except:
          pass
          

  sql = "select * from payments"
  fbcursor.execute(sql)
  padata = fbcursor.fetchone()

    
  showpaidbol =  IntVar()
  showp = Checkbutton(ninetab,variable=showpaidbol,
                      text="Show 'PAID' image on fully paid invoices",
                      onvalue= 1 ,
                      offvalue= 0,
                    )
  showp.place(x=5,y=20)
  if  not padata:
        pass
  else:
    if padata[2] == 1:
      showp.select()
    else:
      showp.deselect()



      
  sendpaybol =  IntVar()
  sendp = Checkbutton(ninetab,variable=sendpaybol,
                        text="Send payment receipt email after payment recorderd",
                        onvalue= 1 ,
                        offvalue= 0,
                    )
  sendp.place(x=5,y=50)
  if  not padata:
    pass
  else:
    if padata[3] == 1:
      sendp.select()
    else:
      sendp.deselect()


  insrtpaybol =  IntVar()
  insert = Checkbutton(ninetab,variable=insrtpaybol,
                        text="Insert PayPal 'Pay Now' button with the remaining balance on unpaid PDF invoices",
                        onvalue= 1 ,
                        offvalue= 0,
                      )
  insert.place(x=340,y=20)
  if  not padata:
        pass
  else:
    if padata[4] == 1:
      insert.select()
    else:
      insert.deselect()



  attachupdbol =  IntVar()
  attach = Checkbutton(ninetab,variable=attachupdbol,
                        text="Attach updated invoice to payment receipt email",
                        onvalue= 1 ,
                        offvalue= 0,
                      )
  attach.place(x=340,y=50)
  if  not padata:
        pass
  else:
    if padata[5] == 1:
      attach.select()
    else:
      attach.deselect()


    
  messagelbframe=LabelFrame(ninetab,text="Payment Receipt Text Labels", height=400, width=460)
  messagelbframe.place(x=5, y=100)

  enterec = StringVar()
  pnr = Label(ninetab,text="Payment Receipt")
  pnr.place(x=15,y=130)
  enrec = Entry(ninetab,textvariable=enterec,width=30)
  if  not padata:
    enterec.set('Payment Receipt')
  else:
    enrec.insert(0, padata[6])
  enrec.place(x=15,y=160)


  enterin = StringVar()
  enin = Label(ninetab,text="Payment for Invoice#")
  enin.place(x=15,y=190)
  newin = Entry(ninetab,textvariable=enterin,width=30)
  if  not padata:
    enterin.set('Payment for Invoice#')
  else:
    newin.insert(0, padata[7])
  newin.place(x=15,y=215)

    
  camou = StringVar()
  carf = Label(ninetab,text="Amount received from:")
  carf.place(x=15,y=245)
  camrf = Entry(ninetab,textvariable=camou,width=30)
  if  not padata:
    camou.set('Amount received from:')
  else:
    camrf.insert(0, padata[8])
  camrf.place(x=15,y=270)
  

  descr = StringVar()
  des = Label(ninetab,text="Description:")
  des.place(x=15,y=300)
  descrip = Entry(ninetab,textvariable=descr,width=30)
  if  not padata:
    descr.set('Description:')
  else:
    descrip.insert(0, padata[9])
  descrip.place(x=15,y=325)

  payrec = StringVar()
  pay = Label(ninetab,text="Payment Received in:")
  pay.place(x=15,y=355)
  payrecin = Entry(ninetab,textvariable=payrec,width=30)
  if  not padata:
    payrec.set('Payment Received in:')
  else:
    payrecin.insert(0, padata[10])
  payrecin.place(x=15,y=380)

  paym = StringVar()
  payr = Label(ninetab,text="Payment Receipt#:")
  payr.place(x=15,y=410)
  paymr = Entry(ninetab,textvariable=paym,width=30)
  if  not padata:
    paym.set('Payment Receipt#:')
  else:
    paymr.insert(0, padata[11])
  paymr.place(x=15,y=435)

  payd = StringVar()
  payda = Label(ninetab,text="Payment Date:")
  payda.place(x=250,y=130)
  paydate = Entry(ninetab,textvariable=payd,width=30)
  if  not padata:
    payd.set('Payment Date:')
  else:
    paydate.insert(0, padata[12])
  paydate.place(x=250,y=160)
    
  payma = StringVar()
  pya = Label(ninetab,text="Payment Amount:")
  pya.place(x=250,y=190)
  paymam = Entry(ninetab,textvariable=payma,width=30)
  if  not padata:
    payma.set('Payment Amount:')
  else:
    paymam.insert(0, padata[13])
  paymam.place(x=250,y=215)
    
    
  tota = StringVar()
  tad = Label(ninetab,text="Total Amount Due")
  tad.place(x=250,y=245)
  totamo = Entry(ninetab,textvariable=tota,width=30)
  if  not padata:
    tota.set('Total Amount Due')
  else:
    totamo.insert(0, padata[14])
  totamo.place(x=250,y=270)

  paid = StringVar()
  totp = Label(ninetab,text="Total Paid:")
  totp.place(x=250,y=300)
  totpai = Entry(ninetab,textvariable=paid,width=30)
  if  not padata:
    paid.set('Total Paid:')
  else:
    totpai.insert(0, padata[15])
  totpai.place(x=250,y=325)

  due = StringVar()
  bdue = Label(ninetab,text="Balance Due")
  bdue.place(x=250,y=355)
  badue = Entry(ninetab,textvariable=due,width=30)
  if  not padata:
    due.set('Balance Due')
  else:
    badue.insert(0, padata[16])
  badue.place(x=250,y=380)

  receipt_prefix = StringVar()
  pprefix = Label(ninetab,text="Payment Receipt Prefix")
  pprefix.place(x=250,y=410)
  prprefix = Entry(ninetab,textvariable=receipt_prefix,width=30)
  if  not padata:
    receipt_prefix.set('RCPT')
  else:
    prprefix.insert(0, padata[17])
  prprefix.place(x=250,y=435)

  savebtn = Button(ninetab,text="Save Settings",width=12,command=payments)
  savebtn.place(x=40,y=470)

  def restore():
    enterec = StringVar()
    pnr = Label(ninetab,text="Payment Receipt")
    pnr.place(x=15,y=130)
    enrec = Entry(ninetab,textvariable=enterec,width=30)
    enrec.place(x=15,y=160)
    enterec.set('Payment Receipt')


    enterin = StringVar()
    enin = Label(ninetab,text="Payment for Invoice#")
    enin.place(x=15,y=190)
    newin = Entry(ninetab,textvariable=enterin,width=30)
    newin.place(x=15,y=215)
    enterin.set('Payment for Invoice#')
  
  
    camou = StringVar()
    carf = Label(ninetab,text="Amount received from:")
    carf.place(x=15,y=245)
    camrf = Entry(ninetab,textvariable=camou,width=30)
    camrf.place(x=15,y=270)
    camou.set('Amount received from:')


    descr = StringVar()
    des = Label(ninetab,text="Description:")
    des.place(x=15,y=300)
    descrip = Entry(ninetab,textvariable=descr,width=30)
    descrip.place(x=15,y=325)
    descr.set('Description:')


    payrec = StringVar()
    pay = Label(ninetab,text="Payment Received in:")
    pay.place(x=15,y=355)
    payrecin = Entry(ninetab,textvariable=payrec,width=30)
    payrecin.place(x=15,y=380)
    payrec.set('Payment Received in:')


    paym = StringVar()
    payr = Label(ninetab,text="Payment Receipt#:")
    payr.place(x=15,y=410)
    paymr = Entry(ninetab,textvariable=paym,width=30)
    paymr.place(x=15,y=435)
    paym.set('Payment Receipt#:')


    payd = StringVar()
    payda = Label(ninetab,text="Payment Date:")
    payda.place(x=250,y=130)
    paydate = Entry(ninetab,textvariable=payd,width=30)
    paydate.place(x=250,y=160)
    payd.set('Payment Date:')
    
    payma = StringVar()
    pya = Label(ninetab,text="Payment Amount:")
    pya.place(x=250,y=190)
    paymam = Entry(ninetab,textvariable=payma,width=30)
    paymam.place(x=250,y=215)
    payma.set('Payment Amount:')
    
    
    tota = StringVar()
    tad = Label(ninetab,text="Total Amount Due")
    tad.place(x=250,y=245)
    totamo = Entry(ninetab,textvariable=tota,width=30)
    totamo.place(x=250,y=270)
    tota.set('Total Amount Due')

    paid = StringVar()
    totp = Label(ninetab,text="Total Paid:")
    totp.place(x=250,y=300)
    totpai = Entry(ninetab,textvariable=paid,width=30)
    totpai.place(x=250,y=325)
    paid.set('Total Paid:')

    due = StringVar()
    bdue = Label(ninetab,text="Balance Due")
    bdue.place(x=250,y=355)
    badue = Entry(ninetab,textvariable=due,width=30)
    badue.place(x=250,y=380)
    due.set('Balance Due')

    receipt_prefix = StringVar()
    pprefix = Label(ninetab,text="Payment Receipt Prefix")
    pprefix.place(x=250,y=410)
    prprefix = Entry(ninetab,textvariable=receipt_prefix,width=30)
    prprefix.place(x=250,y=435)
    receipt_prefix.set('RCPT')


  restrbtn = Button(ninetab,text="Restore defaults",command=restore)
  restrbtn.place(x=290,y=470)


  paidim=LabelFrame(ninetab,text="PAID Image for Invoices (max: 40mm X 25mm)", height=250, width=300)
  paidim.place(x=500, y=100)
  filename_btn=""  
  def upload_btnimg():
    global btnimg,filename_btn
    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
    filename_btn= filedialog.askopenfilename(filetypes=f_types)
    shutil.copyfile(filename_btn, os.getcwd()+'/images/'+filename_btn.split('/')[-1])
    image = Image.open(filename_btn)
    resize_image = image.resize((280, 160))
    btnimg = ImageTk.PhotoImage(resize_image)
   # b2 = Button(ninetab,image=img)
   # b2.place(x=130, y=80)
    
    btlogo = Button(ninetab,width=280,height=160,image=btnimg)
    btlogo.place(x=505,y=120)
    
  try:
    image = Image.open("images/"+padata[19])
    resize_image = image.resize((280, 160))
    image = ImageTk.PhotoImage(resize_image)
    btlogoi = Button(ninetab,width=280,height=160,image=image)
    btlogoi.place(x=505,y=120)
    btlogoi.photo = image
  except:
    pass
 
  def paid_logo():

    paid_sett = Image.open("images/paid.png")
    resize_image_paid = paid_sett.resize((280, 160))
    paid_sett = ImageTk.PhotoImage(resize_image_paid)
    btclogo = Button(ninetab,width=280,height=160,image=paid_sett)
    btclogo.place(x=505,y=120)
    btclogo.photo = paid_sett
    
  btnimg = BooleanVar()      
  btloadima = Button(ninetab,text="Load logo image",command=upload_btnimg)
  btloadima.place(x=510,y=310)

  restrbttn = Button(ninetab,text="Restore defaults",command=paid_logo)
  restrbttn.place(x=690,y=310)


  butnimg=LabelFrame(ninetab,text="PayPal Image for Invoices (max: 40mm X 10mm)", height=130, width=300)
  butnimg.place(x=500, y=370)
    
  def upload_fileimg_logo():
    global logo_img,filename_logo
    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
    filename_logo = filedialog.askopenfilename(filetypes=f_types)
    shutil.copyfile(filename_logo, os.getcwd()+'/images/'+filename_logo.split('/')[-1])
    image = Image.open(filename_logo)
    resize_image = image.resize((280, 55))
    logo_img = ImageTk.PhotoImage(resize_image)
    # b2 = Button(secondtab,image=img)
    # b2.place(x=130, y=80)
    
    btlogo = Button(ninetab,width=280,height=55,image=logo_img)
    btlogo.place(x=506,y=390)

  try:
    image = Image.open("images/"+padata[18])
    resize_image = image.resize((280, 55))
    image = ImageTk.PhotoImage(resize_image)
    bt_logo = Button(ninetab,width=280,height=55,image=image)
    bt_logo.place(x=506,y=390)
    bt_logo.photo = image
  except:
    pass
    

  
    
  def paynow_logo():
      image_paynow = Image.open("images/paynow.png")
      resize_image_paynow = image_paynow.resize((280, 55))
      image_paynow = ImageTk.PhotoImage(resize_image_paynow)
      btlogoi = Button(ninetab,width=280,height=55,image=image_paynow)
      btlogoi.place(x=506,y=390)
      btlogoi.photo = image_paynow

    
  btloadima = Button(ninetab,text="Load logo image",command=upload_fileimg_logo)
  btloadima.place(x=510,y=460)

  restrbttn = Button(ninetab,text="Restore defaults",command=paynow_logo)
  restrbttn.place(x=690,y=460)


  ################### tab010 ###################################

  tentab1=Frame(tab010, relief=GROOVE, bg="#f8f8f2")
  tentab1.pack(side="top", fill=BOTH)

  tentab=Frame(tentab1, bg="#f5f3f2", height=700)
  tentab.pack(side="top", fill=BOTH)


  sql = "select * from company"
  fbcursor.execute(sql)
  podata = fbcursor.fetchone()
  

  pver = Label(tentab,text="Purchase order# prefix")
  pver.place(x=15,y=25)

  prefix_str = StringVar()
  pre_entry = Entry(tentab,textvariable=prefix_str)
  pre_entry.place(x=16,y=50)
  if not podata:
    prefix_str.set('P.ORD')
  else:
    pre_entry.insert(0, podata[41])


  ver1 = Label(tentab,text="Starting purchase order number")
  ver1.place(x=15,y=75)

  def spincall(input):
        
    if input.isdigit():
      return True

    elif input is  "":
      return True

    else:
      return False
    

  pspin2 = Spinbox(tentab,from_=0,to=1000000,width=16)
  regi = tentab.register(spincall)

  pspin2.config(validate = "key",
               validatecommand = (regi, '%S'))
  if not podata:
    pass
  else:
    pspin2.delete(0,END)
    pspin2.insert(0,podata[43])
    pspin2.place(x=16,y=100)

    
              

  ver2 = Label(tentab,text="Header box background color")
  ver2.place(x=15,y=140)

  pwin_menu = StringVar()
  colbox = ttk.Combobox(tentab,textvariable=pwin_menu,width=27)
 # pord_win = pwin_menu.get()
  colbox['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
  if not podata:
    colbox.current(2)
  else:
    colbox.insert(0, podata[42])
  colbox.place(x=15 ,y=160)

  ver3 = Label(tentab,text="Customize purchase order text labels")
  ver3.place(x=15,y=190)

  pord_str1 = StringVar() 
  pord_lbx1 = Entry(tentab, width=30,textvariable=pord_str1)
  if not podata:
    pord_str1.set('Purchase Order')
  else:
    pord_lbx1.insert(0, podata[44])
  pord_lbx1.place(x=15,y=220)
  

  pord_str2 = StringVar() 
  pord_lbx2 = Entry(tentab, width=30,textvariable=pord_str2)
  if not podata:
    pord_str2.set('P.Order#')
  else:
    pord_lbx2.insert(0, podata[45])
  pord_lbx2.place(x=15,y=240)

  pord_str3 = StringVar() 
  pord_lbx3 = Entry(tentab,width=30,textvariable=pord_str3)
  if not podata:
    pord_str3.set('P.Order Date')
  else:
    pord_lbx3.insert(0, podata[46])
  pord_lbx3.place(x=15,y=260)

  pord_str4 = StringVar() 
  pord_lbx4 = Entry(tentab,width=30,
  textvariable=pord_str4)
  if not podata:
    pord_str4.set('Due date')
  else:
    pord_lbx4.insert(0, podata[47])
  pord_lbx4.place(x=15,y=280)


  pord_str5 = StringVar() 
  pord_lbx5 = Entry(tentab,width=30,textvariable=pord_str5)
  if not podata:
    pord_str5.set('Vendor')
  else:
    pord_lbx5.insert(0, podata[48])
  pord_lbx5.place(x=15,y=300)

  pord_str6 = StringVar() 
  pord_lbx6 = Entry(tentab, width=30,textvariable=pord_str6)
  if not podata:
    pord_str6.set('Delivery to')
  else:
    pord_lbx6.insert(0, podata[49])
  pord_lbx6.place(x=15,y=320)

  pord_str7 = StringVar() 
  pord_lbx7 = Entry(tentab, width=30,textvariable=pord_str7)
  if not podata:
    pord_str7.set('P.Order total')
  else:
    pord_lbx7.insert(0, podata[50])
  pord_lbx7.place(x=15,y=340)


  pmessagelbframe=LabelFrame(tentab,text="Predefined terms and conditions text for purchase orders",height=70, width=980)
  pmessagelbframe.place(x=248, y=396)

  pord_str8= scrolledtext.ScrolledText(tentab)
  if not podata:
    pass
  else:
    pord_str8.insert('1.0', podata[51])
  pord_str8.place(x=260,y=415,height=38,width=950)



  def restore_default_pord():
        pord_lbx1.delete(0, 'end')
        pord_lbx1.insert(0, 'Purchase Order')
        pord_lbx2.delete(0, 'end')
        pord_lbx2.insert(0, 'P.Order#')
        pord_lbx3.delete(0, 'end')
        pord_lbx3.insert(0, 'P.Order Date')
        pord_lbx4.delete(0, 'end')
        pord_lbx4.insert(0, 'Due date')
        pord_lbx5.delete(0, 'end')
        pord_lbx5.insert(0, 'Vendor')
        pord_lbx6.delete(0, 'end')
        pord_lbx6.insert(0, 'Delivery to')
        pord_lbx7.delete(0, 'end')
        pord_lbx7.insert(0, 'P.Order total')



  bttermadd1 = Button(tentab,text="Restore defaults",command=restore_default_pord)
  bttermadd1.place(x=45,y=430)



  sql = "select * from company"
  fbcursor.execute(sql)
  podata = fbcursor.fetchone()

    
  frame = Frame(tentab, width=953, height=300)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=247,y=90)
  canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
              
  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
          
  canvas.config(width=953,height=300)
  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
  canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  try:
    pord_image = Image.open("images/"+podata[13])
    pord_resize_image = pord_image.resize((200,100))
    pord_image = ImageTk.PhotoImage(pord_resize_image)

    pord_btlogo = Label(canvas,width=200,height=100,image = pord_image) 
    window_image = canvas.create_window(175, 45, anchor="nw", window=pord_btlogo)
    pord_btlogo.photo = pord_image
  except:
      pass  
  canvas.create_text(202, 160, text=""+pord_str2.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(215, 180, text=""+pord_str3.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(200, 200, text=""+pord_str4.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
  canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 160, text="PORD/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
          
  canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
  PT_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
  PT_address.tag_configure('tag_name',justify='right')
  PT_address.insert('1.0', podata[2])
  PT_address.tag_add('tag_name','1.0', 'end')
  PT_address_window = canvas.create_window(520, 80, anchor="nw", window=PT_address)
  canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
  canvas.create_text(700, 205, text=" "+pord_str1.get(), fill="black", font=('Helvetica 14 bold'))
  canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
            
  canvas.create_text(210, 260, text=""+pord_str5.get(), fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
  canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
        
  s = ttk.Style()
  s.configure('mystyle_2.Treeview.Heading', background=''+pwin_menu.get(),State='DISABLE')

  tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')

  tree.column("# 1", anchor=E, stretch=NO, width=100)
  tree.heading("# 1", text="ID/SKU")
  tree.column("# 2", anchor=E, stretch=NO, width=350)
  tree.heading("# 2", text="Product/Service - Description")
  tree.column("# 3", anchor=E, stretch=NO, width=80)
  tree.heading("# 3", text="Quantity")
  tree.column("# 4", anchor=E, stretch=NO, width=90)
  tree.heading("# 4", text="Unit Price")
  tree.column("# 5", anchor=E, stretch=NO, width=80)
  tree.heading("# 5", text="Price")
            
  window = canvas.create_window(120, 340, anchor="nw", window=tree)

  canvas.create_line(120, 390, 820, 390 )
  canvas.create_line(120, 340, 120, 365 )
  canvas.create_line(120, 365, 120, 390 )
  canvas.create_line(820, 340, 820, 540 )
  canvas.create_line(740, 340, 740, 540 )
  canvas.create_line(570, 340, 570, 540 )
  canvas.create_line(570, 415, 820, 415 )
  canvas.create_line(570, 440, 820, 440 )
  canvas.create_line(570, 465, 820, 465 )
  canvas.create_line(570, 490, 820, 490 )
  canvas.create_line(570, 515, 820, 515 )
  canvas.create_line(650, 340, 650, 390 )
  canvas.create_line(220, 340, 220, 390 )
  canvas.create_line(570, 540, 820, 540 )

  canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
  canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
      
  if comcursignpla.get() == "before amount":
    canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount":
    canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  else:
    pass
          # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
      
          # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
          # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
          # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          
  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

          # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
  else:
    pass

          # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(650, 479, text=""+pord_str6.get(), fill="black", font=('Helvetica 10 bold'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

          # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
          
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
          # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

  canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
            
  canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(150, 608, 795, 608)
          # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
  PT = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
  PT.insert('1.0', pord_str8.get('1.0', END))
  PT_window = canvas.create_window(155, 612, anchor="nw", window=PT)

  canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10')) 

  def refresh():
    sql = "select * from company"
    fbcursor.execute(sql)
    podata1 = fbcursor.fetchone()

    frame = Frame(tentab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
                
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
            
    canvas.config(width=953,height=300)
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      pord_image = Image.open("images/"+podata1[13])
      pord_resize_image = pord_image.resize((200,100))
      pord_image = ImageTk.PhotoImage(pord_resize_image)

      pord_btlogo = Label(canvas,width=200,height=100,image = pord_image) 
      window_image = canvas.create_window(175, 45, anchor="nw", window=pord_btlogo)
      pord_btlogo.photo = pord_image
    except:
        pass  
    canvas.create_text(202, 160, text=""+pord_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(215, 180, text=""+pord_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(200, 200, text=""+pord_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="PORD/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
            
    canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
            # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
    PT_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    PT_address.tag_configure('tag_name',justify='right')
    PT_address.insert('1.0', podata1[2])
    PT_address.tag_add('tag_name','1.0', 'end')
    PT_address_window = canvas.create_window(520, 80, anchor="nw", window=PT_address)
    canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 205, text=" "+pord_str1.get(), fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
              
    canvas.create_text(210, 260, text=""+pord_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
          
    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background=''+pwin_menu.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')

    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
              
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 340, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(220, 340, 220, 390 )
    canvas.create_line(570, 540, 820, 540 )

    canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
        
    if comcursignpla.get() == "before amount":
      canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    else:
      pass
            # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
        
            # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
            # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
            # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
            
    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

            # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    else:
      pass

            # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+pord_str6.get(), fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

            # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
            
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
            # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
              
    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
            # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
    PT = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    PT.insert('1.0', pord_str8.get('1.0', END))
    PT_window = canvas.create_window(155, 612, anchor="nw", window=PT)

    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))          

  refreshbtn = Button(tentab,text="Refresh",width=15,command=refresh)
  refreshbtn.place(x=1090,y=10)   
    

root.mainloop()

