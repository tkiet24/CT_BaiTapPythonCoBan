import math

x = float(input("Nhập một số thực dương x: "))

square_root = math.sqrt(x)

ceiling_value = math.ceil(x)

print(f"Số đã nhập: {x}")
print(f"Căn bậc hai (sqrt(x)): {square_root}")
print(f"Làm tròn lên (ceil(x)): {ceiling_value}")