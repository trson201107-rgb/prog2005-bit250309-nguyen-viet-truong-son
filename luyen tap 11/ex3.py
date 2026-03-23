#Viết chương trình nhận vào một danh sách số từ người dùng và in ra tất cả các số chẵn, đồng thời tính tổng của các số chẵn đó.
arr = list(map(int,input("nhap so(moi lan nhap xong hay su dung dua cach): ").split()))
num_arr = [x for x in arr if x % 2 == 0]

print("cac so chan la: ",num_arr)
print("tong cac so chan la : ",sum(num_arr))

