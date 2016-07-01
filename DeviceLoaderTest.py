import unittest
from DeviceLoader import DeviceLoader
from Device import Device
from DevicePanel import DevicePanel
from PyQt5.QtWidgets import *
import sys

class TestDeviceLoader(unittest.TestCase):
    def test_example_file(self):
        service = DeviceLoader()
        device_list = service.load_file("exampleDevices.json")
        self.assertIsNotNone(device_list)
        self.assertEqual(len(device_list), 3, msg = "Incorrect number of devices")
        for dev_key in device_list.keys():
            device = device_list[dev_key]
            self.assertTrue(isinstance(device, Device), msg = "Device list item not a Device instance")
        # test "LOX Vent" - two sensors, one actuator
        lox_vent = device_list["LOX Vent"]
        self.assertIsNotNone(lox_vent, msg = "Could not find 'LOX Vent' device")
        self.assertEquals(len(lox_vent.sensors), 2, msg = "Incorrect sensor count in 'LOX Vent'")
        self.assertIsNotNone(lox_vent.actuator, msg = "No actuator in 'LOX Vent'")
        self.assertEquals(lox_vent.actuator["name"], "LOX Vent Valve", msg = "LOX Vent device actuator name incorrect")
    pass

    def test_device_panel(self):
        app = QApplication(sys.argv)
        win = QWidget()

        loader = DeviceLoader()
        devices = loader.load_file("exampleDevices.json")
        lox_vent = devices["LOX Vent"]
        self.assertIsNotNone(lox_vent, msg="Could not find 'LOX Vent' object")
        lox_pane = DevicePanel().set_device(lox_vent)

        win.setGeometry(100, 100, 800, 600)
        win.setWindowTitle("LFETS Dashboard")
        win.addWidget(lox_pane.get_panel())

        win.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    unittest.main()

# EOF
