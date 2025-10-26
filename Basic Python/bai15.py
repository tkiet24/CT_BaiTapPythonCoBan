def factorial(n): 
    if n == 0:
        return 1
    
    return n * factorial(n - 1)


num = int(input("Nhập một số nguyên không âm để tính giai thừa: "))

result = factorial(num)
print(f"{num}! = {result}")