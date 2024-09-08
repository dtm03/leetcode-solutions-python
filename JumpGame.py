class Solution(object):
    def canJump(self, nums):
        max_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + num)
            if max_reach >= len(nums) - 1:
                return True
        return False