"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

# N = 2, [ [0,1,2], [0,2] ]
# N = 3, [ [0,1,2,3], [0,2,3], [0,1,3] ]
# N = 4, [ [ 0,1,2,3,4], [0,2,4], [0,2,3,4], [0,1,3,4], [0,1,2,4] ]

class Inefficient_Solution:
    def __init__(self, N):
      self.N = N
      self.paths = []

    def num_ways(self):
        self.step = 0
        self.num_ways_helper(self.N, self.step+1, [0])
        self.num_ways_helper(self.N, self.step+2, [0])

        print(self.paths)
        print(len(self.paths))

    def num_ways_helper(self, N, step, path):
        if N != step and N > step:
            path.append(step)
            new_path = path.copy()
            self.num_ways_helper(N, step+1, path)
            self.num_ways_helper(N, step+2, new_path)
    
        if N == step:
            path.append(step)
            self.paths.append(path)
    
solution = Inefficient_Solution(4)
solution.num_ways()
