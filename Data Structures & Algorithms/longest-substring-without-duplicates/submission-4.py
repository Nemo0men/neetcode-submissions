class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if len(s)<2:
            return len(s)

        i = 0
        j = 1
        longest = 1
        while j<len(s):
            if s[j] in s[i:j]:
                longest = max(longest, len(s[i:j]))
                i+=1
            else:
                j+=1
        longest = max(longest, len(s[i:j]))
        return longest
        