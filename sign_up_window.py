# sign_up_window

import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap

app = QApplication(sys.argv)
class Window(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("X_Library | Sign Up Window")
        self.setWindowIcon(QIcon("icon/app_icon.ico"))
        self.resize(800, 600)

        window_layout = QVBoxLayout()

        image_box = QLabel(self)
        captcha_image = QPixmap("icon/app_icon.ico")
        image_box.setPixmap(captcha_image)
        image_box.setGeometry(100, 100, 300, 300)
        window_layout.addWidget(image_box)

        input_box = QLineEdit(self)
        input_box.setGeometry(150, 400, 200, 30)
        window_layout.addWidget(input_box)

        self.setLayout(window_layout)

Window = Window()
Window.show()
sys.exit(app.exec())