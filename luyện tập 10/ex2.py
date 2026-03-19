# Bài 2
string = input("enter your string: ")
ki_tu = input("enter your ki tu: ")
if len(ki_tu) != 1 :
    print("yeu cau nhap dung 1 ki tu!")
else:
    print("so lan ki tu xuat hien trong chuoi la: ",string.count(ki_tu))