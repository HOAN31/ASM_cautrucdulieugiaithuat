# ==========================================
# KHAI BÁO CÁC THƯ VIỆN CẦN THIẾT DÙNG CHUNG
# ==========================================
import pandas as pd # Import thư viện Pandas để xử lý dữ liệu dạng bảng (DataFrame)
import matplotlib.pyplot as plt # Import thư viện Matplotlib để vẽ biểu đồ cơ bản
import seaborn as sns # Import thư viện Seaborn để vẽ biểu đồ thống kê đẹp mắt hơn
from sklearn.datasets import load_iris, load_wine, fetch_openml # Import các hàm tải bộ dữ liệu mẫu (Iris, Wine, MNIST)
from sklearn.preprocessing import MinMaxScaler # Import công cụ chuẩn hóa dữ liệu về khoảng [0, 1]
from pandas.plotting import parallel_coordinates # Import hàm vẽ biểu đồ tọa độ song song từ Pandas
from sklearn.decomposition import PCA # Import thuật toán giảm chiều dữ liệu tuyến tính PCA
from sklearn.manifold import TSNE # Import thuật toán giảm chiều dữ liệu phi tuyến tính t-SNE


# ==========================================
# BÀI 1: TRỰC QUAN HÓA BẰNG SCATTER PLOT
# ==========================================
iris = load_iris() # Tải bộ dữ liệu hoa Iris (chứa thông số cánh hoa, đài hoa)
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names) # Chuyển dữ liệu ma trận thành bảng DataFrame với tên cột tương ứng
df_iris["species"] = iris.target # Thêm cột 'species' chứa mã số của loài hoa (0, 1, 2)
df_iris["species_name"] = df_iris["species"].map({0: "setosa", 1: "versicolor", 2: "virginica"}) # Ánh xạ mã số thành tên loài hoa thực tế để hiển thị trên chú thích (Legend)

plt.figure(figsize=(8,6)) # Tạo một khung hình (figure) mới với kích thước rộng 8, cao 6 inch
sns.scatterplot( # Gọi hàm vẽ biểu đồ phân tán (Scatter Plot) của thư viện Seaborn
    data=df_iris, # Sử dụng nguồn dữ liệu từ bảng df_iris
    x="petal length (cm)", # Trục hoành (X) biểu diễn chiều dài cánh hoa
    y="petal width (cm)", # Trục tung (Y) biểu diễn chiều rộng cánh hoa
    hue="species_name", # Tô màu các điểm dữ liệu khác nhau dựa trên tên phân lớp loài hoa
    palette="Set1" # Sử dụng bộ màu 'Set1' có sẵn của Seaborn cho các điểm chấm
)
plt.title("Bài 1: Scatter Plot (Iris Dataset)") # Đặt tiêu đề cho biểu đồ
plt.show() # Hiển thị biểu đồ hoàn chỉnh lên màn hình


# ==========================================
# BÀI 2: PHÂN TÍCH DỮ LIỆU BẰNG SCATTER MATRIX
# ==========================================
wine = load_wine() # Tải bộ dữ liệu đánh giá các loại rượu vang (Wine dataset)
df_wine = pd.DataFrame(wine.data, columns=wine.feature_names) # Đưa dữ liệu các thuộc tính của rượu vào bảng DataFrame
df_wine["target"] = wine.target # Thêm cột 'target' chứa mã phân loại rượu (0, 1, 2)

cols = ["alcohol", "malic_acid", "ash", "flavanoids", "target"] # Lập danh sách 4 thuộc tính tiêu biểu và cột nhãn để vẽ (tránh vẽ cả 13 thuộc tính sẽ rất rối)
df_wine_sub = df_wine[cols].copy() # Tạo một bảng dữ liệu con chỉ chứa các cột đã chọn
df_wine_sub["target_name"] = df_wine_sub["target"].map({0: "Class 0", 1: "Class 1", 2: "Class 2"}) # Đổi mã số thành chuỗi văn bản để làm chú thích dễ hiểu

sns.pairplot( # Gọi hàm vẽ ma trận biểu đồ phân tán (Pairplot) của Seaborn
    df_wine_sub.drop("target", axis=1), # Loại bỏ cột 'target' dạng số ra để hệ thống không vẽ nó như một thuộc tính vật lý
    hue="target_name", # Tô màu các điểm và đường cong theo nhãn tên của từng loại rượu
    diag_kind="kde", # Cài đặt các biểu đồ nằm trên đường chéo chính là biểu đồ ước lượng mật độ (KDE) thay vì dạng cột
    palette="Set2" # Sử dụng dải màu 'Set2' cho đồ thị
)
plt.suptitle("Bài 2: Scatter Matrix (Wine Dataset)", y=1.02) # Thêm tiêu đề tổng, y=1.02 giúp đẩy tiêu đề lên cao một chút tránh đè vào hình
plt.show() # Hiển thị ma trận biểu đồ lên màn hình


# ==========================================
# BÀI 3: TRỰC QUAN HÓA VỚI PARALLEL COORDINATES
# ==========================================
features = ["alcohol", "malic_acid", "ash", "alcalinity_of_ash", "magnesium", "flavanoids", "target"] # Chọn ra 6 thuộc tính của rượu vang và cột nhãn
df_wine_pc = df_wine[features].copy() # Tạo bản sao dữ liệu chứa các cột này để thao tác
        
feat_cols = features[:-1] # Lấy danh sách tên các cột thuộc tính (loại bỏ đi cột 'target' ở vị trí cuối cùng)
scaler = MinMaxScaler() # Khởi tạo công cụ chuẩn hóa Min-Max
df_wine_pc[feat_cols] = scaler.fit_transform(df_wine_pc[feat_cols]) # Áp dụng thuật toán ép tất cả các giá trị của thuộc tính về chung một thang đo [0, 1] để đồ thị không bị lệch

df_wine_pc["target_name"] = df_wine_pc["target"].map({0: "Class 0", 1: "Class 1", 2: "Class 2"}) # Đổi mã nhãn thành chuỗi để hiển thị
        
plt.figure(figsize=(10,6)) # Khởi tạo khung hình kích thước rộng 10 inch, cao 6 inch
parallel_coordinates( # Gọi hàm vẽ hệ trục tọa độ song song từ thư viện Pandas
    df_wine_pc.drop("target", axis=1), # Dữ liệu truyền vào (đã bỏ đi cột số 'target')
    "target_name", # Cột được sử dụng để phân loại và tô màu các đường gấp khúc
    colormap=plt.get_cmap("Set1") # Lấy bảng màu 'Set1' của Matplotlib
)
plt.title("Bài 3: Parallel Coordinates (Wine - Normalized)") # Cài đặt tiêu đề biểu đồ
plt.xticks(rotation=45) # Xoay các chữ nhãn trục X (tên thuộc tính) nghiêng 45 độ để chúng không đè lên nhau
plt.show() # Hiển thị biểu đồ


# ==========================================
# BÀI 4: PCA & T-SNE CHIẾU DỮ LIỆU ĐA CHIỀU
# ==========================================
X, y = fetch_openml('mnist_784', version=1, return_X_y=True, parser='auto') # Tải bộ ảnh chữ số viết tay MNIST (mỗi ảnh 28x28 pixel = 784 chiều)
X = X[:2000] # Chỉ lấy ra 2000 mẫu dữ liệu đầu tiên để thuật toán chạy nhanh, tránh treo máy tính
y = y[:2000].astype(int) # Lấy 2000 nhãn tương ứng và ép kiểu từ chuỗi (string) sang số nguyên (integer)

# --- 4A. Thuật toán PCA ---
pca = PCA(n_components=2) # Khởi tạo mô hình Phân tích thành phần chính (PCA), cấu hình giảm thẳng xuống còn 2 chiều
X_pca = pca.fit_transform(X) # Đưa 2000 mẫu (784 chiều) vào để nén và thu về ma trận mới (2 chiều)

plt.figure(figsize=(7,6)) # Tạo khung hình 7x6 inch
scatter_pca = plt.scatter( # Vẽ biểu đồ phân tán
    X_pca[:,0], # Trục hoành là cột dữ liệu số 0 (Thành phần chính 1)
    X_pca[:,1], # Trục tung là cột dữ liệu số 1 (Thành phần chính 2)
    c=y, # Đổ màu các điểm ảnh dựa theo giá trị nhãn y (các số từ 0 đến 9)
    cmap="tab10", # Dùng bộ màu 'tab10' (có 10 màu khác biệt rõ ràng)
    s=10 # Chỉnh kích thước mỗi chấm pixel nhỏ lại bằng 10
)
plt.title("Bài 4: PCA Visualization of MNIST") # Đặt tiêu đề cho đồ thị PCA
plt.xlabel("Principal Component 1") # Đặt tên cho trục X
plt.ylabel("Principal Component 2") # Đặt tên cho trục Y
plt.colorbar(scatter_pca) # Bật hiển thị thanh chú giải màu sắc ở bên phải biểu đồ
plt.show() # Hiện đồ thị PCA

# --- 4B. Thuật toán t-SNE ---
tsne = TSNE( # Khởi tạo mô hình t-SNE (t-Distributed Stochastic Neighbor Embedding)
    n_components=2, # Thiết lập số chiều dữ liệu mong muốn hạ xuống là 2
    perplexity=30, # Cài đặt hệ số perplexity (chỉ số cân bằng sự lân cận), 30 là mức khuyên dùng
    random_state=42 # Khóa hạt giống ngẫu nhiên (seed) để hình ảnh sinh ra luôn cố định ở mọi lần chạy
)
X_tsne = tsne.fit_transform(X) # Đưa 2000 mẫu vào tính toán t-SNE để thu về tọa độ 2 chiều mới

plt.figure(figsize=(7,6)) # Tạo khung hình 7x6 inch
scatter_tsne = plt.scatter( # Vẽ biểu đồ phân tán
    X_tsne[:,0], # Trục hoành là chiều thứ 1 do t-SNE tạo ra
    X_tsne[:,1], # Trục tung là chiều thứ 2 do t-SNE tạo ra
    c=y, # Đổ màu theo giá trị chữ số (0-9)
    cmap="tab10", # Sử dụng bảng 10 màu
    s=10 # Chỉnh cỡ điểm thành 10
)
plt.title("Bài 4: t-SNE Visualization of MNIST") # Đặt tiêu đề cho đồ thị t-SNE
plt.xlabel("Dimension 1") # Tên trục X
plt.ylabel("Dimension 2") # Tên trục Y
plt.colorbar(scatter_tsne) # Bật thanh màu chú thích
plt.show() # Hiện đồ thị t-SNE