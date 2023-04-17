import sys

from PyQt6.QtWidgets import QApplication
from sign_up_window import SignUpWindow

def main():
    app = QApplication(sys.argv)
    window = SignUpWindow()
    window.show()
    sys.exit(app.exec())

main()