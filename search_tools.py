
# Chứa các thuật toán tìm kiếm.
def linear_search_order(order_list, target_id):
    """Tìm kiếm tuần tự để lấy thông tin đơn hàng theo order_id (Không phân biệt hoa thường)"""
    steps = 0
    
    # Chuyển từ khóa người dùng nhập sang chữ thường (chỉ cần làm 1 lần ở ngoài vòng lặp)
    target_lower = target_id.lower()
    
    for order in order_list:
        steps += 1
        # Chuyển order_id trong cơ sở dữ liệu sang chữ thường và so sánh
        if order["order_id"].lower() == target_lower:
            return order, steps
        
    # Nếu chạy hết vòng lặp mà không thấy 
    return None, steps

def binary_search_number(num_list, target_num):
    """Tìm kiếm nhị phân trên mảng số đã sắp xếp"""
    steps = 0
    left = 0
    right = len(num_list) - 1
    
    while left <= right:
        steps += 1
        # Đếm số chia đôi
        mid = (left + right) // 2
        # Lấy phần nguyên
        
        if num_list[mid] == target_num:
            return mid, steps
        elif num_list[mid] < target_num:
            left = mid + 1
        else:
            right = mid - 1 
            
    return -1, steps