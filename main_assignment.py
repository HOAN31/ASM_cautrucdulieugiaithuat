# File chính có menu chạy chương trình.
from data import orders
from search_tools import linear_search_order
from sort_tools import bubble_sort_orders_by_fee
from complexity_report import print_report

def display_orders(order_list):
    """Hàm in danh sách đơn hàng cho đẹp"""
    print(f"{'Mã ĐH':<8} | {'Khách hàng':<15} | {'Khu vực':<15} | {'Khối lượng':<10} | {'Phí giao'}")
    print("-" * 70)
    for o in order_list:
        print(f"{o['order_id']:<8} | {o['customer']:<15} | {o['area']:<15} | {o['weight']:<10.1f} | {o['fee']}")

def main():
    while True:
        print("\n--- HỆ THỐNG QUẢN LÝ ĐƠN HÀNG POLY-SHIP ---")
        print("1. Hiển thị danh sách đơn hàng gốc")
        print("2. Tìm kiếm đơn hàng theo Mã (Linear Search)")
        print("3. Sắp xếp đơn hàng theo Phí giao (Bubble Sort)")
        print("4. Báo cáo phân tích thuật toán")
        print("0. Thoát chương trình")
        
        choice = input("Nhập chức năng bạn muốn chọn (0-4): ")
        
        if choice == '1':
            print("\nDANH SÁCH ĐƠN HÀNG:")
            display_orders(orders)
            
        elif choice == '2':
            target = input("Nhập Mã đơn hàng cần tìm (VD: PS005): ")
            result, steps = linear_search_order(orders, target)
            if result:
                print(f"\n[Thành công] Đã tìm thấy đơn hàng sau {steps} bước!")
                display_orders([result]) # Bỏ vào list để dùng lại hàm display
            else:
                print(f"\n[Thất bại] Không tìm thấy đơn hàng {target} sau {steps} bước.")
                
        elif choice == '3':
            print("\nDANH SÁCH ĐƠN HÀNG ĐÃ SẮP XẾP THEO PHÍ GIAO HÀNG TĂNG DẦN:")
            sorted_orders, steps = bubble_sort_orders_by_fee(orders)
            display_orders(sorted_orders)
            print(f"-> Hoàn thành sắp xếp sau {steps} bước.")
            
        elif choice == '4':
            print_report()
            
        elif choice == '0':
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 0 đến 4.")

if __name__ == "__main__":
    main()