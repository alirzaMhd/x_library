# Sign-up page

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit
from PyQt6.QtGui import QIcon, QFont, QPixmap

class window(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("X_Library - Sign Up")
        self.setWindowIcon(QIcon("icon.ico"))
        self.resize(800, 600)

        image_box = QLabel(self)
        pixmap = QPixmap("icon.ico")
        image_box.setPixmap(pixmap)
        image_box.setGeometry(50, 50, 300, 300)

        input_box = QLineEdit(self)
        input_box.setGeometry(150, 400, 200, 30)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())