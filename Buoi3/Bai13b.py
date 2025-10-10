def tong_uoc(n):
    """Hàm tính tổng các ước số (không kể n)"""
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def la_so_thinh_vuong(n):
    """Kiểm tra số thịnh vượng"""
    return tong_uoc(n) > n

# --- Chương trình chính ---
n = int(input("Nhập số nguyên dương n: "))

if la_so_thinh_vuong(n):
    print(n, "là số thịnh vượng.")
else:
    print(n, " không phải số thịnh vượng.")