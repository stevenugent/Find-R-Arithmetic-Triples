import primes
import triangleUtils
import sys
from genericUtils import INF
from fractions import *

INF_STRING = 'oo'
A = 0
B = 1
C = 2

#Find all r-arithmetic triangle groups.
#(Also categorizes and outputs all triangle groups
#of arithmetic dimension <r) 
#See Algorithm 1.
def findRArithmetic(r=1):

    # Initialize dictionaries mapping r to the set of
    # arithmetic triples, respectiely for the compact
    # (all elements of triple are finite) and non-compact
    # cases
    arithmeticTriples = {}
    noncompact = {}
    for r in range(1,r+1):
        arithmeticTriples[r] = []
        noncompact[r] = []

    #Index of maximum non-dividing prime of r-arithmetric triple
    maxNDPInd = 0
    end = [0,0,0]
    
    for i in range(3):
        # Maximum non-dividing prime of ith element of triple
        maxNDPInd_i = primes.findMaxNDPIndex(r,i)
        # Bound on ith element of triple
        end_i = primes.getUpperBounds(primes.getIthOddPrime(maxNDPInd_i),i)
        # Bounds must be monotonically increasing
        for j in range(3):
            if end_i[j] > end[j]:
                end[j] = end_i[j]
        if maxNDPInd_i > maxNDPInd:
            maxNDPInd = maxNDPInd_i

    # Precompute list of primes
    maxPInd = maxNDPInd*r
    primes.extend(maxPInd)

    # For each value of a and b up to the bounds end[1], end[2],
    # check triples (a,b,c) for all valid c's up to end[3]
    check(INF, INF, INF, r, noncompact)
    for a in range(2, end[A]):
        check(a,INF,INF,r,noncompact)
        for b in range(max(a,3), end[B]):
            if b < end[A]:
                check(a,b,INF,r,noncompact)
            searchCs(r,a,b,end[C],maxNDPInd,arithmeticTriples)

    for i in range(1,r+1):
        print "number of compact ",i,"-arithmetic triples: ", len(arithmeticTriples[i])
        j = 1
        for triple in arithmeticTriples[i]:
            print triple, j
            j += 1
            print
        print "number of noncompact ",i,"-arithmetic triples: ", len(noncompact[i])
        for triple in noncompact[i]:
            print triple
            print

# Find all possible r-arithmetic triples (a,b,c) given a, b, upper bound of c,
# and maximum nondividing prime p, where p is the maxPInd'th odd prime.
# Add these to arithmeticTriples.
def searchCs(r,a,b,maxc,maxNDPInd,arithmeticTriples):
    for c in range(b,primes.getIthOddPrime(maxNDPInd)):
        check(a,b,c,r,arithmeticTriples)
    csToCheck = []
    boundToPrimes = mapBoundsToPrimes(r,a,b,maxc,maxNDPInd)
    divisors = [1]*r
    i = 0 # index in divisors
    for c in range(b,2*primes.getIthOddPrime(maxNDPInd)):
        check(a,b,c,r,arithmeticTriples)
    startc = max(b,2*primes.getIthOddPrime(maxNDPInd))
    for bound in sorted(list(boundToPrimes.keys())):
        checkMultiples(divisors,a,b,startc,bound,r,arithmeticTriples)
        maxq = 0
        for q in boundToPrimes[bound]:
            divisors[i] *= q
            i = (i+1)%r
            if q>maxq:
                maxq = q
        if not boundToPrimes[bound]: # if list empty, we've reached end[C]
            break
        done = True
        for divisor in divisors:
            if divisor < maxc:
                done = False
        if done:
            break
        startc = max(startc,bound)

# Map each bound on c to the primes associated to that bound. See algorithm 2.
def mapBoundsToPrimes(r,a,b,maxc, maxNDPInd):
    boundToPrimes = {}
    for j in range(r*maxNDPInd+1):
        q = primes.getIthOddPrime(j)
        bound = triangleUtils.getBound(a,b,q)
        if bound is not None:
            if bound not in boundToPrimes:
                boundToPrimes[bound] = []
            boundToPrimes[bound].append(q)
    boundToPrimes[maxc] = []
    return boundToPrimes

# Checks if each triangle group (a,b,c) is r-arithmetic, where c is
# a multiple of divisors between startc and bound associated to divisors
def checkMultiples(divisors,a,b,startc,bound,r,arithmeticTriples):
    for j in range(len(divisors)):
        divisor = divisors[j]
        if j > 0 and divisor == 1:
            return
        c = startc - startc%divisor
        if c < startc:
            c += divisor
        while c < bound:
            check(a,b,c,r,arithmeticTriples)
            c += divisor

# Check if (a,b,c) is r-arithmetic, and if so add to running list of triples
def check(a,b,c,r,arithmeticTriples):
    dim = triangleUtils.arithmeticDimension(a,b,c,r)
    if dim > 0 and dim <= r:
        triple = tripleToString(a,b,c)
        if triple not in arithmeticTriples[dim]:
            arithmeticTriples[dim].append(triple)

def tripleToString(a,b,c):
    return "(" + toString(a) + ", " + toString(b) + ", " + toString(c) + ")"

#converts a in Z U {INF} to a string
def toString(a):
    if a == INF:
        return INF_STRING
    return str(a)

def main():
    r = 1
    if (len(sys.argv) > 1):
        r = int(sys.argv[1])
    findRArithmetic(r)

if __name__ == "__main__":
    main()
