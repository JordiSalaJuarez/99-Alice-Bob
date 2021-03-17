#!/usr/bin/env python3

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

