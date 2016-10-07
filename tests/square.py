import sys, atexit
from time import sleep
from mowaysim import *
print 'Executing ' + __name__ + ' test...'


if __name__ == '__main__':
        atexit.register(exit_mow)
	
channel = 8
moway.usbinit_moway()
ret = moway.init_moway(channel)
if ret == 0:
    	print 'Moway RFUSB Connected'
else:	
	print 'Moway RFUSB not connected. Exit'
	exit(-1)

for i in range(4):
	#Set variables for go command
	moway.set_distance(200)
	moway.set_speed(100)
	moway.command_moway(CMD_GO,0)
	#wait for movement end
	moway.wait_mot_end(0)
	#Set variables for rotate command
	moway.set_rotation(90)
	moway.set_rotation_axis(CENTER)
	moway.command_moway(CMD_ROTATERIGHT,0)
	#wait for movement end
	moway.wait_mot_end(0)


