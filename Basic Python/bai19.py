import json

# Chuỗi JSON ban đầu
json_str = '{"name": "Mai", "age": 25, "city": "Hanoi"}'
print(f"Chuỗi JSON ban đầu:\n{json_str}")
print("=" * 40)

print("Chuyển JSON thành Dictionary (json.loads)")
try:
    person_dict = json.loads(json_str)

    print("\n--- Giá trị từ Dictionary ---")
    print(f"Tên: {person_dict['name']}")
    print(f"Tuổi: {person_dict['age']}")
    print(f"Thành phố: {person_dict['city']}")

    print("=" * 40)

    print("Chuyển Dictionary về JSON (json.dumps)")

    new_json_str = json.dumps(person_dict, indent=4)

    print(f"Chuỗi JSON mới:\n{new_json_str}")

except json.JSONDecodeError:
    print("Lỗi: Chuỗi JSON không hợp lệ.")
except KeyError as e:
    print(f"Lỗi: Thiếu khóa {e} trong Dictionary.")
