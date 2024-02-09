"""
Single Responsibility Principle(SRP)

Function should have only one responsibility. Only one reason to change
"""

class MathOperation:
    def __init__(self, nums):
        self.nums = nums

    def calculate_min(self):
        min_num = min(self.nums)
        print('Minimum of given nums is {}'.format(min_num))

    def calculate_max(self):
        max_num = max(self.nums)
        print('Maximum of given nums is {}'.format(max_num))

nums = [1, 3, 2, 4, 5, 6]
mo = MathOperation(nums)
mo.calculate_min()
mo.calculate_max()