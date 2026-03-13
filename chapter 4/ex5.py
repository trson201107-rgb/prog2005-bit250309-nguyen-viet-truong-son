class Product:
    def __init__(self, price):
        self._price = price

    # getter
    def get_price(self):
        return self._price

    # setter
    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print("Giá phải lớn hơn 0")

    def __str__(self):
        return f"Price của product là: {self._price}"


# tạo đối tượng
p1 = Product(100)

# đổi giá
p1.set_price(200)

# in thông tin
print(p1)