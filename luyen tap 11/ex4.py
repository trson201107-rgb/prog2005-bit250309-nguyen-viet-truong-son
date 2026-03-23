
arr = [1,2,3,4,5,]
arr.append(int(input("nhap so ban muon them vao arr: ")))
print("danh sach moi: ",arr)

# nhap k
k = int(input("nhap so k bat ki: "))
print("so lan xuat hien cua so k : ",arr.count(k))

#so nguyen to
def so_nguyen_to(n):
    if n < 2 :
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
#tong so nguy to
print("tong cua so ngyen to la: ",sum(x for x in arr if so_nguyen_to(x)))

# sap xep danh sach
arr.sort()
print("danh sach sau khi sap xep la: ",arr)
#xoa ds
arr.clear()
print("danh sach da xoa! ",arr)


