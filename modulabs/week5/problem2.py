class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = list(jewels) # O(N)
        
        counter = 0 
        for st in stones: # O(M) 
            if st in jewels: # O(N)
                counter += 1
                
        return counter