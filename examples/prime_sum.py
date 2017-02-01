#!/usr/bin/env python

def sieve(num=2000000):
    prime_tracker = [True] * (num+1)

    prime_tracker[0] = prime_tracker[1] = False

    for i in xrange(num+1):
        if prime_tracker[i]:
            for j in xrange(i+i,num+1,i):
                prime_tracker[j] = False

    return prime_tracker

a = sieve()

for i in xrange(1000000,len(a)):
    print((i, a[i]))

