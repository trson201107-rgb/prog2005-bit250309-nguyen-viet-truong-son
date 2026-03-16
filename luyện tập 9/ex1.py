#Ví dụ: nếu `weight = 60kg` và height = `1.65m → BMI ≈ 22.04`
weight = float(input("nhập cân nặng cảu bạn: "))
height = float(input("nhập chiều cao của bạn: "))
BMI =  weight / (height * height)
print("BMI của bạn là: ",round(BMI,2))