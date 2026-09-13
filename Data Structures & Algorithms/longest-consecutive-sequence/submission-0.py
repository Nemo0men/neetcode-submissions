class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        converted = set(nums)
        list_of_starts = []
        highest_streak = 0
        for num in converted:
            if num-1 not in converted:
                list_of_starts.append(num)
        for start in list_of_starts:
            current_streak = 1
            while start+1 in converted:
                start+=1
                current_streak+=1
            highest_streak = max(highest_streak, current_streak)
        return highest_streak