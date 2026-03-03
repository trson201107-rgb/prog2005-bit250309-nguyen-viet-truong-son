def count_vowels(s):
    s = s.lower()
    count = 0

    for char in s:
        if char in "aeiou":
            count += 1

    return count

text = input("Nhập chuỗi: ")


print("Số nguyên âm là:", count_vowels(text))