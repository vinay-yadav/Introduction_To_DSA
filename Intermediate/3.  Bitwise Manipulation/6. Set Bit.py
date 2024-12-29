class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return 1 << A | 1 << B

        # num = 0
        #
        # temp = 1
        #
        # for i in range(A):
        #     temp = temp << 1
        #
        # num = num | temp
        #
        # temp = 1
        #
        # for i in range(B):
        #     temp = temp << 1
        #
        # num = num | temp
        #
        # return num


if __name__ == '__main__':
    # A = 3
    # B = 5

    A = 4
    B = 4

    print(Solution().solve(A, B))

