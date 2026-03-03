
numbers = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))

dem = 0
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            # Đổi chỗ 2 số
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

            dem = dem + 1

print("Danh sách sau khi sắp xếp:", numbers)
print("Số lần hoán đổi:", dem)