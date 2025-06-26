# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj_list = defaultdict(list)
        value = defaultdict(int)
        n = len(employees)
        for i in range(n):
            for j in employees[i].subordinates:
                adj_list[employees[i].id].append(j)
            value[employees[i].id] = employees[i].importance
        def dfs(x):
            if x not in adj_list:
                return value[x]
            count = 0
            for i in range(len(adj_list[x])):
                temp = dfs(adj_list[x][i])
                count +=temp
            return (count +value[x])
        return dfs(id)
            

                
            