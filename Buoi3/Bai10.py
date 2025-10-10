#    *
#    **
#    ***
# *******
# ***
# **
# *

# Hình phía trên
for i in range(1, 4):
    print("" * (3 - i) + "*" * i)

# Dòng giữa (hàng sao dài nhất)
print("*" * 7)

# Hình phía dưới
for i in range(3, 0, -1):
    print("*" * i)


#    *
#    **
#    * *
# *******
# * *
# **
# *


# Phần trên
for i in range(1, 4):
    if i == 1:  # dòng đầu có 1 *
        print(" " * (3) + "*")
    elif i == 2:  # dòng 2 có **
        print(" " * (3) + "**")
    else:  # dòng 3 có * *
        print(" " * (3) + "* *")

# Dòng giữa
print("*" * 7)

# Phần dưới (giảm dần)
for i in range(3, 0, -1):
    if i == 3:
        print("* *")
    elif i == 2:
        print("**")
    else:
        print("*")
