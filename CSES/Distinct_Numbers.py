import sys
input = sys.stdin.readline

def solve(arr):
   
   #O(nlogn)
   arr.sort()
   cnt = 1
   for i in range(1,len(arr)):
      if arr[i] != arr[i-1] : cnt+=1
    
   print(cnt)

   ## Set method is lower in time complexity but for some reason CSES doesn't accept it
   ## O(n)
   ## print(len(set(arr)))

n = int(input())
arr = list(map(int, input().split()))

solve(arr)


