print("--- HỆ THỐNG THỐNG KÊ HỌC VIÊN RIKKEI EDUCATION ---\n")

branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}")
    
    # Đặt trước khi bắt đầu đếm học viên của các lớp trong chi nhánh này
    total_students = 0 
    
    # Vòng lặp trong: Duyệt qua từng lớp của chi nhánh hiện tại
    for classroom in range(1, class_count + 1):
        student_count = int(input(f" Nhập số học viên lớp {classroom}: "))
        
        total_students += student_count
        
    print(f"=> Chi nhánh {branch}: {total_students} học viên")
