# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from typing import Counter


def dis_char ():
    x = int(input())
    str = input()
    Max=0
    count = Counter(str)
    count1 = Counter()
    for i in range(x):
        count[str[i]] -= 1
        count1[str[i]] += 1
        if count[str[i]] == 0:
            del count[str[i]]
        Max = max(Max,len(count)+len(count1))
    print (Max)

x = int(input())
for _ in range(x):
    dis_char()
    