class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        bank = {}

        if length==2:
            return [0, 1]

        for i in range(length):
            number_to_find = target-nums[i]
            if number_to_find in bank:
                return [bank[number_to_find], i]
            else:
                bank[nums[i]] = i
        