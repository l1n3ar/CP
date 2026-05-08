import sys

from collections import *
from math import *
from bisect import *
from heapq import *

input = sys.stdin.readline

n = int(input())

def solve(n):

    res = ''
    res+=str(n)

    while(n!=1):
        if n%2 == 0:
            n = n//2
        else:
            n = n*3+1
    
        res+=' '+str(n)

    print (res)
    
       

solve(n)