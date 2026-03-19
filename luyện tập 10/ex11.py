def bai1():
    text = input("Nhập chuỗi: ")
    print("Độ dài:", len(text))


def bai2():
    text = input("Nhập chuỗi: ")
    char = input("Nhập ký tự: ")
    print("Số lần xuất hiện:", text.count(char))


def bai3():
    n = int(input("Nhập n: "))
    if n < 0:
        print("Không hợp lệ!")
        return

    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    print("Giai thừa:", factorial(n))


def bai4():
    text = input("Nhập chuỗi: ")
    rev = ""
    for c in text:
        rev = c + rev
    print("Chuỗi đảo:", rev)


def bai5():
    while True:
        pw = input("Nhập mật khẩu: ")
        if pw == "python123":
            print("Đúng!")
            break
        else:
            print("Sai, nhập lại!")


# ===== MENU =====
while True:
    print("\n===== MENU =====")
    print("1. Độ dài chuỗi")
    print("2. Đếm ký tự")
    print("3. Giai thừa (đệ quy)")
    print("4. Đảo chuỗi")
    print("5. Nhập mật khẩu")
    print("0. Thoát")

    choice = input("Chọn bài: ")

    if choice == "1":
        bai1()
    elif choice == "2":
        bai2()
    elif choice == "3":
        bai3()
    elif choice == "4":
        bai4()
    elif choice == "5":
        bai5()
    elif choice == "0":
        print("Thoát chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ!")