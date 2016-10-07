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

moway.set_time(20)
moway.command_moway(CMD_GREENLEDON,0)
while True:
	while moway.get_mic() < 40 :
		print moway.get_mic()
		sleep(0.1)
	print moway.get_mic()
	moway.command_moway(CMD_GREENLEDOFF,0)
	moway.command_moway(CMD_GO)
	moway.wait_mot_end(0)
	moway.command_moway(CMD_TURN_AROUND,0)
	moway.wait_mot_end(0)
	moway.command_moway(CMD_GREENLEDON,0)
	sleep(0.5)
