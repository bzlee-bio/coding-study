class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        peoples = dict()
        
        for i, gs in enumerate(groupSizes):     # O(N)
            if gs not in peoples.keys():    # O(N); containment 
                peoples[gs] = list()
            peoples[gs].append(i)   # Space, O(N)
            
        result = list() # Space, O(N)
        for gs in peoples.keys():   # O(N)
            while len(peoples[gs]) > 0: # O(N); 
                result.append(peoples[gs][:gs])
                del peoples[gs][:gs]
                                            
        return result