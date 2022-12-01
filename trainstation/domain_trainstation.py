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
dom.plot(id=3, title="Domain", savefig=False)
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

#intialize people

nn = 10 # number of people
box = [120,130,10,20]                       # coordinates of the box that will be populated [xmin, xmax, ymin, ymax]
dest_name = "door"                          # name given to by domain.add_destination function
radius_distribution = ["uniform",0.4,0.6]   # distribution variable 
velocity_distribution = ["normal",1.2,0.1]  # distribution varible
rng = 0                                     # some seed value for the distribution, if =0 then random value will be chosen on run
dt = 0.05                                   # timestep
dmin_people=0                               # minimal disired distance to other people
dmin_walls=0                                # minimal disired distance to walls
itermax=10                                  # max number of uzawa projectsions, only intressting that is used as projection method
groups = [{"nb":nn, "radius_distribution":radius_distribution, "velocity_distribution":velocity_distribution, "box":box, "destination":dest_name}] #create dict bundeling above values
# has to be a list of a dict for some reason
#curseddatatype
people = people_initialization(dom, groups, dt, dmin_people, dmin_walls, rng, itermax, projection_method='cvxopt')
contacts = None
colors = people["xyrv"][:,2]
plot_people(0,dom,people,contacts,colors)
plt.show()
