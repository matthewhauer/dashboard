import unittest
from DeviceLoader import DeviceLoader
from Device import Device


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


if __name__ == '__main__':
    unittest.main()

# EOF
