
import trilateration
from numpy import *


_P1 = array([0, 0])
_P2 = array([2, 0])
_P3 = array([0, 2])

test = trilateration.Trilateration(_P1, _P2, _P3)

for i in range(1,11):
    print test.Calculate(1.414*i,i,i)
