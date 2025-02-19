# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n,k,q = map(int,input().split())
rs = [0] *((2*(10**5))+2)
run_sum = [0] *((2*(10**5))+2)
for i in range(n):
    x, y = map(int,input().split())
    rs[x] += 1
    rs[y+1] -=1
for i in range(1,len(rs)):
    rs[i] += rs[i-1]
    
for i in range(1,len(rs)):
    if rs[i] >=k:
        run_sum[i] =1
for i in range(1,len(rs)):
    run_sum[i] += run_sum[i-1]
for i in range(q):
    count = 0
    x, y = map(int,input().split())
    print(run_sum[y]-run_sum[x-1])
