# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

def solution(n):
    length = 1 
    count = 9   
    start = 1   

    while n > length * count:
        n -= length * count
        length += 1
        count *= 10
        start *= 10

    num = start + (n - 1) // length
    digit_index = (n - 1) % length
    
    return str(num)[digit_index]

cases = 1
# cases = int(input())
for i in range(cases):
    x = int(input())
    print(solution(x))