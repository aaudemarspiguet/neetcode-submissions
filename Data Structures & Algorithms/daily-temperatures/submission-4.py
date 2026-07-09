class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # if the problem were simple and tomorrow is always hotter than today, we can return an array of 1s
        # instead, we might have a mix: tomorrow's weather might be colder than today's

        # approach: 
        # immediately compute result[i] for when tomorrow is hotter than today (when day i+1 is hotter than day i)
        # we'll skip over a day if the following day is not immediately and come back to it
        # in other words, we'll need a data structure to track days for which we haven't found a hotter day yet
        # thus, every value in this data structure, if being appended to must be in decreasing order. 

        # voila: monotonic stack

        # NOTE: last index is always 0

        # this stack keeps track of days j for which we've yet to see a hotter day, 
        #                                               result[j] is 0 at the moment
        stack = [] 
        result = [0] * len(temperatures)

        # algorithm:

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                popped_index = stack.pop()
                result[popped_index] = i - popped_index

            stack.append(i)

        return result
        





