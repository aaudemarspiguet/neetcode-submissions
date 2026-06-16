class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # word --> freq map of letters (signature)
        # freq map --> lookup key into a dict (key: signature, value: list)
        # if key exists, append word to list
        # finally output list consisting of dict values

        anagram_dict: dict = {}
        
        # build groupings
        for word in strs:
            count: list = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1 # gives index of letter
            signature = tuple(count)
            
            if signature not in anagram_dict:
                anagram_dict[signature] = [] # init with empty list
            anagram_dict[signature].append(word)
        
        # output values
        return list(anagram_dict.values())

                
            
