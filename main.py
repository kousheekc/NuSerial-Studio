import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from dashboard import Dashboard

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dashboard = Dashboard()

    sys.exit(app.exec_())