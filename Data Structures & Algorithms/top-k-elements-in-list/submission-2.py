class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        count = {}
        freq = [[] for i in range(length + 1)]
        ans = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
        for i in range(length, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans
        
        
        