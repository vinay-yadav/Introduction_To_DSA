class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        g_count = 0
        ag_count = 0

        for i in A[::-1]:
            if i == "G":
                g_count += 1

            if i == "A":
                ag_count += g_count

        return ag_count % (10 ** 9 + 7)


if __name__ == "__main__":
    # A = "ABCGAG"
    A = "GAB"

    result = Solution().solve(A=A)
    print(result)
