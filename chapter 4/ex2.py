class SinhVien:
    def __init__(self):
        self.ds = {}   # dictionary lưu tên và điểm

    def them_sinh_vien(self, ten, diem):
        self.ds[ten] = diem

    def tinh_diem_trung_binh(self):
        tong = sum(self.ds.values())
        return tong / len(self.ds)

# sử dụng
sv = SinhVien()

sv.them_sinh_vien("An", 8)
sv.them_sinh_vien("Binh", 7)
sv.them_sinh_vien("Chi", 9)

print("Điểm trung bình:", sv.tinh_diem_trung_binh())