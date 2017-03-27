class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

sol = Solution()
sol.rotate([1, 2], 1)
sol.rotate([1, 2, 3, 4, 5, 6, 7], 3)
