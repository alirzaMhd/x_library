import sys

from PyQt6.QtWidgets import QApplication, QWidget,QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from constants import WINDOW_ICON

class BookSearch(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("X_Library | Book Search Window")
        self.setWindowIcon(QIcon(WINDOW_ICON))
        self.resize(800, 600)
        self.create_widgets()
    
    def create_widgets(self) :
        window_layout = QVBoxLayout()

        heading = QLabel("Enter the title of the book you want :",self)
        heading.setFont(QFont("Times New Roman", 30))
        window_layout.addWidget(heading)

        search_bar = QLineEdit(self)
        window_layout.addWidget(search_bar)

        search_btn = QPushButton("Search", self)
        window_layout.addWidget(search_btn)

        self.setLayout(window_layout)