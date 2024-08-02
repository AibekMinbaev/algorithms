#Solution during the contest | Solved 
# Time: n
# Space: 1 
# Topic: implementation, it is proven that we can change char to any char and also it is always better to choose the second char to change. 


class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        cnt = 0 
        l = 0 
        r = 1 
        while r < len(word): 
            if ord(word[l]) == ord(word[r]) or abs(ord(word[l]) - ord(word[r])) == 1: 
                cnt += 1 
                l += 1 
                r += 1 
            l += 1 
            r += 1 
        return cnt 
        