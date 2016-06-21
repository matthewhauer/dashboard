import sys
from PyQt5.QtWidgets import *
from Device import Device
from DeviceLoader import DeviceLoader


def run_dashboard():
    app = QApplication(sys.argv)
    win = QWidget()

    loader = DeviceLoader()
    theJson = loader.load_file("exampleDevices.json")

    win.setGeometry(100, 100, 800, 600)
    win.setWindowTitle("LFETS Dashboard")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_dashboard()

#EOF
