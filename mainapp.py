#code by leah Kemp 2024
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from firebase_page import ModernUI

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Leahs Firebase Toolkit")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon('icon.png'))

        self.stacked_widget = QStackedWidget(self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        # Create and add pages to stacked widget
        self.home_page = QWidget()
        self.stacked_widget.addWidget(self.home_page)
        self.home_page_ui()

        self.firebase_page = ModernUI()
        self.stacked_widget.addWidget(self.firebase_page)

    def home_page_ui(self):
        layout = QVBoxLayout()

        # Add title label
        title_label = QPushButton("Leah's Firebase Toolkit")
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setStyleSheet("background-color: #f0f0f0; border: none; padding: 20px;")
        title_label.setEnabled(False)
        layout.addWidget(title_label)

        # Add button to launch Firebase page
        firebase_button = QPushButton("Launch Firebase Page")
        firebase_button.setStyleSheet("font-size: 16px; padding: 10px; background-color: #007bff; color: white;")
        firebase_button.clicked.connect(self.show_firebase_page)
        layout.addWidget(firebase_button)

        self.home_page.setLayout(layout)

    def show_firebase_page(self):
        self.stacked_widget.setCurrentWidget(self.firebase_page)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    home_page = HomePage()
    home_page.show()
    sys.exit(app.exec_())
