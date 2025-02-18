# Problem: Books - https://codeforces.com/contest/279/problem/B

n,t = map(int,input().split())
books = list(map(int,input().split()))
res = 0
r= 0
l = 0
Max = 0
while r<n and l<=r:
    res += books[r]
    if res > t:
        res -= books[l]
        l += 1
    Max = max(Max,r-l+1)
    r += 1
print(Max)
    