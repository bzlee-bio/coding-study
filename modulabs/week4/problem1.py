class Solution:
    def minimumSum(self, num: int) -> int:        
        num = [int(x) for x in str(num)]
        num = sorted(num)
        return num[0]*10+num[3]+ num[1]*10+num[2]

if __name__ == "main":
    num = 2932
    soln = Solution()
    print(soln.minimumSum(num))