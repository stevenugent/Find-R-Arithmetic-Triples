from fractions import *
from genericUtils import INF
from genericUtils import ord2

#Finds the size of the group H giving triangles isometric
#to the triangle with angles pi/a, pi/b, pi/c; we need to
#divide by this number to find the number of *unique* hyperbolic
#triangles with angles k*pi/a, k*pi/b, k*pi/c.
#See Section 2 for explanation, notation, and proof.
def getMultiplicity(a,b,c):
    if a != INF and b != INF and c != INF:
        return getMultiplicityForCompact(a,b,c)
    else:
        assert c == INF # must be increasing
        return getMultiplicityForNoncompact(a,b)

# Get multiplicity for (a,b,c), where a,b,c are all finite
# integers. See Theorem 2.1.
def getMultiplicityForCompact(a,b,c):
    numEven = getNumEven(a,b,c)
    u = getNumPairsWithMaxGcd(2,a,b,c)
    if numEven == 0 or a == 2:
        return max(2,2**u)
    else:
        sizeOfH1 = 2*max(2,2**u)
        permutationsToCheck = [0]
        if b!=c:
            permutationsToCheck.append(1)
        if a!=c and a!=b:
            permutationsToCheck.append(2)
        for i in permutationsToCheck:
            abc = [0,0,0]
            for j in range(3):
                abc[j] = (a,b,c)[(j-i)%3]
            if u <= 1:
                ord2a = ord2(abc[0])
                if ord2a==ord2(abc[1]) and ord2(abc[2])<ord2a:
                    return sizeOfH1
            if u == 2:
                if abc[1] % 2 == 0 and abc[2] % 2 == 0 and ord2(abc[1]) == ord2(abc[2]):
                    if gcd(abc[0],abc[1]) == 1 and gcd(abc[0],abc[2])==1:
                        return sizeOfH1
        return sizeOfH1/2

# Get multiplicity for triange group (a,b,INF). See Theorem 2.12.
def getMultiplicityForNoncompact(a,b):
    if a == INF and b == INF:
        return 0
    elif b == INF:
        return 2
    else: # a and b finite
        g = gcd(a,b)
        sizeOfH1 = 0
        if g <= 2 and (a%2==0 or b%2==0):
            sizeOfH1 = 8
        elif g > 2 and a%2==1 and b%2==1:
            sizeOfH1 = 2
        else:
            sizeOfH1 = 4

        sizeOfH2 = 0;
        if g == 1:
            sizeOfH2 = 4
        else:
            sizeOfH2 = 2

        if ord2(a)==ord2(b) and gcd(a,b)!=2:
            return sizeOfH1
        else:
            return sizeOfH1/2

def getNumEven(a,b,c):
    numEven = 0
    for n in [a,b,c]:
        if n % 2 == 0:
            numEven += 1
    return numEven

def getNumPairsWithMaxGcd(maxGcd,a,b,c):
    result = 0
    for g in [gcd(a,b),gcd(b,c),gcd(c,a)]:
        if g <= maxGcd:
            result += 1
    return result
