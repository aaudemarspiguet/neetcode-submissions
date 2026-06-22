class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean
        cleanStr = ""
        for c in s:
            if c.isalnum():
                cleanStr += c.lower()

        # loop
        i = 0
        j = len(cleanStr) - 1
        while i < j:
            if cleanStr[i] == cleanStr[j]:
                i += 1
                j -= 1
                continue
            return False
        return True