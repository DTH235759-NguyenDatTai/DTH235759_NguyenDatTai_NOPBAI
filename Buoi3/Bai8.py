import math


while True:
    a = int(input("Nhập a: "))
    x = int(input("Nhập x: "))
    if a > 0 and a != 1 and x > 0:
        break

kq = x * math.log10(a)

print(kq)