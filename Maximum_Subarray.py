class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = max_till_here = nums[0]
        for i in range(1,len(nums)):
            max_till_here = max(nums[i],max_till_here+nums[i])
            max_so_far = max(max_till_here,max_so_far)
        return max_so_far