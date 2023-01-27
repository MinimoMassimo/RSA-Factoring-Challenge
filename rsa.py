#!/usr/bin/python3

import random
import math

def modular_pow(base, esponente, modulo):
    '''
    calculates (base**esponenente)%modulo
    '''

    res = 1

    while esponente > 0:
        #if y is odd then multiply the base by the result
        if esponente and 1:
            res = (res * base) % modulo

        esponente = esponente >> 1
        base = (base * base) % modulo

    return res

def PollardRho(n):
    '''
    returns prime divisor for n
    '''

    if n == 1:
        return n

    if n % 2 == 0:
        return 2

    #pick random x and c
    x = random.randint(0, 2) % (n - 2)
    y = x
    c = random.randint(0,1) % (n - 1)

    #initializing divisor (i.e. the result)
    d = 1

    while (d == 1):
        #tortoise move: x(i+1) = f(x(i))
        x = modular_pow(x, 2, n) + c + n) % n

        #hare move: y(i+1) = f(f(y(i)))
        y = modular_pow(y, 2, n) + c + n) % n
        y = modular_pow(y, 2, n) + c + n) % n

        #check gcd of |x-y| and n
        d = math.gcd(abs(x - y), n)

        #if algo failed to find prime factor retry with chosen x and c
        if d == n:
            return PollardRho(n)

    return d

f = open(sys.argv[1], "r")
lines = f.readlines()

for n in lines:
    n = int(n.strip())
    res = PollardRho(n)
    print("{}={}*{}".format(n, d, int(n/d))
