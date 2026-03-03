
input_str = input("Nhập các số thực, cách nhau bởi dấu cách: ")

numbers = list(map(float, input_str.split()))

for i in range(1, len(numbers)):
    min = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] < min:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = min

print("Danh sách sau khi sắp xếp giảm dần:", numbers)
