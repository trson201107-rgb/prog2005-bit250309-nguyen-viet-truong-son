# Nhập 5 chuỗi
arr = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i + 1}: ")
    arr.append(s)

n = len(arr)

print("\nBắt đầu sắp xếp:\n")

for i in range(n - 1):
    for j in range(n - 1 - i):
        if len(arr[j]) < len(arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(f"Bước hoán đổi: {arr}")

print("\nKết quả cuối cùng:")
for s in arr:
    print(s, f"(độ dài: {len(s)})")