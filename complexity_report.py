
# Chứa các hàm demo đếm bước, đo thời gian chạy, in bảng so sánh.
import time
from data import orders, sorted_numbers, numbers
from search_tools import linear_search_order, binary_search_number
from sort_tools import bubble_sort_orders_by_fee

def print_report():
    print("\n" + "="*60)
    print("BÁO CÁO PHÂN TÍCH ĐỘ PHỨC TẠP THUẬT TOÁN")
    print("="*60)
    print(f"{'Thuật toán':<20} | {'Input (N)':<10} | {'Số bước':<10} | {'Thời gian (giây)'}")
    print("-" * 60)
    
    # 1. Test Linear Search (Tìm PS006 ở cuối mảng)
    start_time = time.perf_counter()
    _, steps1 = linear_search_order(orders, "PS006")
    end_time = time.perf_counter()
    time_linear = end_time - start_time
    print(f"{'Linear Search':<20} | {len(orders):<10} | {steps1:<10} | {time_linear:.8f}")

    # 2. Test Binary Search (Tìm số 90 ở cuối mảng)
    start_time = time.perf_counter()
    _, steps2 = binary_search_number(sorted_numbers, 90)
    end_time = time.perf_counter()
    time_binary = end_time - start_time
    print(f"{'Binary Search':<20} | {len(sorted_numbers):<10} | {steps2:<10} | {time_binary:.8f}")

    # 3. Test Bubble Sort (Sắp xếp đơn hàng)
    start_time = time.perf_counter()
    _, steps3 = bubble_sort_orders_by_fee(orders)
    end_time = time.perf_counter()
    time_bubble = end_time - start_time
    print(f"{'Bubble Sort (Orders)':<20} | {len(orders):<10} | {steps3:<10} | {time_bubble:.8f}")
    
    print("="*60 + "\n")