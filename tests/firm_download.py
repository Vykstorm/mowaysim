import sys, atexit
from time import sleep
from mowaysim import *
print 'Executing ' + __name__ + ' test...'



channel = 8
if moway.init_prog_moway() == 0:
	print "Moway Battery: " , moway.read_moway_batt()
	if moway.program_moway_channel("../lib/moway.hex",channel) == 0 :
		print("Moway Programmed Succesfully")
	else :
		print("Programming Error")
moway.exit_moway()
	

