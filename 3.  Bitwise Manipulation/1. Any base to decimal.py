class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dec = 0

        i = 0
        while A > 0:
            dec += (A % 10) * (B ** i)
            i += 1
            A = A // 10

        return dec


if __name__ == '__main__':
    # A = 14
    # B = 6

    # A = 1010
    # B = 2

    A = 22
    B = 3

    print(Solution().solve(A, B))
