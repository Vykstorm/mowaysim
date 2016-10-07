# Moway functions

# Gestion libreria Mowai 
def usbinit_moway():
	pass
	
def exit_moway():
	pass

def init_moway(channel):
	return 0
	
def close_moway():
	pass
	
def init_prog_moway():
	return 0
	
def program_moway(f):
	pass
	
def program_moway_channel(f, channel):
	return 0
	
def read_moway_batt():
	return 100 
	
# Funciones para usar motores del robot y
# establecer parametros.

def command_moway(command, timeout):
	print('executing command')

def set_speed(speed):
	print('speed set to: ', speed)
	
def set_rotation(rotation):
	print('rotation set to: ', rotation)

def set_distance(distance):
	print('distance set to: ', distance)

def set_radius(radius):
	print('radius set to: ', radius)

def set_rotation_axis(axis):
	pass

def set_time(time):
	print('time set to: ', time)

def set_frequency(frequency):
	print('frequency set to: ', frequency)
	
def wait_mot_end(timeout):
	print('waiting for command to finish')
	

# Funciones para obtener valores de los sensores.
def get_obs_center_left():
	return 0 
	
def get_obs_side_left():
	return 0
	
def get_obs_center_right():
	return 0

def get_obs_side_right():
	return 0
	
def get_line_left():
	return 0
	
def get_line_right():
	return 0

def get_mic():
	return 0

def get_light():
	return 0

def get_distance():
	return 0
	
def get_accel_X():
	return 0
	
def get_accel_Y():
	return 0
	
def get_accel_Z():
	return 0
	
