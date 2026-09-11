class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n2 < n1:
            return False

        mp1 = {}
        mp2 = {}

        for i in range(n1):
            mp1[s1[i]] = mp1.get(s1[i],0)+1
            mp2[s2[i]] = mp2.get(s2[i],0)+1
            
        if mp1 == mp2:
            return True

        left = 0
        for right in range(n1,n2):
            mp2[s2[right]] = mp2.get(s2[right],0)+1
            mp2[s2[left]] -= 1
            if mp2[s2[left]] == 0:
                del mp2[s2[left]]
            left += 1

            if mp1 == mp2:
                return True
        return False

        
            

        
        