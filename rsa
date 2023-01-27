#!/usr/bin/python3

import sys
import math


def factorization():
    f = open(sys.argv[1], "r")
    lines = f.readlines()

    for n in lines:
        n = int(n.strip())
        MAX = n / 2
        i = 2
        result = False
        if n % 2 != 0:
            MAX += 1
        while i <= MAX:
            if n % i == 0:
                print("{}={}*{}".format(n, int(n/i), i))
                result = True
                break
            else:
                i += 1
                MAX = n/i
        if not result:
            print("{}={}*{}".format(n, n, 1))
    f.close()


factorization()
