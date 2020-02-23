import multiplicityUtil
import genericUtils
from genericUtils import INF
from fractions import *

#return the curvature of the triangle with angles
#k*pi/a, k*pi/b, k*pi/c
def getCurvature(a,b,c,k):
    if a == INF or b == INF or c == INF:
        return -1
    var = reduceAngle(k,c)*a*b
    zero1 = c*abs(reduceAngle(k,a)*b + reduceAngle(k,b)*a - a*b)
    zero2 = c*(a*b-abs(reduceAngle(k,a)*b - reduceAngle(k,b)*a))

    if var == zero1 or var == zero2:
        return 0
    elif var > zero1 and var < zero2:
        return 1
    else:
        return -1

#returns arithmetic dimension of (a,b,c), if it
#is <=r; otherwise, returns 0.
def arithmeticDimension(a,b,c,r=1):

    if a == INF and b == INF and c == INF:
        return 1
    multiplicity = multiplicityUtil.getMultiplicity(a,b,c)

    m = 2*genericUtils.lcm3(a,b,c)
    numHyperbolic = 0
    for k in range(max(2,m)):
        if gcd(m,k) == 1:
            curvature = getCurvature(a,b,c,k)
            if curvature < 0:
                numHyperbolic += 1
                if numHyperbolic > multiplicity * r:
                    return 0 # dim > r

    return numHyperbolic/multiplicity


def getBound(a,b,q):
    if a%q == 0 or b%q == 0:
        return None
    denom = abs(reduceAngle(q,a)*b + reduceAngle(q,b)*a - a*b)
    if denom != 0:
        bound = int(q*a*b)/int(denom)+1
        assert isinstance(bound,int)
        return bound

# reduce k to k_n < n, where cos(k*pi) = cos(k_n*pi)
def reduceAngle(k,n):
    reduced = k%(2*n)
    if reduced > n:
        reduced = 2*n - reduced
    return reduced

