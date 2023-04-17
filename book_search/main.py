import sys

from PyQt6.QtWidgets import QApplication
from book_search import BookSearch

def main():
    app = QApplication(sys.argv)
    window = BookSearch()
    window.show()
    sys.exit(app.exec())

main()