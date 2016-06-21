import unittest
from DeviceLoader import DeviceLoader
from Device import Device


class TestDeviceLoader(unittest.TestCase):
    def test_example_file(self):
        service = DeviceLoader()
        device_list = service.load_file("exampleDevices.json")
        self.assertIsNotNone(device_list)
        self.assertEqual(len(device_list), 3, msg="Incorrect number of devices")
        self.assertTrue(isinstance(device_list[0], Device), msg="Device list not of Device instances")
    pass


if __name__ == '__main__':
    unittest.main()

# EOF
