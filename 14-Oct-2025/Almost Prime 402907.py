# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

import sys
def I(): return int(sys.stdin.readline().strip())
def solution():
    n= I()
    count = 0
    for j in range(2,n+1):
        arr =[]
        for i in range(2,j):
            while j%i == 0:
                arr.append(i)
                j /=i
        if len(set(arr)) == 2:
            count +=1
    return count
 
cases = 1
for i in range(cases):
    print(solution())