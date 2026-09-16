class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2:
            return 0
        
        prefix_highest = [0]*len(height)
        suffix_highest = [0]*len(height)
        total_area = 0
        highest_l = 0
        highest_r = 0
        for i in range(len(height)):
            prefix_highest[i] = highest_l
            highest_l = max(highest_l, height[i])
        for i in range(len(height)-1, -1, -1):
            suffix_highest[i] = highest_r
            highest_r = max(highest_r, height[i])
        for i in range(len(height)):
            area = min(prefix_highest[i], suffix_highest[i])-height[i]
            total_area += max(0, area)
        return total_area


                

