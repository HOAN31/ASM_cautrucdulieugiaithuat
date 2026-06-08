# ==========================================
# KHAI BÁO THƯ VIỆN VÀ TẢI DỮ LIỆU
# ==========================================
import pandas as pd # Thư viện xử lý dữ liệu dạng bảng
import numpy as np # Thư viện toán học và xử lý mảng
import matplotlib.pyplot as plt # Thư viện vẽ biểu đồ
import seaborn as sns # Thư viện vẽ biểu đồ thống kê nâng cao
from scipy import stats # Thư viện toán thống kê (dùng để tính Z-score)
from sklearn.preprocessing import StandardScaler # Hàm chuẩn hóa dữ liệu (Standardization)

# Tải bộ dữ liệu Titanic có sẵn trong seaborn
df = sns.load_dataset('titanic')


# ==========================================
# BÀI 1: KHÁM PHÁ DỮ LIỆU BAN ĐẦU (EDA)
# ==========================================
print("================= BÀI 1 =================")
print("--- 1. Hiển thị 10 dòng đầu tiên ---")
print(df.head(10)) 

print("\n--- 2. Số lượng bản ghi và thuộc tính ---")
print(f"Số dòng (bản ghi): {df.shape[0]}") 
print(f"Số cột (thuộc tính): {df.shape[1]}") 

print("\n--- 3. Kiểu dữ liệu của từng cột ---")
print(df.dtypes) 

print("\n--- 4. Tính toán các thống kê cơ bản ---")
print(df.describe()) 

# --- 5. Trực quan hóa dữ liệu ---
fig1, axes1 = plt.subplots(1, 2, figsize=(12, 5)) 

# a. Histogram cho thuộc tính số (Cột 'age' - Tuổi)
sns.histplot(data=df, x='age', bins=20, kde=True, ax=axes1[0], color='skyblue') 
axes1[0].set_title('Histogram of Age (Thuộc tính số)') 

# b. Bar chart cho thuộc tính phân loại (Cột 'class' - Hạng vé)
sns.countplot(data=df, x='class', ax=axes1[1], palette='Set2') 
axes1[1].set_title('Bar Chart of Passenger Class (Thuộc tính phân loại)') 

plt.tight_layout() 
plt.show() 


# ==========================================
# BÀI 2: LÀM SẠCH DỮ LIỆU
# ==========================================
print("\n================= BÀI 2 =================")
print("--- 1. Kiểm tra dữ liệu bị thiếu ---")
print(df.isnull().sum()) 

# --- Vẽ Boxplot TRƯỚC khi làm sạch (Dùng cột 'age' làm ví dụ) ---
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1) 
sns.boxplot(y=df['age'], color='lightcoral') 
plt.title("Boxplot Age: TRƯỚC khi làm sạch")

# --- 2. Xử lý dữ liệu thiếu ---
age_median = df['age'].median() # Tính trung vị
df['age'] = df['age'].fillna(age_median) # Lấp đầy các ô NaN bằng trung vị
df = df.dropna(subset=['embarked']) # Xóa bản ghi nếu cột 'embarked' bị thiếu

# --- 3. Kiểm tra và loại bỏ bản ghi trùng lặp ---
print(f"Số bản ghi trùng lặp trước khi xóa: {df.duplicated().sum()}") 
df = df.drop_duplicates() 

# --- 4. Chuẩn hóa dữ liệu số (Standardization) ---
scaler = StandardScaler() 
df['age_scaled'] = scaler.fit_transform(df[['age']]) 

# --- Vẽ Boxplot SAU khi làm sạch và chuẩn hóa ---
plt.subplot(1, 2, 2) 
sns.boxplot(y=df['age_scaled'], color='lightgreen') 
plt.title("Boxplot Age: SAU khi làm sạch (Scaled)")

plt.tight_layout()
plt.show() 


# ==========================================
# BÀI 3: PHÁT HIỆN OUTLIERS (Ngoại lệ)
# ==========================================
print("\n================= BÀI 3 =================")
# --- 1. Phương pháp IQR (Kiểm tra trên cột 'fare') ---
Q1 = df['fare'].quantile(0.25) 
Q3 = df['fare'].quantile(0.75) 
IQR = Q3 - Q1 
lower_bound = Q1 - 1.5 * IQR 
upper_bound = Q3 + 1.5 * IQR 

outliers_iqr = df[(df['fare'] < lower_bound) | (df['fare'] > upper_bound)]
print(f"Số lượng Outliers theo phương pháp IQR (cột Fare): {len(outliers_iqr)}")

# --- 2. Phương pháp Z-score ---
z_scores = np.abs(stats.zscore(df['fare']))
outliers_zscore = df[z_scores > 3]
print(f"Số lượng Outliers theo phương pháp Z-score (cột Fare): {len(outliers_zscore)}")

# --- 3. Trực quan hóa Outliers ---
fig3, axes3 = plt.subplots(1, 2, figsize=(12, 5))

# a. Boxplot thể hiện outliers
sns.boxplot(x=df['fare'], ax=axes3[0], color='orange') 
axes3[0].set_title('Boxplot of Fare (Nhiều điểm đen là Outliers)')

# b. Scatter plot (so sánh Tuổi và Giá vé)
sns.scatterplot(data=df, x='age', y='fare', ax=axes3[1], color='purple', alpha=0.6)
axes3[1].set_title('Scatter Plot: Age vs Fare')

plt.tight_layout()
plt.show()

# --- 4. Phân tích ảnh hưởng của Outliers ---
print("\n--- Phân tích ảnh hưởng của Outliers đối với mô hình Học máy ---")
print("- Làm lệch trọng tâm: Outliers kéo giá trị trung bình lệch hẳn về một phía.")
print("- Ảnh hưởng hàm mất mát: Làm tăng sai số (MSE) trong hồi quy tuyến tính.")
print("- Suy giảm độ chính xác: Các thuật toán khoảng cách (KNN, K-Means) rất nhạy cảm và dễ phân cụm sai.")


# ==========================================
# BÀI 4: VẼ SƠ ĐỒ QUY TRÌNH KHOA HỌC DỮ LIỆU
# ==========================================
# Danh sách các bước trong quy trình
steps = [
    "1. Thu thập dữ liệu\n(Data Collection)",
    "2. Làm sạch dữ liệu\n(Data Cleaning)",
    "3. Khám phá dữ liệu\n(EDA)",
    "4. Trích xuất đặc trưng\n(Feature Engineering)",
    "5. Huấn luyện mô hình\n(Model Training)",
    "6. Đánh giá mô hình\n(Model Evaluation)"
]

fig, ax = plt.subplots(figsize=(6, 8)) 
ax.axis('off') # Tắt các trục tọa độ

# Lặp qua từng bước để vẽ các khối hộp và mũi tên
for i, step in enumerate(steps):
    y_pos = 0.9 - i * 0.15 
    
    # Vẽ hộp chứa chữ
    ax.text(0.5, y_pos, step, ha='center', va='center', fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.8', facecolor='lightblue', edgecolor='blue', linewidth=2))
    
    # Vẽ mũi tên chỉ xuống
    if i < len(steps) - 1:
        ax.annotate('', 
                    xy=(0.5, y_pos - 0.05), 
                    xytext=(0.5, y_pos - 0.10), 
                    arrowprops=dict(arrowstyle='->', lw=2, color='gray')) 

plt.title("SƠ ĐỒ CÁC BƯỚC PHÁT TRIỂN MÔ HÌNH", fontsize=14, fontweight='bold', y=1.0) 
plt.show()