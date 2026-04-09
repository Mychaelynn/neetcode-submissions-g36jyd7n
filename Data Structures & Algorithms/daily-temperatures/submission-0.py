class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # result =[]
        # temp2 = [temperatures[0]]
        # count=1
        # b=1
        # i=1
        # while i < len(temperatures):
            
        #     if temp2[-1]<temperatures[i]:
        #         result.append(count)
        #         count=1
        #         temp2.append(temperatures[i])
        #         b+=1
        #         i=b
                
        #     else:
        #         count+=1
        #         i+=1
        # return result

      res = [0] * len(temperatures)
      stack=[]
      for i,t in enumerate(temperatures):
        while stack and t>stack[-1][0]:
            stackTemp, stackInd =stack.pop()
            res[stackInd]=i-stackInd
        stack.append([t,i])
      return res
