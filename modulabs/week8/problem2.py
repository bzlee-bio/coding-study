class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxVal = float(-inf)
        i = 0
        
        while i < len(nums):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                if curr<nums[j]:
                    i=j
                    break
                if maxVal < curr:
                    maxVal = curr
                if i==j:
                    i=len(nums)
        
        return maxVal