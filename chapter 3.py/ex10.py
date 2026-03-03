
numbers = list(map(int, input("Nhập các số, cách nhau bởi dấu cách: ").split()))

tong = 0

print("Các số chẵn trong danh sách là:")

for num in numbers:
    if num % 2 == 0:
        print(num)
        tong = tong + num
print("Tổng các số chẵn là:", tong)