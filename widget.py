from PyQt5.QtWidgets import *

class Widget(QGraphicsItem):
    def __init__(self, scene, title):
        super().__init__()
        self.scene = scene
        self.title = title

        self.scene.add_widget(self)

        self.initUI()

    def initUI(self):
        pass