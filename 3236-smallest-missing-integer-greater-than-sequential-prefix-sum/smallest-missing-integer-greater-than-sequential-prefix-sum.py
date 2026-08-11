class Solution:
    def missingInteger(self, A: list[int]) -> int:
        res = A[0]
        seen = [False] * 52
        seq = True

        seen[A[0]] = True

        for i in range(1, len(A)):
            if seq and A[i] == A[i - 1] + 1:
                res += A[i]
            else:
                seq = False
                if res > 50:
                    return res
            seen[A[i]] = True

        for i in range(res, 52):
            if not seen[i]:
                return i

        return res