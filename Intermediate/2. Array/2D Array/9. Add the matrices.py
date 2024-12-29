class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        row = len(A)
        col = len(A[0])

        # matrix = []
        # for _ in range(row):
        #     matrix.append([0] * col)

        for row_index in range(row):
            for col_index in range(col):
                A[row_index][col_index] += B[row_index][col_index]

        return A


if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    B = [[9, 8, 7],
         [6, 5, 4],
         [3, 2, 1]]

    # A = [[1, 2, 3],
    #      [4, 1, 2],
    #      [7, 8, 9]]
    #
    # B = [[9, 9, 7],
    #      [1, 2, 4],
    #      [4, 6, 3]]

    print(Solution().solve(A, B))
