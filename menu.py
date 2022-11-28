import glob

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget, 
    QHBoxLayout, QVBoxLayout, QFileDialog, QLabel, QLineEdit
)
from PyQt6.QtGui import QPalette, QColor, QPixmap, QPainter, QBrush
from PyQt6.QtCore import Qt, QRect


class Menu(QVBoxLayout):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.file_options_layout = QVBoxLayout()
        self.control_options_layout = QVBoxLayout()

        self.next_btn = QPushButton("Next")
        self.next_btn.clicked.connect(self.next_image)

        self.open_btn = QPushButton("Open")
        self.open_btn.clicked.connect(self.select_dir)

        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.save)
        self.file_options_layout.addWidget(self.open_btn, alignment=Qt.AlignmentFlag.AlignTop)
        self.file_options_layout.addWidget(self.save_btn, alignment=Qt.AlignmentFlag.AlignTop)

        self.control_options_layout.addWidget(self.next_btn)

        self.addLayout(self.file_options_layout, stretch=1)
        self.addLayout(self.control_options_layout, stretch=3)

    def select_dir(self):
        fname = QFileDialog.getExistingDirectory(
            self.parent,
            "Open Dir",
            "${HOME}",
            QFileDialog.Option.ShowDirsOnly
        )

        if fname:
            self.current_dir = iter(sorted(glob.glob(f'{fname}/*.jpg')))
            self.next_image()
    
    def next_image(self):
        if not self.current_dir:
            return
        try:
            next_image = next(self.current_dir)
        except StopIteration:
            return

        self.parent.show_image(next_image)

    def save(self):
        self.parent.save()
        