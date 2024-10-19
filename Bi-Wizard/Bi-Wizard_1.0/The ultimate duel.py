#User function Template for python3

class Solution:
    def minimumAttacks(self, X, K):
        s = 0
        c = 0
        while s <= K:
            s += X+(c*2)
            c+=1
        return c 
