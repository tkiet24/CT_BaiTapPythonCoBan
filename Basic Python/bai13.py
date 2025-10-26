# Định nghĩa hàm greet(name, age)
def greet(name, age):
    """
    Hàm này nhận vào tên (name) và tuổi (age) và in ra lời chào thân thiện.
    """
    print(f"Xin chào {name}, bạn {age} tuổi.")


greet("Alex", 25)

greet("Bob", 32)

greet(age=45, name="Charlie")