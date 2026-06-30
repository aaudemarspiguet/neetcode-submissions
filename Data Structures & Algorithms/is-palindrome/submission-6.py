class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_string = "".join(c.lower() for c in s if c.isalnum())

        j = -1
        for i in range(len(new_string) // 2):
            if new_string[i] == new_string[j]:
                j -= 1
                continue
            return False

        return True