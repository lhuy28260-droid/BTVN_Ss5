print("--- HỆ THỐNG QUẢN LÝ CƠ SỞ VẬT CHẤT ---")

room_count = int(input("Nhập số lượng phòng học cần kiểm tra: "))

# BẪY 1: Kiểm tra số lượng phòng không hợp lệ
if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")
else:
    # Vòng lặp ngoài: Duyệt qua từng phòng học
    for room in range(1, room_count + 1):
        print(f"\n[Đang thiết lập Phòng {room}]")
        
        row_count = int(input("Nhập số hàng ghế của phòng: "))
        seat_count = int(input("Nhập số ghế trên mỗi hàng: "))
        
        if row_count <= 0 or seat_count <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue  # Lập tức quay lại đầu vòng lặp để sang phòng tiếp theo
            
        if row_count > 10 or seat_count > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break  # Phá vỡ và thoát hẳn khỏi vòng lặp phòng học
            
        print("Sơ đồ chỗ ngồi:")
        
        # Vòng lặp duyệt từng hàng
        for row in range(row_count):
            # Vòng lặp duyệt từng ghế trong 1 hàng
            for seat in range(seat_count):
                print("*", end="")
            print()