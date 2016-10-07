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

moway.command_moway(CMD_GO_SIMPLE,0)
while True:
	obstacle = moway.get_obs_center_left() + moway.get_obs_center_right()
	if obstacle > 0:
		moway.command_moway(CMD_TURN_AROUND,0)
		moway.wait_mot_end(0)
		moway.command_moway(CMD_GO_SIMPLE,0)

moway.close_moway()
print 'Exit'
