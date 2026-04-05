class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char.lower() for char in s if char.isalnum())

        length = len(clean)
        mid = length // 2

        for i in range(mid):
            if clean[i] != clean[length - i - 1]:
                return False
        
        return True

    
        