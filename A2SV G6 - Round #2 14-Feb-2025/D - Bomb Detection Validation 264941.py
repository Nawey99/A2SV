# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

x = list(map(int,input().split()))
n = x[0]
m =x[1]
arr = []
flag = 'YES'
for _ in range(n):
    y = input()
    arr.append(y)
d = [-1,0,1]
for i in range(n):
    for j in range(m):
        count = 0
        if arr[i][j] == '*':
            continue
        for di in d:
            for dj in d:
                x  = di + i
                y = dj + j
                if 0 <= x < n and 0 <= y <m and [x,y] != [i,j]:
                    if arr[i][j] == '.' and arr[x][y] == '*': flag = 'NO'
                    elif arr[x][y] == '*': count +=1
        if arr[i][j].isdigit():
            x = int(arr[i][j])
            if x != count:
                flag = 'NO'
print(flag)