n = int(input("Nhập một số nguyên dương n: "))

current_number = 1  
total_sum = 0       

if n < 1:
    print("Tổng chỉ được tính cho các số nguyên lớn hơn hoặc bằng 1.")
else:
    while current_number <= n:
        total_sum += current_number       
        current_number += 1
        
    print(f"Tổng các số từ 1 đến {n} là: {total_sum}")