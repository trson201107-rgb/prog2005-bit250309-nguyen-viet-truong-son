arr = input("Nhap ten: ").split(",")
print("Mang ban dau:", arr)

if len(arr) > 1:
    arr.pop(1)
    print("Mang sau khi xoa:", arr)
else:
    print("Khong du phan tu de xoa")

# bai 2
arr = list(map(int,input("Nhap so: ").split(",")))
dem = 0
for i in arr:
    if i % 2 != 0:
       dem += 1

       print(f"so le la: {i}")
print("tong so le la: ",dem)


# bai 3
lines = ["book 1, 30000"
         ,"book 2, 50000"
         ,"book 3, 100000"
         ,"book 4, 900000"
]
with open("book.txt", "w", endcoding ="utf-8") as f:
    for line in lines:
        f.write(line + "\n")
    print("da tao file book.txt")

# bai 4
layers = {
    "layer - 11":{
        "layer - 21": 90,
        "layer - 22":{
            "layer - 31":43
        }
    },
    "layer - 12": 35
 }
print("layer - 12",layers["layer - 12"])
print("layer - 31",layers["layer - 31"])