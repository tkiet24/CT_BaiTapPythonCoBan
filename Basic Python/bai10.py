print("--- Danh sách các số từ 1 đến 10 ---")
for number in range(1, 11):
    print(number)

print("\n" + "=" * 30 + "\n")

print("--- Các số chẵn từ 1 đến 10 ---")

for number in range(1, 11):
    if number % 2 == 0:
        print(number)