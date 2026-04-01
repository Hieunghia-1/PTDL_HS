 * Công nghệ
 Thư viện: * NumPy: Tính toán ma trận và đại số tuyến tính.

 SciPy: Sử dụng module optimize để giải quyết các bài toán tối ưu.

 SymPy: Tính toán đạo hàm bằng ký hiệu toán học.

 Matplotlib: Trực quan hóa đồ thị hàm số và các điểm tối ưu.
 
* Cách hoạt động
 1. Tính toán Đạo hàm (Derivatives)Sử dụng đạo hàm để xác định độ dốc và hướng thay đổi của hàm số.Tìm các điểm tới hạn (Critical points) nơi đạo hàm bằng 0 để xác định cực đại và cực tiểu.

 2. Thuật toán Gradient DescentNguyên lý: Cập nhật tham số theo hướng ngược lại với Gradient để giảm thiểu hàm mất mát (Loss function).Công thức cập nhật: $x_{new} = x_{old} - \eta \cdot \nabla f(x_{old})$, trong đó $\eta$ là tốc độ học (Learning Rate).

 3. Tối ưu hóa với SciPySử dụng hàm minimize để tìm giá trị nhỏ nhất của các hàm đa biến phức tạp.Áp dụng các phương pháp như BFGS hoặc L-BFGS-B để tối ưu hóa hiệu suất tính toán.
 
 4. Trực quan hóa kết quảVẽ đồ thị 2D/3D của hàm mục tiêu.Mô phỏng quá trình hội tụ của thuật toán từ điểm khởi tạo đến điểm tối ưu toàn cục.