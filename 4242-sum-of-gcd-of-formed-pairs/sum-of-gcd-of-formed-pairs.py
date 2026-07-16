from math import gcd
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        prefixGcd = []
        mx = 0

        # Construct prefixGcd
        for x in nums:
            mx = max(mx, x)
            prefixGcd.append(gcd(x, mx))

        # Sort
        prefixGcd.sort()

        # Pair smallest with largest
        ans = 0
        i, j = 0, len(prefixGcd) - 1

        while i < j:
            ans += gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return ans