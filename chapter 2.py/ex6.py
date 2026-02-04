def giaithua(n):
    if n == 0:
        return 1
    return n * giaithua(n - 1)

n = int(input("Nhập số: "))
print("Giai thừa:", giaithua(n))
