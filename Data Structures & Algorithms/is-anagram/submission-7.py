class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_bank = {}
        t_bank = {}
        self.load_bank(bank=s_bank, word=s)
        self.load_bank(bank=t_bank, word=t)
        return s_bank == t_bank


    def load_bank(self, bank: dict, word: str):
        for char in word:
            if char in bank:
                bank[char] += 1
            else:
                bank[char] = 1