string = input("nhập chuỗi của bản: ")
upper = lower = digit = special = space = vowel = consonant = 0
vowels = "ueoaiUEOAI"
for i in string:
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1
    if i.isdigit():
        digit += 1
    if i.isspace():
        space += 1
    if not i.isalnum() and not i.isspace():
        special += 1
    if i in vowels:
        vowel += 1
    elif i.isalpha():
        consonant += 1

print("Chữ hoa:", upper)
print("Chữ thường:", lower)
print("Chữ số:", digit)
print("Ký tự đặc biệt:", special)
print("Khoảng trắng:", space)
print("Nguyên âm:", vowel)
print("Phụ âm:", consonant)
