import sys

from collections import *
from math import *


input = sys.stdin.readline


def solve(n,arr):
   res = 0
   for i in range(1,n):
      prev,curr = arr[i-1],arr[i]
      if curr >= prev : continue
      else : 
         arr[i] = arr[i-1]
         res+=prev-curr
      
   print(res)

n = int(input())
arr = list(map(int, input().split()))

solve(n,arr)