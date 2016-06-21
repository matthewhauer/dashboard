import json


class DeviceLoader:
    def __init__(self):
        pass

    def load_file(self, filepath):
        the_file = open(filepath, 'r')
        the_json = json.load(the_file)
        print(the_json)
        # should convert the_json into an actual object....
        return the_json

    pass

# EOF
