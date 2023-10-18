from PyQt5 import QtGui
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class GraphicsView(QGraphicsView):
    def __init__(self, scene):
        super().__init__()

        self.min_zoom = 0.1
        self.max_zoom = 4.0

        self.scene = scene
        self.initUI()
        self.setScene(self.scene)

    def initUI(self):
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setDragMode(QGraphicsView.ScrollHandDrag)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setDragMode(QGraphicsView.NoDrag)
        super().mouseReleaseEvent(event)

    def wheelEvent(self, event: QWheelEvent):
        zoom_factor = 1.15 ** (event.angleDelta().y() / 120)
        current_zoom = self.transform().m22()
        new_zoom = current_zoom * zoom_factor

        if self.min_zoom <= new_zoom <= self.max_zoom:
            self.scale(zoom_factor, zoom_factor)
        elif new_zoom < self.min_zoom:
            self.resetTransform()
            self.scale(self.min_zoom, self.min_zoom)
        elif new_zoom > self.max_zoom:
            self.resetTransform()
            self.scale(self.max_zoom, self.max_zoom)




