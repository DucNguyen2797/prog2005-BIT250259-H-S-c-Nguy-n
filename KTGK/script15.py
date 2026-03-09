#Bài 1 :
import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# Tìm số lớn nhất và nhỏ nhất
print("Số lớn nhất:", max(a, b, c))
print("Số nhỏ nhất:", min(a, b, c))

# Giải phương trình bậc hai
if a == 0:
    print("Không phải phương trình bậc hai")
else:
    delta = b ** 2 - 4 * a * c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)

    elif delta == 0:
        x = -b / (2 * a)
        print("Nghiệm kép x =", x)

    else:
        print("Phương trình vô nghiệm")

