from Book import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
class Node:
    def __init__(self, data = None, link = None):        
        self.data = data
        self.link = link

    #def setData(self):
    #    self.data = Book(data)
    #    return self.data;
    #def setLink(self):
    #    self.link = link ;      
    #def getLink(self):
    #    return self.link;
    #def hasNext(self):
    #    return self.next!=None
    #def __str__(self):
    #    self.data = Book(data)
    #    return self.data;

class DSLK:
    def __init__(self):
        self.head = None
        self.tail=None
        
    def isEmpty(self):
        return self.head==None

    def themSau(self,x):
        a=x
        newNode=Node(a);
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.link=newNode;
            self.tail =self.tail.link;
        #if self.head == None:
        #    self.head = Node(x, None)
        #    self.link=None;
        #else:
        #    current=self.head;
        #    while(current!= None):
        #        current=current.link;          
        #    newNode = Node(x, None)
        #    newNode.next = None;
        #    current = newNode;
    def chenTheoViTri(self,pos,x):
        a=x;
        newNode=Node(a);
        n=0;
        current = self.head;
        Truoc = None;
        while current!=None and n<pos:
            n=n+1;
            Truoc=current;
            current = current.link;
        if Truoc==None:
            newNode.link=self.head
            self.head=newNode;
            if self.tail==None:
                self.tail=newNode;
        else:
            if(current==None):
                self.tail.link=newNode;
                self.tail =self.tail.link;
            else:
                Truoc.link=newNode;
                newNode.link=current;
            
    def timDSLK(self,x):
        current = self.head;
        Pos= 0;
        while(current!=None and current.data!=x):
            current=current.link;
            Pos+=1;
        if current==None:
            return None;
        else:
            return Pos


        
    def CapNhat(self,pos):
        current = self.head;
        n= 0;
        while(current!=None and n!=pos):
            current=current.link;
            n+=1;
        if current!=None:
             current.data.Repair();

    def XoaAll(self): 
        current = self.head;
        Truoc = None;
        while current!=None:
            self.head=self.head.link;
            current = current.link;
        del current;
    
    def Xoa1PhanTu(self,x):
        current = self.head;
        Truoc = None;
        while current!=None and current.data != x:
            Truoc=current;
            current = current.link;
        if current!=None:
            if(current==self.head) and (current==self.tail):
                self.head=self.tail=None;
            elif current==self.tail :
                Truoc.link=None;
                self.tail=Truoc;
            elif current==self.head:
                self.head=self.head.link;           
            else :
                Truoc.link=current.link;
            del current;
    def xoa1PhanTuTheoMS(self,x):
        current = self.head;
        Truoc = None;
        while current!=None and current.data.MaSach != x:
            Truoc=current;
            current = current.link;
        if current!=None:
            if(current==self.head) and (current==self.tail):
                self.head=self.tail=None;
            elif current==self.tail :
                Truoc.link=None;
                self.tail=Truoc;
            elif current==self.head:
                self.head=self.head.link;           
            else :
                Truoc.link=current.link;
            del current;

    def dem_PhanTu(self):
        current = self.head
        count = 0;
        while current != None:
            count += 1
            current = current.link        
        return count
    #Sách--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def locSachTheoGiaTri(self,x):
        if x.isnumeric() != True:
            a=chuyenInHoa(x);
        elif x.isnumeric() == True :
            a=int(x);
        current = self.head;
        count = 0;
        while current!=None:     
            if current.data.Nam == a:
                current.data.xuat();
                count += 1
            elif current.data.TacGia == a:
                current.data.xuat();
                count += 1
            elif current.data.NhaXuatBan == a :
                current.data.xuat();
                count += 1
            current=current.link;
        if count==0:
            print("Không có phần tử");
        else:
            print(f"có {count} Phần tử ");

    def timSachTheoTuaDe(self,x):
        if x.isnumeric() != True:
            a=chuyenInHoa(x);
        else :
            a=int(x);
        current = self.head;
        while(current!=None and current.data.TuaDe!=a and current.data.MaSach!=a): 
                current=current.link;     
        if current==None:
            print("Không có phần tử");
        else:
            current.data.xuat();

    def timSachTheoTen(self,TenSach):
        try:
            a=int(TenSach);  
        except:
            a=chuyenInHoa(TenSach);  
        current = self.head;
        while current!=None and current.data.MaSach!=a and current.data.TuaDe!=a:
                current=current.link;     
        if current==None:
            print("Không tìm được mật khẩu");
            return None;
        else:
            current.data.xuat(); 
            return current.data;

    def timSachMuon(self,x):
        try:
            a=int(x);
        except:
            a=chuyenInHoa(x);
        current = self.head;
        while(current!=None): 
            if current.data.MaSach==a :
                    current.data.SoLuong=current.data.SoLuong-1;
                    return
            current=current.link;

    def timSachTra(self,x):
        try:
            a=int(x);
        except:
            a=chuyenInHoa(x);
        current = self.head;
        while(current!=None): 
            if current.data.MaSach==a :
                    current.data.SoLuong=current.data.SoLuong+1;
                    return
            current=current.link;     
        
            current.data.SoLuong=current.data.SoLuong+1;
            print("Đã cập nhật sách thành công")

    def demSachTheoMS(self,x):
        if self.isEmpty()==True:
            return 1;
        a=int(x)
        current = self.head
        count = 0
        while current != None:
            if current.data.MaSach == a:
                count += 1
            current = current.link
        if(count>=1):
            return 0;
        else:
            return 1;

    def CapNhatTheoMaSoSach(self,x):
        current = self.head;
        n= 0;
        while(current!=None and current.data.MaSach!=x):
            current=current.link;
            n+=1;
        if current!=None:
             current.data.Repair();
             current.data.MaSach=x
    def Sua_Sach_TheoMS(self,MaSachTam,TenSachTam,TacGiaTam,NhaXuatBanTam,NamTam,SoLuongTam):
        ds=DSLK()
        current = self.head 
        MaSach=int(MaSachTam)
        Nam=int(NamTam)
        TenSach=chuyenInHoa(TenSachTam)
        TacGia=chuyenInHoa(TacGiaTam)
        NhaXuatBan=chuyenInHoa(NhaXuatBanTam)
        SoLuong=int(SoLuongTam)
        if MaSach!=0 and Nam!=0 and TenSach!="" and TacGia!="" and NhaXuatBan!="" and SoLuong>0 :
         while current!=None :
            if current.data.MaSach==MaSach:
               current.data.TuaDe==TenSach
               current.data.TacGia==TacGia
               current.data.NhaXuatBan==NhaXuatBan
               current.data.Nam == Nam
               current.data.SoLuong==SoLuong
               ds.themSau(current.data)
               break;
            current=current.link
        else:
             while current!=None :
                if current.data.MaSach==MaSach:
                    if Nam!=0:
                        current.data.Nam = Nam
                    if TenSach!="":
                        current.data.TuaDe=TenSach
                    if NhaXuatBan!="":
                        current.data.NhaXuatBan=NhaXuatBan
                    if SoLuong>0:
                        current.data.SoLuong=SoLuong
                    if Nam!=0:
                        current.data.Nam = Nam
                    ds.themSau(current.data)
                    break;
                current=current.link
        ds.GUI_Book()
    def SapXepTheoNhoDenLonTheoMSSach(self):
        current=self.head
        Sau=None
        while(current!=None):
            Sau=current.link
            while Sau!=None:
                if(int(Sau.data.MaSach)<(current.data.MaSach)):
                    temp=Sau.data
                    Sau.data=current.data
                    current.data=temp
                Sau=Sau.link
            current = current.link;

    def SapXepTheoLonDenNhoTheoMSSach(self):
        current=self.head
        Sau=None
        while(current!=None):
            Sau=current.link
            while Sau!=None:
                if(Sau.data.MaSach>current.data.MaSach):
                    temp=Sau.data
                    Sau.data=current.data
                    current.data=temp
                    
                Sau=Sau.link
            current = current.link;
            

    
    

    def in_DS(self):
        n=0
        current=self.head;
        print("|{:-^15}|{:-^25}|{:-^20}|{:-^25}|{:-^10}|{:-^10}|".format('Mã Sách','Tựa Đề','Tác Giả','Nhà Xuất Bản','Năm','Số Lượng'))
        while(current != None):
                current.data.xuat();
                n = n + 1
                current=current.link    
        print("|{:-^15}|{:-^25}|{:-^20}|{:-^25}|{:-^10}|{:-^10}|".format('','','','','',''))

    

    def __str__(self):
        pass
        #if self.first != None:
        #    current = self.first
        #    out = 'LinkedList [\n' +str(current.data) +'\n'
        #    while current.next != None:
        #        current = current.link                
        #        out += str(current.data) + '\n'
        #    return out + ']'
        #return 'LinkedList []'
    #member-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

     #clear
    def clear(self):
        self.__init__()
    #đọc File Sách
    def DocFileSach(self):
        lines=[];
        with open('Sach.txt','r',encoding='UTF-8') as f:
            lines = f.readlines()
            line = [];
            for i in lines:
                line = i.split(',');
                strMaSach = line[0];
                MaSach = int(strMaSach);
                TuaDeTam = line[1];
                TuaDe=chuyenInHoa(TuaDeTam)
                TacGiaTam = line[2];
                TacGia=chuyenInHoa(TacGiaTam)
                NhaXuatBanTam = line[3];
                NhaXuatBan=chuyenInHoa(NhaXuatBanTam)
                strNam = line[4]; 
                Nam = int(strNam);
                strSoLuong = line[5];
                SoLuong = int(strSoLuong);
                sach=Book(MaSach,TuaDe,TacGia,NhaXuatBan,Nam,SoLuong);
                self.themSau(sach);

    def GhiFileSach(self):
        current=self.head
        with open('Sach.txt',mode='w',encoding='UTF-8') as f:
            while current!=None:
                a=str(current.data.MaSach)
                b=str(current.data.TuaDe)
                c=str(current.data.TacGia)
                d=str(current.data.NhaXuatBan)
                e=str(current.data.Nam)
                t=str(current.data.SoLuong)
                f.write("{0},{1},{2},{3},{4},{5}\n".format(a,b,c,d,e,t));
                current=current.link;
    #Gui sách
    def GUI_Book(self):
        Gui_book_screen = tk.Tk()
        Gui_book_screen.title("GUI_member")
        Gui_book_screen.geometry("400x250")
        Label(Gui_book_screen, text="Danh sách Sách",bg="#AEF35A",width="300",height="2", font=("Calibri", 13)).pack()
        Label(Gui_book_screen, text="").pack()
        frame1 = Frame(Gui_book_screen)
        frame1.pack(fill = X, side=TOP)
        Label(frame1, text="").pack(side=LEFT)
        columns = ('MaSach', 'TuaDe', 'TacGia','NhaXuatBan','Nam','SoLuong')
        tree = ttk.Treeview(frame1, columns=columns, show='headings')
        # define headings
        tree.heading('MaSach', text='Mã Sách')
        tree.heading('TuaDe', text='Tựa Đề')
        tree.heading('TacGia', text='Tác Giả')
        tree.heading('NhaXuatBan', text='Nhà Xuất Bản')
        tree.heading('Nam', text='Năm Phát Hành')
        tree.heading('SoLuong', text='Số Lượng')
        contacts = []
        current=self.head
        while(current!=None):
            contacts.append((f'{current.data.MaSach}', f'{current.data.TuaDe}', f'{current.data.TacGia}',f'{current.data.NhaXuatBan}',f'{current.data.Nam}',f'{current.data.SoLuong}'))
            current=current.link
        for contact in contacts:
            tree.insert('', tk.END, values=contact)
        tree.pack(side=LEFT,padx=3, pady=3,fill=X)
        scrollbar = ttk.Scrollbar(frame1, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=LEFT,padx=3, pady=3, fill = Y)
        Label(frame1, text="").pack(side=LEFT)
        

    def Gui_Sach(self,MaSachTam,TenSachTam,TacGiaTam,NhaXuatBanTam,NamTam):
        ds=DSLK()
        MaSach=int(MaSachTam)
        Nam=int(NamTam)
        TenSach=chuyenInHoa(TenSachTam)
        TacGia=chuyenInHoa(TacGiaTam)
        NhaXuatBan=chuyenInHoa(NhaXuatBanTam)
        dstv=DSLK()
        current = self.head 
        if MaSach!=0 and Nam!=0 and TenSach!="" and TacGia!="" and NhaXuatBan!="" :
         while current!=None :
            if current.data.MaSach==MaSachTam and current.data.TuaDe==TenSach and current.data.TacGia==TacGia and current.data.NhaXuatBan==NhaXuatBan and current.data.Nam == Nam :
                ds.themSau(current.data)
                break
            current=current.link
               
        else:
            while current!=None :
             if current.data.MaSach==MaSachTam or current.data.TuaDe==TenSach or current.data.TacGia==TacGia or current.data.NhaXuatBan==NhaXuatBan or current.data.Nam == Nam :
                ds.themSau(current.data)
             current=current.link 
        ds.GUI_Book()      
            
            



def MenuSach():
    n=-1;
    dslk=DSLK();
    dslk.DocFileSach();
    while(n!=0):
        try:
            print("‘{:-^50}".format('Menu'))
            print("1:Thêm Vào Danh Sách")
            print("2:Xóa 1 Cuốn Sách")
            print("3:Sắp Xếp lại Danh Sách")
            print("4:Tìm Một Cuốn Sách ")
            print("5:Đếm Phần Tử trong Danh Sách  ")
            print("6:Xóa Tất Cả Phần Tử Trong Danh Sách ")
            print("7:Lọc dữ liệu theo tên tác giả tựa đề ")
            print("8:Xuất Danh Sách ")
            print("0:Nhap Không Để Thoát")
            n= int(input("Chọn 1 chức năng:"))   
            print();
            if(n==1):
                print("Nhập Sách Bạn Muốn thêm vào")
                a=Nhap();
                Chon=dslk.demSachTheoMS(a.MaSach);
                while Chon==0:
                    try:
                        a.MaSach=int(input("Mã Số Sinh viên đã có vui lòng nhập lại :"));
                        Chon=dslk.demSachTheoMS(a.MaSach);
                    except:
                        print("Bạn đã nhập sai");
                if(dslk.dem_PhanTu()<2):
                    dslk.themSau(a);
                else:
                    #hạm tạm để xét đúng sai giống do while
                    tam=False;#biến đúng sai
                    while(tam==False):
                        try:
                         pos=int(input("Nhập Vị trí bạn muốn thêm vào"));
                         dslk.chenTheoViTri(pos,a)
                         tam=True
                        except:
                         print("Bạn đã Nhập Sai")
            elif n==2:
                print("Nhập Sách Bạn Muốn xóa vào")
                a=Nhap();
                dslk.Xoa1PhanTu(a);
            elif n==3:
                tam=False
                while(tam==False):
                    try:
                        print("1.Sắp xếp Lớn Đến nhỏ theo mã số sách")
                        print("2.Sắp Xếp Nhỏ đến lớn theo mã số sách")
                        Chon=int(input("Chọn Cách bạn sắp xếp:"));
                        if(Chon==1):
                            dslk.SapXepTheoNhoDenLonTheoMSSach();
                        elif(Chon==2):
                            dslk.SapXepTheoLonDenNhoTheoMSSach();                     
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")
                    dslk.in_DS();

            elif n==4:
                tam=False
                while(tam==False):
                    try:
                        print("1.Tìm kiếm chính xác")
                        print("2.Tìm kiếm theo tên sách và mã số ")
                        Chon=int(input("Bạn Muốn Tìm kiếm theo phương thức nào:"));
                        if(Chon==1):
                            a=Nhap();
                            pos=dslk.timDSLK(a)
                            if(pos==None):
                                print("Không có Trong Danh Sách")
                            else:
                                print("Vị Trí của Danh Sach"+pos)
                        elif(Chon==2):
                            Ten=input("Nhập Tựa Đề hoặc mã sách sách cần tìm:");
                            dslk.timSachTheoTuaDe(Ten)
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")

            elif n==5:
                dem = dslk.dem_PhanTu()
                print(f"Số phần tử trong ds : {dem} " );
            elif n==6:
                dslk.XoaAll();
            elif n==7:
                tam=False;
                while(tam==False):
                    try:
                        print("1.Lọc dữ liệu theo tên tác giả");
                        print("2.Lọc dữ liệu theo nhà xuất bản");
                        print("3.Lọc dữ liệu theo năm");
                        Chon=int(input("Bạn Muốn Tìm kiếm theo phương thức nào:"));
                        if(Chon==1):
                            Ten=input("Nhập tên tác giả: ");
                        elif(Chon==2):
                            Ten=input("Nhập tên Nhà Xuất Bản: ");
                        elif(Chon==3):
                            strTen=input("Nhập năm:");
                            Ten=int(strTen);
                        dslk.locSachTheoGiaTri(Ten)
                        tam=True
                    except:
                        print("Bạn đã Nhập Sai")
            elif n==8:
                dslk.in_DS();
            if(n!=0):
                n=HoiTiepTuc();
            
        except:
            print("Bạn đã đã Nhập sai")
        dslk.GhiFileSach();
    return dslk;


def HoiTiepTuc():
    'Bạn có muốn tiếp tục không : (Nếu không có Nhấn phím \"0\")'
    n= int(input('Bạn có muốn tiếp tục không : (Nếu không có Nhấn phím \"0\")'))
    return n

def swap(x,y):
   temp=x
   x=y
   y=temp
   
