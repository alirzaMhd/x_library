# Sign-up page

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap

class window(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("X_Library - Sign Up")
        self.setWindowIcon(QIcon("icon.ico"))
        self.resize(800, 600)

        layout = QVBoxLayout()

        image_box = QLabel(self)
        pixmap = QPixmap("icon.ico")
        image_box.setPixmap(pixmap)
        image_box.setGeometry(100, 100, 300, 300)
        layout.addWidget(image_box)

        input_box = QLineEdit(self)
        input_box.setGeometry(150, 400, 200, 30)
        layout.addWidget(input_box)

        self.setLayout(layout)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())