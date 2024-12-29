class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        row_length = len(A)
        col_length = len(A[0])
        result = list()

        for col in range(col_length):
            temp = 0
            for row in range(row_length):
                temp += A[row][col]
            result.append(temp)

        return result


if __name__ == '__main__':
    A = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 2, 3, 4]
    ]

    print(Solution().solve(A=A))
