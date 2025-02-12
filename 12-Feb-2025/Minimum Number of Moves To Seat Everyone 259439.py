# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], stud: List[int]) -> int:
        seats.sort()
        stud.sort()
        count = 0
        for i in range(len(stud)):
            count += abs(seats[i]-stud[i])
        return count
        