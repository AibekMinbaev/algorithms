class Solution:
    def isPalindrome(self, s: str) -> bool: 
        new_string = "" 

        for ch in s: 
            if ch.isalpha():  
                new_string += ch.lower() 
            elif ch.isdigit():
                new_string += ch 

        l = 0 
        r = len(new_string) - 1 

        while l <= r: 
            if new_string[l] != new_string[r]: 
                return False
            l += 1 
            r -= 1 

        return True 