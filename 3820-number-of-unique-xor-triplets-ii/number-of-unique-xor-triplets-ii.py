from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAXX = 2048  # nums[i] <= 1500, so XOR values are < 2048

        # dp[k][x] = True if XOR value x can be formed
        # using exactly k distinct indices processed so far.
        dp = [[False] * MAXX for _ in range(4)]
        dp[0][0] = True

        for v in nums:
            # Update in reverse so each index is used at most once.
            for k in range(2, -1, -1):
                prev = dp[k]
                cur = dp[k + 1]
                for x in range(MAXX):
                    if prev[x]:
                        cur[x ^ v] = True

        ans = set(nums)  # Cases with repeated indices always reduce to a single value.

        # Add XORs of three distinct indices.
        for x in range(MAXX):
            if dp[3][x]:
                ans.add(x)

        return len(ans)