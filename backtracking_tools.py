
def generate_order_permutations(order_ids):#back
    """Sinh hoán vị mã đơn hàng"""
    result = []
    def backtrack(path, choices):
        # Nếu không còn lựa chọn nào, mảng path đã đầy đủ
        if len(choices) == 0:
            # Lưu bản sao của mảng path vào result
            result.append(path[:])
            return
        # Duyệt qua các lựa chọn còn lại
        for i in range(len(choices)):
            # [Choose] Chọn phần tử thứ i
            chosen = choices[i]
            path.append(chosen)
            # Tạo mảng lựa chọn mới bỏ đi phần tử vừa chọn
            new_choices = choices[:i] + choices[i+1:]
            # [Explore] Gọi đệ quy đi tiếp
            backtrack(path, new_choices)
            # [Unchoose] Xóa phần tử vừa thêm để thử cái khác
            path.pop()

    # Bắt đầu gọi đệ quy
    backtrack([], order_ids)
    return result

def subset_sum_orders(weights, target):#back
    """Tìm các tập con.
    *Lưu ý: Pruning hiện tại tối ưu cho mảng toàn số dương*
    """
    result = []
    def backtrack(index, current_path, current_sum):
        # Nếu tổng hiện tại đã bằng mục tiêu
        if current_sum == target:
            # Lưu mảng hiện tại vào kết quả
            result.append(current_path[:])
            return
            
        # Pruning: Nếu vượt quá mục tiêu hoặc đã hết mảng
        if current_sum > target or index == len(weights):
            return
            
        # Nhánh 1: CHỌN phần tử hiện tại
        current_path.append(weights[index])
        backtrack(index + 1, current_path, current_sum + weights[index])
        # Quay lui
        current_path.pop()
        
        # Nhánh 2: KHÔNG CHỌN phần tử hiện tại
        backtrack(index + 1, current_path, current_sum)

    # Bắt đầu đệ quy từ index 0, tổng = 0
    backtrack(0, [], 0)
    return result

def solve_n_queens(n):#back
    """Giải N-Queens"""
    solutions = []
    # Khởi tạo mảng bàn cờ, ban đầu toàn là -1
    board = [-1] * n 
    
    # Hàm kiểm tra xem đặt Hậu có bị ăn không
    def is_safe(board, row, col):
        # Kiểm tra với các con Hậu đã đặt ở các hàng trên
        for i in range(row):
            placed_col = board[i]
            # Trùng cột hoặc trùng đường chéo
            if placed_col == col or abs(placed_col - col) == abs(i - row):
                return False # Bị ăn
        return True # An toàn

    # Hàm đệ quy duyệt từng hàng
    def backtrack(row):
        # Nếu đã đặt hết n hàng
        if row == n:
            solutions.append(board[:])
            return
        # Thử từng cột
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col # Đặt Hậu
                backtrack(row + 1) # Đi xuống hàng tiếp theo
                board[row] = -1 # Xóa Hậu đi để thử cách khác

    backtrack(0)
    return solutions

# NÂNG CẤP: Hàm phụ trợ để in bàn cờ N-Queens
def print_board(solution):
    """In bàn cờ N-Queens ra màn hình console"""
    # Lấy kích thước bàn cờ
    n = len(solution)
    # Duyệt từng hàng
    for row in range(n):
        line = ""
        # Duyệt từng cột trong hàng đó
        for col in range(n):
            # Nếu tọa độ này là nơi đặt Hậu
            if solution[row] == col:
                line += "[Q] "  # Vẽ quân Hậu (Q)
            else:
                line += "[.] "  # Vẽ ô trống (.)
        # In hàng hiện tại ra màn hình
        print(line)
    # In một đường kẻ ngang để phân cách bàn cờ
    print("-" * (n*4))