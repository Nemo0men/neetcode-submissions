class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        length = len(strs)
        if length==1:
            return [[strs[0]]]
        

        bank_of_banks = {}
        for word in strs:
            word_bank = "".join(sorted(word))
            if word_bank in bank_of_banks:
                bank_of_banks[word_bank].append(word)
            else:
                bank_of_banks[word_bank] = [word]
        list_of_sublists = []
        for bank in bank_of_banks:
            list_of_sublists.append(bank_of_banks[bank])
        return list_of_sublists

