# ==========================================
# KHAI BÁO CÁC THƯ VIỆN CẦN THIẾT
# ==========================================
import pandas as pd # Thư viện thao tác, xử lý dữ liệu dạng bảng
import numpy as np # Thư viện toán học và xử lý mảng
import matplotlib.pyplot as plt # Thư viện vẽ biểu đồ cơ bản
import seaborn as sns # Thư viện vẽ biểu đồ thống kê đẹp mắt (xây dựng dựa trên matplotlib)
from sklearn.datasets import load_diabetes # Import hàm tải bộ dữ liệu bệnh tiểu đường (Diabetes)
import yfinance as yf # Thư viện tải dữ liệu giá cổ phiếu từ Yahoo Finance

# -------------------------------------------------------------------------
# CHUẨN BỊ DỮ LIỆU DÙNG CHUNG CHO BÀI 1, BÀI 3 VÀ BÀI 4
# -------------------------------------------------------------------------
diabetes = load_diabetes() # Tải bộ dữ liệu mẫu từ scikit-learn
# Đổ dữ liệu vào DataFrame, gán tên cột tương ứng với các đặc trưng y tế (age, bmi, bp,...)
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)


# ==========================================
# BÀI 1: PHÂN TÍCH PHÂN PHỐI DỮ LIỆU
# ==========================================
print("Đang chạy Bài 1...")

# Chọn 3 thuộc tính số từ dataset để đem đi phân tích phân phối
features = ['age', 'bmi', 'bp'] # age: Tuổi, bmi: Chỉ số khối cơ thể, bp: Huyết áp

# Khởi tạo một khung vẽ gồm 1 hàng và 3 cột (để chứa 3 biểu đồ kề nhau), kích thước 15x5 inch
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# --- 1. Vẽ Histogram cho thuộc tính 'bmi' lên ô vẽ đầu tiên (axes[0]) ---
# bins=20: Chia dải giá trị của bmi thành 20 cột (khoảng) đều nhau
axes[0].hist(df['bmi'], bins=20, color='skyblue', edgecolor='black')
axes[0].set_title('Histogram of BMI') # Đặt tiêu đề
axes[0].set_xlabel('BMI') # Gán nhãn trục X

# --- 2. Vẽ Density Plot (KDE) cho thuộc tính 'bp' lên ô vẽ thứ 2 (axes[1]) ---
# kdeplot: Vẽ đường cong ước lượng mật độ phân phối, fill=True: Tô màu phần diện tích dưới đường cong
sns.kdeplot(df['bp'], fill=True, ax=axes[1], color='coral')
axes[1].set_title('Density Plot of Blood Pressure')
axes[1].set_xlabel('Blood Pressure')

# --- 3. Vẽ Boxplot cho cả 3 thuộc tính lên ô vẽ thứ 3 (axes[2]) ---
# Vẽ biểu đồ hộp để xem mức độ phân tán, dải phân vị và các điểm dị thường
sns.boxplot(data=df[features], ax=axes[2], palette='pastel')
axes[2].set_title('Boxplot of Age, BMI, BP')

plt.suptitle('Bài 1: Phân tích phân phối dữ liệu', y=1.05) # Tiêu đề chung cho cả 3 đồ thị
plt.tight_layout() # Căn chỉnh tự động các ô vẽ không bị đè chữ lên nhau
plt.show()

'''
Phân tích Bài 1:
- Histogram (BMI): Biểu đồ có hình dạng gần giống quả chuông (phân phối chuẩn), phần lớn dữ liệu tập trung ở khoảng giữa (giá trị 0 do dữ liệu đã được chuẩn hóa).
- KDE (Huyết áp): Đường cong trơn mượt cho thấy mật độ dữ liệu dày đặc nhất ở mức trung bình và giảm dần về hai phía.
- Boxplot: So sánh sự phân tán. Đường nằm ngang trong các hộp là giá trị trung vị (median). Ta thấy BMI có nhiều điểm hình thoi nằm ngoài râu trên, đây chính là các giá trị ngoại lệ (outliers).
'''


# ==========================================
# BÀI 2: PHÂN TÍCH DỮ LIỆU TÀI CHÍNH
# ==========================================
print("Đang chạy Bài 2...")

ticker = "AAPL" # Cài đặt mã cổ phiếu cần phân tích (Apple Inc.)
# Gọi hàm download của yfinance để kéo dữ liệu giao dịch hàng ngày trong vòng 2 năm
stock = yf.download(ticker, start="2022-01-01", end="2024-01-01", progress=False)

# Xử lý trường hợp yfinance trả về MultiIndex (thường gặp ở phiên bản mới) để trích xuất đúng cột giá đóng cửa
if isinstance(stock.columns, pd.MultiIndex):
    close_prices = stock['Close'].iloc[:, 0] # Lấy chuỗi dữ liệu giá đóng cửa
else:
    close_prices = stock['Close']

# Tính toán các đường Trung bình động (Moving Average - MA)
# MA50: Lấy trung bình giá đóng cửa của 50 ngày gần nhất (rolling window = 50)
stock["MA50"] = close_prices.rolling(window=50).mean()
# MA200: Lấy trung bình giá đóng cửa của 200 ngày gần nhất (rolling window = 200)
stock["MA200"] = close_prices.rolling(window=200).mean()

# Bắt đầu vẽ đồ thị chứng khoán
plt.figure(figsize=(12, 6)) # Khởi tạo khung hình kích thước lớn (12x6)
# Vẽ đường biến động giá đóng cửa thực tế
plt.plot(stock.index, close_prices, label='Close Price', color='blue', alpha=0.5)
# Vẽ đường Trung bình động 50 ngày (xu hướng ngắn/trung hạn)
plt.plot(stock.index, stock["MA50"], label='50-Day MA', color='orange', linewidth=2)
# Vẽ đường Trung bình động 200 ngày (xu hướng dài hạn)
plt.plot(stock.index, stock["MA200"], label='200-Day MA', color='red', linewidth=2)

plt.title(f'Bài 2: Giá cổ phiếu {ticker} và Trung bình động (2022-2023)')
plt.xlabel('Date') # Nhãn trục hoành là Ngày tháng
plt.ylabel('Price (USD)') # Nhãn trục tung là Giá (Đô la)
plt.legend() # Hiển thị hộp chú thích (Legend) phân biệt các đường
plt.grid(True, linestyle='--', alpha=0.7) # Bật lưới tọa độ dạng nét đứt mờ để dễ nhìn giá trị
plt.show()

'''
Phân tích Bài 2:
- Đường Close Price dao động rất mạnh, thể hiện tính biến động (volatility) từng ngày của thị trường.
- Đường MA50 (màu cam) bám sát giá hơn, cho thấy xu hướng ngắn hạn.
- Đường MA200 (màu đỏ) rất mượt, chỉ ra xu hướng dài hạn. 
- Tín hiệu giao dịch cơ bản: Khi đường MA50 cắt lên trên đường MA200 ("Golden Cross"), đây thường được coi là tín hiệu xác nhận xu hướng tăng giá dài hạn. Ngược lại, nếu cắt xuống ("Death Cross") là báo hiệu xu hướng giảm.
'''


# ==========================================
# BÀI 3: PHÁT HIỆN OUTLIERS BẰNG BOXPLOT
# ==========================================
print("Đang chạy Bài 3...")

plt.figure(figsize=(10, 6)) # Mở khung hình mới kích thước 10x6
# Lọc lấy tất cả các cột dữ liệu số trong bảng (loại bỏ cột 'sex' vì giới tính là biến phân loại, vẽ Boxplot không có ý nghĩa)
numeric_features = [col for col in df.columns if col != 'sex']

# Vẽ Boxplot cho hàng loạt các thuộc tính số vừa chọn để quét tìm ngoại lệ
sns.boxplot(data=df[numeric_features], palette='Set3')

plt.title('Bài 3: Boxplot phát hiện Outliers trong bộ dữ liệu Diabetes')
plt.xticks(rotation=45) # Xoay nhãn tên các cột ở trục X nghiêng 45 độ để tránh trùng lấp chữ
plt.show()

'''
Phân tích Bài 3:
- Các điểm hình thoi (♦) nằm tách biệt phía trên hoặc phía dưới các "sợi râu" (whiskers) của hộp chính là các giá trị dị thường (Outliers).
- Trong biểu đồ này, ta dễ dàng quan sát thấy thuộc tính 'bmi', 's1', 's2', 's3', 's4', 's5', 's6' đều xuất hiện outliers.
- Ý nghĩa: Các giá trị này vượt quá xa so với phần lớn đám đông (thường là nằm ngoài khoảng 1.5 * IQR tính từ hai mép hộp). Trong y tế, điều này có thể phản ánh một số bệnh nhân có chỉ số cơ thể hoặc lượng đường huyết cao/thấp một cách cực đoan (đột biến).
'''


# ==========================================
# BÀI 4: PHÂN TÍCH MỐI QUAN HỆ BẰNG HEATMAP
# ==========================================
print("Đang chạy Bài 4...")

# Tính toán ma trận hệ số tương quan Pearson giữa tất cả các cặp thuộc tính trong DataFrame
corr_matrix = df.corr()

plt.figure(figsize=(10, 8)) # Khởi tạo khung hình vuông vức kích thước 10x8
# Sử dụng Seaborn để trực quan hóa ma trận số học này thành bản đồ nhiệt
sns.heatmap(
    corr_matrix,       # Truyền biến ma trận vào
    annot=True,        # Bật hiển thị các con số hệ số tương quan lên từng ô vuông
    fmt=".2f",         # Định dạng số chỉ lấy 2 chữ số thập phân sau dấu phẩy (ví dụ: 0.85)
    cmap="coolwarm",   # Dùng dải màu từ Lạnh (xanh dương, tương quan âm) đến Nóng (đỏ đậm, tương quan dương)
    linewidths=0.5     # Thêm đường viền trắng mỏng 0.5 pixel giữa các ô cho đẹp
)

plt.title("Bài 4: Correlation Heatmap của bộ dữ liệu Diabetes")
plt.show()

'''
Phân tích Bài 4:
- Tương quan thuận mạnh (Đỏ đậm): Cặp biến 's1' và 's2' có hệ số tương quan lên tới ~0.90. Điều này chứng tỏ hai chỉ số máu này tăng giảm gần như song hành với nhau. Tương tự với cặp 's3' và 's4' (màu xanh sẫm, tương quan âm mạnh ~-0.74).
- Ý nghĩa: Trong Học máy (Machine Learning), nếu hai biến độc lập (features) có độ tương quan quá cao với nhau (đa cộng tuyến), ta có thể cân nhắc loại bỏ bớt một biến để làm nhẹ mô hình mà không làm giảm quá nhiều sức mạnh dự đoán.
'''