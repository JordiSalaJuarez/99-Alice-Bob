#!/usr/bin/env python3

"""
    Bob should play in a smart way to trick Alice into winning

"""

from random import choice

x = int(input())
while x % 3 == 0:
    print(x + choice([1,2]))
    x = int(input())

while x % 3 != 0:
    if x % 3 == 1:
        print(x+2)
    else:
        print(x+1)
    if x >= 99-2: break
    x = int(input())

