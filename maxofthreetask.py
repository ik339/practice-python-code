#maxproduct of three of any triplet. non-empty array
#n is integer with range of 3-100,000.
#each element of array is integer between -1000 and 1000.
import nums as num
from _testcapi import INT_MIN
from numpy import array

a = array([-3, 1, 2, -2, 5, 6]) #positions 1,2,5 will give max.
b = sorted(a, reverse=True)
print(b)

def max3(b):
    prod = b[0] * b[1] * b[2]
    prod2 = (b[3] * b[4] * b[5])
    if prod > prod2:
        print(prod)
    else:
        print("wrong")
        return max3(b)
print (max3(b))



#position 0,1,2 vs 3,4,5? compare and choose the greater one. use if else?

