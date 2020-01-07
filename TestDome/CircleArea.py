from math import pi
from math import sin
def areas(r, a):
    """
    :param r: (float) The radius of the circle.
    :param a: (float) The angle of the segment.
    :returns: (list) (A list of two elements containing the area inside, and area outside the circle, in that order.)
    """
    segmentArea = (r*r)*(a*pi/180 - sin(a*pi/180))/2
    allArea = pi * r * r
    outsideArea = allArea - segmentArea
    return segmentArea, outsideArea

print(areas(10, 90));