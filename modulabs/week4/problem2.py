class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(' ')
        order = list()
        for i, word in enumerate(s):
            order.append((int(word[-1]),i))

        order.sort(key = lambda x: x[0])
        
        return ' '.join([s[x][:-1] for _, x in order])

