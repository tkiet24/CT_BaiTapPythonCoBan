student = {
  "name": "An",
  "age": 21,
  "major": "Computer Science"
}

print(f"Tên sinh viên: {student['name']}")
print("-" * 20)

student["age"] = 22
print(f"Tuổi sau khi sửa: {student['age']}")
print("-" * 20)

student["GPA"] = 3.5
print(f"Dictionary sau khi thêm GPA: {student}")
print("-" * 20)

del student["major"]

print(f"Dictionary cuối cùng: {student}")