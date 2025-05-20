# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        strn = list(s)
        ans =[]
        sets = []
        for idx,value in enumerate(s):
            if not value.isdigit():
                sets.append(idx)
        n = len(sets)
        for i in range(1<<n):
            temp = strn[:]
            raw = bin(i)[2:]
            bins = '0' * (n - len(raw)) + raw
            for idx,bits in enumerate(bins):
                if bits == '1':
                    if temp[sets[idx]].islower():
                        temp[sets[idx]] = temp[sets[idx]].upper()
                    else:
                        temp[sets[idx]] = temp[sets[idx]].lower()
            temp= ''.join(temp)
            ans.append(temp)
        return ans