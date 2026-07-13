class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        s = "123456789"
        ans = []

        for length in range(2, 10):
            for start in range(10 - length):
                num = int(s[start:start + length])
                if low <= num <= high:
                    ans.append(num)

        return ans