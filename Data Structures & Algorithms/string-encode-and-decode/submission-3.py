class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        encoded_result = ""
        for word in strs:
            encoded_result += str(len(word)) + "#" + word
        return encoded_result
        # "4asdf5asdff6asdfas"

    def decode(self, s: str) -> List[str]:
        decoded_result = []
        i = 0
        while i<len(s):
            word_length = ""
            while s[i]!="#":
                word_length += s[i]
                i += 1
            word_length = int(word_length)
            if word_length == 0:
                decoded_result.append("")
            else:
                decoded_result.append(s[i+1:i+1+word_length])
            i += word_length+1
        return decoded_result


