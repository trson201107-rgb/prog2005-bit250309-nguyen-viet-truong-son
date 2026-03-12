import random
m = int(input("Nhập số hàng M: "))
n = int(input("Nhập số cột N: "))

# tạo ma trận ngẫu nhiên
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1, 100))
    matrix.append(row)

# hiển thị ma trận
print("Ma trận:")
for row in matrix:
    print(row)
# hàng
r = int(input("Nhập số hàng muốn hiển thị: "))
if 1 <= r <= m:
    print("Hàng", r, ":", matrix[r-1])
else:
    print("Hàng không hợp lệ")
# cột
c = int(input("Nhập số cột muốn hiển thị: "))
if 1 <= c <= n:
    print("Cột", c, ":")
    for i in range(m):
        print(matrix[i][c-1])
else:
    print("Cột không hợp lệ")

# tìm giá trị lớn nhất
max_value = matrix[0][0]
for i in range(m):
    for j in range(n):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]

print("Giá trị lớn nhất trong ma trận:", max_value)