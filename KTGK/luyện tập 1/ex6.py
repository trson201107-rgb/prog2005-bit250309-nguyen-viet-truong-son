s = input("Nhập chuỗi số cách nhau bởi dấu ; : ")
numbers = list(map(int, s.split(";")))

# in từng số
print("Các số trong danh sách:")
for num in numbers:
    print(num)

# đếm số chẵn
dem_chan = 0
for num in numbers:
    if num % 2 == 0:
        dem_chan += 1

# đếm số âm
dem_so_am = 0
for num in numbers:
    if num < 0:
        dem_so_am += 1

# hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# đếm số nguyên tố
count_prime = 0
for num in numbers:
    if is_prime(num):
        count_prime += 1

# tính trung bình
trung_binh = sum(numbers) / len(numbers)

# in kết quả
print("Số chẵn:", dem_chan)
print("Số âm:", dem_so_am)
print("Số nguyên tố:", count_prime)
print("Giá trị trung bình:", trung_binh)