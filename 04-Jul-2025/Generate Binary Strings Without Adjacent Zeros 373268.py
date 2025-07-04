# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0","1"]
        ans =[]
        for i in range(1<<n):
            flag = True
            x = bin(i)[2:]
            x = ((n-len(x)) * '0') + x
            for j in range(1,n):
                k = j-1
                if x[k] =='0' and x[j] =='0':
                    flag = False
            if flag:
                ans.append(x)
        return ans