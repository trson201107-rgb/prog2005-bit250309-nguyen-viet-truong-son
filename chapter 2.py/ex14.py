n = int(input("Nhập số: "))

la_nguyen_to = True

if n < 2:
    la_nguyen_to = False
else:
    for i in range(2, n):
        if n % i == 0:
            la_nguyen_to = False
            break

if la_nguyen_to:
    print("Là số nguyên tố")
else:
    print("Không phải số nguyên tố")