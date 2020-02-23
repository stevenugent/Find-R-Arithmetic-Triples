from fractions import *

INF = -1

#return sign of range, or 0 if includes 0    
def signOf(range):
    if range[1] < 0:
        return -1
    elif range[0] > 0:
        return 1
    else:
        return 0

# r=[a,b], s=[c,d].
# If a<x<b, c<y<d, return whether a-d<0<b-c
# if true, x might be equal to y
# if false, x!=y
def eq(r, s):
    return r[0]-s[1] <= 0 and r[1]-s[0] >= 0

#returns the lcm of three numbers
def lcm3(a,b,c):
    nums = [a,b,c]
    for i in range(len(nums)):
        if nums[i] == INF:
            nums[i] = 1
    return lcm2(lcm2(nums[0],nums[1]),nums[2])

#returns the lcm of two numbers
def lcm2(a,b):
    return a*b/gcd(a,b)

#returns the highest power of 2 dividing x
def ord2(x):
    result = 0
    while(x % 2 == 0):
        x = x / 2
        result += 1
    return result
