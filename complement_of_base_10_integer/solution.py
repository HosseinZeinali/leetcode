import math
class Solution(object):
    def bitwiseComplement(self, N):
        if N == 0: return 1
        log = math.log(N, 2)
        return int((2 ** (math.floor(log)+1)) - N - 1)
s = Solution()
a = s.bitwiseComplement(1)
print(a)