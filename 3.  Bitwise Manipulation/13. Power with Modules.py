class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        ans = 1

        for i in range(B):
            ans = (ans * (A % C)) % C

        return ans


if __name__ == '__main__':
    # A = 2
    # B = 3
    # C = 3

    A = 5
    B = 2
    C = 4

    print(Solution().solve(A, B, C))

