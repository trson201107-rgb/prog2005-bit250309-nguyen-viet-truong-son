n = int(input("Nhập số người: "))
d = {}

for _ in range(n):
    name = input("Tên: ")
    age = int(input("Tuổi: "))
    d[name] = age

# tuổi trung bình
avg = sum(d.values()) / len(d)
print("Tuổi trung bình:", avg)

# selection sort theo tuổi giảm dần
items = list(d.items())

for i in range(len(items)):
    max_idx = i
    for j in range(i+1, len(items)):
        if items[j][1] > items[max_idx][1]:
            max_idx = j
    items[i], items[max_idx] = items[max_idx], items[i]

print("Sau khi sắp xếp:", items)