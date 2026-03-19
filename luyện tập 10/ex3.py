def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n-1)
n = int(input("enter your number: "))
if n < 0:
    print("giai thua khong thuc hien duoc voi so am!")
else:
    print(f'ket qua cua {n} la',giai_thua(n))