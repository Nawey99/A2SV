# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B


def solution():
    n,x = map(int,input().split())
    num = list(map(int,input().split()))
    num.sort()
    for i in range (n):
        y = num[i+n] - num[i]
        if y < x:
            return "NO"
    return 'YES'

# cases = 1
cases = int(input())
for i in range(cases):
    print(solution())