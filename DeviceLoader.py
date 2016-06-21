import json
from Device import Device

class DeviceLoader:
    def __init__(self):
        pass

    def load_file(self, filepath):
        the_file = open(filepath, 'r')
        the_json = json.load(the_file)
        # should convert the_json into an actual object....
        devices = []
        for device in the_json:
            devices.append(Device())
            pass
        return devices


    pass

# EOF
