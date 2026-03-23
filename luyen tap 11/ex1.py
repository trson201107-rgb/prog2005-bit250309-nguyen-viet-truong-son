#Nhập 5 chuỗi bất kỳ từ bàn phím, sử dụng insertion sort để sắp xếp đồ dài các chuỗi theo thứ tự giảm dần.
#In ra màn hình từng bước sắp xếp.
arr = []
for i in range(5):
    s = input(f'nhap chuoi cua {i + 1}:')
    arr.append(s)
print(f'ban dau: ',arr)
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    print(f'\n in tung buoc {i}:')
    while j >= 0 and len(arr[j]) < len(key):
        arr[j + 1] = arr[j]
        j -= 1
        print(f'buoc sap xep ', arr)
    arr[j + 1 ] = key
    print(f'\n sau khi chen: ',arr)

print( f'ket qua cuoi cung la:  ',arr)
