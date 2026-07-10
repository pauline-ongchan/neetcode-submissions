#example 1
# 1, 4, 7, 10
# 4, 6, 8, 10

#example 2
# 4, 6, 8, 10
# 1, 3, 5, 7, 9, 
# 0, 1, 2, 3, 4, ...
# 7, 8, 9, 10

#example 3 pos = [1, 4], speed = [5, 2], target = 10
# is this example even correct?
# 1, 6, 8, 10
# 4, 6, 8, 10

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [[0,0]] * len(position)
        for i in range(len(position)):
            cars[i] = [position[i], speed[i]]
        cars.sort(key=lambda x: x[0], reverse=True)

        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            while not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)


            

        

