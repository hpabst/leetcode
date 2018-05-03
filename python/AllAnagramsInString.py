class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        counterP = Counter(p)
        counterWin = Counter(s[:len(p)])
        indices = []
        for i in range(0, len(s)-len(p)):
            if all(counterP[k] == counterWin[k] for k in counterP.keys()):
                indices.append(i)
            counterWin[s[i]] -= 1
            counterWin[s[i+len(p)]] += 1
        if all(counterP[k] == counterWin[k] for k in counterP.keys()):
            indices.append(len(s)-len(p))
        return indices