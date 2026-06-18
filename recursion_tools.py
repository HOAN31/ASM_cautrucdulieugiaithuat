
def recursive_sum_costs(costs, index=0):
    """Tính tổng chi phí giao hàng bằng đệ quy"""
    # Base case: Nếu chỉ số (index) chạy đến cuối danh sách
    if index == len(costs):
        # Không còn phần tử nào để cộng, trả về 0
        return 0
    # Recursive case: Lấy phần tử hiện tại cộng với tổng của các phần tử còn lại
    return costs[index] + recursive_sum_costs(costs, index + 1)

def recursive_max(arr, index=0):
    """Tìm giá trị lớn nhất trong mảng bằng đệ quy"""
    # Nếu mảng rỗng thì trả về None để tránh lỗi chương trình
    if len(arr) == 0:
        return None
        
    # Base case: Nếu chỉ số chạy đến phần tử cuối cùng của mảng
    if index == len(arr) - 1:
        # Trả về chính phần tử cuối cùng đó
        return arr[index]
    
    # Recursive case: Gọi đệ quy để tìm số lớn nhất trong phần còn lại của mảng
    max_of_rest = recursive_max(arr, index + 1)
    
    # So sánh phần tử hiện tại với số lớn nhất của phần còn lại
    if arr[index] > max_of_rest:
        # Nếu phần tử hiện tại lớn hơn, nó là số lớn nhất
        return arr[index]
    else:
        # Ngược lại, số lớn nhất nằm ở phần còn lại
        return max_of_rest

def reverse_string_recursive(s):
    """Đảo ngược chuỗi bằng đệ quy.
    *Lưu ý: Do Python dùng slicing s[1:] tạo ra chuỗi mới tốn O(n) thời gian, 
    tổng thời gian hàm này thực tế là O(n²)*
    """
    # Base case: Nếu chuỗi rỗng hoặc chỉ có 1 ký tự
    if len(s) <= 1:
        # Trả về chính chuỗi đó luôn
        return s
    # Recursive case: Đảo ngược phần đuôi chuỗi, rồi nối ký tự đầu tiên (s[0]) xuống cuối
    #String Slicing
    return reverse_string_recursive(s[1:]) + s[0]

def fib_slow(n):
    """Tính số Fibonacci theo cách đệ quy thông thường (chậm)"""
    # Xử lý ngoại lệ: Nếu đầu vào là số âm
    if n < 0:
        # Trả về chuỗi thông báo lỗi
        return "Lỗi: Đầu vào phải là số nguyên dương"
        
    # Base case: Fibonacci của 0 là 0, của 1 là 1
    if n <= 1:
        return n
    # Recursive case: Bằng tổng của 2 số Fibonacci liền trước cộng lại
    return fib_slow(n - 1) + fib_slow(n - 2)

def fib_memo(n, memo=None):
    """Tính số Fibonacci có sử dụng bộ nhớ đệm (Memoization - nhanh)"""
    # Xử lý ngoại lệ: Nếu đầu vào là số âm
    if n < 0:
        return "Lỗi: Đầu vào phải là số nguyên dương"
        
    # Nếu là lần gọi đầu tiên, khởi tạo từ điển (dictionary) để làm bộ nhớ đệm
    if memo is None:
        memo = {}
        
    # Nếu n đã được tính và lưu trong bộ nhớ đệm
    if n in memo:
        # Trả về kết quả luôn, không cần tính lại
        return memo[n]
        
    # Base case: n = 0 hoặc n = 1
    if n <= 1:
        return n
        
    # Tính toán kết quả và LƯU VÀO bộ nhớ đệm (memo) trước khi trả về
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    # Trả về kết quả vừa lưu
    return memo[n]