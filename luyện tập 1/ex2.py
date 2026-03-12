#**Yêu cầu**: Viết chương trình nhập hai số, tính các giá trị: lũy thừa, căn bậc 2, chia lấy phần nguyên, chia lấy phần dư, làm tròn số.
import math
a = float(input("nhập số bất kì: "))
b = float(input("nhập số bất kì: "))

luy_thua = a**b
can_bac_2 = math.sqrt(a)
chia_lay_phan_nguyen = a//b
chia_du = a%b
lam_tron = round(a)
# kêts  quả
print("kết quả của lũy thừa là: ",luy_thua)
print("kết quả của  căn bậc 2 là: ",can_bac_2)
print("kết quả của chia lấy nguyên là: ",chia_lay_phan_nguyen)
print("kết quả của chia dư là: ",chia_du)
print("kết quả của làm tròn là: ",lam_tron)

