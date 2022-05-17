class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        posB = list()
        res = list()
        for i, element in enumerate(boxes):
            if element=='1':
                posB.append(i)
        
        for i in range(len(boxes)):
            count = 0
            for x in posB:
                count += abs(x-i) 
            res.append(count)
        return res