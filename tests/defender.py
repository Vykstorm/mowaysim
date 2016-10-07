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
        
moway.command_moway(CMD_GO_SIMPLE,0)
moway.command_moway(CMD_GREENLEDON,0)
moway.set_rotation(144)
while True:
        if moway.get_line_left() + moway.get_line_right() > 50:
                moway.set_time(3)
                moway.command_moway(CMD_BACK,0)
                moway.wait_mot_end(0)
                moway.set_time(0)
                moway.command_moway(CMD_ROTATERIGHT,0)
                moway.wait_mot_end(0)
                moway.command_moway(CMD_GO_SIMPLE,0)
        else:
                obstacle = moway.get_obs_center_left() + moway.get_obs_center_right() + moway.get_obs_side_left() + moway.get_obs_side_right()
                if obstacle > 0:
                        moway.command_moway(CMD_PUSH,0)
                        moway.command_moway(CMD_LEDSOFF,0)
                        moway.command_moway(CMD_FRONTLEDON,0)
                        moway.command_moway(CMD_REDLEDON,0)
                        while moway.get_line_left() + moway.get_line_right() < 50:
                                print 'Pushing'
                        moway.command_moway(CMD_LEDSOFF,0)
                        moway.command_moway(CMD_GREENLEDON,0)
                        
