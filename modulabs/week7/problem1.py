class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        cache = [0 for _ in range(n+1)]
        cache[1] = 1
        cache[2] = 1
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]