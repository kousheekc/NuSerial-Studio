from PyQt5.QtWidgets import QWidget, QVBoxLayout
from dashboard_scene import DashboardScene
from dashboard_view import DashboardView

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.scene = DashboardScene()
        self.view = DashboardView(self.scene)

        self.layout.addWidget(self.view)