class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        lenNums = len(nums)
        
        minErrVal = inf
        for i in range(lenNums-2):
            pLeft = i+1
            pRight = lenNums-1 if i!= lenNums-1 else lenNums-2 
            
            
            while pLeft!=pRight:
                sumVal = nums[pLeft] + nums[i] + nums[pRight]
                
                if sumVal == target:
                    return sumVal
                elif sumVal < target:
                    pLeft += 1
                else:
                    pRight -= 1
                    
                if abs(sumVal-target) < abs(minErrVal-target):
                    minErrVal = sumVal
                    
        return minErrVal