
from QuanLyMuonTra import *
import tkinter as tk
from Book import chuyenInHoa
from tkinter import *
from tkinter import ttk
from datetime import date,datetime,time,timedelta

class Node:
    def __init__(self, data = None, link = None):        
        self.data = data
        self.link = link

class DSLKQLMuonTra:
    def __init__(self):
        self.head = None
        self.tail=None
        
    def isEmpty(self):
        return self.head==None

    def themSau(self,x):
        a=x
        newNode=Node(a)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.link=newNode
            self.tail =self.tail.link
    
    def chenTheoViTri(self,pos,x):
        a=x
        newNode=Node(a)
        n=0
        current = self.head
        Truoc = None
        while current!=None and n<pos:
            n=n+1
            Truoc=current
            current = current.link
        if Truoc==None:
            newNode.link=self.head
            self.head=newNode
            if self.tail==None:
                self.tail=newNode
        else:
            if(current==None):
                self.tail.link=newNode
                self.tail =self.tail.link
            else:
                Truoc.link=newNode
                newNode.link=current
            
    def timDSLK(self,x):
        current = self.head
        Pos= 0
        while(current!=None and current.data!=x):
            current=current.link
            Pos+=1
        if current==None:
            return None
        else:
            return Pos


        
    #def CapNhat(self,pos):
    #    current = self.head
    #    n= 0
    #    while(current!=None and n!=pos):
    #        current=current.link
    #        n+=1
    #    if current!=None:
    #         current.data.Repair()

    def XoaAll(self): 
        current = self.head
        Truoc = None
        while current!=None:
            self.head=self.head.link
            current = current.link
        del current
    
    def Xoa1PhanTu(self,x):
        current = self.head
        Truoc = None
        while current!=None and current.data != x:
            Truoc=current
            current = current.link
        if current!=None:
            if(current==self.head) and (current==self.tail):
                self.head=self.tail=None
            elif current==self.tail :
                Truoc.link=None
                self.tail=Truoc
            elif current==self.head:
                self.head=self.head.link           
            else :
                Truoc.link=current.link
            del current

    def SapXepTheoNhoDenLonTheoMaMuonTra(self):
        current=self.head
        Sau=None
        while(current!=None):
            Sau=current.link
            while Sau!=None:
                if(int(Sau.data.MaMuonTra)<int(current.data.MaMuonTra)):
                    temp=Sau.data
                    Sau.data=current.data
                    current.data=temp
                Sau=Sau.link
            current = current.link

    def SapXepTheoLonDenNhoTheoMaMuonTra(self):
        current=self.head
        Sau=None
        while(current!=None):
            Sau=current.link
            while Sau!=None:
                if(Sau.data.MaMuonTra>current.data.MaMuonTra):
                    temp=Sau.data
                    Sau.data=current.data
                    current.data=temp   
                Sau=Sau.link
            current = current.link

    def SapXepTheoNhoDenLonTheoDate(self):
        current=self.head
        Sau=None
        while(current!=None):
            Sau=current.link
            while Sau!=None:
                
                a=current.data.NgayMuon-Sau.data.NgayMuon
                ptint(f"{a.days}")
                if(a.days<0):
                    temp=Sau.data
                    Sau.data=current.data
                    current.data=temp
                Sau=Sau.link
            current = current.link

    def SapXepTheoLonDenNhoTheoDate(self):
        current=self.head
        Sau=None
        while(current!=None):
            Sau=current.link
            while Sau!=None:
                a=(current.data.NgayMuon)
                print(f"{a._days}")
                if(a._days>0):
                    temp=Sau.data
                    Sau.data=current.data
                    current.data=temp
                Sau=Sau.link
            current = current.link

    def Xoa1PhanTuTheoMaSo(self,x):
       if x.isnumberic==True:
        a=int(x)
        current = self.head
        Truoc = None
        while current!=None and current.data.MaMuonTra!=a:
            Truoc=current
            current = current.link
        if current!=None:
            if(current==self.head) and (current==self.tail):
                self.head=self.tail=None
            elif current==self.tail :
                Truoc.link=None
                self.tail=Truoc
            elif current==self.head:
                self.head=self.head.link           
            else :
                Truoc.link=current.link
            del current

    def dem_PhanTu(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.link        
        return count

    def locTheoDocGia(self,x):
        if x.isnumeric() != True:
            a=chuyenInHoa(x)
        elif x.isnumeric() == True :
            a=int(x)
        current = self.head
        count = 0
        while current!=None:     
            if current.data.MaTV:
                current.data.xuatQL()
                count += 1
            elif current.data.HoTen == a:
                current.data.xuatQL()
                count += 1
            current=current.link
        if count==0:
            print("Không có phần tử")
        else:
            print(f"có {count} thành viên ")

    def TimDocGia(self,x):
        if x.isnumeric() == True:
                a=int(x)
        current = self.head
        while(current!=None and current.data.MaTV != a ): 
           current=current.link     
        if current==None:
            return current.data
        else:
            return None
        

    def locTheoSach(self,x):
        if x.isnumeric() != True:
            a=chuyenInHoa(x)
        elif x.isnumeric() == True :
            a=int(x)
        current = self.head
        count = 0
        while current!=None:     
            if current.data.MaSach==a:
                current.data.xuatQL()
                count += 1
            elif current.data.TuaDe == a:
                current.data.xuatQL()
                count += 1
            current=current.link
        if count==0:
            print("Không có phần tử")
        else:
            print(f"có {count} thành viên ")
    
    def timQLMuonTraTheoMS(self,x):
        if x.isnumeric() == True:
            a=int(x)
        current = self.head
        while(current!=None and current.data.MaMuonTra != a ): 
           current=current.link     
        if current==None:
            print("Không có phần tử")
        else:
            current.data.xuatQL()

    def locThanhVien(self,x):
        if x.isnumeric() == False:
            a=chuyenInHoa(x)
        else :
            a=int(x)
        current = self.head
        count = 0
        while current!=None:     
            if current.data.MaTV== a:
                current.data.xuatQL()
                count = count+ 1
            elif current.data.HoTen == a:
                current.data.xuatQL()
                count = count+ 1
            current=current.link
        if count==0:
            print("Không có phần tử")
        else:
            print(f"có {count} thành viên ")


    def locSach(self,x):
        if x.isnumeric() != True:
            a=chuyenInHoa(x)
        elif x.isnumeric() == True :
            a=int(x)
        current = self.head
        count = 0
        while current!=None:     
            if current.data.MaSach == a:
                current.data.xuatQL()
                count = count+ 1
            elif current.data.TuaDe == a:
                current.data.xuatQL()
                count = count+ 1
            current=current.link
        if count==0:
            print("Không có phần tử")
        else:
            print(f"có {count} thành viên ")

    def in_DSMuon(self):
        n=0
        current=self.head
        print("|{:-^15}|{:-^15}|{:-^30}|{:-^15}|{:-^25}|{:-^10}|{:-^11}|".format('Mã mượn trả','Mã thành viên','Họ Tên','Mã Sách ','Tên Sách','Ngày Mượn','Đã trả Sách'))
        while(current != None):
                current.data.xuatQL()
                n = n + 1
                current=current.link    
        print("|{:-^15}|{:-^15}|{:-^30}|{:-^15}|{:-^25}|{:-^10}|{:-^11}|".format('','','','','','','',' '))
    
    def in_DSMuonTra(self):
        n=0
        current=self.head
        print("|{:-^15}|{:-^15}|{:-^30}|{:-^15}|{:-^25}|{:-^10}|{:-^11}|".format('Mã mượn trả','Mã thành viên','Họ Tên','Mã Sách ','Tên Sách','Ngày Trả','Đã trả Sách'))
        while(current != None):
                current.data.xuatQL()
                n = n + 1
                current=current.link    
        print("|{:-^15}|{:-^15}|{:-^30}|{:-^15}|{:-^25}|{:-^10}|{:-^11}|".format('','','','','','','',' '))
    def in_DSMuonCuaTV(self,matv):
        n=0
        current=self.head
        print("|{:-^15}|{:-^15}|{:-^30}|{:-^15}|{:-^25}|{:-^10}|{:-^11}|".format('Mã mượn trả','Mã thành viên','Họ Tên','Mã Sách ','Tên Sách','Ngày Trả','Đã trả Sách'))
        while(current != None):
            if(current.data.MaTV==matv and current.data.DangMuon==False):
                current.data.xuatQL()
                n = n + 1
            current=current.link    
        print("|{:-^15}|{:-^15}|{:-^30}|{:-^15}|{:-^25}|{:-^10}|{:-^11}|".format('','','','','','','',' '))


    def TongTienTrePhat(self,MaTV):
        current = self.head
        TongTien=0
        count=0
        while current!=None :
            if current.data.MaTV==MaTV and current.data.DangMuon==False :
                    SoNgayMuon=date.today()-current.data.NgayMuon
                    if SoNgayMuon.days>14:
                         NgayTam=SoNgayMuon.days-14+1
                         count=count+NgayTam
            current=current.link 
        TongTien=count*1000
        return TongTien

    def LocRaDSTraSachTre(self):
        current = self.head
        DSTraTre=DSLKQLMuonTra()
        while current!=None :
            if current.data.DangMuon==False :
                    SoNgayMuon=date.today()-current.data.NgayMuon
                    if SoNgayMuon.days>14:
                         DSTraTre.themSau(current.data)
            current=current.link 
        DSTraTre.GUI_Muon()        
    
    def locTimDocGia(self,TaiKhoang):
        current = self.head
        count=0
        while current!=None :
            if current.data.MaTV==TaiKhoang and current.data.DangMuon==False:
                count=count+1
            current=current.link     
        return count

    def ChuyenSangDaTra(self,TaiKhoang,Masach):
        current = self.head
        count=0
        while current!=None :
            if current.data.MaTV ==TaiKhoang and current.data.MaSach==Masach  and current.data.DangMuon==False:
                current.data.DangMuon=True
                return
            current=current.link     
     
    def KTCMSach(self,TaiKhoang,Masach):  
        current = self.head
        count=0
        while current!=None :
            if current.data.MaTV ==TaiKhoang and current.data.MaSach==Masach  and current.data.DangMuon==False:
                return True
            current=current.link  
        return False

#ghi file ddocj file
    def DocFileQLMuon(self):
        lines=[]
        with open('QuanLyMuonTra.txt','r',encoding='UTF-8') as f:
            lines = f.readlines()
            line = []
            for i in lines:
                line = i.split(',')
                strMaMuonTra = line[0]
                MaMuonTra = int(strMaMuonTra)
                strMaTV = line[1]
                MaTV = int(strMaTV)
                HoTenTam = line[2]
                HoTen=chuyenInHoa(HoTenTam)
                strMaSach = line[3]
                MaSach = int(strMaSach)
                TuaDeTam = line[4]
                TuaDe=chuyenInHoa(TuaDeTam)
                NgayMuon = line[5].split('-')
                Nam=int(NgayMuon[0])
                thang=int(NgayMuon[1])
                ngay=int(NgayMuon[2])
                NgayMuonSach = date(Nam,thang,ngay) 
                if int(line[6])==1:
                    DangMuon=True
                else:
                    DangMuon=False
                a=QuanLyMuonTra(MaMuonTra,MaTV,HoTen,MaSach,TuaDe,NgayMuonSach,DangMuon)
                self.themSau(a)

    def GhiFileQLMuon(self):
        current=self.head
        with open('QuanLyMuonTra.txt',mode='w',encoding='UTF-8') as f:
            while current!=None:
                a=str(current.data.MaMuonTra)
                b=str(current.data.MaTV)
                c=str(current.data.HoTen)
                d=str(current.data.MaSach)
                e=str(current.data.TuaDe)
                date=str(current.data.NgayMuon)
                #thang=str(current.data.NgayMuon.month)
                #ngay=str(current.data.NgayMuon.day)
                #date=(f"{nam}/{thang}/{ngay}")
                if current.data.DangMuon==True:
                    g=1
                else:
                    g=0
                f.write("{0},{1},{2},{3},{4},{5},{6}\n".format(a,b,c,d,e,date,g))
                current=current.link

    def DocFileQLTra(self):
        lines=[]
        with open('QuanLyTra.txt','r',encoding='UTF-8') as f:
            lines = f.readlines()
            line = []
            for i in lines:
                line = i.split(',')
                strMaMuonTra = line[0]
                MaMuonTra = int(strMaMuonTra)
                strMaTV = line[1]
                MaTV = int(strMaTV)
                HoTenTam = line[2]
                HoTen=chuyenInHoa(HoTenTam)
                strMaSach = line[3]
                MaSach = int(strMaSach)
                TuaDeTam = line[4]
                TuaDe=chuyenInHoa(TuaDeTam)
                NgayMuon = line[5].split('-')
                Nam=int(NgayMuon[0])
                thang=int(NgayMuon[1])
                ngay=int(NgayMuon[2])
                NgayMuonSach = date(Nam,thang,ngay) 
                if int(line[6])==1:
                    DangMuon=True
                else:
                    DangMuon=False
                a=QuanLyMuonTra(MaMuonTra,MaTV,HoTen,MaSach,TuaDe,NgayMuonSach,DangMuon)
                self.themSau(a)

    def GhiFileQLTra(self):
        current=self.head
        with open('QuanLyTra.txt',mode='w',encoding='UTF-8') as f:
            while current!=None:
                a=str(current.data.MaMuonTra)
                b=str(current.data.MaTV)
                c=str(current.data.HoTen)
                d=str(current.data.MaSach)
                e=str(current.data.TuaDe)
                date=str(current.data.NgayMuon)
                #thang=str(current.data.NgayMuon.month)
                #ngay=str(current.data.NgayMuon.day)
                #date=(f"{nam}/{thang}/{ngay}")
                if current.data.DangMuon==True:
                    g=1
                else:
                    g=0
                f.write("{0},{1},{2},{3},{4},{5},{6}\n".format(a,b,c,d,e,date,g))
                current=current.link
    #Gui Mượn
    def GUI_Muon(self):
        GUI_Muon_screen = tk.Tk()
        GUI_Muon_screen.title("GUI_muon")
        GUI_Muon_screen.geometry("400x250")
        Label(GUI_Muon_screen, text="Danh sách Mượn",bg="#AEF35A",width="300",height="2", font=("Calibri", 13)).pack()
        Label(GUI_Muon_screen, text="").pack()
        frame1 = Frame(GUI_Muon_screen)
        frame1.pack(fill = X, side=TOP)
        Label(frame1, text="").pack(side=LEFT)
        columns = ('MaMuonTra', 'MaTV', 'HoTen','MaSach','TuaDe','NgayMuon','DangMuon')
        tree = ttk.Treeview(frame1, columns=columns, show='headings')
        # define headings
        tree.heading('MaMuonTra', text='Mã Mượn sách ')
        tree.heading('MaTV', text='Mã Thành Viên')
        tree.heading('HoTen', text='Họ Tên Thành Viên')
        tree.heading('MaSach', text='Mã sách')
        tree.heading('TuaDe', text='Tựa Đề')
        tree.heading('NgayMuon', text='Ngày Mượn')
        tree.heading('DangMuon',text='Đã Trả')
        contacts = []
        current=self.head
        while(current!=None):
            contacts.append((f'{current.data.MaMuonTra}', f'{current.data.MaTV}', f'{current.data.HoTen}',f'{current.data.MaSach}',f'{current.data.TuaDe}',f'{current.data.NgayMuon}',f'{current.data.DangMuon}'))
            current=current.link
        for contact in contacts:
            tree.insert('', tk.END, values=contact)
        tree.pack(side=LEFT,padx=3, pady=3,fill=X)
        scrollbar = ttk.Scrollbar(frame1, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        #scrollbar.grid(row=0, column=1, sticky='ns')
        scrollbar.pack(side=LEFT,padx=3, pady=3,fill=Y)
    
    def GUI_Tra(self):
        GUI_Tra_screen = tk.Tk()
        GUI_Tra_screen.title("GUI_Tra")
        GUI_Tra_screen.geometry("400x250")
        Label(GUI_Tra_screen, text="Danh sách Trả",bg="#AEF35A",width="300",height="2", font=("Calibri", 13)).pack()
        Label(GUI_Tra_screen, text="").pack()
        frame1 = Frame(GUI_Tra_screen)
        frame1.pack(fill = X, side=TOP)
        Label(frame1, text="").pack(side=LEFT)
        columns = ('MaMuonTra', 'MaTV', 'HoTen','MaSach','TuaDe','NgayTra','DangMuon')
        tree = ttk.Treeview(frame1, columns=columns, show='headings')
        # define headings
        tree.heading('MaMuonTra', text='Mã Mượn sách ')
        tree.heading('MaTV', text='Mã Thành Viên')
        tree.heading('HoTen', text='Họ Tên Thành Viên')
        tree.heading('MaSach', text='Mã sách')
        tree.heading('TuaDe', text='Tựa Đề')
        tree.heading('NgayTra', text='Ngày Trả')
        tree.heading('DangMuon',text='Đã Trả')
        contacts = []
        current=self.head
        while(current!=None):
            contacts.append((f'{current.data.MaMuonTra}', f'{current.data.MaTV}', f'{current.data.HoTen}',f'{current.data.MaSach}',f'{current.data.TuaDe}',f'{current.data.NgayMuon}',f'{current.data.DangMuon}'))
            current=current.link
        for contact in contacts:
            tree.insert('', tk.END, values=contact)
        tree.pack(side=LEFT,padx=3, pady=3,fill=X)
        scrollbar = ttk.Scrollbar(frame1, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        #scrollbar.grid(row=0, column=1, sticky='ns')
        scrollbar.pack(side=LEFT,padx=3, pady=3,fill=Y)
    #Tìm Kiếm mượn-------------------------------------------------------------------------------------
    def Gui_TimKiem_Muon(self,MaMuonTraTam,MaTVTam,HoTenTam,MaSachTam,TuaDeTam,NgayMuonTam):
            DSQL=DSLKQLMuonTra()
            MaMuonTra=int(MaMuonTraTam)
            MaTV=int(MaTVTam)
            HoTen=chuyenInHoa(HoTenTam)
            MaSach=int(MaSachTam)
            TuaDe=chuyenInHoa(TuaDeTam)
            try:
                Day = NgayMuonTam.split('/')
                ngay=int(Day[0])
                thang=int(Day[1])
                Nam=int(Day[2])
                NgayMuon = date(Nam,thang,ngay) 
            except:
                NgayMuon=0
            current = self.head
            if(MaMuonTra!=0 and MaTV!=0 and HoTen!="" and MaSach!=0 and TuaDe!=0 and NgayMuon!=0):
                while(current!=None):
                    if(current.data.MaTV==MaTV and current.data.MaMuonTra==MaMuonTra and current.data.HoTen==HoTen and current.data.MaSach==MaSach and current.data.TuaDe==TuaDe and current.data.NgayMuon==NgayMuonTam and current.data.DangMuon==False):
                        DSQL.themSau(current.data)
                    current=current.link
            elif(MaMuonTra!=0 and MaTV!=0 and HoTen!="" and MaSach!=0 and TuaDe!=0 and NgayMuon==0):
                while(current!=None):
                    if(current.data.MaTV==MaTV and current.data.MaMuonTra==MaMuonTra and current.data.HoTen==HoTen and current.data.MaSach==MaSach and current.data.TuaDe==TuaDe  and current.data.DangMuon==False):
                        DSQL.themSau(current.data)
                    current=current.link
            elif(NgayMuonTam!=0):
                while(current!=None):
                    if(current.data.MaTV==MaTV or current.data.MaMuonTra==MaMuonTra or current.data.HoTen==HoTen or current.data.MaSach==MaSach or current.data.TuaDe==TuaDe or current.data.NgayMuon==NgayMuon)  and(current.data.NgayMuon==NgayMuon and current.data.DangMuon==False):
                        DSQL.themSau(current.data)
                    current=current.link
            else:
                while(current!=None):
                    if(current.data.MaTV==MaTV or current.data.MaMuonTra==MaMuonTra or current.data.HoTen==HoTen or current.data.MaSach==MaSach or current.data.TuaDe==TuaDe)  and current.data.DangMuon==False:
                        DSQL.themSau(current.data)
                    current=current.link
            DSQL.GUI_Muon()
    #Tìm Kiếm Trả -------------------------------------------------------------------------------------
    def Gui_TimKiem_Tra(self,MaMuonTraTam,MaTVTam,HoTenTam,MaSachTam,TuaDeTam,NgayMuonTam):
            DSQL=DSLKQLMuonTra()
            MaMuonTra=int(MaMuonTraTam)
            MaTV=int(MaTVTam)
            HoTen=chuyenInHoa(HoTenTam)
            MaSach=int(MaSachTam)
            TuaDe=chuyenInHoa(TuaDeTam)
            try:
                Day = NgayMuonTam.split('/')
                ngay=int(Day[0])
                thang=int(Day[1])
                Nam=int(Day[2])
                NgayMuon = date(Nam,thang,ngay) 
            except:
                NgayMuon=0
            current = self.head
            if(MaMuonTra!=0 and MaTV!=0 and HoTen!="" and MaSach!=0 and TuaDe!=0 and NgayMuon!=0):
                while(current!=None):
                    if(current.data.MaTV==MaTV and current.data.MaMuonTra==MaMuonTra and current.data.HoTen==HoTen and current.data.MaSach==MaSach and current.data.TuaDe==TuaDe and current.data.NgayMuon==NgayMuonTam and current.data.DangMuon==True):
                        DSQL.themSau(current.data)
                    current=current.link
            elif(MaMuonTra!=0 and MaTV!=0 and HoTen!="" and MaSach!=0 and TuaDe!=0 and NgayMuon==0):
                while(current!=None):
                    if(current.data.MaTV==MaTV and current.data.MaMuonTra==MaMuonTra and current.data.HoTen==HoTen and current.data.MaSach==MaSach and current.data.TuaDe==TuaDe  and current.data.DangMuon==True):
                        DSQL.themSau(current.data)
                    current=current.link
            elif(NgayMuonTam!=0):
                while(current!=None):
                    if(current.data.MaTV==MaTV or current.data.MaMuonTra==MaMuonTra or current.data.HoTen==HoTen or current.data.MaSach==MaSach or current.data.TuaDe==TuaDe or current.data.NgayMuon==NgayMuon)  and(current.data.NgayMuon==NgayMuon and current.data.DangMuon==True):
                        DSQL.themSau(current.data)
                    current=current.link
            else:
                while(current!=None):
                    if(current.data.MaTV==MaTV or current.data.MaMuonTra==MaMuonTra or current.data.HoTen==HoTen or current.data.MaSach==MaSach or current.data.TuaDe==TuaDe)  and current.data.DangMuon==True:
                        DSQL.themSau(current.data)
                    current=current.link
            DSQL.GUI_Tra()
    def Gui_ToanBoMuon(self):
        DSQL=DSLKQLMuonTra()
        current = self.head 
        while current!=None :
            if current.data.DangMuon==False  :
                
                    DSQL.themSau(current.data)
            current=current.link 
        DSQL.GUI_Muon()

    def timKiemQLMuonQuaHan(self,MaTV):
        DSQL=DSLKQLMuonTra()
        try:
            a=int(MaTV)
        except:
            a=chuyenInHoa(MaTV)
        current = self.head 
        while current!=None :
            if current.data.MaTV==MaTV and current.data.DangMuon==False  :
                
                    DSQL.themSau(current.data)
            current=current.link 
        DSQL.GUI_Muon()

def MenuQLMuon():
    QL=DSLKQLMuonTra()
    QL.DocFileQLMuon()
    n=-1
    while(n!=0):
        try:
            print("‘{:-^50}".format('Menu Quản lý mượn'))
            print("1:Sắp Xếp lại Danh Sách Quản lý Theo ngày mươn")
            print("2:Sắp Xếp lại Danh Sách Quản lý đọc giả mượn")
            print("3:Tìm mã số quản lý mượn ")
            print("4:Đếm Số Lượng Mượn ")
            print("5:Xóa Tất Cả Dữ Liệu ")
            print("6:Lọc dữ liệu Đọc Giả ")
            print("7:Xuất Đoc Giả ")
            print("0:Nhap Không Để Thoát")
            n= int(input("Chọn 1 chức năng:"))   
            print()
            if n == 1:
                tam=False
                while(tam==False):
                    try:
                        print("1.Sắp xếp Lớn Đến nhỏ theo Ngày mượn")
                        print("2.Sắp Xếp Nhỏ đến lớn theo Ngày mượn")
                        Chon=int(input("Chọn Cách bạn sắp xếp:"))
                        if(Chon==1):
                            QL.SapXepTheoLonDenNhoTheoDate()                 
                        elif(Chon==2):
                            QL.SapXepTheoNhoDenLonTheoDate()
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")
                    QL.in_DSMember()
            if n==2:
                tam=False
                while(tam==False):
                    try:
                        print("1.Sắp xếp Lớn Đến nhỏ theo mã số mượn")
                        print("2.Sắp Xếp Nhỏ đến lớn theo mã số mượn")
                        Chon=int(input("Chọn Cách bạn sắp xếp:"))
                        if(Chon==1):
                            QL.SapXepTheoLonDenNhoTheoMaMuonTra()                      
                        elif(Chon==2):
                            QL.SapXepTheoNhoDenLonTheoMaMuonTra()
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")
                    QL.in_DSMuon()
           
                        
                    
                    
            elif n==3:
                tam=False
                while(tam==False):
                    try:
                        print("1.Tìm kiếm chính xác")
                        print("2.Tìm kiếm  mã số Mượn ")
                        Chon=int(input("Bạn Muốn Tìm kiếm theo phương thức nào:"))
                        if(Chon==1):
                            a=NhapQLDSMuon()
                            pos=QL.timDSLK(a)
                            if(pos==None):
                                print("Không có Trong Danh Sách")
                            else:
                                print("Vị Trí của Danh Sach"+pos)
                        elif(Chon==2):
                            MsQL=input("Nhập mã số cần tìm:")
                            QL.timQLMuonTraTheoMS(MsQL)                        
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")
            elif n==4:
                dem = QL.dem_PhanTu()
                print(f"Số phần tử trong ds : {dem} " )
            elif n==5:
                QL.XoaAll()
            elif n==6:
                tam=False
                while(tam==False):
                    try:
                        print("1.Lọc theo tên người mượn")
                        print("2.Lọc theo mã số người người mượn  ")
                        print("3.Lọc theo tựa đề sách đang được mượn")
                        print("4.Lọc theo mã sách sách đang được mượn")
                        Chon=int(input("Bạn Muốn Tìm kiếm theo phương thức nào:"))
                        if(Chon==1):
                            tentv=input("Họ Tên Thành Viên Muốn Lọc Muốn lọc:")
                            QL.locThanhVien(tentv)
                        elif(Chon==2):
                            mstv=input("Mã số thành viên muốn tìm :")
                            QL.locThanhVien(mstv)
                        elif Chon == 3:
                            tuade=input("Tựa đề sách muốn lọc là gì :")
                            QL.locSach(tuade)
                        elif Chon == 4:
                            masach=input("Mã sách muốn lọc là gì :")
                            QL.locSach(masach)
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")
            elif n==7:
                print("Xuất toàn bộ đọc giả")
                QL.in_DSMuon()
            print()
        except:
            print("Bạn đã Nhập Sai")
    QL.GhiFileQLMuon()
    return QL

def MenuQLTra():
    QL=DSLKQLMuonTra()
    QL.DocFileQLTra()    
    n=-1
    while(n!=0):
        try:
            print("‘{:-^50}".format('Menu Quản lý mượn'))
            print("1:Sắp Xếp lại Danh Sách Quản lý Theo ngày Trả")
            print("2:Sắp Xếp lại Danh Sách Quản lý đọc giả Trả")
            print("3:Tìm mã số quản lý Trả ")
            print("4:Đếm Số Lượng trả ")
            print("5:Xóa Tất Cả Dữ Liệu ")
            print("6:Lọc dữ liệu  ")
            print("7:Xuất Đoc Giả ")
            print("0:Nhap Không Để Thoát")
            n= int(input("Chọn 1 chức năng:"))   
            print()
            if n == 1:
                tam=False
                while(tam==False):
                    try:
                        print("1.Sắp xếp Lớn Đến nhỏ theo Ngày Trả")
                        print("2.Sắp Xếp Nhỏ đến lớn theo Ngày Trả")
                        Chon=int(input("Chọn Cách bạn sắp xếp:"))
                        if(Chon==1):
                            QL.SapXepTheoLonDenNhoTheoDate()                 
                        elif(Chon==2):
                            QL.SapXepTheoNhoDenLonTheoDate()
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")
                    QL.in_DSMember()
            if n==2:
                tam=False
                while(tam==False):
                    try:
                        print("1.Sắp xếp Lớn Đến nhỏ theo mã số Trả")
                        print("2.Sắp Xếp Nhỏ đến lớn theo mã số Trả")
                        Chon=int(input("Chọn Cách bạn sắp xếp:"))
                        if(Chon==1):
                            QL.SapXepTheoLonDenNhoTheoMaMuonTra()                      
                        elif(Chon==2):
                            QL.SapXepTheoNhoDenLonTheoMaMuonTra()
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")
                    QL.in_DSMuon()
           
                        
                    
                    
            elif n==3:
                tam=False
                while(tam==False):
                    try:
                        print("1.Tìm kiếm chính xác")
                        print("2.Tìm kiếm  mã số trả ")
                        Chon=int(input("Bạn Muốn Tìm kiếm theo phương thức nào:"))
                        if(Chon==1):
                            a=NhapQLDSMuon()
                            pos=QL.timDSLK(a)
                            if(pos==None):
                                print("Không có Trong Danh Sách")
                            else:
                                print("Vị Trí của Danh Sach"+pos)
                        elif(Chon==2):
                            MsQL=input("Nhập mã số cần tìm:")
                            QL.timQLMuonTraTheoMS(MsQL)                        
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")
            elif n==4:
                dem = QL.dem_PhanTu()
                print(f"Số phần tử trong ds : {dem} " )
            elif n==5:
                QL.XoaAll()
            elif n==6:
                tam=False
                while(tam==False):
                    try:
                        print("1.Lọc theo tên người trả")
                        print("2.Lọc theo mã số người người trả  ")
                        print("3.Lọc theo tựa đề sách đang được trả")
                        print("4.Lọc theo mã sách sách đang được trả")
                        Chon=int(input("Bạn Muốn Tìm kiếm theo phương thức nào:"))
                        if(Chon==1):
                            tentv=input("Họ Tên Thành Viên Muốn Lọc Muốn lọc:")
                            QL.locThanhVien(tentv)
                        elif(Chon==2):
                            mstv=input("Mã số thành viên muốn tìm :")
                            QL.locThanhVien(mstv)
                        elif Chon == 3:
                            tuade=input("Tựa đề sách muốn lọc là gì :")
                            QL.locSach(tuade)
                        elif Chon == 4:
                            masach=input("Mã sách muốn lọc là gì :")
                            QL.locSach(masach)
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")
            elif n==7:
                print("Xuất toàn bộ đọc giả")
                QL.in_DSMuonTra()
            print()
        except:
            print("Bạn đã Nhập Sai")
    QL.GhiFileQLTra()    
    return QL


    
    
