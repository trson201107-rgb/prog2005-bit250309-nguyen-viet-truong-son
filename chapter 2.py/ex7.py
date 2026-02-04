a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
uc_ln = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        uc_ln = i

print("ƯCLN:", uc_ln)
