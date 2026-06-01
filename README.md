# Mô tả project, cách chạy, phân tích độ phức tạp.
# Giai Đoạn 1: Quản Lý Đơn Hàng POLY-SHIP

## 1. Giới thiệu
Đây là chương trình quản lý đơn hàng đơn giản áp dụng các kiến thức cơ bản về Cấu trúc dữ liệu và Giải thuật (DSA) bằng Python. 

## 2. Cách chạy chương trình
- Đảm bảo máy bạn đã cài đặt Python 3.
- Mở terminal/command prompt tại thư mục chứa project.
- Chạy lệnh sau:
  `python main_assignment.py`

## 3. Các chức năng hiện có
- Hiển thị danh sách đơn hàng.
- Tìm kiếm đơn hàng theo mã bằng Linear Search.
- Sắp xếp đơn hàng theo phí giao hàng bằng Bubble Sort.
- Đo thời gian chạy thực tế và đếm số bước của thuật toán.

## 4. Phân tích độ phức tạp (Big-O Notation)
- **Linear Search:** Độ phức tạp thời gian là $O(n)$ do trong trường hợp xấu nhất phải duyệt qua toàn bộ $n$ phần tử trong danh sách.
- **Binary Search:** Độ phức tạp thời gian là $O(\log n)$ do sau mỗi lần lặp, không gian tìm kiếm được chia đôi.
- **Bubble Sort:** Độ phức tạp thời gian là $O(n^2)$ do sử dụng hai vòng lặp lồng nhau để so sánh và hoán vị từng cặp phần tử liền kề.