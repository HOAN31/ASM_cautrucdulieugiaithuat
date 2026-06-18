# Giai Đoạn 2: Đệ quy, chia để trị và backtracking cho POLY-SHIP

## 7.1. Thông tin sinh viên
- **Họ tên:** [TRƯƠNG VĂN HOÀN]
- **MSSV:** [PH64180]
- **Lớp:** [AI21302]

## 7.2. Mô tả project
Project ASM GD2 tiếp tục phát triển hệ thống thuật toán nền tảng cho POLY-SHIP, tập trung vào:
1. Đệ quy.
2. Chia để trị.
3. Merge Sort và Quick Sort.
4. Fibonacci memoization.
5. Backtracking.
6. Phân tích độ phức tạp thuật toán.

## 7.3. Cách chạy chương trình
- Bước 1: Mở terminal tại thư mục project.
- Bước 2: Chạy lệnh: `python main_assignment.py`
- Bước 3: Nhập số từ bàn phím để chọn chức năng theo menu console.

## 7.4. Danh sách chức năng đã hoàn thành
- [x] 1. Hiển thị dữ liệu mẫu
- [x] 2. Tính tổng chi phí bằng đệ quy
- [x] 3. Tìm giá trị lớn nhất bằng đệ quy
- [x] 4. Đảo ngược chuỗi bằng đệ quy
- [x] 5. So sánh Fibonacci thường và memoization
- [x] 6. Binary search bằng đệ quy
- [x] 7. Merge Sort
- [x] 8. Merge Sort có đếm số bước
- [x] 9. Quick Sort
- [x] 10. Quick Sort có đếm số bước
- [x] 11. Sắp xếp đơn hàng theo phí bằng Merge Sort
- [x] 12. Sắp xếp đơn hàng theo khối lượng bằng Merge Sort
- [x] 13. Sinh hoán vị đơn hàng bằng backtracking
- [x] 14. Subset Sum tải trọng đơn hàng
- [x] 15. N-Queens (Có in bàn cờ trực quan)
- [x] 16. So sánh thuật toán sắp xếp (Bubble vs Merge vs Quick)
- [x] 17. So sánh tốc độ tăng của backtracking

## 7.5. Bảng phân tích độ phức tạp
| Thuật toán / Hàm | Best Case | Average Case | Worst Case | Space Complexity | Ghi chú |
|---|---|---|---|---|---|
| `recursive_sum_costs` | O(n) | O(n) | O(n) | O(n) | Do call stack |
| `recursive_max` | O(n) | O(n) | O(n) | O(n) | Duyệt từng phần tử |
| `reverse_string_recursive` | O(n²) | O(n²) | O(n²) | O(n) | Phép cắt chuỗi s[1:] tốn O(n) |
| `fib_slow` | O(2^n) | O(2^n) | O(2^n) | O(n) | Tính lặp nhiều |
| `fib_memo` | O(n) | O(n) | O(n) | O(n) | Có memo |
| `binary_search_recursive` | O(1) | O(log n) | O(log n) | O(log n) | Do call stack |
| `merge_sort` | O(n log n) | O(n log n) | O(n log n) | O(n) | Stable sort |
| `quick_sort` | O(n log n) | O(n log n) | O(n²) | O(log n) | Đã tối ưu pivot ở giữa mảng |
| `generate_order_permutations` | O(n! × n) | O(n! × n) | O(n! × n) | O(n) | Nếu không tính result |
| `subset_sum_orders` | O(2^n) | O(2^n) | O(2^n) | O(n) | Bài toán Chọn/không chọn |
| `solve_n_queens` | O(n!) | O(n!) | O(n!) | O(n) | Có pruning cắt nhánh |

## 7.6. Nhận xét thuật toán
1. Đệ quy giúp code ngắn gọn nhưng bắt buộc phải có base case rõ ràng.
2. Nếu thiếu base case, chương trình sẽ rơi vào vòng lặp vô hạn và bị lỗi RecursionError.
3. Binary search đệ quy có thời gian O(log n) rất nhanh nhưng tốn thêm bộ nhớ call stack so với vòng lặp while.
4. Merge Sort có độ ổn định rất cao (luôn là O(n log n)), nhưng nhược điểm là cần thêm bộ nhớ O(n) để tạo mảng lưu trữ tạm thời khi gộp.
5. Quick Sort thường chạy rất nhanh trong thực tế, worst case O(n²) đã được hạn chế bằng cách chọn pivot ở giữa mảng thay vì cuối mảng.
6. Fibonacci memoization cải thiện tốc độ đáng kinh ngạc so với đệ quy thường nhờ việc lưu trữ các giá trị đã tính vào dictionary.

## 7.7. Nguồn tham khảo
- Slide bài giảng môn Cấu trúc dữ liệu và giải thuật (Bài 1, Bài 2, Bài 3).
- Tài liệu Python chính thức (docs.python.org) về cách sử dụng slicing và dictionary.

## 7.8. Kết luận cá nhân
Thông qua Assignment Giai đoạn 2, em đã nắm vững cách tư duy và triển khai Đệ quy, hiểu rõ bản chất của quá trình chia nhỏ bài toán bằng Divide and Conquer (đặc biệt là qua Merge Sort). Đồng thời, em đã áp dụng thành công kỹ thuật Memoization để tối ưu hóa thời gian chạy và sử dụng mô hình Choose-Explore-Unchoose trong Backtracking để giải quyết các bài toán duyệt nghiệm tổ hợp. Cấu trúc chương trình đã được cải thiện với khả năng bắt lỗi (try-except) giúp nâng cao trải nghiệm người dùng.