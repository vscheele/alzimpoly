# this code checks whether two lines intersect http://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ("(" + str(self.x) + "," + str(self.y) + ")")

    def __repr__(self):
        return str(self)

def ccw(A, B, C):
    return (C.y - A.y) * (B.x - A.x) >= (B.y - A.y) * (C.x - A.x)



def intersection(s1, s2):
        segment_endpoints = []
        left = max(min(s1[0], s1[2]), min(s2[0], s2[2]))
        right = min(max(s1[0], s1[2]), max(s2[0], s2[2]))
        top = max(min(s1[1], s1[3]), min(s2[1], s2[3]))
        bottom = min(max(s1[1], s1[3]), max(s2[1], s2[3]))

        if top > bottom or left > right:
            segment_endpoints = []
            #print 'NO INTERSECTION'
            #print segment_endpoints
            return False

        elif top == bottom and left == right:
            segment_endpoints.append(left)
            segment_endpoints.append(top)
            #print 'POINT INTERSECTION'
            #print segment_endpoints
            return True
        else:
            segment_endpoints.append(left)
            segment_endpoints.append(bottom)
            segment_endpoints.append(right)
            segment_endpoints.append(top)
            #print 'SEGMENT INTERSECTION'
            #print segment_endpoints
            return True

def intersect2(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def intersect3(A, B, C, D):
    if A.x == B.x:
        return not (C.x == D.x and A.x != C.x)
    elif C.x == D.x:
        return True
    else:
        m1 = (A.y - B.y) / (A.x - B.x)
        m2 = (C.y - D.y) / (C.x - D.x)
        return m1 != m2


def intersect(A, B, C, D):
    return intersection([A.x,A.y,B.x,B.y],[C.x,C.y,D.x,D.y])