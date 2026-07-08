class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operators = { '+', '-', '*', '/' }

        for t in tokens:
            if t not in operators:
                operands.append(int(t))
                continue
            # since tokens is assumed to always be valid RPN sequence
            # we'll never have examples like: ['+', '3', ...]

            y = int(operands.pop())            
            x = int(operands.pop())

            if t == '+':
                operands.append(x + y)
            elif t == '-':
                operands.append(x - y)
            elif t == '*':
                operands.append(x * y)
            else:
                operands.append(int(x / y))
            
        return operands[-1] # should be the result
        
