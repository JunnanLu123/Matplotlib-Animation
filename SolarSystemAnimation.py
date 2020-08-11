"""
Matplotlib is a Python library containing tools 
for plots and animation in three dimensional 
spaces. Setup by importing matplotlib module. 
Matplotlib includes API for generating animation
and figure plot. The FuncAnimation function 
makes animation by calling frame update function 
repeatlly.
"""

import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np

matplotlib.use("Agg")

# File based ffmpeg writer
Writer = matplotlib.animation.writers['ffmpeg']

# Film are writen to temporary files on disk
# Stitched together at the end
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

# Labels of the plants to animate
PLANT = ['Mercury', 'Venus', 'Earth','Mars']

# Processing orbiting data by combining 
def loadData(name):
    Data = []
    # Load picked object from 'npz' or 'npy' file
    data = np.load(name)
    # Load data from mercury column
    mer = data['mercury']
    # Load data from venus column
    ven = data['venus']
    # Load data from earth column
    ear = data['earth']
    # Load data from mars column
    mars = data['mars']
    # Add oribits data of four planets to the list
    Data.append(mer)
    Data.append(ven)
    Data.append(ear)
    Data.append(mars)
    return Data

# Oribting matrix is ready for future processing
Data = loadData("C:/Users/JunnanLu/orbits.npz")

# Store transposed oribiting matrix
data = []

# Transposing orbiting matrix
for dat in Data:
    data.append(np.transpose(dat))

# Create figure object
fig = plt.figure(figsize=(12,6))
# Create 3D axes object
ax = fig.add_subplot(projection='3d')

# Set 3D X axis limit
ax.set_xlim3d([-1.375,1.375])
# Set X axis label
ax.set_xlabel('X Axis')
# Set 3D Y axis limit
ax.set_ylim3d([-1.375,1.375])
# Set Y axis label
ax.set_ylabel('Y Axis')
# Set Z axis limit
ax.set_zlim3d([-3.0,3.0])
# Set Z axis label
ax.set_zlabel('Z Axis')
# Set figure title
ax.set_title("A Capricorn's Solar Orbiters")

# Ploting the sun with marker, marker size, and color
Sun = ax.plot([-0.951049],[1.52138],[-2.35551],'o',color='#8c1907',label='SUN',markersize=8.0)

# Ploting the oribiting lines with line width at 0.8
Line = [ax.plot(dat[0,0:1400],dat[1,0:1400],dat[2,0:1400],linestyle='-',linewidth=0.8)[0] for dat in data]

# Ploting four solar planets with color, marker and labels
planets = [ax.plot(dat[0,0:1],dat[1,0:1],dat[2,0:1],'o',markersize=6.0,color=ln.get_color(),label=names)[0] for dat, ln, names in zip(data,L,PLANT)]

# Place legend on the top left corner
ax.legend(loc=2)

# Updating animation frame with four planets
# Number of frame is define by parameter num
# Data is passed by parameter data
# Plot objects are passed by parameter line
def update(num,data,line):
    # Load Mercury orbits
    Mercury=data[0]
    # Load Venus orbits
    Venus=data[1]
    # Load Earth orbits
    Earth=data[2]
    # Load Mars orbits
    Mars=data[3]

    # Load Mercury X axis oribits
    MerX = Mercury[0,:num]
    # Load Mercury Y axis orbits
    MerY = Mercury[1,:num]
    # Load Mercury Z axis orbits
    MerZ = Mercury[2,:num]

    # Load Venus X axis oribits
    VenX = Venus[0,:num]
    # Load Venus Y axis oribits
    VenY = Venus[1,:num]
    # Load Venus Z axis oribits
    VenZ = Venus[2,:num]

    # Load Earth X axis oribits
    EarX = Earth[0,:num]
    # Load Earth Y axis oribits
    EarY = Earth[1,:num]
    # Load Earth Z axis oribits
    EarZ = Earth[2,:num]

    # Load Mars X axis oribits
    MarX = Mars[0,:num]
    # Load Mars Y axis oribits
    MarY = Mars[1,:num]
    # Load Mars Z axis oribits
    MarZ = Mars[2,:num]

    # Will update once the oribits data changed
    if (num>0):
        # Updating Mercury's latest move X axis 
        MX = MerX[-1]
        # Updating Mercury's latest move Y axis
        MY = MerY[-1]
        # Updating Mercury's latest move Z axis
        MZ = MerZ[-1]
        
        # Updating Venus's latest move X axis
        VX = VenX[-1]
        # Updating Venus's latest move Y axis
        VY = VenY[-1]
        # Updating Venus's latest move Z axis
        VZ = VenZ[-1]

        # Updating Earth's latest move X axis
        ERX = EarX[-1]
        # Updating Earth's latest move Y axis
        ERY = EarY[-1]
        # Updating Earth's latest move Z axis
        ERZ = EarZ[-1]

        # Updating Mars latest move X axis
        MRX = MarX[-1]
        # Updating Mars latest move Y axis
        MRY = MarY[-1]
        # Updating Mars latest move Z axis
        MRZ = MarZ[-1]

        # Ploting Mercury's update in three dimensions
        Line[0].set_data(MX,MY)
        Line[0].set_3d_properties(MZ)

        # Ploting Venus's update in three dimensions
        Line[1].set_data(VX,VY)
        Line[1].set_3d_properties(VZ)

        # Ploting Earth's update in three dimensions
        Line[2].set_data(ERX,ERY)
        Line[2].set_3d_properties(ERZ)

        # Ploting Mars's update in three dimensions
        Line[3].set_data(MRX,MRY)
        Line[3].set_3d_properties(MRZ)
    
    return Line,
if __name__=='__main__':
   # Making animation by repeatlly calling update function
   ani = FuncAnimation(fig,update,frames=1000,fargs=(data,planets),interval=80)
   # Saving the animation film on local disk
   ani.save("solar.mp4",writer=writer)
   plt.draw()
   # Comment out plt.show due to saving animation
   #plt.show()
