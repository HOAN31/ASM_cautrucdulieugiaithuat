def bubble_sort_orders_by_fee(order_list):
    """Sắp xếp danh sách đơn hàng theo phí giao hàng (tăng dần)"""
    # Tạo bản sao để không làm hỏng dữ liệu gốc ban đầu
    arr = order_list[:] 
    n = len(arr)
    steps = 0
    
    for i in range(n):
        for j in range(0, n - i - 1):
            steps += 1 # Đếm số phép so sánh
            # So sánh phí giao hàng
            if arr[j]["fee"] > arr[j+1]["fee"]:
                # Đổi chỗ 2 phần tử
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps += 1 # Đếm số phép hoán vị (đổi chỗ)
                
    return arr, steps

def bubble_sort_numbers(num_list):
    """Sắp xếp danh sách số tăng dần"""
    arr = num_list[:]
    n = len(arr)
    steps = 0
    
    for i in range(n):
        for j in range(0, n - i - 1):
            steps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps += 1
                
    return arr, steps