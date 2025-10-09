import math


print("Nhập tọa độ của điểm A(x,y):")
xA = int(input("Nhập x: "))
yA = int(input("Nhập y: "))

print("Nhập tọa độ của điểm B(x,y):")
xB = int(input("Nhập x: "))
yB = int(input("Nhập y: "))

d = math.sqrt(math.pow((xB - xA), 2) + math.pow((yB - yA), 2))

print("Độ dài của đoạn AB là: " , d)