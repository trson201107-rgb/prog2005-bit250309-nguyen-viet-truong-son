mau_sac = ["red","green","orange","yellow","white"]
print("danh sách ban đầu: ",mau_sac)

try :
    mau_sac.remove("green")
    print("đã xóa màu green. ")

except ValueError:
    print("không tìm thấy green trong danh sách")

print("danh sách sau khi xử lý :",mau_sac)

