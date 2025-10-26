def describe_person(*args, **kwargs):
    print("--- Thông tin Cá nhân ---")
    
    if kwargs:
        for key, value in kwargs.items():
            print(f"- {key.title()}: {value}")
    else:
        print("Không có thông tin cá nhân nào được cung cấp.")

    print("\n--- Sở thích (Hobbies) ---")
    
    if args:
        hobbies_list = ", ".join(args)
        print(hobbies_list)
    else:
        print("Không có sở thích nào được cung cấp.")



print("Ví dụ 1: Đầy đủ thông tin")
describe_person(
    "Đọc sách", "Chơi game", "Nấu ăn", 
    name="Hải", age=28, city="Đà Nẵng", job="Designer"
)

print("\n" + "="*40 + "\n")

print("Ví dụ 2: Chỉ cung cấp sở thích")
describe_person("Chạy bộ", "Nghe nhạc")

print("\n" + "="*40 + "\n")

print("Ví dụ 3: Chỉ cung cấp thông tin cá nhân")
describe_person(
    name="Vy", city="Hồ Chí Minh"
)