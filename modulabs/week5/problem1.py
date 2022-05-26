class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:   
        elements = dict()
        for e in nums:
            if e in elements.keys():
                elements[e]+=1
            else:
                elements[e]=1
        
        counter = 0
        for val in elements.values():
            counter += val*(val-1)/2

        return int(counter)