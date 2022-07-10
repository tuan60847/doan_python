from Member import *
from Book import chuyenInHoa
import tkinter as tk
from tkinter import *
from tkinter import ttk
from DSBook import DSLK,MenuSach,HoiTiepTuc,swap 
from DSQLMuonTra import DSLKQLMuonTra,MenuQLTra,MenuQLMuon 
from QuanLyMuonTra import QuanLyMuonTra
from Book import chuyenInHoa
class Node:
    def __init__(self, data = None, link = None):        
        self.data = data
        self.link = link

class DSLKMember:
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


        
    def CapNhat(self,pos):
        current = self.head 
        n= 0 
        while(current!=None and n!=pos):
            current=current.link 
            n+=1 
        if current!=None:
             current.data.Repair() 

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
    def Xoa1PhanTuTheoMaSo(self,x):
       
        a=int(x) 
        current = self.head 
        Truoc = None 
        while current!=None and current.data.MaTV != a:
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
    def demMemberTheoMS(self,x):
        if self.isEmpty()==True:
            return 1 
        a=int(x)
        current = self.head
        count = 0
        while current != None:
            if current.data.MaTV == a:
                count += 1
            current = current.link
        if(count>=1):
            return 0 
        else:
            return 1 
        
    def in_DSMember(self):
        n=0
        current=self.head 
        print("|{:-^15}|{:-^30}|{:-^20}|{:-^25}|{:-^11}|".format('Mã Thành viên','Họ Tên','Mật Khẩu','Năm','Mượn Sách','Tiền phí'))
        while(current != None):
                current.data.xuat() 
                n = n + 1
                current=current.link    
        print("|{:-^15}|{:-^30}|{:-^20}|{:-^25}|{:-^11}|".format('','','','','',''))
    
    def SapXepTheoNhoDenLonTheoMSTV(self):
        current=self.head
        Sau=None
        while(current!=None):
            Sau=current.link
            while Sau!=None:
                if(int(Sau.data.MaTV)<int(current.data.MaTV)):
                    temp=Sau.data
                    Sau.data=current.data
                    current.data=temp
                Sau=Sau.link
            current = current.link 

    def SapXepTheoLonDenNhoTheoMSTV(self):
        current=self.head
        Sau=None
        while(current!=None):
            Sau=current.link
            while Sau!=None:
                if(Sau.data.MaTV>current.data.MaTV):
                    temp=Sau.data
                    Sau.data=current.data
                    current.data=temp   
                Sau=Sau.link
            current = current.link 
    
    def CapNhatTheoMaSoTV(self,x):
        current = self.head 
        n= 0 
        while(current!=None and current.data.MaTV!=x):
            current=current.link 
            n+=1 
        if current!=None:
             current.data.Repair() 
             current.data.MaSach=x

    def timMemberTheoTenVaMS(self,x):
        if x.isnumeric() != True:
            a=chuyenInHoa(x) 
        else :
            a=int(x) 
        current = self.head 
        while(current!=None and current.data.HoTen!=a and current.data.MaTV!=a): 
                current=current.link      
        if current==None:
            print("Không có phần tử") 
        else:
            current.data.xuat() 

    def timMemberMuonSach(self,x):
        a=int(x) 
        current = self.head 
        while(current!=None):
            if current.data.HoTen==a or current.data.MaTV==a:
                current.data.MuonSach=True
            current=current.link      
        
            

    def timMemberTraSach(self,x): 
        try:
            a=int(x) 
        except:
            a=chuyenInHoa(x)
        current = self.head 
        while(current!=None):
            if current.data.HoTen==a or current.data.MaTV==a:
                self.TinhTongTienMuon1TV(x)
                current.data.MuonSach=False 
            current=current.link  

    def TinhTongTienMuon1TV(self,x):
        try:
            a=int(x) 
        except:
            a=chuyenInHoa(x)
        dsMuon=DSLKQLMuonTra()
        dsMuon.DocFileQLMuon()
        current=self.head
        TongTien=0
        while (current!=None):
            if current.data.HoTen==a or current.data.MaTV==a:
                current.data.TienPhat=dsMuon.TongTienTrePhat(current.data.MaTV)
                TongTien=current.data.TienPhat
            current=current.link


    def locMemberTheoNam(self,x):
        try:
            a=int(x) 
        except:
            a=chuyenInHoa(x)
        current = self.head 
        count = 0 
        while current!=None:     
            if current.data.NamSinh == a:
                current.data.xuat() 
                count += 1 
            current=current.link 
        if count==0:
            print("Năm Có có đọc giả sinh ra ") 
        else:
            print(f"có {count} thành viên ") 

    def locMemberChuaMuonSach(self):
        current = self.head 
        count = 0 
        while current!=None:     
            if current.data.MuonSach == False:
                current.data.xuat() 
                count = count + 1 
            current=current.link 
        if count == 0:
            print("Năm Có có đọc giả sinh ra ") 
        else:
            print(f"có {count} thành viên ") 

    def locMemberMuonSach(self):
        current = self.head 
        count = 0 
        while current!=None:     
            if current.data.MuonSach == True:
                current.data.xuat() 
                count = count + 1 
            current=current.link 
        if count==0:
            print("Năm Có có đọc giả sinh ra ") 
        else:
            print(f"có {count} thành viên ") 

    def demMemberTheoMS(self,x):
       if self.isEmpty()==True:
            return 1 
       try:
        a=int(x)
        current = self.head
        count = 0
        while current != None:
            if (current.data.MaTV == a):
                count += 1
            current = current.link
        if(count>=1):
            return 0 
        else:
            return 1 
       except:
           return 0
    def DocFileMember(self):
        lines=[] 
        with open('Member.txt','r',encoding='UTF-8') as f:
            lines = f.readlines()
            line = [] 
            for i in lines:
                line = i.split(',') 
                strMaTV = line[0] 
                MaTV = int(strMaTV) 
                HoTenTam = line[1] 
                HoTen=chuyenInHoa(HoTenTam)
                MatKhau = str(line[2]) 
                NamTam = line[3] 
                Nam=int(NamTam)
                if int(line[4])==1:
                    MuonSach=True 
                else:
                    MuonSach=False 
                strTienPhat=line[5]
                TienPhat=int(strTienPhat)
                DocGia=Member(MaTV,HoTen,MatKhau,Nam,MuonSach,TienPhat) 
                self.themSau(DocGia) 

    def GhiFileMember(self):
        current=self.head
        with open('Member.txt',mode='w',encoding='UTF-8') as f:
            while current!=None:
                a=str(current.data.MaTV)
                b=str(current.data.HoTen)
                c=str(current.data.MatKhau)
                d=str(current.data.NamSinh)
                if current.data.MuonSach==True:
                    e=1 
                else:
                    e=0 
                g=str(current.data.TienPhat)
                f.write("{0},{1},{2},{3},{4},{5}\n".format(a,b,c,d,e,g)) 
                current=current.link 
    def GUI_Member(self):
        Gui_member_screen = tk.Tk()
        Gui_member_screen.title("GUI_member")
        Gui_member_screen.geometry("650x250")
        Label(Gui_member_screen, text="Danh sách thành viên",bg="#AEF35A",width="300",height="2", font=("Calibri", 13)).pack()
        Label(Gui_member_screen, text="").pack()
        #DSTV=DSLKMember()
        #DSTV.DocFileMember() 
        frame1 = Frame(Gui_member_screen)
        frame1.pack(fill = X, side=TOP)
        Label(frame1, text="").pack(side=LEFT)
        columns = ('MaTV', 'HoTen', 'MatKhau','NamSinh','MuonSach','TienPhat')
        tree = ttk.Treeview(frame1, columns=columns, show='headings')
        # define headings
        tree.heading('MaTV', text='Mã TV')
        tree.heading('HoTen', text='Họ Tên')
        tree.heading('MatKhau', text='Mật khẩu')
        tree.heading('NamSinh', text='Năm Sinh')
        tree.heading('MuonSach', text='Mượn Sách')
        tree.heading('TienPhat', text='Tiền Phạt')
        contacts = []
        current=self.head
        while(current!=None):
            contacts.append((f'{current.data.MaTV}', f'{current.data.HoTen}', f'{current.data.MatKhau}',f'{current.data.NamSinh}',f'{current.data.MuonSach}',f'{current.data.TienPhat}'))
            current=current.link
        for contact in contacts:
            tree.insert('', tk.END, values=contact)
        tree.pack(side=LEFT,padx=3, pady=3,fill=X)
        scrollbar = ttk.Scrollbar(frame1, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        #scrollbar.grid(row=0, column=1, sticky='ns')
        scrollbar.pack(side=LEFT,padx=3, pady=3, fill = Y)
        Label(frame1, text="").pack(side=LEFT)



    def Gui_TV(self,mstv):
        try:
            a=int(mstv)
        except:
            a=chuyenInHoa(mstv)
        dstv=DSLKMember()
        current = self.head 
        while current!=None :
            if current.data.MaTV==a or current.data.HoTen==a  :
                dstv.themSau(current.data)
                
            elif current.data.NamSinh==a:
                dstv.themSau(current.data)
            current=current.link 
        dstv.GUI_Member()
    def Gui_Tim_TV(self,mstv,HoTen,NamSinh,MuonSach):
    
        dstv=DSLKMember()
        current = self.head 
        if mstv!=0 and NamSinh!=0 and HoTen!="":
         while current!=None :
            if current.data.MaTV==mstv and current.data.HoTen==HoTen and current.data.NamSinh==NamSinh and current.data.MuonSach==MuonSach :
                dstv.themSau(current.data)
                break
            current=current.link
        elif mstv!=0 and NamSinh==0 and HoTen=="" and MuonSach==True:
         while current!=None :
            if current.data.MaTV==mstv and current.data.MuonSach==MuonSach:
                dstv.themSau(current.data)
            current=current.link
        elif mstv!=0 and NamSinh==0 and HoTen=="" and MuonSach==False:
         while current!=None :
            if current.data.MaTV==mstv and current.data.MuonSach==MuonSach:
                dstv.themSau(current.data)
            current=current.link
        elif NamSinh!=0:
             while current!=None :
                if current.data.NamSinh==NamSinh:
                    dstv.themSau(current.data)
                current=current.link
        else:
         while current!=None :
            if current.data.MaTV==mstv or current.data.HoTen==HoTen or current.data.NamSinh==NamSinh or current.data.MuonSach==MuonSach:
                dstv.themSau(current.data)
            current=current.link 
        dstv.GUI_Member()
    def Repair_infor_TV(self,MaTVTam,HoTen,MatKhau,NamSinhTam):
        MaTV=int(MaTVTam)
        NamSinh=int(NamSinhTam)
        current=self.head
        while current!=None :
                if current.data.MaTV==MaTV:
                    if HoTen!="":
                        current.data.HoTen = HoTen
                    if MatKhau!="":
                        current.data.MatKhau=MatKhau
                    if NamSinh!=0:
                        current.data.NamSinh=NamSinh
                    break;
                current=current.link

    def timMStraveMk(self,matv):   
        current = self.head 
        while current!=None and current.data.MaTV!=matv:
                current=current.link      
        if current==None:
            print("Không tìm được mật khẩu") 
            return None 
        else:
           return current.data 

    


def DangKi():
        DsTV=DSLKMember()
        DsTV.DocFileMember()
        a=NhapMember() 
        Chon=DsTV.demMemberTheoMS(a.MaTV)
        while Chon==0:
            try:
                    a.MaTV=int(input("Đã có mã thành viên đó mời bạn nhập lại :")) 
                    Chon=DsTV.demMemberTheoMS(a.MaTV) 
            except:
                    print("Bạn đã nhập sai") 
        a.xuat() 
        DsTV.themSau(a) 
        DsTV.GhiFileMember() 

    
        
           
       



def MenuMember():
    n=-1 
    dslkmeber=DSLKMember()
    dslkmeber.DocFileMember()    
    while(n!=0):
        try:
            print("‘{:-^50}".format('Menu Member'))
            print("1:Xóa 1 Đọc giả")
            print("2:Sắp Xếp lại Danh Sách Đọc Giả")
            print("3:Tìm Một Đọc Giả ")
            print("4:Đếm Số Lượng Đọc Giả ")
            print("5:Xóa Tất Cả Đọc Giả ")
            print("6:Lọc dữ liệu Đọc Giả ")
            print("7:Xuất Đoc Giả ")
            print("0:Nhap Không Để Thoát")
            n= int(input("Chọn 1 chức năng:"))   
            print() 
            if n == 1:
                tam=False
                while(tam==False):
                    try:
                        print("1.Xóa 1 phần tử member chính xác")
                        print("2.Xóa 1 Phần tử theo mã số :")
                        Chon=int(input("Chọn Cách Xóa:")) 
                        if(Chon==1):
                           print("Nhập Sách Bạn Muốn xóa vào")
                           a=NhapMember() 
                           dslkmeber.Xoa1PhanTu(a) 
                        elif(Chon==2):
                            matv=int(input("Chọn mã thành viên muốn xóa:"))  
                            dslkmeber.Xoa1PhanTuTheoMaSo(matv) 
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")
            elif n==2:
                tam=False
                while(tam==False):
                    try:
                        print("1.Sắp xếp Lớn Đến nhỏ theo mã số sách")
                        print("2.Sắp Xếp Nhỏ đến lớn theo mã số sách")
                        Chon=int(input("Chọn Cách bạn sắp xếp:")) 
                        if(Chon==1):
                            dslkmeber.SapXepTheoLonDenNhoTheoMSTV() 
                        elif(Chon==2):
                            dslkmeber.SapXepTheoNhoDenLonTheoMSTV()
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")
                    dslkmeber.in_DSMember() 
                        
                    
                    
            elif n==3:
                tam=False
                while(tam==False):
                    try:
                        print("1.Tìm kiếm chính xác")
                        print("2.Tìm kiếm theo tên thành viên và mã số ")
                        Chon=int(input("Bạn Muốn Tìm kiếm theo phương thức nào:")) 
                        if(Chon==1):
                            a=NhapMember() 
                            pos=dslkmeber.timDSLK(a)
                            if(pos==None):
                                print("Không có Trong Danh Sách")
                            else:
                                print("Vị Trí của Danh Sach"+pos)
                        elif(Chon==2):
                            Ten=input("Nhập Ten hoặc mã số cần tìm:") 
                            dslkmeber.timMemberTheoTenVaMS(Ten)                         
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")
            elif n==4:
                dem = dslkmeber.dem_PhanTu()
                print(f"Số phần tử trong ds : {dem} " ) 
            elif n==5:
                dslkmeber.XoaAll() 
            elif n==6:
                tam=False
                while(tam==False):
                    try:
                        print("1.Lọc theo tên năm")
                        print("2.Lọc theo thành viên chưa mượn sách ")
                        print("3.Lọc theo thành viên đang mượn sách ")
                        Chon=int(input("Bạn Muốn Tìm kiếm theo phương thức nào:")) 
                        if(Chon==1):
                            Nam=int(input("Năm Muốn lọc:")) 
                            dslkmeber.locMemberTheoNam(Nam) 
                        elif(Chon==2):
                            dslkmeber.locMemberChuaMuonSach()
                        elif Chon == 3:
                            dslkmeber.locMemberMuonSach()
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")
            elif n==7:
                print("Xuất toàn bộ đọc giả")
                dslkmeber.in_DSMember()
            print() 
        except:
            print("Bạn đã Nhập Sai")
    dslkmeber.GhiFileMember() 
    return dslkmeber
    
    
    


def DangNhap():
     dsTV=DSLKMember()
     tam=False 
     while(tam==False):
      try:
       TaiKhoang=int(input("Bạn có thể mã thành viên :")) 
       MatKhau=  input("Nhập mật khẩu            :") 
       tam=True 
      except:
        print("Bạn đã nhập Sai")  
     if TaiKhoang ==-1 and MatKhau=="admin":
           MenuAdmin() 
     else:
        dsTV.DocFileMember() 
        TV=dsTV.timMStraveMk(TaiKhoang)
        while(TV==None):
           print("Mã số của bạn vừa nhập không tồn tại xin mời bạn nhập lại ")
           tam=False 
           while(tam==False):
                try:
                    TaiKhoang=int(input("Bạn có thể mã thành viên :")) 
                    MatKhau=  input("Nhập mật khẩu            :") 
                    tam=True 
                except:
                    print("MÃ THÀNH VIÊN LÀ SỐ")  
           TV=dsTV.timMStraveMk(TaiKhoang)
        while TV.MatKhau!=MatKhau:
            print("Bạn đã nhập sai mật khẩu vui lần nhập lại") 
            print(f"Bạn có thể mã thành viên :{TaiKhoang}")
            MatKhau=input("Nhập mật khẩu            :")
            TV=dsTV.timMStraveMk(TaiKhoang)
        print("Bạn đã đăng nhập thành công")
        
        dsSach=DSLK() 
        dsSach.DocFileSach() 
        n=-1   
        while(n!=0):
            try:
                print("‘{:-^50}".format('Menu'))
                print("1:Xem Thông Tin Cá Nhân")
                print("2:Tìm kiếm sách")
                print("3:Lọc sách")
                print("4:In tất cả các đầu sách")
                
                now=int(date.today().year) 
                year=now-TV.NamSinh 
                if(year>17):
                    print("5:Muợn Sách")
                    print("6:Trả Sách")
                    print("7:in sách đã mượn chưa trả")
                else:
                    print("bạn không đủ tuổi để sử dụng chức năng mượn trả sách") 
                print("0: để đăng xuất")
                n= int(input("Chọn 1 chức năng:"))   
                print() 
                if n==1:
                    print("|{:-^15}|{:-^30}|{:-^20}|{:-^25}|{:-^11}|{:-^10}|".format('Mã Thành viên','Họ Tên','Mật Khẩu','Năm','Mượn Sách','Tiền Phạt')) 
                    TV.xuat() 
                    print("|{:-^15}|{:-^30}|{:-^20}|{:-^25}|{:-^11}|{:-^10}|".format('','','','','','','')) 
                elif n==2:
                    tam=False
                    while(tam==False):
                     try:
                        print("1.Tìm kiếm chính xác")
                        print("2.Tìm kiếm theo tên sách và mã số ")
                        Chon=int(input("Bạn Muốn Tìm kiếm theo phương thức nào:")) 
                        if(Chon==1):
                            Sach=Nhap() 
                            pos=dsSach.timDSLK(Sach)
                            if(pos==None):
                                print("Không có Trong Danh Sách")
                            else:
                                print("Vị Trí của Danh Sach"+pos)
                        elif(Chon==2):
                            Ten=input("Nhập Tựa Đề hoặc mã sách sách cần tìm:") 
                            dsSach.timSachTheoTuaDe(Ten)
                        tam=True
                     except:
                        print("Bạn đã Nhập Sai")
                elif n==3:
                        tam=False 
                        while(tam==False):
                         try:
                            print("1.Lọc dữ liệu theo tên tác giả") 
                            print("2.Lọc dữ liệu theo nhà xuất bản") 
                            print("3.Lọc dữ liệu theo năm") 
                            Chon=int(input("Bạn Muốn Tìm kiếm theo phương thức nào:")) 
                            if(Chon==1):
                                Ten=input("Nhập tên tác giả: ") 
                            elif(Chon==2):
                                Ten=input("Nhập tên Nhà Xuất Bản: ") 
                            elif(Chon==3):
                                strTen=input("Nhập năm:") 
                                Ten=int(strTen) 
                            dsSach.locSachTheoGiaTri(Ten)
                            tam=True
                         except:
                            print("Bạn đã Nhập Sai")
                elif n==4:
                    dsSach.in_DS() 
                if(year>17):
                      if n==5:
                          DSMuon=DSLKQLMuonTra() 
                          DSMuon.DocFileQLMuon() 
                          
                          KT=DSMuon.locTimDocGia(TaiKhoang) 
                          print(f"số sách đã mượn là {KT}")
                          if KT<3:
                            TenSach=input("Nhập tên sách muốn mượn hoặc mã số sách muốn mượn:")
                            print(TenSach) 
                            Sach=dsSach.timSachTheoTen(TenSach) 
                            maMuonTra=TaiKhoang*Sach.MaSach 
                            #nếu mà chưa trả thì xem là false
                            Muon=QuanLyMuonTra(maMuonTra,TV.MaTV,TV.HoTen,Sach.MaSach,Sach.TuaDe,date.today(),False) 
                            Muon.xuatQL()
                            DSMuon.themSau(Muon) 
                            dsSach.timSachMuon(Sach.MaSach) 
                            dsTV.timMemberMuonSach(TV.MaTV) 
                            dsTV.GhiFileMember() 
                            dsSach.GhiFileSach() 
                            DSMuon.GhiFileQLMuon() 
                          else:
                            print("Bạn đã mượn quá 3 cuốn sách vui lòng trả sách để mươn thêm") 
                      elif n==6:
                          DSMuon=DSLKQLMuonTra() 
                          DSMuon.DocFileQLMuon() 
                          DSMuon.in_DSMuonCuaTV(TV.MaTV)
                          DSTra=DSLKQLMuonTra() 
                          DSTra.DocFileQLTra() 
                          KT=DSMuon.locTimDocGia(TaiKhoang) 
                          if KT>0:
                            TenSach=input("Nhập tên sách muốn trả hoặc mã số sách muốn trả:")
                            Sach=dsSach.timSachTheoTen(TenSach)
                            maMuonTra=TaiKhoang*Sach.MaSach 
                            if DSMuon.KTCMSach(TV.MaTV,Sach.MaSach)==True:
                                #nếu mà trả rồi thì xem là true
                                Tra=QuanLyMuonTra(maMuonTra,TV.MaTV,TV.HoTen,Sach.MaSach,Sach.TuaDe,date.today(),True) 
                                Tra.xuatQL() 
                                DSTra.themSau(Tra) 
                                DSMuon.ChuyenSangDaTra(TV.MaTV,Sach.MaSach)
                                DSMuon.GhiFileQLMuon()
                                DSTra.GhiFileQLTra()
                                dsSach.timSachTra(Sach.MaSach)
                                dsTV.timMemberTraSach(TV.MaTV)
                                dsTV.GhiFileMember()
                                dsSach.GhiFileSach()
                            else:
                                print("Bạn Không có mượn sách đó ")

                          else:
                            print("Bạn nên mượn thêm sách để có thể trả sách")
                      elif n == 7:
                           DSMuon=DSLKQLMuonTra()
                           DSMuon.DocFileQLMuon()
                           DSMuon.in_DSMuonCuaTV(TV.MaTV) 
                      
            except:
                print("Bạn đã Nhập Sai") 
            


def MenuAdmin():
    n=1 
    while n!=0:
            print("‘{:-^50}".format('Menu Member'))
            print("1:Menu xem sách ")
            print("2:Menu xem đọc giả ")
            print("3:Menu người mượn sách ")
            print("4:Menu người trả sách")
            print("5:Đăng nhập lai")
            print("0:Để Thoát ")
            n= int(input("Chọn 1 chức năng:"))   
            print() 
            if n==1:
               dslk=MenuSach() 
            elif n==2:
               dslk=MenuMember() 
            elif n ==3:
               dslk=MenuQLMuon() 
            elif n ==4:
               dslk=MenuQLTra() 
            elif n==5:
                DangNhap()
            if n!=0:
                n=HoiTiepTuc() 

def TinhTienNopPhat():
        dstv=DSLKMember()
        dstv.DocFileMember()
        dsMuon=DSLKQLMuonTra()
        dsMuon.DocFileQLMuon()
        TV=dstv.head
        while (TV!=None):
            TV.data.TienPhat=dsMuon.TongTienTrePhat(TV.data.MaTV)
            Tong=TV.data.TienPhat
            TV=TV.link
        dstv.GhiFileMember()
        dsMuon.GhiFileQLMuon()
      
        
    
