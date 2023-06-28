class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        while B > 0:
            A = A >> 1
            B -= 1

        return A & 1


if __name__ == '__main__':
    A = 4
    B = 1

    # A = 5
    # B = 2

    print(Solution().solve(A, B))
