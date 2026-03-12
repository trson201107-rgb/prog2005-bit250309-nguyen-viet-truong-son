class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

sv1 = Student("linh", 8.5)
sv2 = Student("sơn", 7.0)

# in thông tin
print("Sinh viên 1:", sv1.name, "-", sv1.score)
print("Sinh viên 2:", sv2.name, "-", sv2.score)