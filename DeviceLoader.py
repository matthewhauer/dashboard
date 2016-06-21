import json
from Device import Device

class DeviceLoader:
    def __init__(self):
        pass

    def build_sensor(self, device, the_json):
        pass

    def build_actuator(self, device, the_json):
        pass

    def build_device(self, the_json):
        d = Device()
        if "name" in the_json:
            d.name = the_json["name"]
        if "sensors" in the_json:
            for sensor in the_json["sensors"]:
                self.build_sensor(d, the_json)
        if "actuator" in the_json:
            self.build_actuator(d, the_json)
        return d

    def load_file(self, filepath):
        the_file = open(filepath, 'r')
        the_json = json.load(the_file)
        # should convert the_json into an actual object....
        devices = []
        for device in the_json:
            if '__type__' in device and device['__type__'] is "Device":
                devices.append(self.build_device(device))
            pass
        return devices


    pass

# EOF
