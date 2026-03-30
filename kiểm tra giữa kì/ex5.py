class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
       print("ten: ",self.name)
       print("mau: ",self.color)

# Khởi tạo đối tượng
hoa1 = Flower("Hoa hồng", "Đỏ")

hoa1.__str__()