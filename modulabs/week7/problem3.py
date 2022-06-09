class Solution:
    @lru_cache(None)
    def search(self, i):
        if i is None or i >= len(self.days):
            return 0
        
        j = i + 1
        i2 = i3 = None
        while (i2 is None or i3 is None) and j < len(self.days):
            if i2 is None and self.days[j] >= self.days[i]+7:
                i2 = j
            if i3 is None and self.days[j] >= self.days[i]+30:
                i3 = j
            j += 1
        
        pay1 = self.search(i+1)
        pay2 = self.search(i2)
        pay3 = self.search(i3)

        
        return min(pay1 + self.costs[0], pay2 + self.costs[1], pay3 + self.costs[2])
    
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.costs = costs
        self.days = days

        return self.search(0)
        