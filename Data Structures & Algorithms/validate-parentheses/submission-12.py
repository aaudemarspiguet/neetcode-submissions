class Solution:
    def isValid(self, s: str) -> bool:
        delims = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char not in delims:
                stack.append(char)
                continue
            elif stack and stack[-1] == delims[char]:
                stack.pop()
                continue
            return False
        
        return True if not stack else False
