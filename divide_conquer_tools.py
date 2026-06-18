
def binary_search_recursive(arr, target, left, right):#t
    """Tìm kiếm nhị phân bằng đệ quy"""
    # Điều kiện dừng: Biên trái vượt biên phải (không tìm thấy)
    if left > right:
        return -1
    # Tìm vị trí chính giữa
    mid = (left + right) // 2
    # Nếu phần tử ở giữa là số cần tìm
    if arr[mid] == target:
        return mid
    # Nếu phần tử ở giữa nhỏ hơn số cần tìm, tìm ở nửa bên phải
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    # Nếu phần tử ở giữa lớn hơn số cần tìm, tìm ở nửa bên trái
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

def merge(left, right):
    """Hàm gộp 2 mảng đã sắp xếp"""
    # Mảng chứa kết quả
    result = []
    # Con trỏ duyệt 2 mảng
    i = j = 0
    # Lặp khi cả 2 mảng vẫn còn phần tử
    while i < len(left) and j < len(right):
        # So sánh, đưa phần tử nhỏ hơn vào mảng kết quả
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Đưa các phần tử còn dư của mảng trái vào
    result.extend(left[i:])
    # Đưa các phần tử còn dư của mảng phải vào
    result.extend(right[j:])
    return result

def merge_sort(arr):#t
    """Thuật toán Merge Sort"""
    # Base case: Mảng có 1 hoặc 0 phần tử thì mặc định đã sắp xếp
    if len(arr) <= 1:
        return arr
    # Cắt mảng làm đôi
    mid = len(arr) // 2
    # Gọi đệ quy sắp xếp nửa trái
    left_sorted = merge_sort(arr[:mid])
    # Gọi đệ quy sắp xếp nửa phải
    right_sorted = merge_sort(arr[mid:])
    # Gộp 2 nửa lại bằng hàm merge
    return merge(left_sorted, right_sorted)

def quick_sort(arr):#t
    """Thuật toán Quick Sort"""
    # Base case
    if len(arr) <= 1:
        return arr
        
    # NÂNG CẤP: Chọn phần tử ở GIỮA làm pivot để tránh trường hợp xấu nhất O(n^2)
    mid_idx = len(arr) // 2
    pivot = arr[mid_idx]
    
    # Tạo 3 mảng để phân loại
    smaller = []
    equal = []
    greater = []
    
    # Duyệt từng số trong mảng
    for num in arr:
        if num < pivot:
            smaller.append(num) # Bỏ vào nhóm nhỏ hơn
        elif num == pivot:
            equal.append(num)   # Bỏ vào nhóm bằng
        else:
            greater.append(num) # Bỏ vào nhóm lớn hơn
            
    # Gọi đệ quy sắp xếp nhóm nhỏ, nhóm lớn và nối 3 mảng lại
    return quick_sort(smaller) + equal + quick_sort(greater)

def merge_sort_with_steps(arr):
    """Merge Sort có đếm bước so sánh"""
    if len(arr) <= 1:
        # Mảng 1 phần tử tốn 0 bước
        return arr, 0
    mid = len(arr) // 2
    # Lấy mảng con và số bước của nửa trái
    left_half, left_steps = merge_sort_with_steps(arr[:mid])
    # Lấy mảng con và số bước của nửa phải
    right_half, right_steps = merge_sort_with_steps(arr[mid:])
    
    result = []
    i = j = merge_steps = 0
    
    # Vòng lặp gộp
    while i < len(left_half) and j < len(right_half):
        # Đếm mỗi lần thực hiện so sánh
        merge_steps += 1
        if left_half[i] <= right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
            
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    # Tổng số bước = bước nửa trái + bước nửa phải + bước lúc gộp
    total_steps = left_steps + right_steps + merge_steps
    return result, total_steps

def quick_sort_with_steps(arr):
    """Quick Sort có đếm số bước so sánh"""
    if len(arr) <= 1:
        return arr, 0
        
    # NÂNG CẤP: Chọn pivot ở GIỮA
    mid_idx = len(arr) // 2
    pivot = arr[mid_idx]
    
    smaller, equal, greater = [], [], []
    steps = 0
    
    for num in arr:
        # Đếm mỗi lần so sánh số num với pivot
        steps += 1
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)
            
    # Đệ quy và nhận lại số bước
    sorted_smaller, steps_smaller = quick_sort_with_steps(smaller)
    sorted_greater, steps_greater = quick_sort_with_steps(greater)
    
    # Cộng dồn tổng số bước
    total_steps = steps + steps_smaller + steps_greater
    return sorted_smaller + equal + sorted_greater, total_steps

def merge_sort_orders_by_fee(orders):
    """Sắp xếp danh sách đơn hàng theo fee"""
    # Nâng cấp: Kiểm tra danh sách rỗng để tránh lỗi
    if not orders: return []
    # Base case
    if len(orders) <= 1: return orders
        
    mid = len(orders) // 2
    left_half = merge_sort_orders_by_fee(orders[:mid])
    right_half = merge_sort_orders_by_fee(orders[mid:])
    
    result = []
    i = j = 0
    # Gộp dựa trên value của key 'fee' trong dictionary
    while i < len(left_half) and j < len(right_half):
        if left_half[i]["fee"] <= right_half[j]["fee"]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
            
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    return result

def merge_sort_orders_by_weight(orders):
    """Sắp xếp danh sách đơn hàng theo weight"""
    # Nâng cấp: Kiểm tra danh sách rỗng để tránh lỗi
    if not orders: return []
    # Base case
    if len(orders) <= 1: return orders
        
    mid = len(orders) // 2
    left_half = merge_sort_orders_by_weight(orders[:mid])
    right_half = merge_sort_orders_by_weight(orders[mid:])
    
    result = []
    i = j = 0
    # Gộp dựa trên value của key 'weight' trong dictionary
    while i < len(left_half) and j < len(right_half):
        if left_half[i]["weight"] <= right_half[j]["weight"]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
            
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    return result