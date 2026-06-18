
from data import orders, delivery_costs, numbers, small_orders, order_weights, target_weight
from recursion_tools import recursive_sum_costs, recursive_max, reverse_string_recursive
from divide_conquer_tools import binary_search_recursive, merge_sort, merge_sort_with_steps, quick_sort, quick_sort_with_steps, merge_sort_orders_by_fee, merge_sort_orders_by_weight
from backtracking_tools import generate_order_permutations, subset_sum_orders, solve_n_queens, print_board
from complexity_report import compare_fibonacci, compare_backtracking_growth, compare_sorting_algorithms

def main():
    while True:
        # In menu tương tác
        print("\n===== POLY-SHIP ASM GD2 =====")
        print("1. Hiển thị dữ liệu mẫu")                              # Thao tác I/O cơ bản
        print("2. Tính tổng chi phí bằng đệ quy")                     # Đệ quy tuyến tính, O(n)
        print("3. Tìm giá trị lớn nhất bằng đệ quy")                  # Đệ quy tuyến tính, O(n)
        print("4. Đảo ngược chuỗi bằng đệ quy")                       # Đệ quy tuyến tính, O(n²) do cắt chuỗi
        print("5. So sánh Fibonacci thường và memoization")           # Đệ quy nhị phân O(2^n) vs Memoization O(n)
        print("6. Binary search bằng đệ quy")                         # Chia để trị, O(log n)
        print("7. Merge Sort")                                        # Chia để trị, luôn O(n log n), tốn ram O(n)
        print("8. Merge Sort có đếm số bước")                         # Chia để trị + đếm phép so sánh
        print("9. Quick Sort")                                        # Chia để trị, Pivot ở giữa tránh worst case O(n²)
        print("10. Quick Sort có đếm số bước")                        # Chia để trị + đếm phép so sánh
        print("11. Sắp xếp đơn hàng theo phí bằng Merge Sort")        # Merge Sort tùy chỉnh trên mảng Dictionary
        print("12. Sắp xếp đơn hàng theo khối lượng bằng Merge Sort") # Merge Sort tùy chỉnh trên mảng Dictionary
        print("13. Sinh hoán vị đơn hàng bằng backtracking")          # Quay lui sinh hoán vị, độ phức tạp O(n!)
        print("14. Subset Sum tải trọng đơn hàng")                    # Quay lui phân nhánh nhị phân (Chọn/Không chọn), O(2^n)
        print("15. N-Queens (In bàn cờ)")                             # Quay lui kết hợp Cắt nhánh (Pruning) bằng is_safe()
        print("16. So sánh thuật toán sắp xếp")                       # Đo lường thời gian thực thi (Benchmarking)
        print("17. So sánh tốc độ tăng của backtracking")             # Thực nghiệm chứng minh sự bùng nổ của O(n!)
        print("0. Thoát chương trình")                                # Lệnh break thoát vòng lặp while
        
        # Nhập lựa chọn
        choice = input("\nNhập số để chọn chức năng: ")
        
        # Nâng cấp: Dùng Try-Except để chống crash chương trình khi nhập sai kiểu dữ liệu
        try:
            if choice == '0':
                print("Đã thoát chương trình.")
                break
                
            elif choice == '1':
                print(f"Chi phí: {delivery_costs}\nKhối lượng: {order_weights}\nMảng số: {numbers}")
                
            elif choice == '2':
                print(f"Tổng chi phí mảng {delivery_costs} là: {recursive_sum_costs(delivery_costs)}")
                
            elif choice == '3':
                print(f"Số lớn nhất trong {numbers} là: {recursive_max(numbers)}")
                
            elif choice == '4':
                # Nâng cấp: Bỏ hardcode, cho người dùng nhập trực tiếp chuỗi
                s = input("Nhập chuỗi bạn muốn đảo ngược: ")
                print(f"Đảo ngược của '{s}' là: {reverse_string_recursive(s)}")
                
            elif choice == '5':
                compare_fibonacci()
                
            elif choice == '6':
                # Sắp xếp mảng trước khi Binary Search
                arr_sorted = sorted(numbers)
                print(f"Mảng đã sắp xếp: {arr_sorted}")
                # Nâng cấp: Bỏ hardcode, cho người dùng nhập số cần tìm (ép sang kiểu int)
                target = int(input("Nhập số cần tìm: "))
                idx = binary_search_recursive(arr_sorted, target, 0, len(arr_sorted)-1)
                print(f"Tìm số {target} ở vị trí index: {idx}")
                
            elif choice == '7':
                print(f"Mảng gốc: {numbers}\nMerge Sort: {merge_sort(numbers)}")
                
            elif choice == '8':
                arr, steps = merge_sort_with_steps([5, 1, 4, 2, 8])
                print(f"Mảng [5, 1, 4, 2, 8] -> {arr} | Số phép so sánh: {steps}")
                
            elif choice == '9':
                print(f"Mảng gốc: {numbers}\nQuick Sort: {quick_sort(numbers)}")
                
            elif choice == '10':
                arr, steps = quick_sort_with_steps([5, 1, 4, 2, 8])
                print(f"Mảng [5, 1, 4, 2, 8] -> {arr} | Số phép so sánh: {steps}")
                
            elif choice == '11':
                for o in merge_sort_orders_by_fee(orders): print(o["order_id"], o["fee"])
                
            elif choice == '12':
                for o in merge_sort_orders_by_weight(orders): print(o["order_id"], o["weight"])
                
            elif choice == '13':
                perms = generate_order_permutations(small_orders)
                print(f"Có {len(perms)} hoán vị:")
                for p in perms: print(p)
                
            elif choice == '14':
                print(f"Subset Sum (Target {target_weight}): {subset_sum_orders(order_weights, target_weight)}")
                
            elif choice == '15':
                # Nâng cấp: Cho nhập kích thước bàn cờ
                n = int(input("Nhập kích thước bàn cờ n x n (VD: 4, 5): "))
                sols = solve_n_queens(n)
                print(f"Số nghiệm N-Queens ({n}x{n}): {len(sols)}\n")
                if len(sols) > 0:
                    print("Hiển thị nghiệm ĐẦU TIÊN:")
                    # Gọi hàm in bàn cờ giao diện trực quan
                    print_board(sols[0]) 
                    
            elif choice == '16':
                compare_sorting_algorithms()
                
            elif choice == '17':
                compare_backtracking_growth()
                
            else:
                # Báo lỗi nếu nhập số ngoài danh sách menu
                print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
                
        # Bắt lỗi nếu ép kiểu int() thất bại (VD người dùng nhập chữ cái vào mục số 6, 15)
        except ValueError:
            print("Lỗi: Vui lòng nhập đúng định dạng số!")
        # Bắt các lỗi hệ thống không lường trước khác
        except Exception as e:
            print(f"Lỗi hệ thống: {e}")

# Kích hoạt hàm main nếu chạy trực tiếp
if __name__ == "__main__":
    main()