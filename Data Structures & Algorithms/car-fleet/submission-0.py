class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        # fleet = 0
        # times =[0, False] * len(position)
        # for i in range (len(position)):
        #     currCarP = position.pop()
        #     currCarV = speed.pop()

        #     timeToTarget = float(target-currCarP)/currCarV

        #     if timeToTarget<times[-1][0]: 
        #         if times[-1][1]==False:
        #             fleet+=1
        #         else:

        #             times.append(timeToTarget, True)

        #     times.append(timeToTarget, False)
        # return fleet



        pair = [[p,s] for p,s in zip(position, speed)]
        fleet = 0
        pair = sorted(pair)
        stack=[]
        for p,s in pair[::-1]: #reverse order
            time = (target-p)/s
            stack.append(time)

            if len(stack)>=2 and stack[-1]<= stack[-2]:
                fleet+=1
                stack.pop()
        return len(stack)




