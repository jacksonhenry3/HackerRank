#!/bin/python3

t = int(input().strip())
for a in range(t):
    n = int(input().strip())-1
    print(int(sum([n//abs(m)*m*(1+n//abs(m))//2 for m in [3,5,-15]])))
