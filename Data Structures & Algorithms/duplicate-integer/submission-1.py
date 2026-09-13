class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newset = set()
        for each in nums:
            newset.add(each)
        if (len(newset) == len(nums)):
            return False
        else:
            return True
        