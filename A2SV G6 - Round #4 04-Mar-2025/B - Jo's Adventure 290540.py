# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B


def solution(fr,re):
    x,y=map(int,input().split())
    if x<y:
        return fr[y] - fr[x]
    else:
        return re[-y] - re[-x]


n,cases=map(int,input().split())
build = list(map(int,input().split()))
dam_fr=[0]
dam_re = [0]
re_pr = [0]
fr_pr=[0]
for i in range(1,n):
    if build[i]< build[i-1]:
        dam_fr.append(build[i-1]-build[i])
    else:
        dam_fr.append(0)
for i in range(n-2,-1,-1):
    if build[i]< build[i+1]:
        dam_re.append(build[i+1]-build[i])
    else:
        dam_re.append(0)
for i in range(len(dam_re)):
    re_pr.append(re_pr[-1]+dam_re[i])
    fr_pr.append(fr_pr[-1]+dam_fr[i])
for i in range(cases):
    print(solution(fr_pr,re_pr))