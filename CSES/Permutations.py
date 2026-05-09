import sys

from collections import *
from math import *
from bisect import *
from heapq import *

input = sys.stdin.readline
# Single integer
# n = int(input())

# Multiple integers
# n, m = map(int, input().split())

# List of integers
# arr = list(map(int, input().split()))

# String input
# s = input().strip()

# List of strings
# arr = input().split()

# Matrix input
# grid = [list(map(int, input().split())) for _ in range(n)]

# Character grid
# grid = [list(input().strip()) for _ in range(n)]

# Multiple test cases
# t = int(input())
# for _ in range(t):
#     solve()

# ---------------------------------

def solve(n):
    if n == 1:
        print(1)
        return
    if n <= 3:
        print("NO SOLUTION")
        return
    
    evens = list(range(2, n+1, 2))
    odds  = list(range(1, n+1, 2))
    
    print(*evens + odds)

n = int(input())
solve(n)