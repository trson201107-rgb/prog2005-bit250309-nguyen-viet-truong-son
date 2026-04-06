# bai 1
R = int(input("nhap ban kinh: "))
Pi = 3.14
chu_vi = 2*Pi*R
print("chu vi cua hinh tron la: ",chu_vi)


# bai 2
a = int(input("nhap so a: "))
b = int(input("nhap so b: "))
tong = a + b
hieu = a - b
tich = a * b
print("tong cua 2 so la: ",tong)
print("hieu cua 2 so la: ",hieu)
print("tich cua 2 so la: ",tich)

# bai3

class Book :
    def __init__(self,name,price):
        self.name = name
        self.price = price

    class Book:
        def __init__(self, name, price):
            self.name = name
            self.price = price
        # getter
        def get_name(self):
            return self.name

        def get_price(self):
            return self.price

    # Khởi tạo đối tượng
    book1 = Book("dayj con lam giau", 90000)
    print(book1.get_price())
