class Device:
	def __init__(self):
		name = ''
		geometry = {}
		sensors = []
		actuator = None
		draw_state = {}
		draw_state.pos_x = 0
		draw_state.pos_y = 0


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

