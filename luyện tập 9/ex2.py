numbers = int(input("nhập số của bạn: "))

tong = 0

while numbers > 0:
    tong += numbers % 10
    numbers //= 10

print("Tổng các chữ số là:", tong)

