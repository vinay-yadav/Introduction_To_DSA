class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        transpose = list()

        # for i in range(n):
        #     for j in range(i, n):
        #         A[i][j], A[j][i] = A[j][i], A[i][j]

        row = len(A)
        column = len(A[0])

        for i in range(column):
            temp = list()
            for j in range(row):
                temp.append(A[j][i])
            transpose.append(temp)

        return transpose


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # A = [[1, 2], [1, 2], [1, 2]]

    print(Solution().solve(A=A))
