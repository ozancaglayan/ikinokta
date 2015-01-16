# Imports the monkeyrunner modules used by this program
import sys
import time
import subprocess

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
print "Wait for connection.."
device = MonkeyRunner.waitForConnection()

# sets a variable with the package's internal name
package = 'com.weplaydots.twodotsandroid'

# sets a variable with the name of an Activity in the package
activity = 'com.prime31.UnityPlayerNativeActivity'

# sets the name of the component to start
runComponent = package + '/' + activity

# Runs the component
#print "Start activity.."
#device.startActivity(component=runComponent)

#device.drag((219, 766), (347, 765), 0.25)
#device.drag((347, 765), (347, 894), 0.25)
#device.drag((347, 894), (218, 894), 0.25)
#device.drag((218, 894), (219, 766), 0.25)

device.drag((347, 1214), (347, 1086), 0.25)
device.drag((347, 1086), (347, 959), 0.25)
device.drag((347, 959), (347, 830), 0.25)
#device.drag((988, 1087), (219, 1087), 0.25)
#device.drag((218, 894), (219, 766), 0.25)
sys.exit(1)



while 1:
    caps = device.takeSnapshot()
    caps.writeToFile("/tmp/twodots.png", "png")
    # We can't use numpy here as monkeyrunner is using JPython that's
    # why we have to run another program here :)
    output = subprocess.Popen(["python", "digitize.py", "/tmp/twodots.png"], stdout=subprocess.PIPE).communicate()[0]
    print output
    break

