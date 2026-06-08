import pandas as pd  # Thư viện xử lý dữ liệu cấu trúc bảng (DataFrame)
import numpy as np  # Thư viện toán học và xử lý mảng dữ liệu nhiều chiều
import matplotlib.pyplot as plt  # Thư viện nền tảng phục vụ vẽ biểu đồ, đồ thị
import seaborn as sns  # Thư viện trực quan dữ liệu nâng cao dựa trên matplotlib
from sklearn.datasets import load_iris  # Hàm tải bộ dữ liệu mẫu hoa Iris
from sklearn.preprocessing import MinMaxScaler  # Công cụ chuẩn hóa dữ liệu về đoạn [0, 1]

# Tải dữ liệu Iris từ thư viện scikit-learn vào bộ nhớ
iris = load_iris()
# Đổ dữ liệu vào bảng Pandas DataFrame và gán tên các cột tương ứng với tên thuộc tính của hoa
df = pd.DataFrame(iris.data, columns=iris.feature_names) 

#bai1
# Tính toán ma trận hệ số tương quan tuyến tính giữa các cặp thuộc tính trong DataFrame
corr_matrix = df.corr()

# Khởi tạo khung hình vẽ biểu đồ mới với kích thước chiều rộng 8 inch, chiều cao 6 inch
plt.figure(figsize=(8,6))

# Sử dụng Seaborn để vẽ biểu đồ nhiệt (Heatmap) từ ma trận tương quan
sns.heatmap(
    corr_matrix,       # Truyền ma trận dữ liệu tương quan vào cấu trúc biểu đồ
    annot=True,        # annot=True: Bật hiển thị giá trị số tương quan cụ thể trên mỗi ô vuông
    cmap="coolwarm",   # cmap="coolwarm": Dùng dải màu từ lạnh (xanh - âm) sang nóng (đỏ - dương)
    linewidths=0.5     # linewidths=0.5: Tạo đường kẻ mỏng 0.5 pixel phân tách giữa các ô
)

# Đặt tên tiêu đề chính cho biểu đồ Heatmap vừa tạo
plt.title("Correlation Heatmap")

# Lệnh yêu cầu hệ thống hiển thị biểu đồ hoàn chỉnh lên màn hình
plt.show()

#bai2
# Khóa seed ngẫu nhiên để đảm bảo các số sinh ra ngẫu nhiên giống nhau ở mọi lần chạy code
np.random.seed(42)
# Sinh một mảng gồm 10,000 số ngẫu nhiên tuân theo phân phối chuẩn để giả lập tập dữ liệu lớn
values = np.random.randn(10000) 

# Tính độ dài một cạnh của ma trận vuông bằng căn bậc hai của tổng số phần tử rồi làm tròn lên
size = int(np.ceil(np.sqrt(len(values))))

# Tạo một mảng ban đầu chứa toàn số 0 với tổng số ô là một hình vuông (size * size)
pixel_matrix = np.zeros(size * size)

# Sao chép và điền tất cả các giá trị từ mảng dữ liệu 'values' ban đầu vào phần đầu mảng số 0
pixel_matrix[:len(values)] = values

# Tái cấu trúc mảng 1 chiều này thành mảng 2 chiều (ma trận vuông) với kích thước (size, size)
pixel_matrix = pixel_matrix.reshape(size, size)

# Tạo khung hình mới cho biểu đồ pixel với kích thước tỷ lệ vuông 6x6 inch
plt.figure(figsize=(6,6))

# Vẽ ma trận dữ liệu lên khung ảnh dưới dạng các điểm ảnh pixel màu dựa vào dải màu chỉ định
plt.imshow(pixel_matrix, cmap="viridis")

# Hiển thị thanh thước đo sắc độ màu (Colorbar) bên cạnh biểu đồ để giải nghĩa giá trị màu sắc
plt.colorbar()

# Đặt tiêu đề cho biểu đồ trực quan hóa dựa trên Pixel
plt.title("Pixel-based Visualization")

# Lệnh hiển thị biểu đồ lên màn hình
plt.show()
#bai3
# Trích xuất danh sách tên của tất cả các cột thuộc tính có trong DataFrame dữ liệu
features = df.columns.tolist() 

# Tạo một bộ chuyển đổi dữ liệu Min-Max Scaler để đưa dữ liệu về cùng một thang đo
scaler = MinMaxScaler()

# Áp dụng tính toán chuẩn hóa tất cả các giá trị thuộc tính đã chọn về khoảng từ 0 đến 1
scaled_data = scaler.fit_transform(df[features])

# Định nghĩa hàm vẽ một biểu đồ Star Glyph (biểu đồ mạng nhện) lên một ô vẽ (ax) cụ thể
def star_plot(values, label, ax):
    # Lấy tổng số lượng biến số/thuộc tính cần phải biểu diễn
    num_vars = len(values)
    
    # Chia đều vòng tròn (2*pi) thành các góc tương ứng với số biến, không lấy điểm trùng cuối
    angles = np.linspace(0, 2*np.pi, num_vars, endpoint=False)
    
    # Ghép thêm giá trị của phần tử đầu tiên vào cuối mảng dữ liệu giúp đường vẽ khép kín hình
    values = np.concatenate((values, [values[0]]))
    
    # Ghép thêm góc đầu tiên vào cuối mảng góc để điểm vẽ cuối nối về điểm xuất phát ban đầu
    angles = np.concatenate((angles, [angles[0]]))
    
    # Vẽ đường viền đa giác nối các giá trị dữ liệu trên các trục của hệ tọa độ cực (polar)
    ax.plot(angles, values)
    
    # Tô màu nền mờ cho phần diện tích nằm phía trong đa giác vừa vẽ với độ đậm nhạt alpha = 0.3
    ax.fill(angles, values, alpha=0.3)
    
    # Thiết lập tiêu đề tên mẫu cho từng biểu đồ sao nhỏ này
    ax.set_title(label)
    
    # Đặt vị trí các vạch chia góc trên vòng tròn (bỏ qua phần tử góc khép kín cuối cùng)
    ax.set_xticks(angles[:-1])
    
    # Gán tên nhãn hiển thị cho từng trục góc tương ứng (ví dụ: đặt tên trục là F1, F2, F3, F4)
    ax.set_xticklabels([f"F{i+1}" for i in range(num_vars)])

# Tạo một lưới biểu đồ gồm 1 hàng và 3 cột, đồng thời cấu hình sử dụng hệ tọa độ cực (polar=True)
fig, axes = plt.subplots(1, 3, figsize=(12, 4), subplot_kw=dict(polar=True))

# Chọn ra 3 chỉ mục (index) dòng dữ liệu ngẫu nhiên đại diện cho 3 nhóm hoa khác nhau
sample_indices = [0, 50, 100]

# Sử dụng vòng lặp để vẽ đồ thị Star Glyph lần lượt cho 3 mẫu hoa lên 3 ô biểu đồ con
for i, idx in enumerate(sample_indices):
    star_plot(scaled_data[idx], f"Sample {idx}", axes[i])

# Tự động tối ưu căn chỉnh không gian giữa các biểu đồ con để tránh hiện tượng chữ đè nhau
plt.tight_layout()

# Lệnh hiển thị nhóm biểu đồ lên màn hình
plt.show()
#bai4
# Định nghĩa hàm vẽ một khuôn mặt Chernoff tùy biến dựa vào mảng thuộc tính truyền vào
def draw_face(ax, data):
    # Chuyển đổi giá trị thuộc tính thứ 1 thành tỷ lệ kích cỡ của khuôn mặt (từ 0.5 đến 1.0)
    face_size = 0.5 + data[0] * 0.5
    # Chuyển đổi giá trị thuộc tính thứ 2 thành tỷ lệ kích thước tròng mắt (từ 0.05 đến 0.1)
    eye_size = 0.05 + data[1] * 0.05
    # Chuyển đổi giá trị thuộc tính thứ 3 thành tham số quy định độ cong của miệng cười hay mếu
    mouth_curve = data[2] - 0.5
    # Chuyển đổi giá trị thuộc tính thứ 4 thành tỷ lệ kích thước to nhỏ của mũi (từ 0.05 đến 0.1)
    nose_size = 0.05 + data[3] * 0.05

    # Khởi tạo một hình tròn làm khung viền ngoài của khuôn mặt tại tọa độ trung tâm (0.5, 0.5)
    face = plt.Circle((0.5,0.5), face_size*0.4, fill=False, linewidth=2)
    # Gắn hình tròn khuôn mặt này vào vùng ô vẽ đồ thị (ax)
    ax.add_patch(face)
    
    # Khởi tạo hình tròn đen biểu thị mắt bên trái tại vị trí tọa độ (0.35, 0.6)
    left_eye = plt.Circle((0.35,0.6), eye_size, color="black")
    # Khởi tạo hình tròn đen biểu thị mắt bên phải tại vị trí tọa độ (0.65, 0.6)
    right_eye = plt.Circle((0.65,0.6), eye_size, color="black")
    # Gắn mắt bên trái vào vùng vẽ
    ax.add_patch(left_eye)
    # Gắn mắt bên phải vào vùng vẽ
    ax.add_patch(right_eye)
    
    # Khởi tạo một hình tròn nhỏ màu đen đại diện cho mũi tại vị trí chính giữa (0.5, 0.5)
    nose = plt.Circle((0.5,0.5), nose_size, color="black")
    # Gắn chiếc mũi vừa tạo vào vùng vẽ
    ax.add_patch(nose)
    
    # Tạo một mảng gồm 100 điểm chia đều từ khoảng 0.35 đến 0.65 làm trục hoành (X) để vẽ miệng
    x = np.linspace(0.35,0.65,100)
    # Tính tọa độ trục tung (Y) theo phương trình parabol nhằm tạo độ uốn cong biểu cảm cho khuôn miệng
    y = 0.35 + mouth_curve*(x-0.5)**2 * -4
    # Thực hiện vẽ đường cong nét miệng nối từ tập hợp các điểm tọa độ (x, y) với độ dày nét là 2
    ax.plot(x,y,linewidth=2)
    
    # Giới hạn trục hoành X của ô vẽ từ 0 đến 1 để giữ cố định tỷ lệ hiển thị khuôn mặt
    ax.set_xlim(0,1)
    # Giới hạn trục tung Y của ô vẽ từ 0 đến 1 để giữ cố định tỷ lệ hiển thị khuôn mặt
    ax.set_ylim(0,1)
    # Ẩn hoàn toàn các đường trục tọa độ và các vạch thước số xung quanh để chỉ hiện khuôn mặt
    ax.axis("off")

# Chọn ra một tập hợp gồm 6 mẫu bản ghi dữ liệu khác nhau từ ma trận đã chuẩn hóa
samples = [scaled_data[0], scaled_data[10], scaled_data[50], 
           scaled_data[60], scaled_data[100], scaled_data[110]]

# Tạo lưới biểu đồ gồm 2 hàng và 3 cột (chứa đủ 6 khuôn mặt) với tổng kích thước khung là 9x6 inch
fig, axes = plt.subplots(2, 3, figsize=(9, 6))

# Duyệt qua từng ô vẽ trong lưới sau khi đã được làm phẳng mảng 2 chiều bằng hàm `.flat`
for i, ax in enumerate(axes.flat):
    # Gọi hàm vẽ biểu cảm khuôn mặt cho mẫu dữ liệu thứ i lên ô vẽ tương ứng
    draw_face(ax, samples[i])
    # Đặt tiêu đề định danh cho từng khuôn mặt dữ liệu (ví dụ: Sample 1, Sample 2,...)
    ax.set_title(f"Sample {i+1}")

# Căn chỉnh tự động khoảng cách giữa các khuôn mặt trên lưới để bố cục nhìn sạch đẹp gọn gàng
plt.tight_layout()

# Lệnh hiển thị tất cả các khuôn mặt Chernoff lên màn hình
plt.show()