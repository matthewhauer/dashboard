class Device:
    sensors = []
    draw_state = {}
    actuator = None

    def __init__(self):
        name = ''
        geometry = {}
        self.draw_state["pos_x"] = 0
        self.draw_state["pos_y"] = 0

    def add_sensor(self, the_sensor):
        if the_sensor is not None:
            self.sensors.append(the_sensor)

    def get_sensor(self, sensor_name):
        return self.sensors[sensor_name]


DeviceStates = ['NOMINAL', 'WARNING', 'ERROR', 'DISABLED',
    'VALVE-OPEN', 'VALVE-CLOSED', 'CHANGING']


class Sensor:
    def __init__(self):
        name = ''
        connection = {}
        unit = ''
        log = {}
        log.log_size = 0
        log.data = []

# EOF

