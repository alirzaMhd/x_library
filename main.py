# Main file

import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap
from sign_up_window import Window

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

main()