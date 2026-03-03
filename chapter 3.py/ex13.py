s = input("Nhập chuỗi: ")
dao_nguoc = s[::-1]

if s == dao_nguoc:
    print("Đây là chuỗi Palindrome (đối xứng).")
else:
    print("Đây không phải là chuỗi Palindrome.")