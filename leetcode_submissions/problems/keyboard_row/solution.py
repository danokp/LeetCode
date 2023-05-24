class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_line = set("qwertyuiop")
        second_line = set("asdfghjkl")
        third_line = set("zxcvbnm")
        def is_word_in_one_line(word):
            for line in (first_line, second_line, third_line):
                if not set(word.lower()).difference(line):
                    return True
            return False
        return list(filter(
            lambda word:is_word_in_one_line(word),
            words
        ))