class Student:
    def __init__(self, name, score):
        if score < 0 or score > 10:
            print("Điểm không hợp lệ! Điểm phải nằm trong khoảng 0–10.")
        else:
            self.name = name
            self.score = score

# tạo 2 sinh viên
sv1 = Student("An", 8.5)
sv2 = Student("Bình", 11)  # điểm sai

# in thông tin sinh viên hợp lệ
if hasattr(sv1, "score"):
    print(sv1.name, "-", sv1.score)

if hasattr(sv2, "score"):
    print(sv2.name, "-", sv2.score)