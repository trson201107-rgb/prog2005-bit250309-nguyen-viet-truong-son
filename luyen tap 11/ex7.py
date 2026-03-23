import csv

name = input("Tên: ")
age = input("Tuổi: ")
id = input("ID: ")

# ghi file txt
with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write(f"{name}, {age}, {id}")

# ghi file csv
with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tên", "Tuổi", "ID"])
    writer.writerow([name, age, id])

print("Đã ghi file!")0