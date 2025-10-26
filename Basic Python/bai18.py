def safe_division():
    """
    Chương trình nhập hai số và tính thương, có xử lý lỗi.
    """
    print("--- Chương trình Tính Thương An toàn ---")
    
    # Bắt đầu khối try: nơi chứa code có khả năng gây ra lỗi
    try:
        # Nhập số tử số (numerator) và chuyển sang float
        numerator = float(input("Nhập tử số (số bị chia, x): "))
        
        # Nhập số mẫu số (denominator) và chuyển sang float
        denominator = float(input("Nhập mẫu số (số chia, y): "))
        
        # Thực hiện phép chia
        result = numerator / denominator
        
        # In kết quả nếu phép chia thành công
        print("\n--- KẾT QUẢ ---")
        print(f"Thương của {numerator} chia cho {denominator} là: {result}")
    
    # Bắt lỗi khi mẫu số là 0
    except ZeroDivisionError:
        print("\n--- LỖI ---")
        print("Lỗi: Không thể chia cho 0. Mẫu số phải khác 0.")
        
    # Bắt lỗi khi người dùng nhập chữ hoặc ký tự không phải số (cho float())
    except ValueError:
        print("\n--- LỖI ---")
        print("Lỗi: Đầu vào không hợp lệ. Vui lòng nhập giá trị số (nguyên hoặc thực).")
        
    # Khối else (Tùy chọn): Chạy nếu KHÔNG có lỗi nào xảy ra trong khối try
    else:
        print("Phép toán được thực hiện thành công.")
        
    # Khối finally (Tùy chọn): Luôn chạy, dù có lỗi hay không
    finally:
        print("Kết thúc chương trình tính thương.")

# Chạy hàm chính
safe_division()
