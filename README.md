# Hệ Thống Dự Đoán Bệnh Tiểu Đường

Một dự án machine learning sử dụng mô hình Random Forest để dự đoán nguy cơ mắc bệnh tiểu đường dựa trên các chỉ số sức khỏe và lối sống. Dự án sử dụng dữ liệu từ Hệ thống Giám sát Yếu tố Nguy cơ Hành vi (BRFSS) của CDC năm 2015.

## Tổng Quan

Dự án này xây dựng một hệ thống dự đoán bệnh tiểu đường thông qua việc phân tích các yếu tố nguy cơ sức khỏe và hành vi. Hệ thống cung cấp giao diện web cho phép người dùng nhập các chỉ số sức khỏe và nhận kết quả dự đoán.

## Tính Năng

- Giao diện web tương tác
- Sử dụng mô hình Random Forest với độ chính xác khoảng 75%
- Phân tích đa yếu tố bao gồm:
  - Huyết áp
  - Chỉ số cholesterol
  - Chỉ số BMI
  - Hoạt động thể chất
  - Thói quen sinh hoạt
  - Tiền sử bệnh
  - Các yếu tố nhân khẩu học

## Công Nghệ Sử Dụng

- Python 3.x
- scikit-learn (RandomForest, GridSearchCV)
- pandas
- Flask
- HTML/CSS

## Cấu Trúc Dự Án
├── Data/ │ └── diabetes_2015.csv # Dữ liệu từ BRFSS ├── templates/ │ ├── home.html # Giao diện nhập liệu │ ├── after.html # Giao diện kết quả │ └── style.css # File CSS ├── model.ipynb # Notebook phát triển mô hình ├── app.py # Ứng dụng Flask └── README.md


## Cài Đặt và Sử Dụng

1. Clone repository
2. Cài đặt các thư viện cần thiết:
```bash
pip install pandas numpy scikit-learn flask
```
3. Chạy ứng dụng Flask:
```bash
python app.py
```
4. Truy cập localhost để sử dụng

Chi Tiết Mô Hình
Thuật toán: Random Forest Classifier
Độ chính xác: ~75%
Các metric đánh giá:
F1-score
Precision
Recall
Accuracy
Tối ưu hóa thông qua GridSearchCV
Nguồn Dữ Liệu
Dataset từ CDC's Behavioral Risk Factor Surveillance System (BRFSS) 2015

Nguồn: Kaggle Dataset
Số lượng mẫu: 70,692
Số lượng đặc trưng: 21

Tác Giả
Le Duc Nam

Lưu Ý
Kết quả dự đoán từ hệ thống chỉ mang tính chất tham khảo và không thể thay thế cho chẩn đoán y tế chuyên nghiệp. Vui lòng tham khảo ý kiến bác sĩ để có đánh giá chính xác về tình trạng sức khỏe.


![image](https://github.com/user-attachments/assets/7c34d8be-b965-4a06-9d8e-d5d3dc85763a)
