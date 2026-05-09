import sys

input = sys.stdin.readline

def solve(k,d,a):

    cnt = 0
    d.sort()
    a.sort()

    i,j = 0,0
    while (i < len(d) and j < len(a)):
        desired = d[i]
        actual = a[j]

        if actual <= desired: 
            if (desired - k) <= actual <= (desired + k) : 
                cnt+=1
                i+=1
            #Either bought or nobody later can buy    
            j+=1
        else:
            #desired < actual
            if (desired - k) <= actual <= (desired + k):
                 cnt+=1
                 #person got, move on
                 i+=1
                 j+=1
            else:
                #It is possible that the next person might get it
                i+=1

    print(cnt)

arr = list(map(int, input().split()))
k = arr[2]
d = list(map(int, input().split()))
a = list(map(int, input().split()))

solve(k,d,a)