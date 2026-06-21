from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            # make a word signature (freq of letters)
            signature = [0] * 26
            for letter in word:
                pos = ord(letter) - ord("a") # ascii code letter - a (range b/t 0 and 25)
                signature[pos] += 1 # increment
            groups[tuple(signature)].append(word)

        return list(groups.values())   