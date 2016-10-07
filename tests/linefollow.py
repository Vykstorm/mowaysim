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

moway.set_rotation_axis(WHEEL)
while True:
	line_r = moway.get_line_right()
	if line_r < 50:
		moway.command_moway(CMD_ROTATERIGHT,0)
	else: 
		moway.command_moway(CMD_ROTATELEFT,0)

moway.close_moway()
print 'Exit'
