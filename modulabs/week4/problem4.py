class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsNew = sorted(nums)
        q, r = divmod(len(nums), 2)
        pL = q -1 + r
        pR = len(nums) - 1
        pCurr = 0
        while pR > q -1 + r:
            nums[pCurr], nums[pCurr+1] = numsNew[pL], numsNew[pR]
            pL -= 1
            pR -= 1
            pCurr += 2
            
        if r==1:
            nums[pCurr]=numsNew[0]