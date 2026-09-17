class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bank = set()

        if len(s)<2:
            return len(s)


        bank.add(s[0])
        i = 0
        j = 1
        longest = 1
        while j<len(s):
            if s[j] in bank:
                bank.remove(s[i])
                i+=1
            else:
                bank.add(s[j])
                longest = max(longest, len(bank))
                j+=1
        return longest
        