import unittest
from DeviceLoader import DeviceLoader
from Device import Device


class TestDeviceLoader(unittest.TestCase):
    def test_example_file(self):
        service = DeviceLoader()
        device_list = service.load_file("exampleDevices.json")
        self.assertIsNotNone(device_list)
        self.assertEqual(len(device_list), 3, msg="Incorrect number of devices")
        for device in device_list:
            self.assertTrue(isinstance(device, Device), msg="Device list item not a Device instance")
    pass


if __name__ == '__main__':
    unittest.main()

# EOF
