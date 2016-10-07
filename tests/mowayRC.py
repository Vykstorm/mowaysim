import sys, atexit , msvcrt
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

while True:
	ch = raw_input()
	if ch=='w':
		moway.command_moway(CMD_GO_SIMPLE,0)
		moway.command_moway(CMD_LEDSOFF,0)
		moway.command_moway(CMD_FRONTLEDON,0)
	if ch=='z':
		moway.command_moway(CMD_BACK_SIMPLE,0)
		moway.command_moway(CMD_LEDSOFF,0)
		moway.command_moway(CMD_BRAKELEDON,0)
	if ch=='a':
		moway.command_moway(CMD_LEFT_SIMPLE,0)
		moway.command_moway(CMD_LEDSOFF,0)
		moway.command_moway(CMD_GREENLEDON,0)
	if ch=='d':
		moway.command_moway(CMD_RIGHT_SIMPLE,0)
		moway.command_moway(CMD_LEDSOFF,0)
		moway.command_moway(CMD_REDLEDON,0)
	if ch=='s':
		moway.command_moway(CMD_STOP,0)
		moway.command_moway(CMD_LEDSOFF,0)
		moway.command_moway(CMD_BRAKELEDON,0)
