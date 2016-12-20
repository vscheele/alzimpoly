# list certain special polys

from VSCAlzim import *
from VSCPolyDrawer import *

def getBigPoly(n):
    result=[]
    for i in range(0,n):
        if i%4 ==0 : result.append((i,0))
        elif i%4==1: result.append((n-1,i))
        elif i%4==2:result.append((n-i,n))
        else: result.append((0,i))
    return result
def main():
    print (getBigPoly(11))
    drawNow(getBigPoly(11))

if  __name__ =='__main__':
    main()