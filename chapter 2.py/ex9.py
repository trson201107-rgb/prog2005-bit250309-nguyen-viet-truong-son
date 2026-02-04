n = int(input("Nhập số 5 chữ số: "))
max_so = 0
while n > 0:
    so = n % 10
    if so > max_so:
        max_so = so
    n //= 10

print("Chữ số lớn nhất:", max_so)