class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = "".join(c.lower() for c in s if c.isalnum())
        

        j = -1
        for i in range(len(clean_str) // 2):
            if clean_str[i] == clean_str[j]:
                j -= 1
                continue
            return False

        return True