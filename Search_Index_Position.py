class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_idx = 0
        end_idx = len(nums)-1
        while start_idx <= end_idx:
            mid = (start_idx+end_idx)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end_idx = mid-1
            elif nums[mid] < target:
                start_idx = mid+1
        return start_idx