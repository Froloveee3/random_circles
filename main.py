import sys
from random import randrange
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtCore import QRectF
from UI import *


def draw_ellipse(qp):
    x = randrange(1000)
    y = randrange(1000)
    radius = randrange(1080)
    ellipse_x = x - radius // 2
    ellipse_y = y - radius // 2
    rectangle = QRectF(ellipse_x, ellipse_y, radius, radius)
    qp.setBrush(QColor(randrange(255), randrange(255), randrange(255)))
    qp.drawEllipse(rectangle)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Git и желтые окружности')
        self.show()
        self.ui.DrawCircles.clicked.connect(self.draw)

    def draw(self):
        self.ui.DrawCircles.hide()
        qp = QPainter(self.ui.Ground.pixmap())
        qp.begin(self)
        for i in range(randrange(1, 21)):
            draw_ellipse(qp)
        qp.end()
        self.update()


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
