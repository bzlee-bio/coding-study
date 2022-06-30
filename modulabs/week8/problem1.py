from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        L = len(nums)/2
        for n in nums:
            count[n]+=1
            if count[n]>=L:
                return n

            
        