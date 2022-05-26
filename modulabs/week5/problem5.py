class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        soln = 0
        count = 0
        for p in s: # O(N)
            if p=='(':
                count += 1
            elif p == ')':
                count -= 1
            
            if count < 0: ## Right parenthesis dominant (when there was no left one)
                soln += 1
                count = 0
                    
        soln += count
        
        return soln