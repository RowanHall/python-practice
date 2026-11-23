class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sdict = {}
        tdict = {}
        for letter in s:
            if letter not in sdict:
                sdict[letter] = 1
            sdict[letter] += 1

        for letter in t:
            if letter not in tdict:
                tdict[letter] = 1
            tdict[letter] += 1
        
        if tdict == sdict:
            return True
        return False


