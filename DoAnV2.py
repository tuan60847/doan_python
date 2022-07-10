import tkinter as tk
from tkinter import *
from tkinter import ttk
from DSSLMember import *
from tkinter.messagebox import showinfo
from Member import *
from DSBook import DSLK
from DSQLMuonTra import DSLKQLMuonTra
from QuanLyMuonTra import QuanLyMuonTra
from Book import Book
from tkcalendar import *
import os
import datetime
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("700x250")
 
    global username
    global password
    global name
    global year
    global username_entry
    global password_entry
    global name_entry
    global year_entry
    username = StringVar()
    password = StringVar()
    name=StringVar()
    year=StringVar()
 
    Label(register_screen, text="Đăng kí để mượn sách", bg="#AEF35A", width="300", height="2", font=("Calibri", 13)).pack()
    Label(register_screen, text="").pack()
    frame1 = Frame(register_screen)
    frame1.pack(fill=X)
    username_lable = Label(frame1, text="Nhap mã số bạn muốn chọn:",width=30,anchor=W)
    username_lable.pack(side=LEFT, padx=5, pady=5)
    #username_lable.grid(column=0, row=0)
    username_entry = Entry(frame1, textvariable=username,width=60)
    username_entry.pack(side=LEFT, padx=5)
    #username_entry.grid(column=1, row=0)
    frame2 = Frame(register_screen)
    frame2.pack(fill=X)
    password_lable = Label(frame2, text="Password * ",width=30,anchor=W)
    password_lable.pack(side=LEFT, padx=5, pady=5)
    ##password_lable.grid(column=0, row=1)
    password_entry = Entry(frame2, textvariable=password, show='*',width=60)
    password_entry.pack(side=LEFT, padx=5)
    ##password_entry.grid(column=1, row=1)
    frame3 = Frame(register_screen)
    frame3.pack(fill=X)
    name_lable = Label(frame3, text="Họ Tên",width=30,anchor=W)
    name_lable.pack(side=LEFT, padx=5, pady=5)
    ##name_lable.pack()
    name_entry = Entry(frame3, textvariable=name,width=60)
    name_entry.pack(side=LEFT, padx=5)
    frame4 = Frame(register_screen)
    frame4.pack(fill=X)
    year_lable = Label(frame4, text="Năm Sinh",width=30,anchor=W)
    year_lable.pack(side=LEFT, padx=5, pady=5)
    year_entry = Entry(frame4, textvariable=year,width=60)
    year_entry.pack(side=LEFT, padx=5)
    frame5 = Frame(register_screen)
    frame5.pack(fill=X)
    Label(frame5, text="",width=5).pack(side=RIGHT)
    Button(frame5, text="Register", width="10", height=1, bg="#87cefa", command = register_user).pack(side=RIGHT)
    
    
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("400x250")
    Label(login_screen, text="Đăng nhập",bg="#AEF35A",width="300",height="2", font=("Calibri", 13)).pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
    frame1 = Frame(login_screen)
    frame1.pack(fill=X)
    Label(frame1, text="Mã Thành Viên * ",width=15,anchor=W).pack(side=LEFT, padx=5, pady=5)
    username_login_entry = Entry(frame1,textvariable=username_verify,width=30)
    username_login_entry.pack(side=LEFT, padx=5, pady=5)
    Label(login_screen, text="").pack()
    frame2 = Frame(login_screen)
    frame2.pack(fill=X)
    Label(frame2, text="Password * ",width=15,anchor=W).pack(side=LEFT, padx=5, pady=5)
    password_login_entry = Entry(frame2, textvariable=password_verify, show= '*',width=30)
    password_login_entry.pack(side=LEFT, padx=5, pady=5)
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
  
 
# Implementing event on register button
 
def register_user():
    DSTV=DSLKMember()
    DSTV.DocFileMember()
    tam=False
  
    username_info = username.get()
    password_info = password.get()
    name_info = name.get()
    year_info=year.get()
    
    try:
        a=int(username_info)
        b=int(year_info)
        Chon=DSTV.demMemberTheoMS(a)
        if Chon==1:
            TV=Member(username_info,name_info,password_info,year_info,False,0)
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            name_entry.delete(0,END)
            year_entry.delete(0,END)
            registration_success()
            DSTV.themSau(TV)
            DSTV.GhiFileMember()
            register_screen.destroy()
            
        else:
            username_entry.delete(0, END)
            ID_Was_exist()
    except:
        try:
            a=int(username_info)
        except:
            False_ID()
            username_entry.delete(0, END)
        try:
            b=int(year_info)
        except:
            False_Year_TV()
            year_entry.delete(0,END)

 
# Implementing event on login button 


 
def login_verify():
   try:
    username1 = username_verify.get()
    password1 = password_verify.get()
    DSTV=DSLKMember()
    
    
    DSTV.DocFileMember() 
    
    try:
            a=int(username1)
    except:
            a=0
            False_ID()
            username_login_entry.delete(0, END)
    if a==-1 and password1=="admin":
        Admin_main()
        
    else:
      TV = DSTV.timMStraveMk(a)
      if TV!=None:
        
        if TV.MatKhau == password1:
            login_sucess()
            
        else:
            password_not_recognised()
            password_login_entry.delete(0, END)
      else:
        user_not_found()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
   except:
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
#admin
def Admin_main():
    login_screen.destroy()
    global admin_screen
    admin_screen = Toplevel()
    admin_screen.title("Menu_ADMIN")
    admin_screen.geometry("250x400")
    Label(admin_screen, text="Bạn Chọn Chức năng",bg="#AEF35A",width="300",height="2", font=("Calibri", 13)).pack()
    Label(admin_screen, text="").pack()
    Button(admin_screen,text="Menu danh sách thành viên", height="2", width="30",command=Menu_TV).pack()
    Label(admin_screen,text="").pack()
    Button(admin_screen,text="Menu danh sách Sách", height="2", width="30",command=Menu_Sach).pack()
    Label(admin_screen,text="").pack()
    Button(admin_screen,text="Menu danh sách quản lý mượn", height="2", width="30",command=Menu_Muon).pack()
    Label(admin_screen,text="").pack()
    Button(admin_screen,text="Menu danh sách quản lý trả", height="2", width="30",command=Menu_Tra).pack()
    Label(admin_screen,text="").pack()
    Button(admin_screen,text="Thoát", height="2", width="30",command=Thoat_admin).pack()
    Label(admin_screen,text="").pack()
def Thoat_admin():
    login()
    admin_screen.destroy()
#Menu Danh Sách Trả ----------------------------------------------------------------------------------------
def Menu_Tra():
    admin_screen.destroy()
    global Menu_Tra_screen
    Menu_Tra_screen = Toplevel()
    Menu_Tra_screen.title("Menu trả ")
    Menu_Tra_screen.geometry("650x400")
    global codeMuonTra
    global codeBook
    global titleBook
    global username_TV
    global name_TV
    global NgayMuonTra
    global codeMuonTra_entry
    global codeBook_entry
    global titleBook_entry
    global username_TV_entry
    global name_TV_entry
    codeBook = StringVar()
    titleBook = StringVar()
    codeMuonTra=StringVar()
    NXB=StringVar()
    username_TV=StringVar()
    name_TV=StringVar()
    NgayMuonTra=StringVar()
    Label(Menu_Tra_screen, text="Menu Danh Sách Trả", bg="#AEF35A", width="300", height="2", font=("Calibri", 13)).pack()
    Label(Menu_Tra_screen, text="").pack()
    frame1 = Frame(Menu_Tra_screen)
    frame1.pack(fill=X)
    codeMuonTra_lable = Label(frame1, text="Nhap mã Mượn :",width=30,anchor=W)
    codeMuonTra_lable.pack(side=LEFT, padx=5, pady=5)
    #username_lable.grid(column=0, row=0)
    codeMuonTra_entry = Entry(frame1, textvariable=codeMuonTra,width=60)
    codeMuonTra_entry.pack(side=LEFT, padx=5)
    #-------------------------------------------------------------------
    frame2 = Frame(Menu_Tra_screen)
    frame2.pack(fill=X)
    username_TV_lable = Label(frame2, text="Mã Thành Viên",width=30,anchor=W)
    username_TV_lable.pack(side=LEFT, padx=5, pady=5)
    ##name_lable.pack()
    username_TV_entry = Entry(frame2, textvariable=username_TV,width=60)
    username_TV_entry.pack(side=LEFT, padx=5)
    frame3 = Frame(Menu_Tra_screen)
    frame3.pack(fill=X)
    name_TV_lable = Label(frame3, text="Tên Thành Viên",width=30,anchor=W)
    name_TV_lable.pack(side=LEFT, padx=5, pady=5)
    name_TV_entry = Entry(frame3, textvariable=name_TV,width=60)
    name_TV_entry.pack(side=LEFT, padx=5)
    #------------------------------------------------------------------------------
    frame4 = Frame(Menu_Tra_screen)
    frame4.pack(fill=X)
    codeBook_lable = Label(frame4, text="Nhập mã Sách:",width=30,anchor=W)
    codeBook_lable.pack(side=LEFT, padx=5, pady=5)
    ##password_lable.grid(column=0, row=1)
    titleBook_entry = Entry(frame4, textvariable=codeBook,width=60)
    titleBook_entry.pack(side=LEFT, padx=5)
    frame5 = Frame(Menu_Tra_screen)
    frame5.pack(fill=X)
    titleBook_lable = Label(frame5, text="Nhập tiêu đề:",width=30,anchor=W)
    titleBook_lable.pack(side=LEFT, padx=5, pady=5)
    ##password_lable.grid(column=0, row=1)
    titleBook_entry = Entry(frame5, textvariable=titleBook,width=60)
    titleBook_entry.pack(side=LEFT, padx=5)
    ##password_entry.grid(column=1, row=1)
    
    frame6 = Frame(Menu_Tra_screen)
    frame6.pack(fill=X)
    NgayMuon_lable = Label(frame6, text="Ngày Mượn",width=30,anchor=W)
    NgayMuon_lable.pack(side=LEFT, padx=5, pady=5)
    NgayMuonTra = DateEntry(frame6, width=60, background='darkblue',foreground='white', borderwidth=2)
    NgayMuonTra.pack(side=LEFT, padx=5)
    
    
    
    #Label(frame5, text="",width=5).pack()
    
    frame7 = Frame(Menu_Tra_screen)
    frame7.pack(fill=X)
    Label(frame7, text="",width=10).pack(side=LEFT)
    Button(frame7, text="Tìm kiếm", width="15", height=1,command=Tim_Kiem_Tra).pack(side=LEFT)
    Label(frame7, text="",width=10).pack(side=LEFT)
    Button(frame7, text="Toàn Bộ", width="15", height=1,command=Toan_Bo_Tra).pack(side=LEFT)
    Label(frame7, text="",width=10).pack(side=LEFT)
    Button(frame7, text="Thoát", width="15", height=1,command=Thoat_Tra).pack(side=LEFT)
    Label(Menu_Tra_screen, text="",width=10).pack()
    frame8 = Frame(Menu_Tra_screen)
    frame8.pack(fill=X)
    Label(frame8, text="",width=10).pack(side=LEFT)
    Button(frame8, text="TK không theo ngày", width="15", height=1,command=Tim_Kiem_Tra_ktn).pack(side=LEFT)

#Thoát----------------------------------------------------------------------------------------------------------
def Thoat_Tra():
    Admin_main()
    Menu_Tra_screen.destroy()
#Toàn Bộ Trả --------------------------------------------------------------------------------------------------
def Toan_Bo_Tra():
    DS=DSLKQLMuonTra()
    DS.DocFileQLTra()
    DS.GUI_Tra()
#Tìm Kiếm Trả---------------------------------------------------------------------------------------------
def Tim_Kiem_Tra():
    DS=DSLKQLMuonTra()
    DS.DocFileQLTra()
    codeMuonTra_info=codeMuonTra.get()
    codeBook_info=codeBook.get()
    titleBook_info=titleBook.get()
    username_info = username_TV.get()
    name_info = name_TV.get()
    NgayMuonTra_info=NgayMuonTra.get_date()
    
    a=0
    b=0
    c=0
    d=0
    if codeMuonTra_info == "":
        a=0
    else:
        try:
            a=int(codeMuonTra_info)
        except:
            a=0
            codeMuonTra_entry.delete(0,END);
    if username_info == "":
        b=0
    else:
        try:
            b=int(username_info)
        except:
            b=0
            username_TV_entry.delete(0,END)
    if codeBook_info == "":
        c=0
    else:
        try:
            c=int(codeBook_info)
        except:
            c=0
            codeBook_entry.delete(0,END)
    if NgayMuonTra_info=="":
        d=0
    else:
        try:
            d = NgayMuonTra_info.strftime("%d/%m/%Y")
        except:
            d=0
    DS.Gui_TimKiem_Tra(a,b,name_info,c,titleBook_info,d)   
#Tìm Kiếm trả không theo ngày---------------------------------------------------------------------------------------------
def Tim_Kiem_Tra_ktn():
    DS=DSLKQLMuonTra()
    DS.DocFileQLTra()
    codeMuonTra_info=codeMuonTra.get()
    codeBook_info=codeBook.get()
    titleBook_info=titleBook.get()
    username_info = username_TV.get()
    name_info = name_TV.get()
    NgayMuonTra_info=0
    
    a=0
    b=0
    c=0
    d=0
    if codeMuonTra_info == "":
        a=0
    else:
        try:
            a=int(codeMuonTra_info)
        except:
            a=0
            codeMuonTra_entry.delete(0,END);
    if username_info == "":
        b=0
    else:
        try:
            b=int(username_info)
        except:
            b=0
            username_TV_entry.delete(0,END)
    if codeBook_info == "":
        c=0
    else:
        try:
            c=int(codeBook_info)
        except:
            c=0
            codeBook_entry.delete(0,END)
    if NgayMuonTra_info=="":
        d=0
    else:
        try:
            d = NgayMuonTra_info.strftime("%d/%m/%Y")
        except:
            d=0
    DS.Gui_TimKiem_Tra(a,b,name_info,c,titleBook_info,d)  
#Menu Danh Sách mượn ---------------------------------------------------------------------------------------
def Menu_Muon():
    admin_screen.destroy()
    global Menu_Muon_screen
    Menu_Muon_screen = Toplevel()
    Menu_Muon_screen.title("Menu Mượn ")
    Menu_Muon_screen.geometry("650x450")
    global codeMuonTra
    global codeBook
    global titleBook
    global username_TV
    global name_TV
    global NgayMuonTra
    global codeMuonTra_entry
    global codeBook_entry
    global titleBook_entry
    global username_TV_entry
    global name_TV_entry
    codeBook = StringVar()
    titleBook = StringVar()
    codeMuonTra=StringVar()
    NXB=StringVar()
    username_TV=StringVar()
    name_TV=StringVar()
    NgayMuonTra=StringVar()
    Label(Menu_Muon_screen, text="Menu Danh Sách Mượn", bg="#AEF35A", width="300", height="2", font=("Calibri", 13)).pack()
    Label(Menu_Muon_screen, text="").pack()
    frame1 = Frame(Menu_Muon_screen)
    frame1.pack(fill=X)
    codeMuonTra_lable = Label(frame1, text="Nhap mã Mượn :",width=30,anchor=W)
    codeMuonTra_lable.pack(side=LEFT, padx=5, pady=5)
    #username_lable.grid(column=0, row=0)
    codeMuonTra_entry = Entry(frame1, textvariable=codeMuonTra,width=60)
    codeMuonTra_entry.pack(side=LEFT, padx=5)
    #-------------------------------------------------------------------
    frame2 = Frame(Menu_Muon_screen)
    frame2.pack(fill=X)
    username_TV_lable = Label(frame2, text="Mã Thành Viên",width=30,anchor=W)
    username_TV_lable.pack(side=LEFT, padx=5, pady=5)
    ##name_lable.pack()
    username_TV_entry = Entry(frame2, textvariable=username_TV,width=60)
    username_TV_entry.pack(side=LEFT, padx=5)
    frame3 = Frame(Menu_Muon_screen)
    frame3.pack(fill=X)
    name_TV_lable = Label(frame3, text="Tên Thành Viên",width=30,anchor=W)
    name_TV_lable.pack(side=LEFT, padx=5, pady=5)
    name_TV_entry = Entry(frame3, textvariable=name_TV,width=60)
    name_TV_entry.pack(side=LEFT, padx=5)
    #------------------------------------------------------------------------------
    frame4 = Frame(Menu_Muon_screen)
    frame4.pack(fill=X)
    codeBook_lable = Label(frame4, text="Nhập mã Sách:",width=30,anchor=W)
    codeBook_lable.pack(side=LEFT, padx=5, pady=5)
    ##password_lable.grid(column=0, row=1)
    titleBook_entry = Entry(frame4, textvariable=codeBook,width=60)
    titleBook_entry.pack(side=LEFT, padx=5)
    frame5 = Frame(Menu_Muon_screen)
    frame5.pack(fill=X)
    titleBook_lable = Label(frame5, text="Nhập tiêu đề:",width=30,anchor=W)
    titleBook_lable.pack(side=LEFT, padx=5, pady=5)
    ##password_lable.grid(column=0, row=1)
    titleBook_entry = Entry(frame5, textvariable=titleBook,width=60)
    titleBook_entry.pack(side=LEFT, padx=5)
    ##password_entry.grid(column=1, row=1)
    
    frame6 = Frame(Menu_Muon_screen)
    frame6.pack(fill=X)
    NgayMuon_lable = Label(frame6, text="Ngày Mượn",width=30,anchor=W)
    NgayMuon_lable.pack(side=LEFT, padx=5, pady=5)
    NgayMuonTra = DateEntry(frame6, width=60, background='darkblue',foreground='white', borderwidth=2)
    NgayMuonTra.pack(side=LEFT, padx=5)
    
    
    
    #Label(frame5, text="",width=5).pack()
    
    frame7 = Frame(Menu_Muon_screen)
    frame7.pack(fill=X)
    Label(frame7, text="",width=10).pack(side=LEFT)
    Button(frame7, text="Tìm kiếm", width="15", height=1,command=Tim_Kiem_Muon).pack(side=LEFT)
    Label(frame7, text="",width=10).pack(side=LEFT)
    Button(frame7, text="Toàn Bộ", width="15", height=1,command=Toan_Bo_Muon).pack(side=LEFT)
    Label(frame7, text="",width=10).pack(side=LEFT)
    Button(frame7, text="Thoát", width="15", height=1,command=Thoat_Muon).pack(side=LEFT)
    Label(Menu_Muon_screen, text="",width=10).pack()
    frame8 = Frame(Menu_Muon_screen)
    frame8.pack(fill=X)
    Label(frame8, text="",width=10).pack(side=LEFT)
    Button(frame8, text="TK không theo ngày", width="15", height=1,command=Tim_Kiem_Muon_ktn).pack(side=LEFT)
    Label(frame8, text="",width=10).pack(side=LEFT)
    Button(frame8, text="DS Trả trễ ", width="15", height=1,command=TraKhongDungHen).pack(side=LEFT)
#Lọc theo DS Trả trễ -------------------------------------------------------------------------------------------
def TraKhongDungHen():
    DSMuon=DSLKQLMuonTra()
    DSMuon.DocFileQLMuon()
    DSMuon.LocRaDSTraSachTre()
#Thoát----------------------------------------------------------------------------------------------------------
def Thoat_Muon():
    Admin_main()
    Menu_Muon_screen.destroy()
#Toàn Bộ Mượn --------------------------------------------------------------------------------------------------
def Toan_Bo_Muon():
    DS=DSLKQLMuonTra()
    DS.DocFileQLMuon() 
    DS.Gui_ToanBoMuon()
#Tìm Kiếm Mượn---------------------------------------------------------------------------------------------
def Tim_Kiem_Muon():
    DS=DSLKQLMuonTra()
    DS.DocFileQLMuon()  
    codeMuonTra_info=codeMuonTra.get()
    codeBook_info=codeBook.get()
    titleBook_info=titleBook.get()
    username_info = username_TV.get()
    name_info = name_TV.get()
    NgayMuonTra_info=NgayMuonTra.get_date()
    
    a=0
    b=0
    c=0
    d=0
    if codeMuonTra_info == "":
        a=0
    else:
        try:
            a=int(codeMuonTra_info)
        except:
            a=0
            codeMuonTra_entry.delete(0,END);
    if username_info == "":
        b=0
    else:
        try:
            b=int(username_info)
        except:
            b=0
            username_TV_entry.delete(0,END)
    if codeBook_info == "":
        c=0
    else:
        try:
            c=int(codeBook_info)
        except:
            c=0
            codeBook_entry.delete(0,END)
    if NgayMuonTra_info=="":
        d=0
    else:
        try:
            d = NgayMuonTra_info.strftime("%d/%m/%Y")
        except:
            d=0
    DS.Gui_TimKiem_Muon(a,b,name_info,c,titleBook_info,d)   
#Tìm Kiếm Mượn---------------------------------------------------------------------------------------------
def Tim_Kiem_Muon_ktn():
    DS=DSLKQLMuonTra()
    DS.DocFileQLMuon()  
    codeMuonTra_info=codeMuonTra.get()
    codeBook_info=codeBook.get()
    titleBook_info=titleBook.get()
    username_info = username_TV.get()
    name_info = name_TV.get()
    NgayMuonTra_info=0
    
    a=0
    b=0
    c=0
    d=0
    if codeMuonTra_info == "":
        a=0
    else:
        try:
            a=int(codeMuonTra_info)
        except:
            a=0
            codeMuonTra_entry.delete(0,END);
    if username_info == "":
        b=0
    else:
        try:
            b=int(username_info)
        except:
            b=0
            username_TV_entry.delete(0,END)
    if codeBook_info == "":
        c=0
    else:
        try:
            c=int(codeBook_info)
        except:
            c=0
            codeBook_entry.delete(0,END)
    if NgayMuonTra_info=="":
        d=0
    else:
        try:
            d = NgayMuonTra_info.strftime("%d/%m/%Y")
        except:
            d=0
    DS.Gui_TimKiem_Muon(a,b,name_info,c,titleBook_info,d)  
   
#Menu Danh Sách Sách ---------------------------------------------------------------------------------------
def Menu_Sach():
    admin_screen.destroy()
    global Menu_Sach_screen
    Menu_Sach_screen = Toplevel()
    Menu_Sach_screen.title("Menu Sách ")
    Menu_Sach_screen.geometry("650x350")
 
    global codeBook
    global titleBook
    global nameAuthur
    global NXB
    global Year_Book
    global SoLuong
    global codeBook_entry
    global titleBook_entry
    global nameAuthur_entry
    global NXB_entry
    global Year_Book_entry
    global SoLuong_entry
    codeBook = StringVar()
    titleBook = StringVar()
    nameAuthur=StringVar()
    NXB=StringVar()
    Year_Book=StringVar()
    SoLuong=StringVar()
    Label(Menu_Sach_screen, text="Chọn sách tìm kiếm", bg="#AEF35A", width="300", height="2", font=("Calibri", 13)).pack()
    Label(Menu_Sach_screen, text="").pack()
    frame1 = Frame(Menu_Sach_screen)
    frame1.pack(fill=X)
    codeBook_lable = Label(frame1, text="Nhap mã số sách:",width=30,anchor=W)
    codeBook_lable.pack(side=LEFT, padx=5, pady=5)
    #username_lable.grid(column=0, row=0)
    codeBook_entry = Entry(frame1, textvariable=codeBook,width=60)
    codeBook_entry.pack(side=LEFT, padx=5)
    #username_entry.grid(column=1, row=0)
    frame2 = Frame(Menu_Sach_screen)
    frame2.pack(fill=X)
    titleBook_lable = Label(frame2, text="Nhập tiêu đề:",width=30,anchor=W)
    titleBook_lable.pack(side=LEFT, padx=5, pady=5)
    ##password_lable.grid(column=0, row=1)
    titleBook_entry = Entry(frame2, textvariable=titleBook,width=60)
    titleBook_entry.pack(side=LEFT, padx=5)
    ##password_entry.grid(column=1, row=1)
    frame3 = Frame(Menu_Sach_screen)
    frame3.pack(fill=X)
    name_lable = Label(frame3, text="Tác Giả",width=30,anchor=W)
    name_lable.pack(side=LEFT, padx=5, pady=5)
    ##name_lable.pack()
    nameAuthur_entry = Entry(frame3, textvariable=nameAuthur,width=60)
    nameAuthur_entry.pack(side=LEFT, padx=5)
    frame4 = Frame(Menu_Sach_screen)
    frame4.pack(fill=X)
    NXB_lable = Label(frame4, text="Nhà Sản Xuất",width=30,anchor=W)
    NXB_lable.pack(side=LEFT, padx=5, pady=5)
    NXB_entry = Entry(frame4, textvariable=NXB,width=60)
    NXB_entry.pack(side=LEFT, padx=5)
    frame5 = Frame(Menu_Sach_screen)
    frame5.pack(fill=X)
    Year_Book_lable = Label(frame5, text="Năm sản xuất",width=30,anchor=W)
    Year_Book_lable.pack(side=LEFT, padx=5, pady=5)
    Year_Book_entry = Entry(frame5, textvariable=Year_Book,width=60)
    Year_Book_entry.pack(side=LEFT, padx=5)
    frame6 = Frame(Menu_Sach_screen)
    frame6.pack(fill=X)
    SoLuong_lable = Label(frame6, text="Số Lượng Sách",width=30,anchor=W)
    SoLuong_lable.pack(side=LEFT, padx=5, pady=5)
    SoLuong_entry = Entry(frame6, textvariable=SoLuong,width=60)
    SoLuong_entry.pack(side=LEFT, padx=5)
    #Label(frame5, text="",width=5).pack()
    frame7 = Frame(Menu_Sach_screen)
    frame7.pack(fill=X)
    Label(frame7, text="",width=10).pack(side=LEFT)
    Button(frame7, text="Thêm", width="15", height=1,command=Them_Sach).pack(side=LEFT)
    Label(frame7, text="",width=10).pack(side=LEFT)
    Button(frame7, text="Xóa", width="15", height=1,command=Xoa_sach).pack(side=LEFT)
    Label(frame7, text="",width=10).pack(side=LEFT)
    Button(frame7, text="Sửa", width="15", height=1,command=Sua_Sach_Admin).pack(side=LEFT)
    Label(Menu_Sach_screen, text="",width=10).pack()
    frame8 = Frame(Menu_Sach_screen)
    frame8.pack(fill=X)
    Label(frame8, text="",width=10).pack(side=LEFT)
    Button(frame8, text="Tìm kiếm", width="15", height=1,command=TimKiemSach_user).pack(side=LEFT)
    Label(frame8, text="",width=10).pack(side=LEFT)
    Button(frame8, text="Toàn Bộ", width="15", height=1,command=ToanBo_Sach).pack(side=LEFT)
    Label(frame8, text="",width=10).pack(side=LEFT)
    Button(frame8, text="Thoát", width="15", height=1,command=Thoat_Sach).pack(side=LEFT)
#Thoát 
def Thoat_Sach():
    Menu_Sach_screen.destroy();
    Admin_main()
#Sửa Sách
def Sua_Sach_Admin():
    DS=DSLK()
    DS.DocFileSach()
    codeBook_info = codeBook.get()
    titleBook_info = titleBook.get()
    nameAuthur_info = nameAuthur.get()
    NXB_info=NXB.get()
    Year_Book_info=Year_Book.get()
    SoLuong_info=SoLuong.get()
    a=0
    b=0
    c=0
    if codeBook_info == "":
        a=0
    else:
        try:
            a=int(codeBook_info)
        except:
            a=0
            codeBook_entry.delete(0,END);
    if Year_Book_info == "":
        b=0
    else:
        try:
            b=int(Year_Book_info)
        except:
            b=0
            Year_Book_entry.delete(0,END)
    if SoLuong_info == "":
        c=0
    else:
        try:
            c=int(SoLuong_info)
        except:
            c=0
            SoLuong_entry.delete(0,END)
    if DS.timSachTheoTen(a)==None:
        codeBook_was_not_exist()
        codeBook_entry.delete(0,END)
    #elif a==0 or codeBook_info=="" or nameAuthur_info=="" or NXB_info=="" or b== 0 or c<=0:
        #repair_Sach_Fail()
    else:
        DS.Sua_Sach_TheoMS(a,titleBook_info,nameAuthur_info,NXB_info,b,c)
        DS.GhiFileSach();
        repair_Sach_success()
#thêm Sách
def Them_Sach():
    DS=DSLK()
    DS.DocFileSach()
    codeBook_info = codeBook.get()
    titleBook_info = titleBook.get()
    nameAuthur_info = nameAuthur.get()
    NXB_info=NXB.get()
    Year_Book_info=Year_Book.get()
    SoLuong_info=SoLuong.get()
    a=0
    b=0
    c=0
    if codeBook_info == "":
        a=0
    else:
        try:
            a=int(codeBook_info)
        except:
            a=0
            codeBook_entry.delete(0,END);
    if Year_Book_info == "":
        b=0
    else:
        try:
            b=int(Year_Book_info)
        except:
            b=0
            Year_Book_entry.delete(0,END)
    if SoLuong_info == "":
        c=0
    else:
        try:
            c=int(SoLuong_info)
        except:
            c=0
            SoLuong_entry.delete(0,END)
    if DS.timSachTheoTen(a)!=None:
        codeBook_was_exist()
        codeBook_entry.delete(0,END)
    elif a==0 or codeBook_info=="" or nameAuthur_info=="" or NXB_info=="" or b== 0 or c<=0:
        Add_Sach_Fail()
    else:
        Sach=Book(a,titleBook_info,nameAuthur_info,NXB_info,b,c)
        DS.themSau(Sach)
        Add_Sach_Success()
        DS.GhiFileSach();
#xóa Sách
def Xoa_sach():
    DS=DSLK()
    DS.DocFileSach()
    
    codeBook_info = codeBook.get()
    titleBook_info = titleBook.get()
    nameAuthur_info = nameAuthur.get()
    NXB_info=NXB.get()
    Year_Book_info=Year_Book.get()
    a=0
    b=0
    if codeBook_info == "":
        a=0
    else:
        try:
            a=int(codeBook_info)
        except:
            a=0
            codeBook_entry.delete(0,END);
    if Year_Book_info == "":
        b=0
    else:
        try:
            b=int(Year_Book_info)
        except:
            b=0
            Year_Book_entry.delete(0,END)
    if a==0:
        DS.Gui_Sach(a,titleBook_info,nameAuthur_info,NXB_info,b)
    else:
        DS.xoa1PhanTuTheoMS(a)
        DS.GhiFileSach()
        DS.GUI_Book()

def ToanBo_Sach():
    ds=DSLK()
    ds.DocFileSach()
    ds.GUI_Book()
#Menu danh sách Thành Viên ---------------------------------------------------------------------------------
def Menu_TV():
    admin_screen.destroy()
    global Menu_TV_screen
    Menu_TV_screen = Toplevel()
    Menu_TV_screen.title("Menu_TV")
    Menu_TV_screen.geometry("700x350")
 
    global username_TV
    global muonSach_TV
    global name_TV
    global year_TV
    global username_TV_entry
    global name_TV_entry
    global year_TV_entry
    
    username_TV = StringVar()
    muonSach_TV = StringVar()
    name_TV=StringVar()
    year_TV=StringVar()
 
    Label(Menu_TV_screen, text="Menu ADMIN THành Viên", bg="#AEF35A", width="300", height="2", font=("Calibri", 13)).pack()
    Label(Menu_TV_screen, text="").pack()
    frame1 = Frame(Menu_TV_screen)
    frame1.pack(fill=X)
    username_lable = Label(frame1, text="Mã Số TV:",width=30,anchor=W)
    username_lable.pack(side=LEFT, padx=5, pady=5)
    #username_lable.grid(column=0, row=0)
    username_TV_entry = Entry(frame1, textvariable=username_TV,width=60)
    username_TV_entry.pack(side=LEFT, padx=5)
    #username_entry.grid(column=1, row=0)
    frame2 = Frame(Menu_TV_screen)
    frame2.pack(fill=X)
    name_lable = Label(frame2, text="Họ Tên",width=30,anchor=W)
    name_lable.pack(side=LEFT, padx=5, pady=5)
    ##name_lable.pack()
    name_TV_entry = Entry(frame2, textvariable=name_TV,width=60)
    name_TV_entry.pack(side=LEFT, padx=5)
    frame3 = Frame(Menu_TV_screen)
    frame3.pack(fill=X)
    year_lable = Label(frame3, text="Năm Sinh",width=30,anchor=W)
    year_lable.pack(side=LEFT, padx=5, pady=5)
    year_TV_entry = Entry(frame3, textvariable=year_TV,width=60)
    year_TV_entry.pack(side=LEFT, padx=5)
    frame4 = Frame(Menu_TV_screen)
    frame4.pack(fill=X)
    DaMuon_lable = Label(frame4, text="Mượn Sách ",width=30,anchor=W)
    DaMuon_lable.pack(side=LEFT, padx=5, pady=5)
    options = [
            "Đã mượn Sách",
            "Chưa Mượn Sách",
            ]
    muonSach_TV.set("Chưa Mượn Sách")
    drop = OptionMenu( frame4 , muonSach_TV , *options )
    drop.pack(side=LEFT, padx=5, pady=5)
    frame6 = Frame(Menu_TV_screen)
    frame6.pack(fill=X)
    Label(frame6, text="",width=10).pack(side=LEFT)
    Button(frame6, text="Tìm kiếm", width="15", height=1,command=Tim_Kiem_TV).pack(side=LEFT)
    Label(frame6, text="",width=10).pack(side=LEFT)
    Button(frame6, text="Xóa", width="15", height=1,command=Xoa_TV).pack(side=LEFT)
    Label(frame6, text="",width=10).pack(side=LEFT)
    Button(frame6, text="Toàn Bộ", width="15", height=1,command=Toan_Bo_TV).pack(side=LEFT)
    Label(Menu_TV_screen, text="",width=10).pack()

    frame7 = Frame(Menu_TV_screen)
    frame7.pack(fill=X)
    Label(frame7, text="",width=37).pack(side=LEFT)
    
    Button(frame7, text="Thoát", width="15", height=1,command=Thoat_TV).pack(side=LEFT)
    
#Thóa TV
def Thoat_TV():
    Menu_TV_screen.destroy()
    Admin_main()
    
#xóa TV
def Xoa_TV():
    DS=DSLKMember()
    DS.DocFileMember()    
    username_info = username_TV.get()
    name_info = name_TV.get()
    muonSach_info = muonSach_TV.get()
    Year_info=year_TV.get()
    a=0
    b=0
    if username_info == "":
        a=0
    else:
        try:
            a=int(username_info)
        except:
            a=0
            codeBook_entry.delete(0,END);
    if Year_info == "":
        b=0
    else:
        try:
            b=int(Year_info)
        except:
            b=0
            year_TV_entry.delete(0,END)
    if muonSach_info == "Chưa Mượn Sách":
        tam=False
    else:
        tam=True
    if(a==0):
        DS.Gui_Tim_TV(a,name_info,b,tam)
    else:
        DS.Xoa1PhanTuTheoMaSo(a);
        DS.GUI_Member()
        DS.GhiFileMember()


def Toan_Bo_TV():
    DS=DSLKMember()
    DS.DocFileMember()
    DS.GUI_Member()

def Tim_Kiem_TV():
    DS=DSLKMember()
    DS.DocFileMember()    
    username_info = username_TV.get()
    name_info = name_TV.get()
    muonSach_info = muonSach_TV.get()
    Year_info=year_TV.get()
    a=0
    b=0
    if username_info == "":
        a=0
    else:
        try:
            a=int(username_info)
        except:
            a=0
            codeBook_entry.delete(0,END);
    if Year_info == "":
        b=0
    else:
        try:
            b=int(Year_info)
        except:
            b=0
            year_TV_entry.delete(0,END)
    if muonSach_info == "Chưa Mượn Sách":
        tam=False
    else:
        tam=True
    DS.Gui_Tim_TV(a,name_info,b,tam)
#user--------------------------------------------------------------------------------------------------------------------------------------------
def User_main():
    
    login_success_screen.destroy()
    global user_screen
    user_screen = Toplevel()
    user_screen.title("Menu_DocGia")
    user_screen.geometry("250x650")
    Label(user_screen, text="Bạn Chọn Chức năng",bg="#AEF35A",width="300",height="2", font=("Calibri", 13)).pack()
    Label(user_screen, text="").pack()
    global usernameT
    usernameT = username_verify.get()
    login_screen.destroy()
    DSTV=DSLKMember()
    DSTV.DocFileMember() 
    a=int(usernameT)
    TV = DSTV.timMStraveMk(a)
    Button(user_screen,text="Xem Thông Tin Cá Nhân", height="2", width="30",command=xuat1TV).pack()
    Label(user_screen,text="").pack()
    Button(user_screen,text="Sửa Thông Tin Cá Nhân", height="2", width="30",command=repair_information).pack()
    Label(user_screen,text="").pack()
    Button(user_screen,text="Tìm kiếm sách", height="2", width="30",command=timSach).pack()
    Label(user_screen,text="").pack()
    Button(user_screen,text="In tất cả các đầu sách", height="2", width="30",command=xuatSach).pack()
    Label(user_screen,text="").pack()
    now=int(date.today().year) 
    year=now-TV.NamSinh 
    if(year>17):
        DSMuon=DSLKQLMuonTra() 
        DSMuon.DocFileQLMuon()
        KT=DSMuon.locTimDocGia(a)
        if(KT<3):
            Button(user_screen,text="Muợn Sách", height="2", width="30",command=Dang_Ki_Muon_Sach).pack()
            Label(user_screen,text="").pack()
        if(KT>0):
            Button(user_screen,text="Trả Sách", height="2", width="30",command=Dang_Ki_Tra_Sach).pack()
            Label(user_screen,text="").pack()
        Button(user_screen,text="in sách đã mượn chưa trả", height="2", width="30",command=Muon_Chua_Tra).pack()
        Label(user_screen,text="").pack()
    Button(user_screen,text="Thoát", height="2", width="30",command=Exit_User).pack()
#Sửa thông tin sinh viên 
def repair_information():
    global repair_information_screen
    repair_information_screen = Toplevel()
    repair_information_screen.title("Sửa thông tin Cá nhân")
    repair_information_screen.geometry("700x250")
    
    
    global password
    global name
    global year
    
    global password_entry
    global name_entry
    global year_entry
    
    password = StringVar()
    name=StringVar()
    year=StringVar()
 
    Label(repair_information_screen, text="Sửa thông tin thông tin cá nhân", bg="#AEF35A", width="300", height="2", font=("Calibri", 13)).pack()
    Label(repair_information_screen, text="").pack()
    frame2 = Frame(repair_information_screen)
    frame2.pack(fill=X)
    password_lable = Label(frame2, text="Password * ",width=30,anchor=W)
    password_lable.pack(side=LEFT, padx=5, pady=5)
    ##password_lable.grid(column=0, row=1)
    password_entry = Entry(frame2, textvariable=password,width=60)
    password_entry.pack(side=LEFT, padx=5)
    ##password_entry.grid(column=1, row=1)
    frame3 = Frame(repair_information_screen)
    frame3.pack(fill=X)
    name_lable = Label(frame3, text="Họ Tên",width=30,anchor=W)
    name_lable.pack(side=LEFT, padx=5, pady=5)
    ##name_lable.pack()
    name_entry = Entry(frame3, textvariable=name,width=60)
    name_entry.pack(side=LEFT, padx=5)
    frame4 = Frame(repair_information_screen)
    frame4.pack(fill=X)
    year_lable = Label(frame4, text="Năm Sinh",width=30,anchor=W)
    year_lable.pack(side=LEFT, padx=5, pady=5)
    year_entry = Entry(frame4, textvariable=year,width=60)
    year_entry.pack(side=LEFT, padx=5)
    frame5 = Frame(repair_information_screen)
    frame5.pack(fill=X)
    Label(frame5, text="",width=5).pack(side=RIGHT)
    Button(frame5, text="Sửa Thông TIn", width="10", height=1, bg="#87cefa", command = repair_information_varify).pack()

def repair_information_varify():
    DSTV=DSLKMember()
    DSTV.DocFileMember()
    password_info = password.get()
    name_info = name.get()
    year_info=year.get()
    b=0
    a=int(usernameT)
    if year_info == "":
        b=0
    else:
        try:
            b=int(year_info)
        except:
            b=0
            year_entry.delete(0,END)
    DSTV.Repair_infor_TV(a,name_info,password_info,b)
    DSTV.GhiFileMember()
    repair_information_success()
#chay file hoat Động 
def Dang_Ki_Tra_Sach():
    global Dang_Ki_Tra_Sach_screen
    Dang_Ki_Tra_Sach_screen = Toplevel(user_screen)
    Dang_Ki_Tra_Sach_screen.title("Đăng kí Mượn sách")
    Dang_Ki_Tra_Sach_screen.geometry("400x250")
    Label(Dang_Ki_Tra_Sach_screen, text="Đăng kí trả sách",bg="#AEF35A",width="300",height="2", font=("Calibri", 13)).pack()
    Label(Dang_Ki_Tra_Sach_screen, text="").pack()
 
    global CodeBook_Tra_verify
    global tilteBook_Tra_verify
 
    CodeBook_Tra_verify = StringVar()
    tilteBook_Tra_verify = StringVar()
 
    global CodeBook_Tra_entry
    global tilteBook_Tra_entry
    frame1 = Frame(Dang_Ki_Tra_Sach_screen)
    frame1.pack(fill=X)
    Label(frame1, text="Mã Sách:",width=15,anchor=W).pack(side=LEFT, padx=5, pady=5)
    CodeBook_Muon_entry = Entry(frame1,textvariable=CodeBook_Tra_verify,width=30)
    CodeBook_Muon_entry.pack(side=LEFT, padx=5, pady=5)
    Label(Dang_Ki_Tra_Sach_screen, text="").pack()
    frame2 = Frame(Dang_Ki_Tra_Sach_screen)
    frame2.pack(fill=X)
    Label(frame2, text="Tựa Đề ",width=15,anchor=W).pack(side=LEFT, padx=5, pady=5)
    tilteBook_Muon_entry = Entry(frame2, textvariable=tilteBook_Tra_verify,width=30)
    tilteBook_Muon_entry.pack(side=LEFT, padx=5, pady=5)
    Label(Dang_Ki_Tra_Sach_screen, text="").pack()
    Button(Dang_Ki_Tra_Sach_screen, text="Đăng kí trả", width=10, height=1, command = Tra_Sach_User).pack()

def Dang_Ki_Muon_Sach():
    global Dang_Ki_Muon_Sach_screen
    Dang_Ki_Muon_Sach_screen = Toplevel(user_screen)
    Dang_Ki_Muon_Sach_screen.title("Đăng kí Mượn sách")
    Dang_Ki_Muon_Sach_screen.geometry("400x250")
    Label(Dang_Ki_Muon_Sach_screen, text="Đăng kí mượn sách",bg="#AEF35A",width="300",height="2", font=("Calibri", 13)).pack()
    Label(Dang_Ki_Muon_Sach_screen, text="").pack()
 
    global CodeBook_verify
    global tilteBook_verify
 
    CodeBook_verify = StringVar()
    tilteBook_verify = StringVar()
 
    global CodeBook_Muon_entry
    global tilteBook_Muon_entry
    frame1 = Frame(Dang_Ki_Muon_Sach_screen)
    frame1.pack(fill=X)
    Label(frame1, text="Mã Sách:",width=15,anchor=W).pack(side=LEFT, padx=5, pady=5)
    CodeBook_Muon_entry = Entry(frame1,textvariable=CodeBook_verify,width=30)
    CodeBook_Muon_entry.pack(side=LEFT, padx=5, pady=5)
    Label(Dang_Ki_Muon_Sach_screen, text="").pack()
    frame2 = Frame(Dang_Ki_Muon_Sach_screen)
    frame2.pack(fill=X)
    Label(frame2, text="Tựa Đề ",width=15,anchor=W).pack(side=LEFT, padx=5, pady=5)
    tilteBook_Muon_entry = Entry(frame2, textvariable=tilteBook_verify,width=30)
    tilteBook_Muon_entry.pack(side=LEFT, padx=5, pady=5)
    Label(Dang_Ki_Muon_Sach_screen, text="").pack()
    Button(Dang_Ki_Muon_Sach_screen, text="Đăng kí mượn", width=10, height=1, command = Muon_Sach_User).pack()

def Tra_Sach_User():
    DSMuon=DSLKQLMuonTra() 
    DSMuon.DocFileQLMuon()
    DSTra=DSLKQLMuonTra() 
    DSTra.DocFileQLTra()
    DSSach=DSLK()
    DSSach.DocFileSach()
    CodeBookT = CodeBook_Tra_verify.get()
    tilteBookT = tilteBook_Tra_verify.get()
    if CodeBookT == "":
        a=0
        DSSach.Gui_Sach(a,tilteBookT,"","",0)
    else:
        try:
            MaSach=int(CodeBookT)
            DSTV=DSLKMember()
            DSTV.DocFileMember()
            maTV=int(usernameT)
            KT=DSMuon.locTimDocGia(maTV)
            if(KT>0):
                TV = DSTV.timMStraveMk(maTV)
                Sach=DSSach.timSachTheoTen(MaSach)
                maMuonTra=maTV*Sach.MaSach 
                if DSMuon.KTCMSach(TV.MaTV,Sach.MaSach)==True:
                                #nếu mà trả rồi thì xem là true
                                Tra=QuanLyMuonTra(maMuonTra,TV.MaTV,TV.HoTen,Sach.MaSach,Sach.TuaDe,date.today(),True) 
                                 
                                DSTra.themSau(Tra) 
                                DSMuon.ChuyenSangDaTra(TV.MaTV,Sach.MaSach)
                                DSMuon.GhiFileQLMuon()
                                DSTra.GhiFileQLTra()
                                DSSach.timSachTra(Sach.MaSach)
                                DSTV.timMemberTraSach(TV.MaTV)
                                DSTV.GhiFileMember()
                                DSSach.GhiFileSach()
                                Tra_sach_success()
            else:
                Tra_sach_fail()
        except:
            
            CodeBook_Tra_entry.delete(0,END);
def Muon_Sach_User():
    DSMuon=DSLKQLMuonTra() 
    DSMuon.DocFileQLMuon()
    DSSach=DSLK()
    DSSach.DocFileSach()
    CodeBookM = CodeBook_verify.get()
    tilteBookM = tilteBook_verify.get()
    if CodeBookM == "":
        a=0
        DSSach.Gui_Sach(a,tilteBookM,"","",0)
    else:
        try:
            MaSach=int(CodeBookM)
            DSTV=DSLKMember()
            DSTV.DocFileMember()
            maTV=int(usernameT)
            KT=DSMuon.locTimDocGia(maTV)
            if(KT<3):
                TV = DSTV.timMStraveMk(maTV)
                Sach=DSSach.timSachTheoTen(MaSach)
                if Sach!=None:
                    maMuonTra=maTV*Sach.MaSach 
                    #nếu mà chưa trả thì xem là false
                    Muon=QuanLyMuonTra(maMuonTra,TV.MaTV,TV.HoTen,Sach.MaSach,Sach.TuaDe,date.today(),False) 
                    DSMuon.themSau(Muon) 
                    DSSach.timSachMuon(Sach.MaSach) 
                    DSTV.timMemberMuonSach(TV.MaTV) 
                    DSTV.GhiFileMember() 
                    DSSach.GhiFileSach() 
                    DSMuon.GhiFileQLMuon()
                    muon_sach_success()
                else:
                    None_Book()
            else:
                muon_sach_fail()
        except:
            
            CodeBook_Muon_entry.delete(0,END);
    



def Muon_Chua_Tra():
    DSMuon=DSLKQLMuonTra()
    DSMuon.DocFileQLMuon()
    a=int(usernameT)
    DSMuon.timKiemQLMuonQuaHan(a)

def xuat1TV():
    DSTV=DSLKMember()
    DSTV.DocFileMember() 
    TinhTienNopPhat();
    a=int(usernameT)
    DSTV.Gui_TV(a)

def xuatSach():
    DSSach=DSLK()
    DSSach.DocFileSach()
    DSSach.GUI_Book();

def timSach():
    global Tim_sach_screen
    Tim_sach_screen = Toplevel(user_screen)
    Tim_sach_screen.title("Tìm Kiếm Sách ")
    Tim_sach_screen.geometry("700x250")
 
    global codeBook
    global titleBook
    global nameAuthur
    global NXB
    global Year_Book
    global codeBook_entry
    global titleBook_entry
    global nameAuthur_entry
    global NXB_entry
    global Year_Book_entry
    codeBook = StringVar()
    titleBook = StringVar()
    nameAuthur=StringVar()
    NXB=StringVar()
    Year_Book=StringVar()
 
    Label(Tim_sach_screen, text="Chọn sách tìm kiếm", bg="#AEF35A", width="300", height="2", font=("Calibri", 13)).pack()
    Label(Tim_sach_screen, text="").pack()
    frame1 = Frame(Tim_sach_screen)
    frame1.pack(fill=X)
    codeBook_lable = Label(frame1, text="Nhap mã số sách:",width=30,anchor=W)
    codeBook_lable.pack(side=LEFT, padx=5, pady=5)
    #username_lable.grid(column=0, row=0)
    codeBook_entry = Entry(frame1, textvariable=codeBook,width=60)
    codeBook_entry.pack(side=LEFT, padx=5)
    #username_entry.grid(column=1, row=0)
    frame2 = Frame(Tim_sach_screen)
    frame2.pack(fill=X)
    titleBook_lable = Label(frame2, text="Nhập tiêu đề:",width=30,anchor=W)
    titleBook_lable.pack(side=LEFT, padx=5, pady=5)
    ##password_lable.grid(column=0, row=1)
    titleBook_entry = Entry(frame2, textvariable=titleBook,width=60)
    titleBook_entry.pack(side=LEFT, padx=5)
    ##password_entry.grid(column=1, row=1)
    frame3 = Frame(Tim_sach_screen)
    frame3.pack(fill=X)
    name_lable = Label(frame3, text="Tác Giả",width=30,anchor=W)
    name_lable.pack(side=LEFT, padx=5, pady=5)
    ##name_lable.pack()
    nameAuthur_entry = Entry(frame3, textvariable=nameAuthur,width=60)
    nameAuthur_entry.pack(side=LEFT, padx=5)
    frame4 = Frame(Tim_sach_screen)
    frame4.pack(fill=X)
    NXB_lable = Label(frame4, text="Nhà Sản Xuất",width=30,anchor=W)
    NXB_lable.pack(side=LEFT, padx=5, pady=5)
    NXB_entry = Entry(frame4, textvariable=NXB,width=60)
    NXB_entry.pack(side=LEFT, padx=5)
    frame5 = Frame(Tim_sach_screen)
    frame5.pack(fill=X)
    Year_Book_lable = Label(frame5, text="Năm sản xuất",width=30,anchor=W)
    Year_Book_lable.pack(side=LEFT, padx=5, pady=5)
    Year_Book_entry = Entry(frame5, textvariable=Year_Book,width=60)
    Year_Book_entry.pack(side=LEFT, padx=5)
    #Label(frame5, text="",width=5).pack()
    frame6 = Frame(Tim_sach_screen)
    frame6.pack(fill=X)
    Button(frame6, text="Tìm kiếm", width=10, height=1, bg="#87cefa", command = TimKiemSach_user).pack()

def TimKiemSach_user():
    DS=DSLK()
    DS.DocFileSach()
    
    codeBook_info = codeBook.get()
    titleBook_info = titleBook.get()
    nameAuthur_info = nameAuthur.get()
    NXB_info=NXB.get()
    Year_Book_info=Year_Book.get()
    a=0
    b=0
    if codeBook_info == "":
        a=0
    else:
        try:
            a=int(codeBook_info)
        except:
            a=0
            codeBook_entry.delete(0,END);
    if Year_Book_info == "":
        b=0
    else:
        try:
            b=int(Year_Book_info)
        except:
            b=0
            Year_Book_entry.delete(0,END)
    DS.Gui_Sach(a,titleBook_info,nameAuthur_info,NXB_info,b)
    
    
       
   
#Gui
#def GUI_Member():
#   Gui_member_screen = tk.Tk()
#   Gui_member_screen.title("GUI_member")
#   Gui_member_screen.geometry("400x250")
#   Label(Gui_member_screen, text="Danh sách thành viên",bg="#AEF35A",width="300",height="2", font=("Calibri", 13)).pack()
#   Label(Gui_member_screen, text="").pack()
#   DSTV=DSLKMember()
#   DSTV.DocFileMember() 
#   #frm=Frame()
#   #frm.pack(side=LEFT,padx=20)
#   columns = ('MaTV', 'HoTen', 'MatKhau','NamSinh','MuonSach','TienPhat')
#   tree = ttk.Treeview(Gui_member_screen, columns=columns, show='headings')
#   # define headings
#   tree.heading('MaTV', text='Mã TV')
#   tree.heading('HoTen', text='Họ Tên')
#   tree.heading('MatKhau', text='Mật khẩu')
#   tree.heading('NamSinh', text='Năm Sinh')
#   tree.heading('MuonSach', text='Mượn Sách')
#   tree.heading('TienPhat', text='Tiền Phạt')
#   contacts = []
#   current=DSTV.head
#   while(current!=None):
#        contacts.append((f'{current.data.MaTV}', f'{current.data.HoTen}', f'{current.data.MatKhau}',f'{current.data.NamSinh}',f'{current.data.MuonSach}',f'{current.data.TienPhat}'))
#        current=current.link
#   for contact in contacts:
#        tree.insert('', tk.END, values=contact)
#   tree.pack()
#   scrollbar = ttk.Scrollbar(Gui_member_screen, orient=tk.VERTICAL, command=tree.yview)
#   tree.configure(yscroll=scrollbar.set)
#   #scrollbar.grid(row=0, column=1, sticky='ns')
#   scrollbar.pack(fill=X)

#Notice
def None_Book():
    global None_Book_screen
    None_Book_screen = Toplevel(Dang_Ki_Muon_Sach_screen)
    None_Book_screen.title("None_Book_screen")
    None_Book_screen.geometry("350x150")
    Label(None_Book_screen, text="KHÔNG TÌM THẤY SÁCH BẠN MUỐN MƯỢN").pack()
    Button(None_Book_screen, text="OK", command=delete_None_Book_screen).pack()
def repair_information_success():
    global repair_information_success_screen
    repair_information_success_screen = Toplevel(repair_information_screen)
    repair_information_success_screen.title("Thành Công")
    repair_information_success_screen.geometry("200x150")
    Label(repair_information_success_screen, text="Sửa thông tin Thành Công").pack()
    Button(repair_information_success_screen, text="OK", command=delete_repair_information_success).pack()
def repair_Sach_success():
    global repair_Sach_success_screen
    repair_Sach_success_screen = Toplevel(Menu_Sach_screen)
    repair_Sach_success_screen.title("Thành Công")
    repair_Sach_success_screen.geometry("200x100")
    Label(repair_Sach_success_screen, text="Sửa sách Thành Công").pack()
    Button(repair_Sach_success_screen, text="OK", command=delete_repair_Sach_success).pack()
def repair_Sach_Fail():
    global repair_Sach_Fail_screen
    repair_Sach_Fail_screen = Toplevel(Menu_Sach_screen)
    repair_Sach_Fail_screen.title("Fail")
    repair_Sach_Fail_screen.geometry("200x100")
    Label(repair_Sach_Fail_screen, text="Sửa sách Thất Bại").pack()
    Button(repair_Sach_Fail_screen, text="OK", command=delete_repair_Sach_Fail).pack()
def codeBook_was_not_exist():
    global codeBook_was_not_exist_screen
    codeBook_was_not_exist_screen = Toplevel(Menu_Sach_screen)
    codeBook_was_not_exist_screen.title("Fail")
    codeBook_was_not_exist_screen.geometry("200x100")
    Label(codeBook_was_not_exist_screen, text="Mã Số Sách không tồn tồn tài").pack()
    Button(codeBook_was_not_exist_screen, text="OK", command=delete_codeBook_was_not_exist).pack()
def codeBook_was_exist():
    global codeBook_was_exist_screen
    codeBook_was_exist_screen = Toplevel(Menu_Sach_screen)
    codeBook_was_exist_screen.title("Fail")
    codeBook_was_exist_screen.geometry("200x100")
    Label(codeBook_was_exist_screen, text="Mã Số Sách đã tồn tài").pack()
    Button(codeBook_was_exist_screen, text="OK", command=delete_codeBook_was_exist).pack()


def Add_Sach_Success():
    global Add_Sach_Success_screen
    Add_Sach_Success_screen = Toplevel(Menu_Sach_screen)
    Add_Sach_Success_screen.title("Success")
    Add_Sach_Success_screen.geometry("200x100")
    Label(Add_Sach_Success_screen, text="Thêm sách thành công").pack()
    Button(Add_Sach_Success_screen, text="OK", command=delete_Add_Sach_Success).pack()
def Add_Sach_Fail():
    global Add_Sach_Fail_screen
    Add_Sach_Fail_screen = Toplevel(Menu_Sach_screen)
    Add_Sach_Fail_screen.title("Fail")
    Add_Sach_Fail_screen.geometry("200x100")
    Label(Add_Sach_Fail_screen, text="Thêm sách Thất bại").pack()
    Button(Add_Sach_Fail_screen, text="OK", command=delete_Add_Sach_Fail).pack()

def Exit_User():
    global Exit_User_screen
    Exit_User_screen = Toplevel(user_screen)
    Exit_User_screen.title("Exit user")
    Exit_User_screen.geometry("200x100")
    Label(Exit_User_screen, text="Bạn chắc có muốn thoát").pack()
    #frame1 = Frame(Exit_User_screen)
    #frame1.pack(fill=X)
    Label(Exit_User_screen,text="",height="2")
    Button(Exit_User_screen, text="OK",width="10" ,command=Exit_User_success).pack(side=TOP,padx=5, pady=5)
    Label(Exit_User_screen,text="",height="2")
    Button(Exit_User_screen, text="Không",width="10" ,command=Exit_User_False).pack(side=TOP,padx=5, pady=5)

def Tra_sach_success():
    global Tra_sach_successs_screen
    Tra_sach_successs_screen = Toplevel(Dang_Ki_Tra_Sach_screen)
    Tra_sach_successs_screen.title("Success")
    Tra_sach_successs_screen.geometry("200x100")
    Label(Tra_sach_successs_screen, text="Trả Sách Thành Công ").pack()
    Button(Tra_sach_successs_screen, text="OK", command=delete_Tra_sach_successs).pack()

def Tra_sach_fail():
    global Tra_sach_fail_screen
    Tra_sach_fail_screen = Toplevel(Dang_Ki_Tra_Sach_screen)
    Tra_sach_fail_screen.title("Success")
    Tra_sach_fail_screen.geometry("200x100")
    Label(Tra_sach_fail_screen, text="Mượn Sách Thành Công ").pack()
    Button(Tra_sach_fail_screen, text="OK", command=delete_Tra_sach_Fail).pack()

def muon_sach_success():
    global muon_sach_success_screen
    muon_sach_success_screen = Toplevel(Dang_Ki_Muon_Sach_screen)
    muon_sach_success_screen.title("Success")
    muon_sach_success_screen.geometry("200x100")
    Label(muon_sach_success_screen, text="Mượn Sách Thành Công ").pack()
    Button(muon_sach_success_screen, text="OK", command=delete_muon_sach_success).pack()


def muon_sach_fail():
    global muon_sach_fail_screen
    muon_sach_fail_screen = Toplevel(Dang_Ki_Muon_Sach_screen)
    muon_sach_fail_screen.title("Fail")
    muon_sach_fail_screen.geometry("200x100")
    Label(muon_sach_fail_screen, text="Mượn Sách Thất Bại(bạn nên trả sách rồi mượn tiếp) ").pack()
    Button(muon_sach_fail_screen, text="OK", command=muon_sach_fail_success).pack()

def registration_success():
    global registration_success_screen
    registration_success_screen = Toplevel(register_screen)
    registration_success_screen.title("Success")
    registration_success_screen.geometry("200x100")
    Label(registration_success_screen, text="Registration success ").pack()
    Button(registration_success_screen, text="OK", command=delete_registration_success).pack()


def ID_Was_exist():
    global ID_was_exist_screen
    ID_was_exist_screen = Toplevel(register_screen)
    ID_was_exist_screen.title("False")
    ID_was_exist_screen.geometry("200x100")
    Label(ID_was_exist_screen, text="ID Đã Tồn tại xin vui lòng nhập ID khác ").pack()
    Button(ID_was_exist_screen, text="OK", command=delete_ID_Was_exist).pack()


def False_ID():
    global False_ID_screen
    False_ID_screen = Toplevel(register_screen)
    False_ID_screen.title("False")
    False_ID_screen.geometry("200x100")
    Label(False_ID_screen, text="Nhập ID là Số không được là chữ ").pack()
    Button(False_ID_screen, text="OK", command=delete_false_id).pack()

def False_Year_TV():
    global  False_Year_TV_screen
    False_Year_TV_screen = Toplevel(register_screen)
    False_Year_TV_screen.title("False")
    False_Year_TV_screen.geometry("200x100")
    Label(False_Year_TV_screen, text="Nhập Năm là Số không được là chữ ").pack()
    Button(False_Year_TV_screen, text="OK", command=delete_false_year_tv).pack()
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=User_main).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
def delete_repair_information_success():
    repair_information_success_screen.destroy()
    repair_information_screen.destroy()
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
def delete_None_Book_screen():
    None_Book_screen.destroy()
def delete_repair_Sach_success():
    repair_Sach_success_screen.destroy()
def delete_repair_Sach_Fail():
    repair_Sach_Fail_screen.destroy()
def delete_codeBook_was_not_exist():
    codeBook_was_not_exist_screen.destroy()

def delete_codeBook_was_exist():
    codeBook_was_exist_screen.destroy()

def delete_Add_Sach_Success():
    Add_Sach_Success_screen.destroy()


def delete_Add_Sach_Fail():
    Add_Sach_Fail_screen.destroy()

def delete_Tra_sach_Fail():
    Tra_sach_fail_screen.destroy()
    Dang_Ki_Tra_Sach_screen.destroy()


def delete_Tra_sach_successs():
    muon_sach_success_screen.destroy()

def delete_registration_success():
    registration_success_screen.destroy()
    register_screen.destroy()
    
    
def Exit_User_success():
    Exit_User_screen.destroy()
    user_screen.destroy()

def Exit_User_False():
    Exit_User_screen.destroy()

def delete_false_id():
    False_ID_screen.destroy()

def muon_sach_fail_success():
    muon_sach_fail_screen.destroy()
    Dang_Ki_Muon_Sach_screen.destroy()

def delete_muon_sach_success():
    muon_sach_success_screen.destroy()

def delete_ID_Was_exist():
    ID_was_exist_screen.destroy()


def delete_false_year_tv():
    False_Year_TV_screen.destroy()


def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    TinhTienNopPhat();
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="#AEF35A", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
#User_main
