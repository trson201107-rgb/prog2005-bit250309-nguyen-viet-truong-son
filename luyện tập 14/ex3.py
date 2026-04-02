n = 4
print("Hình 1:")
for i in range(n):
    print("1   " * n)

print("\nHình 2:")
for i in range(n):
    for j in range(1, n + 1):
        print(j, end="   ")
    print()
print("\nHình 3:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="   ")
    print()

print("\nHình 4:")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="   ")
    print()

print("\nHình 5:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print(j, end="   ")
        else:
            print(" ", end="   ")
    print()

print("\nHình 6:")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print(j, end="   ")
        else:
            print(" ", end="   ")
    print()
print("\nHình 7:")
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    print((str(i) + "   ") * i)

print("\nHình 8:")
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

print("\nHình 9:")
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    if i == n:
        for j in range(1, n + 1): print(j, end=" ")
        for j in range(n - 1, 0, -1): print(j, end=" ")
    else:
        print("1", end="")
        if i > 1:
            print("  " * (2 * i - 3), end=" 1")
    print()
print("\nHình 10 (Tam giác số ngược):")
for i in range(n, 0, -1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()