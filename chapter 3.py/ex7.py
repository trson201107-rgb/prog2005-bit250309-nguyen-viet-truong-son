
numbers = list(map(int, input("Nhập các số, cách nhau bởi dấu cách: ").split()))
target = int(input("Nhập số cần tìm: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Tìm thấy số ở vị trí (chỉ số):", i)
        found = True
        break

if not found:
    print("Không tìm thấy số trong danh sách.")