def thong_ke(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)

    return tong, lon_nhat, nho_nhat


# Ví dụ
t = (3, 7, 1, 9, 4)
tong, lon_nhat, nho_nhat = thong_ke(t)

print("Tổng:", tong)
print("Lớn nhất:", lon_nhat)
print("Nhỏ nhất:", nho_nhat)