from Book import chuyenInHoa
from datetime import date
def NhapMember():
    n=False
    while(n==False):
        try:
            strMaTV= input("Nhập mã số Thành viên :")
            MaTV=int(strMaTV);
            HoTen = input("Nhap Họ Tên :");
            HoTen = chuyenInHoa(HoTen);
            NhapNam = input("Nhap năm Sinh  :");
            NamSinh= int(NhapNam)
            MatKhau = input("Nhap tên mật khẩu :");
            #'biến kiếm thử'
            MuonSach=False;
            TienPhat=0
            n=True
        except:
            print("Bạn Nhập Sai Vui lòng Nhập lại")

    b=Member(MaTV,HoTen,MatKhau,NamSinh,MuonSach,TienPhat);
    return b;
#class dsBook(object):
#    """description of class"""

#    def __init__(self,
#                list: Book = [0],
#                n: int = 0,
#                ):

#        """Hàm tạo của dsBook"""
#        self.list = list
#        self.n = n;


class Member(object):
     def __init__(self,
                MaTV: int = 0,
                HoTen: str =' ',
                MatKhau: str=' ',
                NamSinh: int=0,
                MuonSach: bool=False,
                TienPhat: int= 0
                ):

        """Hàm tạo của Book"""
        self.MaTV = MaTV;
        self.HoTen = chuyenInHoa(HoTen);
        self.MatKhau = MatKhau;
        self.NamSinh = int(NamSinh);        
        self.MuonSach= bool(MuonSach);
        self.TienPhat=int(TienPhat)
     def __str__(self):
        return Member(self.MaTV,self.HoTen,self.MatKhau,self.NamSinh,self.MuonSach,self.TienPhat);


     def xuat(self):
        """Xuất Sách ra"""
        #print(f"|{:^15}|{:^25}|{:^20}|{:^25}|{:^6}|{:^6}|".format({self.MaSach},{self.TuaDe},{self.TacGia},{self.NhaXuatBan},{self.NamSinh},{self.SoLuong}))
        print(f"|{self.MaTV:^15}|{self.HoTen:^30}|{self.MatKhau:^20}|{self.NamSinh:^25}|{self.MuonSach:^11}|{self.TienPhat:^10}|")
        


     def data(self):
        """Xuất Sách ra"""
        return (f"|{self.MaTV:^15}|{self.HoTen:^30}|{self.MatKhau:^20}|{self.NamSinh:^25}|{self.MuonSach:^11}|{self.TienPhat:^10}|");


     def Repair(self):
        print("""sửa Thông tin """)
        HoTen = input("Nhap Họ Tên :");
        self.HoTen = chuyenInHoa(HoTen);
        NhapNam = input("Nhap năm Sinh  :");
        self.NamSinh= int(NhapNam)
        self.MatKhau = input("Nhap tên mật khẩu :");
     def DaMuon(self):
        self.MuonSach=True;
     def DaTra(self):
        self.MuonSach=False;
     

           
