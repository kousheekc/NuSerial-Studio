from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from graphics_scene import GraphicsScene
from graphics_view import GraphicsView

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.scene = GraphicsScene()

        self.view = GraphicsView(self.scene)
        self.layout.addWidget(self.view)

        self.setWindowTitle("NuSerial Studio")
        self.show()

        self.addDebugContent()

    def addDebugContent(self):
        green_brush = QBrush(Qt.green)
        black_brush = QPen(Qt.black)
        black_brush.setWidth(2)

        rect = self.scene.addRect(-100, -100, 60, 100, black_brush, green_brush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)