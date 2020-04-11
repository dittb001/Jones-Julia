# Error hunting
from math import pi
h = 5.0
b = 2.0
r = 1.5

area_parallelogram = h*b
print ("The area of the parallelogram is {:.3f}.".format(area_parallelogram))

area_square = b**2
print ("The area of the square is {}.".format(area_square))

area_circle = pi*r**2
print ("The area of the circle is {:.3f}.".format(area_circle))

volume_cone = 1.0/3*pi*r**2*h
print ("The volume of the cone is {:.3f}.".format(volume_cone))
