class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        stack.append(0)

        for i in range(1, len(temperatures), 1):
            # monotonically grow stack
            if temperatures[i] < temperatures[i - 1]:
                stack.append(i)
                continue

            while stack and temperatures[stack[-1]] < temperatures[i]:
                popped_index = stack.pop()
                result[popped_index] = i - popped_index
            
            stack.append(i)
        
        return result

        

