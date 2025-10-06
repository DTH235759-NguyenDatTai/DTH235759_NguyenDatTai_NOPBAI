# Hình vuông
def square():
    for i in range(4):
        if i == 0 or i == 3:
            print("*" *4)
        else:
            print("*" + " " * 2 + "*")

square()

# Hình tam giác
def tamGiac():
    for i in range (1, 5):
        print(" " * (4 - i) + "*" * i)

tamGiac()

# Hình còn lại
for i in range(1, 4):
    if i == 1 or i == 2:
        print("*" * i)
    else:
        print("*" + " " * (i - 2) + "*")

# Phần 2: hàng sao đầy
print("*" * (4 * 2 - 1))

# Phần 3: tam giác ngược lệch phải
spaces = 4
for i in range(4, 0, -1):
    print(" " * (4 + (3 - i)) + ("*" + " " * (i - 2) + "*" if i > 1 else "*"))