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
	
sides = int(raw_input("Enter sides of the regular polygon (3 -10): "));
length = int(raw_input("Enter length of the side (100 - 255 mm): "));

if sides < 3 and sides > 10:
        print "Sides number not correct. Exit"
        exit(-1)
if length < 100 and length > 255:
        print "Sides number not correct. Exit"
        exit(-1)        

angle = 180 * (1 - float(sides-2)/float(sides))
print angle

for i in range(sides):
	#Set variables for go command
	moway.set_distance(length)
	moway.set_speed(100)
	moway.command_moway(CMD_GO,0)
	#wait for movement end
	moway.wait_mot_end(0)
	#Set variables for rotate command
	moway.set_rotation(int(angle))
	moway.set_rotation_axis(CENTER)
	moway.command_moway(CMD_ROTATERIGHT,0)
	#wait for movement end
	moway.wait_mot_end(0)


