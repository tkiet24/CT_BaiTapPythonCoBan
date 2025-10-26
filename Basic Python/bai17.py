file_name = "data.txt"

student_names = [
    "Nguyen Van Hung",
    "Tran Thi Mai",
    "Le Hoang Nam",
    "Pham Duc Viet",
    "Doan Thi Thao"
]

print(f"--- Ghi {len(student_names)} tên vào '{file_name}' ---")

with open(file_name, 'w', encoding='utf-8') as file:
    for name in student_names:
        file.write(name + '\n')

print("Ghi file hoàn tất.")

print("\n" + "=" * 30 + "\n")


print(f"--- Đọc nội dung từ '{file_name}' ---")

with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())

print("Đọc file hoàn tất.")