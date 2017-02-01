#!/usr/bin/env python

def fib():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b

gen = fib()
for i in range(100):
    print(gen.next())
