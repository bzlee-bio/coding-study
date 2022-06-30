from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n]+=1
        
        counter = sorted(counter.items(), key = lambda item: item[1], reverse=True)
        
        return [kk for kk, vv in counter][:k]
        