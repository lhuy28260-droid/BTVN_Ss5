print("--- HỆ THỐNG NHẬP VÀ BÁO CÁO DOANH THU ---")

final_report = ""

for branch in range(1, 4):
    print(f"\n[Đang nhập liệu cho Chi nhánh {branch}]")
    
    for month in range(1, 4):
        
        revenue = input(f" - Nhập doanh thu tháng {month} (triệu đồng): ")
        
        final_report = final_report + f"Chi nhánh {branch}, tháng {month}: {revenue} triệu đồng\n"



print("\n===========================================")
print("      BÁO CÁO TỔNG HỢP")
print(final_report)
