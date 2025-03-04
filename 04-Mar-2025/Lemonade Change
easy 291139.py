# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5=0
        count10=0
        for i in bills:
            if i == 5:
                count5+=1
            elif i ==10:
                count5 -=1
                count10+=1
            else:
                count5-=1
                count10 -=1
            check = count5 + (count10*2)
            if check < 0 or count5 < 0:
                return False
        return True