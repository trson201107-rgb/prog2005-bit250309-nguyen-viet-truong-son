class Person:
    count = 0

    # constructor
    def __init__(self, name, age):
        if age <= 0:   # validate cách 1
            raise ValueError("Tuổi phải > 0")
        self._name = name
        self._age = age
        Person.count += 1

    # getter
    def get_name(self):
        return self._name

    # setter
    def set_age(self, age):
        if age <= 0:   # validate cách 2
            raise ValueError("Tuổi không hợp lệ")
        self._age = age

    # __str__
    def __str__(self):
        return f"{self._name} - {self._age} tuổi"

    # method thường
    def say_hello(self):
        return "Xin chào!"

    # class method
    @classmethod
    def get_count(cls):
        return cls.count

    # static method
    @staticmethod
    def is_adult(age):
        return age >= 18

    # nạp chồng ==
    def __eq__(self, other):
        return self._name == other._name and self._age == other._age



class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self._student_id = student_id

    def __str__(self):
        return f"{self._name} - {self._age} tuổi - ID: {self._student_id}"

    def study(self):
        return "Đang học bài..."

p1 = Person("An", 20)
p2 = Person("An", 20)
s1 = Student("Bình", 19, "SV01")

# in thông ti
print(p1)
print(s1)

# getter/setter
print(p1.get_name())
p1.set_age(25)
print(p1)

# method
print(p1.say_hello())
print(s1.study())

# class method
print("Số người:", Person.get_count())

# static method
print("Có phải người lớn:", Person.is_adult(17))

# so sánh
print("p1 == p2:", p1 == p2)

# test lỗi
try:
    p3 = Person("C", -1)
except ValueError as e:
    print("Lỗi:", e)