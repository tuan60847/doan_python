

def Nhap():
    n=False
    while(n==False):
        try:
            NhapMSSach= input("Nhap Mã Số sách :")
            MaSach=int(NhapMSSach)
            TuaDe = input("Nhap Tên Sách :")
            TuaDe = chuyenInHoa(TuaDe)
            TacGia = input("Nhap Tên tác giả :")
            TacGia = chuyenInHoa(TacGia)
            NhaXuatBan = input("Nhap tên nhà xuất bản tựa đề :")
            NhaXuatBan =chuyenInHoa(NhaXuatBan)
            #'biến kiếm thử'
            NhapNam = input("Nhap năm ra đời  :")
            Nam= int(NhapNam)
            NhapSoLuong = input("Nhap số lượng Sach:")
            SoLuong= int(NhapSoLuong)
            n=True
        except:
            print("Bạn Nhập Sai Vui lòng Nhập lại")

    b=Book(MaSach,TuaDe,TacGia,NhaXuatBan,Nam,SoLuong)
    return b
#class dsBook(object):
#    """description of class"""

#    def __init__(self,
#                list: Book = [0],
#                n: int = 0,
#                ):

#        """Hàm tạo của dsBook"""
#        self.list = list
#        self.n = n


class Book(object):
     def __init__(self,
                MaSach: int = 0,
                TuaDe: str =' ',
                TacGia: str=' ',
                NhaXuatBan: str=' ',
                Nam: int=0,
                SoLuong: int=0
                ):

        """Hàm tạo của Book"""
        self.MaSach = MaSach
        self.TuaDe = TuaDe
        self.TacGia = TacGia
        self.NhaXuatBan = NhaXuatBan
        self.Nam = int(Nam)        
        self.SoLuong= int(SoLuong)
     def __str__(self):
        return Book(self.MaSach,self.TuaDe,self.TacGia,self.NhaXuatBan,self.Nam,self.SoLuong)


     def xuat(self):
        """Xuất Sách ra"""
        #print(f"|{:^15}|{:^25}|{:^20}|{:^25}|{:^6}|{:^6}|".format({self.MaSach},{self.TuaDe},{self.TacGia},{self.NhaXuatBan},{self.Nam},{self.SoLuong}))
        print(f"|{self.MaSach:^15}|{self.TuaDe:^25}|{self.TacGia:^20}|{self.NhaXuatBan:^25}|{self.Nam:^10}|{self.SoLuong:^10}|")

     def data(self):
        """Xuất Sách ra"""
        return (f"{self.TuaDe} của {self.TacGia},Mã Sách: {self.MaSach} , {self.NhaXuatBan}, {self.Nam} còn {self.SoLuong}")


     def Repair(self):
        print("""sửa sách """)
        self.TuaDe = input("Nhap Tên tựa đề :")
        self.TacGia = input("Nhap Tên tác giả :")
        self.NhaXuatBan = input("Nhap tên nhà xuất bản tựa đề :")
        'biến kiếm thử'
        NhapNam = input("Nhap năm ra đời  :")
        self.Nam= int(NhapNam)
        NhapSoLuong = input("Nhap số lượng :")
        self.SoLuong= int(NhapSoLuong)

     def DaMuon(self):
        self.SoLuong=self.SoLuong-1
     
     def DaTra(self):
        self.SoLuong=self.SoLuong+1

            


def chuyenInHoa(x):
    a=str(x)
    x=a.upper()
    a= x
    return a