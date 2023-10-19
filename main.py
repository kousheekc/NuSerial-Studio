import sys
from PyQt5.QtWidgets import QApplication

from nuserial import NuSerial

if __name__ == "__main__":
    app = QApplication(sys.argv)

    nuserial = NuSerial()

    sys.exit(app.exec_())