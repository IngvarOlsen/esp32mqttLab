# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import sys
#This is so the program can see the files in the Lib underfolder aswell
sys.path.reverse()