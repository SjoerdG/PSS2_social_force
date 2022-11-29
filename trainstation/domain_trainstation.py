# sys and Os are used to interact with the terminal and filesystem
import sys, os
# a trick to add the root folder of the project to the list of folders that will be searched when importing libs
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..',)
sys.path.append( mymodule_dir )

from cromosim import *
from cromosim.micro import *
from matplotlib.patches import Circle
from matplotlib.lines import Line2D

#create a domain object from picture walls_trainstation
dom = Domain(name = 'trainstation', background = 'walls_trainstation.png', pixel_size = 0.1)


## To define the color for the walls
wall_color = [0,0,0]

## To define the color for the issue of the room
door_color = [255,0,0]


dom.build_domain()
dom.plot(id=3, title="Domain")
## To create a Destination object towards the door
dest = Destination(name='door', colors=[door_color],
                   excluded_colors=[wall_color])
dom.add_destination(dest)



dom.plot_wall_dist(id=1, step=20,
    title="Distance to walls and its gradient",
    savefig=False, filename="room_wall_distance.png")

dom.plot_desired_velocity('door',id=2, step=20,
    title="Distance to the destination and desired velocity",
    savefig=False, filename="room_desired_velocity.png")

plt.show()