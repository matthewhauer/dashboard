from Device import Device
from PyQt5.QtWidgets import *

class DevicePanel:
    def __init__(self):
        self.device = None
        self.widget = None
        self.layout = None

    def set_device(self, dev):
        widget = QWidget()
        layout = QFormLayout()
        # name
        layout.addRow(QLabel("Name"), QLabel(dev.name))
        # sensor count
        layout.addRow(QLabel("Sensor Ct"), QLabel(str(len(dev.sensors))))
        # actuator?
        if dev.actuator is not None:
            layout.addRow(QLabel("Actuator?"), QLabel("True"))
        else:
            layout.addRow(QLabel("Actuator?"), QLabel("False"))
        # logger? -- loggers are per sensor/actuator, not device.
        # if dev.logger is not None:
        #     layout.addRow(QLabel("Actuator?"), QLabel("True"))
        # else:
        #     layout.addRow(QLabel("Actuator?"), QLabel("True"))
        widget.setLayout(layout)
        return self # builder pattern

    def get_panel(self):
        return self.widget

# EOF
