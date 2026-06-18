# Khai báo thư viện tính giờ
import time
# Khai báo thư viện tạo số ngẫu nhiên
import random

# Đã xóa các import dư thừa (orders, sorted_numbers...)
from sort_tools import bubble_sort_numbers
from recursion_tools import fib_slow, fib_memo
from divide_conquer_tools import merge_sort, quick_sort
from backtracking_tools import generate_order_permutations

def compare_fibonacci():
    """So sánh tốc độ Fibonacci"""
    # In tiêu đề
    print(f"{'n':<10} | {'fib_slow':<15} | {'fib_memo':<15}")
    print("-" * 45)
    # Lặp qua các số test
    for n in [5, 10, 20, 30]:
        # Xử lý trường hợp n = 30 để máy không bị đơ
        if n == 30:
            print(f"{n:<10} | {'bỏ qua (chậm)':<15} | ", end="")
            start = time.perf_counter()
            fib_memo(n)
            end = time.perf_counter()
            print(f"{(end - start):.6f}s")
        else:
            # Đo tốc độ hàm slow
            start_slow = time.perf_counter()
            fib_slow(n)
            end_slow = time.perf_counter()
            
            # Đo tốc độ hàm memo
            start_memo = time.perf_counter()
            fib_memo(n)
            end_memo = time.perf_counter()
            
            # In ra 2 kết quả để so sánh
            print(f"{n:<10} | {(end_slow - start_slow):.6f}s{'':<6} | {(end_memo - start_memo):.6f}s")

def compare_backtracking_growth():
    """Đo lường sự bùng nổ nghiệm n! của thuật toán sinh hoán vị"""
    print("\nSo sánh tốc độ tăng của bài toán hoán vị (Backtracking):")
    print(f"{'n':<5} | {'Số hoán vị (n!)'}")
    print("-" * 25)
    for n in [3, 4, 5]:
        # Tạo mảng test
        arr = list(range(1, n + 1))
        # Sinh hoán vị
        result = generate_order_permutations(arr)
        # In ra độ dài kết quả đếm được
        print(f"{n:<5} | {len(result)}")

def compare_sorting_algorithms():
    """Chạy đua tốc độ của các thuật toán Sort"""
    print("\nSo sánh tốc độ thuật toán sắp xếp:")
    print(f"{'Thuật toán':<17} | {'Input (N)':<10} | {'Thời gian (giây)'}")
    print("-" * 50)
    
    # NÂNG CẤP: Tăng dữ liệu lên 2000 để thấy rõ tốc độ chênh lệch của O(n^2)
    arr_large = [random.randint(1, 10000) for _ in range(2000)]
    
    # Test Bubble Sort
    arr_test1 = arr_large[:] 
    start = time.perf_counter()
    bubble_sort_numbers(arr_test1)
    end = time.perf_counter()
    print(f"{'Bubble Sort':<17} | {'2000':<10} | {(end - start):.6f}s")
    
    # Test Merge Sort
    arr_test2 = arr_large[:]
    start = time.perf_counter()
    merge_sort(arr_test2)
    end = time.perf_counter()
    print(f"{'Merge Sort':<17} | {'2000':<10} | {(end - start):.6f}s")
    
    # Test Quick Sort
    arr_test3 = arr_large[:]
    start = time.perf_counter()
    quick_sort(arr_test3)
    end = time.perf_counter()
    print(f"{'Quick Sort':<17} | {'2000':<10} | {(end - start):.6f}s")
    
    # Test Python Sorted
    arr_test4 = arr_large[:]
    start = time.perf_counter()
    sorted(arr_test4)
    end = time.perf_counter()
    print(f"{'Python sorted()':<17} | {'2000':<10} | {(end - start):.6f}s")