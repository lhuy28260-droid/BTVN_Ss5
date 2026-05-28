while True:
    print("\n====== MENU ======")
    print("1. Nhập dữ liệu và xem báo cáo thống kê")
    print("2. Xem hướng dẫn sử dụng")
    print("3. Thoát chương trình")
    
    menu_choice = int(input("Nhập lựa chọn của bạn (1-3): "))
    
    # BẪY 2: Bắt lỗi nhập sai Menu
    if menu_choice not in [1, 2, 3]:
        print("[!] Lựa chọn không hợp lệ. Vui lòng nhập lại từ 1 đến 3.")
        continue 
        
    if menu_choice == 3:
        print("Đang thoát chương trình. Hẹn gặp lại!")
        break
        
    elif menu_choice == 2:
        print("\n--- HƯỚNG DẪN SỬ DỤNG ---")
        print("- Chọn (1) để tiến hành nhập dữ liệu thống kê.")
        print("- Nhập số lượng chi nhánh và số lớp theo yêu cầu.")
        print("- Số lượng học viên nhập vào phải lớn hơn hoặc bằng 0.")
        
    elif menu_choice == 1:
        branch_count = int(input("\nNhập số lượng chi nhánh: "))
        class_count = int(input("Nhập số lớp học của từng chi nhánh: "))
        
        # Biến toàn cục để theo dõi chi nhánh có số học viên cao nhất
        max_students = -1
        best_branch = 0
        
        # Vòng lặp ngoài: Xử lý từng chi nhánh
        for branch in range(1, branch_count + 1):
            print(f"\n--- Chi nhánh {branch} ---")
            
            # Biến cục bộ: Reset lại khi sang chi nhánh mới
            branch_total = 0
            low_attendance_classes = [] 
            
            # Vòng lặp trong: Xử lý từng lớp
            for classroom in range(1, class_count + 1):
                
                while True:
                    student_count = int(input(f" Nhập số học viên của lớp {classroom}: "))
                    if student_count < 0:
                        print(" [Lỗi] Số học viên không hợp lệ (không được âm). Vui lòng nhập lại.")
                    else:
                        break # Hợp lệ thì phá vỡ vòng lặp xác thực
                        
                # Cộng dồn học viên cho chi nhánh
                branch_total += student_count
                
                if student_count < 10:
                    low_attendance_classes.append(str(classroom))
            
            print(f"=> Tổng số học viên của Chi nhánh {branch}: {branch_total}")
            
            # BẪY 3: Kiểm tra và in danh sách các lớp dưới 10 học viên
            if len(low_attendance_classes) == 0:
                print("=> Thông báo: Không có lớp nào dưới 10 học viên.")
            else:
                classes_str = ", ".join(low_attendance_classes)
                print(f"=> Danh sách các lớp có sĩ số dưới 10 học viên: Lớp {classes_str}")
                
            # --- TÌM CHI NHÁNH ĐÔNG NHẤT ---
            if branch_total > max_students:
                max_students = branch_total
                best_branch = branch
                
        print("\n=========== BÁO CÁO TỔNG KẾT ===========")
        print(f"Chi nhánh có tổng số học viên cao nhất là: CHI NHÁNH {best_branch}")
        print(f"Tổng số học viên đạt được: {max_students}")
        print("========================================")