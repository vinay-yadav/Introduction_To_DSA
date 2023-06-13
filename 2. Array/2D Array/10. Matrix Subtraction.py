class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        for row in range(len(A)):
            for col in range(len(A[0])):
                A[row][col] -= B[row][col]

        return A


if __name__ == '__main__':
    # A = [[1, 2, 3],
    #      [4, 5, 6],
    #      [7, 8, 9]]
    #
    # B = [[9, 8, 7],
    #      [6, 5, 4],
    #      [3, 2, 1]]

    A = [[1, 1]]

    B = [[2, 3]]

    print(Solution().solve(A, B))
