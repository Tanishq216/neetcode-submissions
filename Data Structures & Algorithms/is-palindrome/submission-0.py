class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join([char for char in s if char.isalnum()])
        s = s.lower()
        rev = s[::-1]
        if s == rev:
            return True
        return False
        