# list certain special polys

from VSCPolyDrawer import *

def getBigPoly(n):
    result=[]
    for i in range(0,n):
        #if i%4 ==0 : result.append((i,0))
        #elif i%4==1: result.append((n-1,i))
        #elif i%4==2:result.append((n-i,n))
        #else: result.append((0,i))
        if i<=n/4:
            result.append((i*4,0))
        elif i<n/2:
            result.append((n-1,(i-(n/4))*4))
        elif i<n*3/4:
            result.append(((n-1)-(i-n/2)*4,n-1))
        else:
            result.append((0,(n-1)-(i-n*3/4)*4))
    return result
def main():
    n=21
    print (getBigPoly(n))
    drawNow(getBigPoly(n))

if  __name__ =='__main__':
    main()