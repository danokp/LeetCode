class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        return sum(
            map(
                lambda ind, let: (letters.index(let) + 1) * 26 ** (len(columnTitle) - ind - 1),
                (i for i in range(len(columnTitle))),
                (x for x in columnTitle)
            )
        )