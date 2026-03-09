#
arr = list(map(int, input("nhập số vào mảng(mỗi lần nhập xong sử dụng dấu cách)").split()))

for i in range(len(arr)):
    min_i = i
    for j in range(i +1 , len(arr)):
        if arr[j] > arr[min_i]:
            min_i = j
    arr[i], arr[min_i]= arr[min_i],arr[i]

print("danh sách sau khi sắp xếp là:",arr)
