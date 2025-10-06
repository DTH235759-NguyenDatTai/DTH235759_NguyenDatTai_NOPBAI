import math
print("Nhập 3 cạnh của tam giác:")
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

if( a <= 0 or b <= 0 or c <=0
   or (a + b) <= c or (a + c) < b or (b + c) <= a):
    print("Tam giác không hợp lệ!")
else:
    p = (a + b + c) / 2
    dt = math.sqrt(p * (p - a) * (p - b) * (p - c))

print("Diện tích tam giác là: ", dt) 
