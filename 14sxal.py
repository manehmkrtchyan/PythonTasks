"14"
from cmath import pi
r = int(input(f"enter the radius of the circle: "))
def area(r):
    import math
    return pi * r ** 2

def volume(r):
    import math
    return (4 / 3) * pi * r ** 3
    
print(f"The are of the circle is {area} and the volume of the ball is {volume}")
