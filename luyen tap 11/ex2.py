
arr = [1, 2, 3, 4, 5]

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1

try:
    x = int(input("Nhập số cần tìm: "))
    pos = binary_search(arr, x)

    if pos != -1:
        print(f"Tìm thấy tại vị trí: {pos}")
    else:
        print("Không tìm thấy")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")