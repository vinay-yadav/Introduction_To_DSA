class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        for row in range(len(A)):
            for col in range(len(A[0])):
                if A[row][col] != B[row][col]:
                    return 0

        return 1


if __name__ == '__main__':
    # A = [[1, 2, 3],
    #      [4, 5, 6],
    #      [7, 8, 9]]
    # B = [[1, 2, 3],
    #      [4, 5, 6],
    #      [7, 8, 9]]

    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    B = [[1, 2, 3],
         [7, 8, 9],
         [4, 5, 6]]

    print(Solution().solve(A, B))
