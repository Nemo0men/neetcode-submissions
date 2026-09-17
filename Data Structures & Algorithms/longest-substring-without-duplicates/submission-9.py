class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bank = set()

        if len(s)==0:
            return 0


        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in bank:
                bank.remove(s[l])
                l+=1
            bank.add(s[r])
            longest = max(longest, r-l+1)
        return longest