import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLabel, QLineEdit, QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tool khoa học dữ liệu máy tính")
        self.setFixedSize(1300, 650)
        self.setStyleSheet("QMainWindow { background-color: white; }")

        # Bước 1: tạo central widget và gắn vào cửa sổ
        khung_chinh = QWidget()
        self.setCentralWidget(khung_chinh)
        khung_chinh.setStyleSheet("background-color: #dbeafe;")   # tô xanh nhạt cho central widget
        self.statusBar().showMessage("Sẵn sàng")                  # bật thanh trạng thái
        # Bước 2: tạo layout và gắn vào central widget
        layout_doc = QVBoxLayout()
        khung_chinh.setLayout(layout_doc)

        # Bước 3: tạo các widget (lưu vào self để hàm khác dùng được)
        self.tieu_de = QLabel("Xin chào!")
        self.o_nhap = QLineEdit()
        self.o_nhap.setPlaceholderText("Nhập tên của bạn...")
        self.nut_bam = QPushButton("Chào")

        # Bước 4: thêm widget vào layout theo thứ tự từ trên xuống
        layout_doc.addWidget(self.tieu_de)
        layout_doc.addWidget(self.o_nhap)
        layout_doc.addWidget(self.nut_bam)
        layout_doc.addStretch()   # khoảng trống co giãn, đẩy các widget lên trên

        # Bước 5: nối sự kiện click với hàm xử lý (không có dấu ngoặc)
        self.nut_bam.clicked.connect(self.khi_bam_nut)

        self.dua_ra_giua_man_hinh()

    def khi_bam_nut(self):
        ten = self.o_nhap.text()
        self.tieu_de.setText(f"Xin chào, {ten}!")

    def dua_ra_giua_man_hinh(self):
        khung = self.frameGeometry()
        tam = self.screen().availableGeometry().center()
        khung.moveCenter(tam)
        self.move(khung.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())