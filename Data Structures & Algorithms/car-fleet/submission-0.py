class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        combined = [[p,s] for p,s in zip(position, speed)]

        combined.sort(key=lambda x: x[0], reverse=True)

        my_stack = []

        for p,s in combined:
            my_stack.append((target - p) / s)
            if len(my_stack) >= 2 and my_stack[-1] <= my_stack[-2]:
                my_stack.pop()
        return len(my_stack)

                
        






                


        

        

        
        