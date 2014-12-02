
import trilateration
from numpy import *


_P1 = array([0, 0])
_P2 = array([1, 0])
_P3 = array([0, 1])

test = trilateration.Trilateration(_P1, _P2, _P3)

print test.calculate(1.414,1,1)