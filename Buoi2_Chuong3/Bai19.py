import math

x = int(input("Nhập x: "))
n = int(input("Nhập n: "))

sum = 0

def giaiThua(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * giaiThua(n - 1)

for i in range(n+1):
    sum += math.pow(x, (2 * i + 1)) /  giaiThua((2 * i + 1))

print(sum)