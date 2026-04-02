n = int(input("nhap so: "))
print("hinh 1")
for i in range(n):
    for j in range(n):
        print("*", end = " ")
    print()
print("hinh 2")
for i in range(1,n +1):
    for j in range(i):
        print("*", end = " ")
    print()
print("hinh 3")
for i in range (n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
print("hinh 4")
for i in range(1, n + 1):
    print(" " * (n - i),end ="")
    for j in range(i):
        print("*", end = "")
    print()

print("hinh 5")
for i in range(n, 0, -1):
    print("  " * (n - i), end="")
    for j in range(i):
        print("*", end=" ")
    print()
print("hinh 6")
for i in range(1, n+1):
    print("   ", end="")

    for j in range(1, n + 2 - i):
        if i == 1:
            print("* ", end="")

        elif i == 2:
            if j == 1 or j == 3:
                print("* ", end="")
            else:
                print("  ", end="")
        elif i == 3:
            if j == 1 or j == 2:
                print("* ", end="")
            else:
                print("    ", end="")

        elif i == 4:
            if j == 1:
                print("* ", end="")

    print()
print("hinh 7")
