class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = "".join(char.lower() for char in s if char.isalnum())

        j = -1
        for i in range(len(clean_str) // 2):
            if clean_str[i] != clean_str[j]:
                return False
            j -= 1
        
        return True
