class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_bank = {}
        t_bank = {}
        self.load_bank(bank=s_bank, word=s)
        self.load_bank(bank=t_bank, word=t)
        if s_bank == t_bank:
            return True
        else:
            return False


    def load_bank(self, bank: dict, word: str):
        for char in word:
            if char in bank:
                bank[char] += 1
            else:
                bank[char] = 1
            