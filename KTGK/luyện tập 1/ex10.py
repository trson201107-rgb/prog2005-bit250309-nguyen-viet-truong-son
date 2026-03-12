
code = input("Mã sản phẩm: ")
name = input("Tên sản phẩm: ")
price = input("Giá: ")


f = open("products.txt", "a", encoding="utf-8")
f.write(code + ";" + name + ";" + price + "\n")
f.close()


f = open("products.txt", "r", encoding="utf-8")
products = []

for line in f:
    data = line.strip().split(";")
    products.append(data)

f.close()

print("Danh sách sản phẩm:")
for p in products:
    print(p)

products.sort(key=lambda x: float(x[2]), reverse=True)

print("\nSau khi sắp xếp theo giá giảm dần:")
for p in products:
    print(p)