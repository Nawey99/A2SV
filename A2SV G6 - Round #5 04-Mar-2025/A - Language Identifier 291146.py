# Problem: A - Language Identifier - https://codeforces.com/gym/591928/problem/A


def solution():
    dic = {0:'FILIPINO',1:'JAPANESE',2:'JAPANESE',3:'KOREAN'}
    y = ["po", "masu", "desu", "mnida"]
    
    x = input().strip()
    
    for i in range(len(y)):
        suffix = y[i]
        if x[-len(suffix):] == suffix: 
            return dic[i]

# cases = 1
cases = int(input())
for i in range(cases):
    print(solution())