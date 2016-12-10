#this code checks whether two lines intersect http://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __str__(self):
		return ("(" + str(self.x) + ":" + str(self.y)+")")
	def __repr__(self):
		return str(self)

def ccw(A,B,C):
	return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)
def intersect(A,B,C,D):
	return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
