import math
def distance(x1, y1, x2, y2):
    a=(x2-x1)**2
    b=(y2-y1)**2
    c=a+b
    d=math.sqrt(c)
    print(d)

distance(2,5,6,9)
