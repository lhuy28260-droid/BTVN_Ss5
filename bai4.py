print("--- HỆ THỐNG KIỂM TRA SĨ SỐ LỚP HỌC ---")

branch_count = int(input("Nhập số lượng chi nhánh: "))

# Duyệt qua từng chi nhánh
for branch in range(1, branch_count + 1):
    print(f"Chi nhánh {branch}:")
    
    for classroom in range(1, 3):
        
        # BẪY 1: Vòng lặp Validation bắt buộc người dùng nhập số >= 0
        while True:
            student_count = int(input(f"Nhập số học viên đi học của lớp {classroom}: "))
            if student_count < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
            else:
                break  # Dữ liệu hợp lệ, phá vỡ vòng lặp nhập liệu để đi tiếp
                
        # BẪY 2: Xử lý trường hợp lớp vắng toàn bộ
        if student_count == 0:
            print(f"Chi nhánh {branch} - Lớp {classroom}: Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
            continue  # Bỏ qua phần đánh giá bên dưới, lập tức nhảy sang lớp tiếp theo
            
        if student_count >= 20:
            print(f"Chi nhánh {branch} - Lớp {classroom}: Lớp học ổn định")
        else:
            print(f"Chi nhánh {branch} - Lớp {classroom}: Lớp cần được nhắc nhở theo dõi")
