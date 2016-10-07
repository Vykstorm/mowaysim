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
	
moway.set_rotation(210)
while True:
	moway.command_moway(CMD_LINE_FOLLOW_L,0)
	obstacle = moway.get_obs_center_left() + moway.get_obs_center_right() + moway.get_obs_side_left() + moway.get_obs_side_right()
	if obstacle > 0:
		moway.command_moway(CMD_ROTATELEFT,0)
		moway.command_moway(CMD_BRAKELEDON,0)
		moway.wait_mot_end(0)
		moway.command_moway(CMD_BRAKELEDOFF,0)
