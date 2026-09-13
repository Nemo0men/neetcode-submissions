class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [0]*length
        right = [0]*length
        output = [0]*length
        aggregate = 1
        for i in range(length):
            aggregate *= nums[i]
            left[i] = aggregate
        aggregate = 1
        for i in range(length-1,-1,-1):
            aggregate *= nums[i]
            right[i] = aggregate
        for i in range(length):
            if i==0:
                output[i] = right[i+1]
            elif i==length-1:
                output[i] = left[i-1]
            else:
                output[i] = left[i-1]*right[i+1]
        return output