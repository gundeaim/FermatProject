import random
from math import floor


def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)


# The time complexity of mod_exp is O(n^3). If we add up each the time complexity of each sub part,
#we get O(n^2) and then multiply that by n because we run this recursively log base 2 (y) which is n.
# The space complexity is O(log(n)) this is because we are saving subsequent x's, y's, and z's everytime n halves.
#This gives a constant * log(n)
def mod_exp(x, y, N):

    #check to see if recursion can stop
    #time complexity is O(n) + some constant for the check and return
    if y == 0:
        return 1

    #recursive calls until y hits 0 it will then work backwards
    #time complexity is O(n^2) for the division + some constant for setting the value
    z = mod_exp(x, floor(y / 2), N)

    #if even we will square the current answer
    #time complexity O(n^2) + O(n^2) + some constant
    if (y % 2) == 0:
        return (pow(z, 2)) % N

    #if odd we will square the current answer and include one more x
    #time complexity is O(n^2) + O(n^2) + O(n^2) + some constant
    else:

        return ((pow(z, 2) * x ) % N)
	

#The time complexity of fprobability is O(n^2) because we multiplying
# .5 k times and then doing one subtraction.
# Space Complexity is O(1)

def fprobability(k):
    return 1 - (pow(.5, k))


#The time complexity of mprobability is O(n^2) because we multiplying
# .25 k times and then doing one subtraction. Space Complexity is O(1)
def mprobability(k):
    return 1 - (pow(.25, k))


#The total time complexity of fermat is O(k * n^3)
#Space Complexity O(log(n)) because it utilizes mod_exp which is O(log(n)) and then adds 1 for storing a.
def fermat(N,k):

    #we will generate k number of a's to test primality
    #Time complexity is 2 steps done k times
    for x in range(k):
        a = random.randint(2, N-1)
        #Time complexity is O(n^3)
        if mod_exp(a, N-1, N) != 1:
            return 'composite'
    #if mod_exp never returned a non 1 number we can return prime.
    return 'prime'


#The time complexity of miller-rabin is O(k * n^3).
#Space Complexity is O(log(n)) because it utilizes mod_exp which is
# O(log(n)) and then adds 1 for storing a, z, & expN.
def miller_rabin(N,k):

    #we will generate k number of a's to test primality
    #time complexity for loop will run k times
    for x in range(k):
        #1 step
        a = random.randint(2, N-1)
        #O(n^3)
        z = mod_exp(a, N - 1, N)
        #tests if the return is 1 or -1 else it will return composite
        #1 step
        if (z == 1) or (z == N-1):
            expN = N - 1
            #while loop takes the sqaure root of the exponent until it is odd
            #time complexity of while loop log base 2 (expN)
            while expN % 2 == 0:
                #time complexity O(n^2)
                expN = expN/2
                #checks what the previous z value is
                #time complexity O(n^3)
                if z == 1:
                    z = mod_exp(a, expN, N)
                    if (z != 1) and (z != N-1):
                        return 'composite'
        else:
            return 'composite'
    return 'prime'

