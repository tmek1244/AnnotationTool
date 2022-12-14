from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QFileDialog, QLabel
from PyQt6.QtGui import QPalette, QColor, QPixmap, QPainter, QBrush
from PyQt6.QtCore import Qt, QRect

from menu import Menu
from canvas import Canvas

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_dir = None
        self.current_image = None

        self.setWindowTitle("AnnotationTool")

        self.main_layout = QHBoxLayout()
        self.menu_layout = Menu(self)
        self.canvas = Canvas(self)
        self.changes_layout = QLabel()

        self.main_layout.addLayout(self.menu_layout, stretch=1)
        self.main_layout.addWidget(self.canvas, stretch=5)
        self.main_layout.addWidget(self.changes_layout, stretch=2)
        
        widget = QWidget()
        width = 1000
        height = 500
        # setting  the fixed width of window
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)
 
    def show_image(self, image):
        self.current_image = image
        pixmap = QPixmap(image)
        self.canvas.show_image(pixmap)
    
    def save(self):
        self.canvas.save_to_file(self.current_image.split('/')[-1])
        

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication([])

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()
