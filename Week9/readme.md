*Công nghệ sử dụng
Ngôn ngữ lập trình: Python 3.12+

Thư viện chính: * nltk: Thư viện nền tảng để làm việc với dữ liệu ngôn ngữ con người.

re: Biểu thức chính quy (Regular Expression) để lọc và tìm kiếm văn bản.

random: Để trích xuất mẫu dữ liệu ngẫu nhiên.

Dữ liệu (Corpus) sử dụng:

Gutenberg: Kho văn bản văn học cổ điển.

Stopwords: Danh sách các từ dừng trong nhiều ngôn ngữ khác nhau.

WordNet: Cơ sở dữ liệu từ vựng tiếng Anh (Synsets, Hyponyms).

Names: Tập hợp tên nam và nữ (hơn 7,900 tên).
* Cách hoạt động
Xử lý Corpus & Stopwords
Khám phá: Liệt kê tệp tin và danh sách từ dừng của hơn 30 ngôn ngữ.

Lọc văn bản: Tách từ (word_tokenize) và loại bỏ các từ vô nghĩa (Stopwords) để làm sạch dữ liệu.

Phân tích ngữ nghĩa (WordNet)
Tra cứu: Truy xuất định nghĩa, ví dụ, từ đồng nghĩa và trái nghĩa.

Độ tương đồng: Tính toán mức độ giống nhau giữa các danh từ/động từ bằng thuật toán Wu-Palmer.

Gán nhãn & Trích xuất đặc trưng
POS Tagging: Phân tích từ loại (Danh từ, Động từ,...) và sử dụng Regex để lọc ký tự.

Xử lý dữ liệu tên: Thống kê giới tính và trích xuất ký tự cuối của tên để nhận dạng đặc trưng giới tính.