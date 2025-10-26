class Car:
    """
    Định nghĩa lớp Car với các thuộc tính make, model, year
    và phương thức trả về thông tin.
    """
    
    def __init__(self, make, model, year):
        # Thiết lập các thuộc tính (instance attributes)
        self.make = make
        self.model = model
        self.year = year
        
    def get_info(self):
        """Trả về thông tin xe dưới dạng chuỗi: "Năm Hãng Model"."""
        return f"{self.year} {self.make} {self.model}"


car1 = Car("Toyota", "Camry", 2022)

car2 = Car("Honda", "Civic", 2024)

car3 = Car("Ford", "Mustang", 1969)

print("--- Thông tin các xe được tạo ---")

print(f"Xe 1: {car1.get_info()}")
print(f"Xe 2: {car2.get_info()}")
print(f"Xe 3: {car3.get_info()}")
