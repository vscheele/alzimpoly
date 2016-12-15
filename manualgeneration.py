########################
###
### Pen and paper generation since for large n there is no AI solution found yet with my algorithm..
###
#########################

from VSCAlzim import *

ns=[7,11,17,23, 29, 37, 47, 59, 71, 83, 97, 113, 131, 149, 167, 191, 223, 257, 293, 331, 373, 419, 467, 521]

def genLowerArea(n):
    result=[]
    for i in range(1,n+1):
        if i==1:result.append((1,1))
        if i<n-3 and i>1:
            if i%2==0: result.append((i,n-i/2+1))
            else: result.append((i,i/2+1))
        if i==n-3:result.append((i,(n-1)/2+2))
        if i==n-2:result.append((i,(n-1)/2+3))
        if i==n-1:result.append((i,(n-1)/2+1))
        if i==n:result.append((i,(n-1)/2))
    return result


def genHigherArea(n):
    result=[]
    #case1: n/10 is odd
    if (n/2)%2==1:
        for i in range(1,n+1):
            if i==1:result.append((1,1))
            if i==2:result.append((2,n))
            if i==3:result.append((3,(n-1)/2))
            if i<n-3 and i>3:
                if i%2==0: result.append((i,n-i/2+1))
                else: result.append((i,i/2+1))
            if i==n-3:result.append((i,(n-1)/2+2))
            if i==n-2:result.append((i,(n-1)/2+3))
            if i==n-1:result.append((i,(n-1)/2+1))
            if i==n:result.append((i,2))
        return result
    else:
        for i in range(1,n+1):
            if i==1:result.append((1,1))
            if i==2:result.append((2,n))
            if i==3:result.append((3,2))
            if i==4:result.append((4,n-1))
            if i==5:result.append((5,(n-1)/2))
            if i<n-3 and i>5:
                if i%2==0: result.append((i,n-i/2+1))
                else: result.append((i,i/2+1))
            if i==n-3:result.append((i,(n-1)/2+2))
            if i==n-2:result.append((i,(n-1)/2+3))
            if i==n-1:result.append((i,(n-1)/2+1))
            if i==n:result.append((i,3))
        return result


for i in range(0,len(ns)):
    print genLowerArea(ns[i]),";"
    print genHigherArea(ns[i]),";"

if  __name__ =='__main__':
    drawPoly2(genHigherArea(521))
    drawPoly2(genLowerArea(521))