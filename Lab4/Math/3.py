import math


def ar():
    n=int(input())
    l=int(input())
    R=int(((n*(l**2)) / (4 * math.tan(math.pi / n))))
    print("Input number of sides:" ,n,"\nInput the length of a side:",l, "\nThe area of the polygon is:", R)



ar()