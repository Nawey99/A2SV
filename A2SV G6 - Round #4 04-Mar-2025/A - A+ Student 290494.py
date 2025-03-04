# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A


def solution():
    count = 0
    ans = []
    mark = list(map(int,input().split()))
    Max = 0
    for i in range(3):
        Max = max(Max, mark[i])
    for i in mark:
        if i == Max:
            count +=1
    for i in mark:
        if Max == i and count == 1:
            ans.append(0)
        else:
            x = Max +1
            ans.append(x-i)
    return ans

# cases = 1
cases = int(input())
for i in range(cases):
    print(*solution())