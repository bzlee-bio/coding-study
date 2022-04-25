class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        friends = list(range(1,n+1))
        curIdx = 0
        while len(friends)!=1:
            curIdx += k-1   ## Current index also counts in k friends, thus only move k-1 friends
            curIdx = curIdx % len(friends)
            friends.pop(curIdx)
            
        return friends[0]