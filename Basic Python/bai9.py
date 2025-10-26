# Nhập dữ liệu từ người dùng và chuyển sang số nguyên
n = int(input("Nhập một số nguyên (n): "))

# Kiểm tra điều kiện
if n > 0:
    print("Số dương")
elif n < 0:
    print("Số âm")
else: # Trường hợp còn lại là n = 0
    print("Số không")