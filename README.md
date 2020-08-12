![Python](https://img.shields.io/pypi/pyversions/3) [![DOI](https://zenodo.org/badge/286806261.svg)](https://zenodo.org/badge/latestdoi/286806261)
# Solar Orbit Animation With Matplotlib and Python
Three dimensional plots and animation are useful for visualizing scientific computation solutions such as ODE and PDES. Some of the very advanced Matplotlib libraries include: (1). Support for Latex formated labels and texts. (2). High quality output supporting format such as PNG, PDF, SVG, and PGF. (3). GUI for interactively exploring figures.

The most important objects are figures, axes, and lines. In this simple project, we explore the functionaily for line ploting and animation in 3D. We then save the animation film as MP4 file to the local disk.
### Orbit Data
We download the orbit.npz file which contains the orbits for Mercury, Venus, Earth, and Mars. The orbits are stored as 3D numpy array for each of the planets. For each planets, there are three columns of orbits in X, Y, and Z coordinates respectively. The center of the solar system is the Sun. All planets relative to the Sun are expressed in the astronomical units. That is the distance between Earth and Sun which is approximately 150 million kilometers.
The loadData function processes the oribits from the downloaded npz file. This function returns coordinate of matrics in dimension of 1400 X 3 for Mercury, Venus, Earth, and Mars respectively. That is there are 1400 rows of coordinate for each of the columns. The matrices will be stored in Data.
### Ploting
The plt.figure() creates a matplotlib.figure.Figure object. Both 3D ploting and animation require to define the figure object. The figure object allows the animation to be updated and modified.
Axes are spaces to plot on. It is created by the add_subplot() function. Figures have multiple axes.
We plot the Sun, planets orbit lines, and planets in three seperate plots. The Sun is plotted at a fixed coordinate. Then we draw the oribit lines for each of the four planets. The orbit lines are not animated. Finally, we animate the four planets orbiting alone with the oribiting lines.
We call the FuncAnimate function to update the movement of the four planets. The coordinate data and plot information are passed into the function with parameter fargs. The update function will be taken by parameter func. We choose to save the animation film to disk. If you want to display the animation, please comment the ani.save call and uncomment plt.show().
### Updating Animation
We define the logic for updating the planets movement in update function. The update function has three parameters which are num, data, and line. Parameter num is defined for number of frames to be animated as whole. The seconde parameter is for the 3D coordinate data for each of the four planets. The final parameter is the plot objects for each of the four planets.
### Detail
For more details of the implementation, please read the Solar Orbit ipynb file.
