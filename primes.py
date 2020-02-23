ODD_PRIMES = [3]

def getIthOddPrime(i):
    extend(i)
    return ODD_PRIMES[i]

# Maximum non-diviving prime of the ith element
# of an r-arithmetic triple
def findMaxNDPIndex(r,i):
    prod = 1
    j = r
    extend(j)
    p = ODD_PRIMES[j]
    while prod < primeProdBound(p,i):
        j += 1
        p = getIthOddPrime(j)
        prod *= getIthOddPrime(j-r)
    return j-1

def primeProdBound(p,i):
    if i == 0:
        return 12*p*p*p*(2*p+1)
    if i == 1:
        return 16*p*p*p*p*p*(2*p+1)*(2*p+1)
    if i == 2:
        return 16*p*p*p*p*p
    if i == 3:
        return 8*p*p*p

def extend(i):
    # First potential new prime to check
    n = ODD_PRIMES[len(ODD_PRIMES)-1]+2
    while len(ODD_PRIMES) <= i:
        prime = True
        for p in ODD_PRIMES:
            if n%p == 0:
                prime = False
        if prime:
            ODD_PRIMES.append(n)
        n += 2

def getUpperBounds(p,i):
    if i == 0:
        return (3*p, 4*p, p*(2*p+1))
    if i == 1:
        return (2*p,2*p*(p+1),4*p*p*p*(p+1))
    if i == 2:
        return (2*p,2*p,4*p*p*p)
    if i == 3:
        return (2*p,2*p,2*p)
    else:
        assert False
