from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QInputDialog,
    QWidget, QHBoxLayout, QVBoxLayout, QFileDialog, QLabel
)
from PyQt6.QtGui import QPalette, QColor, QPixmap, QPainter, QBrush
from PyQt6.QtCore import Qt, QRect


class Canvas(QLabel):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.objects = []

    def paintEvent(self, event):
        super().paintEvent(event)

        if not self.pos:
            return
        qp = QPainter(self)
        br = QBrush(QColor(100, 10, 10, 40))
        qp.setBrush(br)

        for object in self.objects:
            qp.drawRect(object[0])
            qp.drawText(object[0].topLeft(), object[1])

    def mousePressEvent(self, e):
        self.rect_begin = e.pos()

    def mouseReleaseEvent(self, e):
        self.rect_end = e.pos()
        print(e.pos())

        text, ok = QInputDialog.getText(self, 'Label', 'Enter label:')
		
        if ok:
            print(str(text))
            self.objects.append(
                    (QRect(self.rect_begin, self.rect_end), str(text)))
            self.update()
    
    def save_to_file(self, image):
        with open("output.csv", 'a') as output:
            for object, label in self.objects:
                output.write(f"{image},{label},{','.join(map(str, object.getCoords()))}\n")

    def show_image(self, pixmap):
        self.objects = []
        self.update()
        self.setPixmap(
            pixmap.scaled(
                self.width(), 
                self.height(), 
                Qt.AspectRatioMode.KeepAspectRatio
            )
        )
