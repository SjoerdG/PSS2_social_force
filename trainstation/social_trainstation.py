# sys and Os are used to interact with the terminal and filesystem
import sys, os
# a trick to add the root folder of the project to the list of folders that will be searched when importing libs
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..',)
sys.path.append( mymodule_dir )

from cromosim import *
from cromosim.micro import *
from optparse import OptionParser
import json

plt.ion()