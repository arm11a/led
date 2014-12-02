import numpy
from math import *
from numpy import *

DEBUG = True;

class Trilateration:
    _P1 = array([0, 0])
    _P2 = array([1, 0])
    _P3 = array([0, 1])
    
    def __init__(self, P1, P2, P3):
        self._P1 = P1
        self._P2 = P2
        self._P3 = P3
    
    def Calculate(self, DistA, DistB, DistC):
        #from wikipedia
        #transform to get circle 1 at origin
        #transform to get circle 2 on x axis
        ex = (self._P2 - self._P1)/(numpy.linalg.norm(self._P2 - self._P1))
        i = dot(ex, self._P3 - self._P1)
        ey = (self._P3 - self._P1 - i*ex)/(numpy.linalg.norm(self._P3 - self._P1 - i*ex))
        #ez = numpy.cross(ex,ey)
        d = numpy.linalg.norm(self._P2 - self._P1)
        j = dot(ey, self._P3 - self._P1)
        
        #from wikipedia
        #plug and chug using above values
        x = (pow(DistA,2) - pow(DistB,2) + pow(d,2))/(2*d)
        y = ((pow(DistA,2) - pow(DistC,2) + pow(i,2) + pow(j,2))/(2*j)) - ((i/j)*x)
        
        #print x, y
        
        # only one case shown here
        #z = sqrt(pow(DistA,2) - pow(x,2) - pow(y,2))
        
        #triPt is an array with ECEF x,y,z of trilateration point
        #triPt = P1 + x*ex + y*ey #+ z*ez
        
        #convert back to lat/long from ECEF
        #convert to degrees
        #lat = math.degrees(math.asin(triPt[2] / earthR))
        #lon = math.degrees(math.atan2(triPt[1],triPt[0]))
        return x,y

