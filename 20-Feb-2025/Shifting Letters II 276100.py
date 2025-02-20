# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = list(s)
        ain = [0] * (len(arr)+1)
        for i in range(len(arr)):
            arr[i] = ord(arr[i]) -97
        for i in shifts:
            if i[-1] == 0:
                ain[i[0]] -= 1
                ain[i[1]+1] +=1
            else:
                ain[i[0]] += 1
                ain[i[1]+1] -=1
        for i in range(1,len(ain)):
            ain[i]+=ain[i-1]
        print(ain)
        ans=[]
        for i in range(len(arr)):
            x = (ain[i]+arr[i])%26
            ans.append(x+97)
        ans = ''.join(map(chr,ans))
        return ans