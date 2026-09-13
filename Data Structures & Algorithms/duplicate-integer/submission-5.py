class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        check = {}

        if length==0:
            return False

        for i in range(length):
            if nums[i] in check:
                return True
            else:
                check[nums[i]] = 1
            
        return False