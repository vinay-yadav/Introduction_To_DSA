class Solution:
    # @param A : long
    # @param B : integer
     # @return an long
    def solve(self, A, B):
        ans = A
        for i in range(B):
            if A & 1 << i:
                ans -= 1 << i

        return ans


if __name__ == '__main__':
    # A = 25
    # B = 3

    A = 37
    B = 3

    print(Solution().solve(A, B))
