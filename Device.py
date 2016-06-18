class Device:
    def __init__(self):
        name = ''
        geometry = {}
        sensors = []
		actuator = None
		drawState = {
			posX: 0,
			posY: 0
		}
    pass

DeviceStates = ['NOMINAL', 'WARNING', 'ERROR', 'DISABLED',
	'VALVE-OPEN', 'VALVE-CLOSED', 'CHANGING']

class Sensor:
	def __init__(self):
		name = ''
		connection = {}
		unit = ''
		log = {logSize = 0, data = []}
		
pass
