original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_evens = [number ** 2 for number in original_list if number % 2 == 0]

print(f"List ban đầu: {original_list}")
print(f"Bình phương của các số chẵn: {squared_evens}")