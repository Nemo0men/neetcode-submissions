class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        if length==1:
            return True
        raw_list = []
        for char in s:
            if char.isalnum():
                raw_list.append(char.lower())
            else:
                continue
        raw = "".join(raw_list)
        print(raw)
        length_raw = len(raw)
        i = 0
        j = length_raw-1
        if length_raw%2==0:
            while(i<j):
                if raw[i]!=raw[j]:
                    return False
                i+=1
                j-=1
            return True
        else:
            while(i+1<j):
                if raw[i]!=raw[j]:
                    return False
                i+=1
                j-=1
            return True
