class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        for row in range(len(A)):
            for col in range(len(A[0])):
                A[row][col] *= B

        return A


if __name__ == '__main__':
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    B = 2

    # A = [[1]]
    # B = 5

    print(Solution().solve(A, B))
