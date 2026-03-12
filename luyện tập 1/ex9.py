class Student:
    def __init__(self, name, score):
        if score < 0 or score > 10:
            print("Điểm không hợp lệ! Điểm phải nằm trong khoảng 0–10.")
        else:
            self.name = name
            self.score = score

    def display(self):
        print(f"Sinh viên {self.name} có điểm là {self.score}")

sv1 = Student("A", 10)
sv2 = Student("B", 8)

sv1.display()
sv2.display()