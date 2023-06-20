class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) < 2:
            return True

        alph_dict = {chr: i for i, chr in enumerate(order)}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            flag = True
            for chr1, chr2 in zip(word1, word2):
                pos1 = alph_dict[chr1]
                pos2 = alph_dict[chr2]
                if pos1 > pos2:
                    return False
                if pos1 < pos2:
                    flag = False
                    break
            if len(word1) > len(word2) and flag:
                return False
        return True