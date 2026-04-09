from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ans = []
        dict1 = defaultdict(int)

        for num in nums:
            dict1[num] += 1

        for i in range(k):

            high1 = max(dict1, key=dict1.get)
            ans.append(high1)
            del dict1[high1]

        return ans

        