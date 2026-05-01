class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num in count:
           freq[count[num]].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            if not freq[i] == []:
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
            else:
                pass    

        return res        