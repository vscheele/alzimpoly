################################################################################
#
# Solver for a differrent approach: take a large polygon with n number of vertices
#   - mutate the polygons and score them according to their area and validity
#   - Challenge is to find a suitable factor for scoring.
#
#
#
##################################################################################

from PolySpec import *
import copy, random


#simpler, has no "to pop" members compared to the Vscpoly class
from VSCAlzim import distanceToToupleFast, findAreaTouple, getslopeTouple, doesintersectPoint, doesintersectTuple
from VSCPolyDrawer import PolyDrawer


class SimplePoly:
    nsize=0
    points=[]
    slopes=[]
    length=0
    score=-1
    xs=-1
    ys=-1
    area=-1
    diffslopes=-1 # number of different slopes

    def __init__(self,list):
        self.points=list
        self.nsize=len(list)
        self.slopes=[]
        for i in range(1,len(list)):
            self.length+=distanceToToupleFast(list[i-1],list[i])
            newslope=getslopeTouple(list[i-1],list[i])
            if newslope not in self.slopes:
                self.slopes.append(newslope)
        XSFACTOR, YSFACTOR, AREAFACTOR, SLOPEFACTOR = 1, 1, 1, 1
        # count number of different x
        self.xs = len(set([seq[0] for seq in self.points]))
        # count number of different y
        self.ys = len(set([seq[1] for seq in self.points]))
        # area should be large
        self.area = findAreaTouple(self.points)
        #self.score=scoresimplepoly(self)
        self.diffslopes=len(set(self.slopes))
        self.score=scoresimplepoly(self)

    def getCopy(self):
        dup=copy.deepcopy(self)
        return dup

def mutateFromBig(poly1):
    newpoints=[]
    mutationtrys=10
    for p in poly1.points:
        counttry=0
        found=False
        while counttry<mutationtrys and not found:
            newx=max(0,min(len(poly1.points),(p[0] +  random.randint(-2,2))))
            newy=max(0,min(len(poly1.points),(p[1] + random.randint(-2, 2))))
            if len(newpoints)>1 and doesintersectTuple(newpoints[-1],(newx,newy),newpoints ):
                counttry+=1
            else:
                newpoints.append((newx,newy))
                found=True
                break
        if not found:
            return [] #this will not lead to a valid polygon, enough tries!
    return SimplePoly(newpoints)


def mutateFromBig2(poly1):
    ppoints=poly1.points
    mutationtrys=20
    counttry=0
    while counttry<mutationtrys:
        randindex=random.randint(0,len(ppoints)-1)
        p=ppoints[randindex]
        newx = max(0, min(len(ppoints), (p[0] + random.randint(-2, 2))))
        newy = max(0, min(len(ppoints), (p[1] + random.randint(-2, 2))))
        if doesintersectTuple(ppoints[(randindex-1)%len(ppoints)], (newx, newy), ppoints[:randindex]) or doesintersectTuple(ppoints[(randindex-1)%len(ppoints)], (newx, newy), ppoints[randindex+1:]):
            counttry += 1
        else: #found
            ppoints[randindex]=(newx,newy)
            return ppoints
    print "nosolution found...."
    return[]

currentindex=1 # used to cycle through the polygon
maxtranslation=3 # maximumtranslation

def mutateFromBig3(poly1):
    global currentindex
    ppoints = copy.deepcopy(poly1.points)
    cpoint=ppoints[currentindex]
    newpoints,newpolys=[],[]
    for xtrans in range(-1*maxtranslation,maxtranslation): # build new points "square"
        for ytrans in range(-1 * maxtranslation, maxtranslation):
            newpoints.append((cpoint[0]+xtrans,cpoint[1]+ytrans))
    #building a line with a gap at the changed index
    if currentindex==0:
        overlappoly=ppoints[2:-1]
    elif currentindex==1:
        overlappoly=ppoints[3:]
    elif currentindex==len(ppoints)-2:
        overlappoly =ppoints[:-3]
    elif currentindex==len(ppoints)-1:
        overlappoly =ppoints[1:-2]
    else:
        overlappoly=ppoints[:currentindex-2]+ppoints[currentindex+2:]
    for p in newpoints:
        if not doesintersectTuple(ppoints[(currentindex-1)%len(ppoints)],p,overlappoly):
            if not doesintersectTuple(p, ppoints[(currentindex +1)%len(ppoints)],  overlappoly):
                newpoly=SimplePoly(ppoints[:currentindex]+[p]+ppoints[currentindex+1:])
                newpolys.append(newpoly)
    newpolys.sort(key=lambda x: x.score, reverse=True)
    currentindex=(currentindex+1)%len(ppoints)
    return newpolys[0]

def scoresimplepoly(poly1):
    XSFACTOR,YSFACTOR,AREAFACTOR,SLOPEFACTOR=1,1,1,1
    #count number of different x
    xs = len(set([seq[0] for seq in poly1.points]))
    #count number of different y
    ys = len(set([seq[1] for seq in poly1.points]))
    #area should be large
    area= findAreaTouple(poly1.points)
    #number of slopes should be high
    numslopes=len(set(poly1.slopes))
    score=XSFACTOR*xs+YSFACTOR*ys+AREAFACTOR*area+SLOPEFACTOR*numslopes
    return score

def main():
    n=23
    spread=1
    steps=0
    podraw=PolyDrawer()
    solutions=[]
    #initialize first polygon
    polylist=[SimplePoly(getBigPoly(n))]
    #loop until solution is found
    while steps<100000 and polylist:
        # sort by score
        polylist.sort(key=lambda x: x.score, reverse=False)
        bestitem=polylist.pop()
        for i in range(0,spread):
            newpoly=mutateFromBig3(bestitem)
            if newpoly:
                polylist.append(newpoly)
        if steps%1==0:
            podraw.drawNewPoly(bestitem.points)
            print "xs:"+str(bestitem.xs)+" ys:"+str(bestitem.xs)+" diffslopes:"+str(bestitem.diffslopes)+"score:"+str(bestitem.score), bestitem.points
        steps+=1

if  __name__ =='__main__':
    main()