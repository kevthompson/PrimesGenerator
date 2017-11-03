#!/bin/python
import math
import time
import bisect
import fractions

def generateSumPrimes(limit):
    length = 1
    primes = [2, 3, 5, 7]
    while 1:
        groupOne = primes[:length+1]
        groupTwo = [1] * (length+1)
        length += 1

        # change the groups
        for j in range(2**(length-1)): # for each arrangement,

            productOne = reduce(lambda x, y: x * y, groupOne, 1)
            productTwo = reduce(lambda x, y: x * y, groupTwo, 1)
            productSum = productOne + productTwo    # get the productSum for radicals

            for zap in range(1, primes[length]**2):
                if(productOne == 1):
                    z = 1
                else:
                    z = zap
                # if z is a multiple of productOne and is coprime to productTwo
                if(fractions.gcd(productOne, z) == productOne and fractions.gcd(productTwo, z) == 1):
                    if(productTwo == 1):
                        productSum = z+1
                        if(productSum < primes[length]**2 and productSum < limit and productSum not in primes):
                            bisect.insort(primes, productSum)
                    else:
                        y = 0
                        while y-z < primes[length]**2:
                            y += 1
                            # if y is a multiple of productTwo and is coprime to productSum
                            if(fractions.gcd(productTwo, y) == productTwo and fractions.gcd(productOne, y) == 1):
                                productSum = z + y
                                if(productSum < primes[length]**2 and productSum < limit and productSum not in primes):
                                    bisect.insort(primes, productSum)

            #print(groupOne, groupTwo, primes)
            for index in range(length):
                if (groupTwo[-index] == 1):
                    groupTwo[-index] = groupOne[-index]
                    groupOne[-index] = 1
                    break

        #print(groupOne, groupTwo, productDiff, primes, primes[length])
        if primes[length]**2 >= limit:
            return primes

def generateDiffPrimes(limit):
    length = 1
    primes = [2, 3, 5]
    while 1:
        groupOne = primes[:length+1]
        groupTwo = [1] * (length+1)
        length += 1

        # change the groups
        for j in range(2**(length-1)): # for each arrangement,


            productOne = reduce(lambda x, y: x * y, groupOne, 1)
            productTwo = reduce(lambda x, y: x * y, groupTwo, 1)
            productDiff = abs(productOne - productTwo)    # get the productDiff for radicals

            for zap in range(1, primes[length]**2):
                if(productOne == 1):
                    z = 1
                else:
                    z = zap
                # if z is a multiple of productOne and is coprime to productTwo
                if(fractions.gcd(productOne, z) == productOne and fractions.gcd(productTwo, z) == 1):
                    if(productTwo == 1):
                        productDiff = abs(z-1)
                        if(productDiff != 1 and productDiff < primes[length]**2 and productDiff < limit and productDiff not in primes):
                            bisect.insort(primes, productDiff)
                    else:
                        y = 0
                        while y-z < primes[length]:
                            y += 1
                            # if y is a multiple of productTwo and is coprime to productOne
                            if(fractions.gcd(productTwo, y) == productTwo and fractions.gcd(productOne, y) == 1):
                                productDiff = abs(z - y)
                                if(productDiff != 1 and productDiff < primes[length]**2 and productDiff < limit and productDiff not in primes):
                                    bisect.insort(primes, productDiff)

            #print(groupOne, groupTwo, primes)
            for index in range(length):
                if (groupTwo[-index] == 1):
                    groupTwo[-index] = groupOne[-index]
                    groupOne[-index] = 1
                    break
            else:
                groupOne[index] = groupTwo[index]
                groupTwo[index] = 1

        #print(groupOne, groupTwo, productDiff, primes, primes[length])
        if primes[length]**2 >= limit:
            return primes
s = time.time()
output = generateDiffPrimes(121)
print output, len(output), time.time() -s
