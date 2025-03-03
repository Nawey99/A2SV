# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

def solution(stones_pr,sorted_s_pr):
    ans = 0
    tar,l,r = map(int,input().split())
    if tar == 1:
        ans = stones_pr[r] - stones_pr[l-1]
    else:
        ans = sorted_s_pr[r] - sorted_s_pr[l-1]
    return ans

n = int(input())
stones = list(map(int,input().split()))
sorted_s = sorted(stones)
sorted_s_pr = [0]
stones_pr = [0]
for i in range(n):
    sorted_s_pr.append(sorted_s_pr[-1]+sorted_s[i])
    stones_pr.append(stones[i] + stones_pr[-1])
cases = int(input())
for i in range(cases):
    print(solution(stones_pr,sorted_s_pr))