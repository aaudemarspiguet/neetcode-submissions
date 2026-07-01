class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '{' or char == '(' or char == '[':
                stack.append(char)
                continue
            elif len(stack) != 0 and char == '}' and stack[-1] == '{':
                stack.pop()
                continue
            elif len(stack) != 0 and char == ']' and stack[-1] == '[':
                stack.pop()
                continue
            elif len(stack) != 0 and char == ')' and stack[-1] == '(':
                stack.pop()
                continue
            return False

        if len(stack) != 0:
            return False
        
        return True # default
