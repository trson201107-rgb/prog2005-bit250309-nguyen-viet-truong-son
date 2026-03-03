
m = int(input("Nhập số dòng (m): "))
n = int(input("Nhập số cột (n): "))

print("Nhập ma trận thứ nhất:")
A = []
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

print("Nhập ma trận thứ hai:")
B = []
for i in range(m):
    row = list(map(int, input().split()))
    B.append(row)

C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Ma trận sau khi cộng là:")
for row in C:
    print(row)