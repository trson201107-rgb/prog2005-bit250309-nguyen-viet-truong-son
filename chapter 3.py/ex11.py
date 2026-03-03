
numbers = list(map(int, input("Nhập các số, cách nhau bởi dấu cách: ").split()))

max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("Giá trị lớn nhất là:", max_value)
print("Giá trị nhỏ nhất là:", min_value)