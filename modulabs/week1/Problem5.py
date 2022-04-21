class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        solPairs = list()
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    wordConcat = words[i] + words[j]
                    mid, rem = divmod(len(wordConcat),2)
                    if rem==0:
                        seq1 = wordConcat[:mid]
                        seq2 = wordConcat[-1:mid-1:-1]
                        
                    elif rem!=0:
                        seq1 = wordConcat[:mid]
                        seq2 = wordConcat[-1:mid:-1]
                    if seq1==seq2:
                            solPairs.append([i,j])
        return solPairs