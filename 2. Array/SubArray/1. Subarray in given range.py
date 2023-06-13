class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        return [A[i] for i in range(B, C + 1)]


if __name__ == '__main__':
    A = [6, 3, 3, 6, 7, 8, 7, 3, 7]
    B = 1
    C = 2

    # A = [4, 3, 2, 6]
    # B = 1
    # C = 3

    print(Solution().solve(A, B, C))
