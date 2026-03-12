#**Yêu cầu**: Yêu cầu người dùng nhập vào một số trong khoảng từ 1 đến 9, sau đó hiển thị bảng cửu chương của số đó từ 1 đến 9.
n = int(input("yêu cầu người dùng nhập số từ 1 đén 9: "))
if n < 1 or n > 9:
    print(" nhập số không hợp lệ! ")
else:
    for i in range (1,10):
            print(f"{i} x {n} = {i*n}")