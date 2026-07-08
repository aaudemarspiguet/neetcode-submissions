class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        stack.append(0)

        for i in range(1, len(temperatures), 1):
            # monotonically grow stack
            if temperatures[i] < temperatures[i - 1]:
                stack.append(i)
                print(stack)
                continue

            while stack and temperatures[stack[-1]] < temperatures[i]:
                popped_index = stack.pop()
                days_elapsed = i - popped_index
                result[i - days_elapsed] = days_elapsed
            
            stack.append(i)
        
        return result

        

