#!/usr/bin/env python

for i in range(101):
    string = ''
    string += 'Fizz' if i % 3 == 0 else ''
    string += 'Buzz' if i % 5 == 0 else ''

    if string:
        print(string)
    else:
        print(i)


