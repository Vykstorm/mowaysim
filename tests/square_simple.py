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
        moway.command_moway(CMD_GO_SIMPLE,0)
        sleep(2)
        moway.command_moway(CMD_RIGHT_SIMPLE,0)
        sleep(1)
