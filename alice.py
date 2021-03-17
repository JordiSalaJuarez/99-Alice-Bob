#!/usr/bin/env python3
import sys
from subprocess import Popen, PIPE
from random import choice

"""
    Bob is given the number 1 by Alice and Bob has to reply to Alice with
    that number increased by 1 or 2, and Alice will do the same to Bob until
    someone sends 99, whoever sends 99 wins the game

"""

with Popen([sys.executable, '-u', 'bob.py'], stdin=PIPE, stdout=PIPE,
        universal_newlines=True, bufsize=1) as cat:
    print("0", file=cat.stdin, flush=True)
    print("Alice 0")
    while True:
        x = int(cat.stdout.readline())
        print(f"Bob {x}")
        if x == 99:
            print(">>> Bob won")
            break
        y = x+choice([1, 2])
        print(f"Alice {y}")
        if x >= 99:
            print(">>> Alice won")
            break
        print(y, file=cat.stdin, flush=True)
