from PyQt5.QtWidgets import QMainWindow
from dashboard import Dashboard

class NuSerial(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        edit_menu = menubar.addMenu('Edit')
        view_menu = menubar.addMenu('View')
        run_menu = menubar.addMenu('Run')
        help_menu = menubar.addMenu('Help')

        dashboard = Dashboard()
        self.setCentralWidget(dashboard)

        self.setWindowTitle("NuSerial Studio")
        self.setMinimumSize(800, 600)
        self.showMaximized()
