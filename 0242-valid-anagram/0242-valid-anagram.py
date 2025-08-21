class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s)!=len(t)):
            return False

        freqcounter={}

        for ltr in s:
            if ltr not in freqcounter:
                freqcounter[ltr]=1
            else:
                freqcounter[ltr]+=1
        
        for ltr in t:
            if ltr not in freqcounter:
                return False

            freqcounter[ltr]-=1

            if(freqcounter[ltr]<0):
                return False 
        
        return True