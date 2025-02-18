# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C


def solution():
    n = int(input())
    subs = list(map(int,input().split()))
    l = 0
    bmax = 0
    while l < n:
        if subs[l] >= 0:
            Max = 0
            while l<n and subs[l] > 0 :
                Max = max(Max, subs[l])
                l += 1
            bmax += Max
        else:
            Max = subs[l]
            while l<n and subs[l] < 0:
                Max = max(Max, subs[l])
                l+=1
            bmax += Max
    return bmax

# cases = 1
cases = int(input())
for i in range(cases):
    print(solution())