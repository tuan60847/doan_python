from Book import chuyenInHoa
from datetime import date
def NhapQLDSMuonTra():
    n=False
    while(n==False):
        try:
            strMaMuonTra= input("Nhập mã số Quản lý sách :")
            MaMuonTra=int(strMaMuonTra)
            strMaTV= input("Nhập mã số Thành viên :")
            MaTV=int(strMaTV)
            HoTen = input("Nhap Họ Tên :")
            HoTen = chuyenInHoa(HoTen)
            NhapMSSach= input("Nhap Mã Số sách :")
            MaSach=int(NhapMSSach)
            TuaDe = input("Nhap Tên Sách :")
            TuaDe = chuyenInHoa(TuaDe)
            #hanoi_tz = datetime.timezone(datetime.timedelta(hours=7))
            NgayMuon = date.today()
            DangMuon=False
            n=True
        except:
            print("Bạn Nhập Sai Vui lòng Nhập lại")
    a=QuanLyMuonTra(MaMuonTra,MaTV,HoTen,MaSach,TuaDe,NgayMuon,DangMuon)
    return a


def NhapQLDSMuon():
    n=False
    while(n==False):
        try:
            strMaMuonTra= input("Nhập mã số Quản lý sách :")
            MaMuonTra=int(strMaMuonTra)
            strMaTV= input("Nhập mã số Thành viên :")
            MaTV=int(strMaTV)
            HoTen = input("Nhap Họ Tên :")
            HoTen = chuyenInHoa(HoTen)
            NhapMSSach= input("Nhap Mã Số sách :")
            MaSach=int(NhapMSSach)
            TuaDe = input("Nhap Tên Sách :")
            TuaDe = chuyenInHoa(TuaDe)
            #hanoi_tz = datetime.timezone(datetime.timedelta(hours=7))
            strNgay= input("Nhập Ngày :")
            Ngay=int(strNgay)
            strThang= input("Nhập Tháng :")
            Thang=int(strThang)
            strNam= input("Nhập Năm:")
            Nam=int(strNam)
            NgayMuon = date(Nam,Thang,Ngay)
            DangMuon=False
            n=True
        except:
            print("Bạn Nhập Sai Vui lòng Nhập lại")
    a=QuanLyMuonTra(MaMuonTra,MaTV,HoTen,MaSach,TuaDe,NgayMuon,DangMuon)
    return a
class QuanLyMuonTra(object):
     def __init__(self,
                MaMuonTra: int = 0,
                MaTV: int = 0,
                HoTen: str =' ',
                MaSach: int=0,
                TuaDe: str=' ',
                NgayMuon: date=date.today(),
                DangMuon: bool=False
                ):

        """Hàm tạo của Book"""
        self.MaMuonTra  = int(MaMuonTra)
        self.MaTV = int(MaTV)
        self.HoTen = HoTen
        self.MaSach = int(MaSach)
        self.TuaDe = TuaDe
        self.NgayMuon=NgayMuon
        self.DangMuon= bool(DangMuon)
        
     def __str__(self):
        return QuanLyMuonTra(self.MaMuonTra,self.MaTV,self.HoTen,self.MaSach,self.TuaDe,self.NgayMuon,self.DangMuon)


     def xuatQL(self):
        """Xuất Sách ra"""
        #print(f"|{:^15}|{:^25}|{:^20}|{:^25}|{:^6}|{:^6}|".format({self.MaSach},{self.TuaDe},{self.TacGia},{self.NhaXuatBan},{self.Nam},{self.SoLuong}))
        print(f"""|{self.MaMuonTra:^15}|{self.MaTV:^15}|{self.HoTen:^30}|{self.MaSach:^15}|{self.TuaDe:^25}|{self.NgayMuon.strftime("%d/%m/%Y"):^10}|{self.DangMuon:^11}|""")
        


     def data(self):
        """Xuất Sách ra"""
        return (f"|{self.MaMuonTra:^5}|{self.MaTV:^15}|{self.HoTen:^30}|{self.MaSach:^15}|{self.TuaDe:^25}||{self.NgayMuon:^15}|{self.DangMuon:^11}|")

     def DaTra(self):
         self.DangMuon=True



