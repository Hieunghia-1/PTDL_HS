1. Công nghệ sử dụng

Dự án sử dụng các công nghệ và thư viện sau:

Python 3

Jupyter Notebook (chạy trên Visual Studio Code)

Pandas: xử lý và phân tích dữ liệu

Matplotlib: vẽ biểu đồ trực quan

Seaborn: hỗ trợ trực quan hóa dữ liệu nâng cao
2. Cách hoạt động

Quy trình thực hiện bài toán gồm các bước chính:

Nạp dữ liệu

Đọc tập dữ liệu titanic_disaster.csv bằng thư viện Pandas.

Kiểm tra cấu trúc và các cột dữ liệu cơ bản.

Tiền xử lý dữ liệu

Lựa chọn các đặc trưng liên quan đến khả năng sống sót như:
Sex, Age, Pclass, Fare, SibSp, Parch, Embarked.

Tạo thêm đặc trưng FamilySize từ SibSp + Parch.

Khai thác dữ liệu (EDA)

Với mỗi đặc trưng:

Hiển thị bảng dữ liệu thống kê (crosstab, describe, sample).

Thực hiện trực quan hóa dữ liệu bằng biểu đồ.

Đưa ra nhận xét rút trích thông tin có giá trị.

Phân tích & nhận xét

Phân tích mối quan hệ giữa các đặc trưng và khả năng sống sót của hành khách.