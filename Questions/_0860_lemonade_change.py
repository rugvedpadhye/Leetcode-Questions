class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        i=0 #number of 5's
        j=0 #numer of 10's
        for amt in bills:
            if amt==5:
                i+=1
            
            if amt==10:
                if i>=1:
                    i-=1
                    j+=1
                else:
                    return False
            if amt==20:
                if i>=1 and j>=1:
                    i-=1
                    j-=1
                elif i>=3:
                    i-=3
                else:
                    return False
        return True