# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def checker(sting):
            x = sting.split('.')
            for i in x:
                if len(i) > 1 and i[0] == '0':
                    return False
                if int(i)> 255:
                    return False
            return True
        def backtracking(i,strbef,straft):
            nonlocal ans
            if i == 3:
                if not straft:
                    return
                if checker(strbef + straft):
                    ans.append(strbef + straft)
                return
            
            for j in range(1,4):
                backtracking(i+1, strbef+straft[0:j]+'.',straft[j:])
        ans = []
        backtracking(0,'',s)
        return ans
