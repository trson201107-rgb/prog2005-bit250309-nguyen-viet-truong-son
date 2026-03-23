rows = int(input("Nhập số hàng: "))
cols = int(input("Nhập số cột: "))

A = []
B = []

print("Nhập ma trận A:")
for i in range(rows):
    row = list(map(int, input().split()))
    if len(row) != cols:
        print("Lỗi nhập!")
        exit()
    A.append(row)

print("Nhập ma trận B:")
for i in range(rows):
    row = list(map(int, input().split()))
    if len(row) != cols:
        print("Lỗi nhập!")
        exit()
    B.append(row)

# cộng ma trận
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Kết quả:")
for row in C:
    print(row)