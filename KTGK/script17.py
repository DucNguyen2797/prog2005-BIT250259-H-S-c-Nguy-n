# Bài 4:

# Nhập số phần tử của mảng
n = int(input("Nhap N: "))

# Nhập các phần tử
a = []
for i in range(n):
    x = int(input("Nhap phan tu thu " + str(i+1) + ": "))
    a.append(x)

# Sắp xếp chọn theo thứ tự giảm dần
for i in range(0, n-1):
    max = i

    for j in range(i+1, n):
        if a[j] > a[max]:
            max = j

    # đổi chỗ
    temp = a[i]
    a[i] = a[max]
    a[max] = temp

    # in mảng sau mỗi bước
    print("Sau buoc", i+1, ":", a)

# in kết quả cuối
print("Mang sau khi sap xep giam dan:", a)
