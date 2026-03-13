class SinhVien:
    def __init__(self):
        self.ds = {}

    def them_sinh_vien(self, ten, diem):
        self.ds[ten] = diem

    def kiem_tra_key(self, ten):
        if ten in self.ds:
            print("Key tồn tại trong dictionary")
        else:
            print("Key không tồn tại")

# sử dụng
sv = SinhVien()

sv.them_sinh_vien("An", 8)
sv.them_sinh_vien("Binh", 7)
sv.them_sinh_vien("Chi", 9)

ten = input("Nhập tên cần kiểm tra: ")
sv.kiem_tra_key(ten)