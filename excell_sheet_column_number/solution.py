class Solution:
    def titleToNumber(self, s: str) -> int:
        result = self.calculate(s)

        return result

    def calculate(self, word):
        dictionary = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
            "J": 10,
            "K": 11,
            "L": 12,
            "M": 13,
            "N": 14,
            "O": 15,
            "P": 16,
            "Q": 17,
            "R": 18,
            "S": 19,
            "T": 20,
            "U": 21,
            "V": 22,
            "W": 23,
            "X": 24,
            "Y": 25,
            "Z": 26,
        }
        i = len(word) - 1
        res = 0
        while i >= 0:
            print(dictionary[word[i]])
            res = res + dictionary[word[i]] * self.power(26, (len(word) - 1) - i)

            i = i-1

        return res
    def power(self, base, power):
        i = 0
        res = 1
        while i < power:
            res = res*base
            i = i + 1

        return res

solution = Solution()
solution.titleToNumber("ZY")