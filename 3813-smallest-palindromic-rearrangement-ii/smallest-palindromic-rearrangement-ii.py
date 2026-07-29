class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        m = len(s) >> 1
        freq = Counter(s[:m])

        # base permutation
        ways = factorial(m)      
        for v in freq.values():
            ways //= factorial(v)

        if k > ways: return ""

        # main logic, building the k-th smallest first half
        half = ""
        for i in range(m):       # choose the correct char c
            for c in ascii_lowercase:
                if not freq[c]: continue

                t = ways * freq[c] // (m - i) #  ways × P(c|ways)
                if k <= t: 
                    half += c    # append c
                    freq[c] -= 1
                    ways = t  
                    break
                k -= t           # skip

        mid = s[m] if len(s) & 1 else ""
        return half + mid + half[::-1]