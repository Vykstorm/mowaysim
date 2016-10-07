import sys, atexit
from time import sleep
from mowaysim import *
print 'Executing ' + __name__ + ' test...'


if __name__ == '__main__':
        atexit.register(exit_mow)
        
channel = 3
moway.usbinit_moway()
ret = moway.init_moway(channel)
if ret == 0:
        print 'Moway RFUSB Connected'
else:   
        print 'Moway RFUSB not connected. Exit'
        exit(-1)

while True:
        moway.command_moway(CMD_LINE_FOLLOW_L,0)
        light = moway.get_light()
        print light
        if light < 40:
                moway.command_moway(CMD_FRONTLEDON,0)
        else:
                moway.command_moway(CMD_FRONTLEDOFF,0)
        sleep(1)
