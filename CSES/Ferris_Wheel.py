import sys

input = sys.stdin.readline


def solve(d,arr):

    arr.sort()
    cnt = 0
    i,j = 0,len(arr)-1

    while (i <= j):
        if arr[i] + arr[j] <= d:
            cnt+=1
            i+=1
        else:
            cnt+=1
        j-=1
        
    
    print(cnt)

n, max_allowed_weight = map(int, input().split())
w8s = list(map(int, input().split()))

solve(max_allowed_weight,w8s)