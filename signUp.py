# Sign-up page

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont

class signUp(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("X_Library - Sign Up")
        self.setWindowIcon(QIcon("icon.ico"))
        self.resize(800, 600)


app = QApplication(sys.argv)
signUp = signUp()
signUp.show()
sys.exit(app.exec())