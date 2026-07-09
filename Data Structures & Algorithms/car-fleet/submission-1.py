class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # approach:

        # iterate through position and speed, for each car compute the time it will take to arrive and push to stack
        # before pushing however, check to see if top of stack is >= to current car's speed 
        # (if so, we skip --> previous will catch up and form a fleet)
        # stack will contain non-overlapping travel times, thus its size inherently tracks the # of fleets

        # okay a naive assumptios made earlier: 
        # 1) positions would given in increasing order - fix: sort array
        # AND
        # 2) earlier cars catch up to a fleet before the car in front of it does fix: order by descending

        cars = sorted(
            list(zip(position, speed)), # create array cf cars
            key=lambda car: car[0], # sort by position
            reverse=True # order by descending
        )

        fleets = []
        for car in cars:
            time_to_destination = (target - car[0]) / car[1]

            if not fleets or fleets[-1] < time_to_destination:
                fleets.append(time_to_destination)
            
        
        return len(fleets)


            

