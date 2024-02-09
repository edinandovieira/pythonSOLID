class MathOperation:
    def __init__(self, nums):
        self.nums = nums

    def math_operation(self):
        min_num = min(self.nums)
        print('Minimum of given nums is {}'.format(min_num))
        max_num = max(self.nums)
        print('Maximum of given nums is {}'.format(max_num))

nums = [1, 3, 2, 4, 5, 6]
mo = MathOperation(nums)
mo.math_operation()