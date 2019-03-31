#Solution to problem #10
#Python Program that displays a plot of the functions x, x**2 and 2**x in the range [0,4].
#Daria J. Ostrowska

#I import core scientific library Numpy as a container for my data and functions
import numpy as np
#I import the plotting functionality 
import matplotlib.pyplot as plt
xvals = np.arange(1.0, 5.0) #Define the grid in the range spacing from 1.0 to 4.0
yvals = xvals #Evaluate function on xvals
plt.plot(xvals, yvals) #Create line plot with yvals against xvals


#I import core scientific library Numpy as a container for my data and functions
import numpy as np
#I import the plotting functionality 
import matplotlib.pyplot as pylab
xvals1 = np.arange(1.0, 5.0) #Define the grid in the range spacing from 1.0 to 4.0
yvals1 = xvals1**2 #Evaluate function on xvals1
plt.plot(xvals1, yvals1) #Create line plot with yvals against xvals1


#I import core scientific library Numpy as a container for my data and functions
import numpy as np
#I import the plotting functionality 
import matplotlib.pyplot as pylab
xvals2 = np.arange(1.0, 5.0) #Define the grid in the range spacing from 1.0 to 4.0
yvals2 = 2**(xvals2) #Evaluate function on xvals2
pylab.plot(xvals2, yvals2) # Create line plot with yvals against xvals2

plt.show() # Show the figures

#Based on: http://courses.csail.mit.edu/6.867/wiki/images/3/3f/Plot-python.pdf

