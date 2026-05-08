import sys

from collections import *
from math import *
from bisect import *
from heapq import *

input = sys.stdin.readline

def solve(n,arr):
  arr_sum = sum(arr)
  print((n*(n+1)//2) - arr_sum)
    

n = int(input())
arr = list(map(int, input().split()))

solve(n,arr)