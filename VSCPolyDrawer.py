#######################################################################
#
# Valentin Scheele
#
# Part of Python Learning Exercises:
# - Write a class which creates an manages a Matplotlib TK Window
# - This Windows shows a coordinate system, draws given polygons
# - Writes some information in the coordinate system (maybe later into a textares?
# - Clears the content to draw a fresh poly
#
#######################################################################

from VSCPoint import *
#from VSCAlzim import *              #maybe this should be removed
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import time

class PolyDrawer:
    started = False
    plt=0
    currentPlot=0 # holds the current figure, is deleted when clean is called.
    fig=0
    def __init__(self): #initializes basic values. Open if it already calls createWindow
        self.started=True
    def createWindow(self):
        plt.ion()
        self.fig = plt.figure()
        return True
    def drawNewPoly(self,listOfPoints,xmax=-1,ymax=-1):  # draws a Poly in the Window
        verts = listOfPoints
        verts.append(verts[0])  # add first point as last (close the polygon)
        codes = [1]
        codes[0] = Path.MOVETO # move to the point where we start drawing
        for v in range(0, len(verts) - 2): # draw the lines
            codes.append(Path.LINETO)
        codes.append(Path.CLOSEPOLY)
        path = Path(verts, codes)
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        patch = patches.PathPatch(path, facecolor='orange', lw=2)
        ax.add_patch(patch)
        ax.set_xlim(0, max([x[0] for x in verts]) )  # x
        ax.set_ylim(0, max([x[1] for x in verts]) )  # y
        plt.grid()
        plt.pause(.1)

    def clean(self):  # cleans the PolyDrawer (removes all existing polys and text from the plot
        self.fig.clear()
        return True

def main():
    #plt.ion()
    #plt.plot([1.6, 2.7])

    pd=PolyDrawer()
    pd.createWindow()
    pointlist=[(1,1),(2,2),(4,1),(4,0.5)]
    pd.drawNewPoly(pointlist)
    pointlist=[(1,0),(2,2),(4,1),(3,0.5)]
    pd.drawNewPoly(pointlist)
    plt.ioff()
    plt.show()

if  __name__ =='__main__':
    main()