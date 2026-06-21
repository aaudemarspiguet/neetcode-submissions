class Solution:

    def encode(self, strs: List[str]) -> str:
        # dynamic delim: len(word) + "%"
        encode_str = ""
        for word in strs:
            encode_str += str(len(word)) + "%" + word
        return encode_str

    def decode(self, s: str) -> List[str]:
        # expecting first char to be a num
        # cast char at current position to length,
        # skip delim char
        # length of word, and add to list
        # continue while curr position is < len(s)

        words = []
        global_index = 0
        while global_index < len(s):

            delim_index = global_index + 1
            while delim_index < len(s):
                if s[delim_index] == "%":
                    break
                delim_index += 1
                        
            length = int(s[global_index:delim_index])
            # e.g. "3%bye5%hello"
            words.append(s[delim_index + 1: delim_index + 1 + length])
            global_index = delim_index + 1 + length
        return words
        




