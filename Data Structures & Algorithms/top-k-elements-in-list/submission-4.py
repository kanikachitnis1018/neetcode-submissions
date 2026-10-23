from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        n= len(nums)
        buckets = [[] for _ in range(n + 1)]


        for key, value in counter.items():  # key = number and value = frequency
            if  buckets[value] == 0:
                buckets[value] = [key]
            else:
                buckets[value].append(key)
        
        ret = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ret.extend(buckets[i])
            if len(ret) == k:
                break
        return ret
