#########################################
#
# Valentin Scheele
# Al Zimmerman's new Programming Contest
# 1st try with drawing polygons and  some initial code
#
#########################################


POLYSEED=3 #max number of Polys generated from the old one in one iteration.
solutions=[]

import copy
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from VSCPoint import Point, intersect

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

# this method assumes that A.y differs from B.y
def getslope(A,B):
    return (float(A.y) - float(B.y)) / (float(A.x) - float(B.x))

class Vscpoly:
    size=5
    length=0.0
    xtopop=range(1,size)
    ytopop=range(1,size)
    #keeps track of all slopes already used
    slopesused={}
    selectedpoints=[Point(0, 0)]
    def __init__(self,size):
        self.size=size
        self.xtopop = range(1, size)
        self.ytopop = range(1, size)
    def printPoly(self):
        return "polysize:"+str(len(self.selectedpoints))+"\tlinelength:"+str(self.length)+"\tpoints:"+str(self.selectedpoints)
    def printPolyAli(self):
        transpoints  = [ Point(p.x+1,p.y+1) for p in self.selectedpoints ]
        return "polysize:"+str(len(self.selectedpoints))+"\tlinelength:"+str(self.length)+"\tpoints:"+str(self.selectedpoints)+"\tpoints:"+str(transpoints)
    def getPointlist(self):
        res=[]
        for p in self.selectedpoints:
            res.append((p.x,p.y))
        return res
    def getCopy(self):
        dup=copy.deepcopy(self)
        dup.xtopop = copy.deepcopy(self.xtopop)
        dup.ytopop = copy.deepcopy(self.ytopop)
        dup.slopesused = copy.deepcopy(self.slopesused)
        dup.selectedpoints = copy.deepcopy(self.selectedpoints)
        return dup

#poly must have all points selected<
def scorePoly(P):
    return P.slopesused.size

#translates all points +1 because 1 to n
def tra(list):
    return [Point(p[0]+1, p[1] + 1) for p in list]

def doesintersect(P1,P2,L): # Point, ListToCheck
    for i in range(0,len(L)-2):
        test=intersect(P1,P2,L[i],L[i+1])
       # print test,P1,P2,L[i],L[i+1]
        if intersect(P1,P2,L[i],L[i+1]) :
            return True
    return False


def mutateRandom(Poly1):  #gets Vscpoly and returns valid mutations from the original one by random
    result=[]
    xbucket=list(Poly1.xtopop)
    ybucket=list(Poly1.ytopop)
    random.shuffle(xbucket)
    random.shuffle(ybucket)
    pointsbucket=[(x,y) for x in xbucket for y in ybucket]
    while len(pointsbucket)>0 and len(result)<POLYSEED : # create up to Polyseed new Polygons
        newpoint=pointsbucket.pop()
        #newpoint=[(0, 0), (6, 1), (4, 2), (5, 3), (2, 6), (1, 4), (3, 5)][len(Poly1.selectedpoints)]
        newx=newpoint[0]
        newy=newpoint[1]
        newslope=getslope(Poly1.selectedpoints[-1], Point(newx, newy))
        #if newx==4 and newy==4:
        #    print "krit"
        if newslope not in Poly1.slopesused and not doesintersect(Poly1.selectedpoints[-1], Point(newx, newy), Poly1.selectedpoints): #new Slope not used and no intersection
            #lets create the new polygon!!
            newPoly=Poly1.getCopy()
            newPoly.selectedpoints.append(Point(newx, newy))
            newPoly.slopesused[newslope]=1
            newPoly.length+=newx*newx+newy*newy  #length of Poly
            #remove the used Points
            newPoly.xtopop.remove(newx)
            newPoly.ytopop.remove(newy)
            result.append(newPoly)
    return result

#calculates the area of a Vscpoly with the help of Numpy package
def findArea(P):
    x,y=[],[]
    for p in P.selectedpoints:
        x.append(p.x)
        y.append(p.y)
    return PolyArea(x,y)

def drawPoly(Poly1):
    verts=Poly1.getPointlist()
    verts.append((0,0))
    codes=[1]
    codes[0]=Path.MOVETO
    for v in range(0,len(verts)-2):
        codes.append(Path.LINETO)
    codes.append(Path.CLOSEPOLY)
    print codes
    print verts
    path = Path(verts, codes)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    patch = patches.PathPatch(path, facecolor='orange', lw=2)
    ax.add_patch(patch)
    ax.set_xlim(0,len(verts))
    ax.set_ylim(0,len(verts))
    plt.show()

def drawPoly2(list):
    a=Vscpoly(len(list))
    a.selectedpoints=[ Point(p[0],p[1]) for p in list]
    drawPoly(a)

polys=[Vscpoly(223)]
for i in range(0,3000):
    if len(polys)>0:
        poly1=polys.pop()
        if i % 100 == 0:  print "Step " + str(i) + poly1.printPoly()
        #print "ITERATION "+str(i)+" with size of "+str(len(polys))
        #print poly1.printPoly()
        if len(poly1.selectedpoints)==poly1.size:
            #closing the polygon may be a problem
            lastslope=getslope(poly1.selectedpoints[-1],Point(0,0))
            if lastslope not in poly1.slopesused and not doesintersect(poly1.selectedpoints[-1],Point(0,0),poly1.selectedpoints[1:]):
                solutions.append(poly1)
        else:
            newpolys=mutateRandom(poly1)
            polys = polys+newpolys

solutions.sort(key=lambda x: findArea(x), reverse=True)

for s in solutions:
    print "solution found with area: " + str(findArea(s)) + "\t" + s.printPolyAli()

drawPoly(solutions[0])
drawPoly(solutions[-1])
print solutions[0].printPolyAli()+str(findArea(solutions[0]))
print solutions[-1].printPolyAli()+str(findArea(solutions[-1]))
#[(0, 0), (1, 4), (3, 1), (2, 3), (4, 2), (0.0, 0.0)]
#solution found with area: 5.0	polysize:5	linelength:60.0	points:[(0,0), (2,4), (3,3), (1,2), (4,1)]	points:[(1,1), (3,5), (4,4), (2,3), (5,2)]

print doesintersect(Point(1,2),Point(0,0),[ Point(2,1), Point(4,3), Point(1,2)])
