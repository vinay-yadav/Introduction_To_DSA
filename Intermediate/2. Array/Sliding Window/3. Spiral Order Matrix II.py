class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        matrix = []
        num = 1

        for i in range(A):
            matrix.append([0]*A)

        row_index = col_index = 0

        n = A
        while n > 1:
            for _ in range(1, n):
                matrix[row_index][col_index] = num
                col_index += 1
                num += 1

            for _ in range(1, n):
                matrix[row_index][col_index] = num
                row_index += 1
                num += 1

            for _ in range(1, n):
                matrix[row_index][col_index] = num
                col_index -= 1
                num += 1

            for _ in range(1, n):
                matrix[row_index][col_index] = num
                row_index -= 1
                num += 1

            row_index += 1
            col_index += 1
            n -= 2

        if n == 1:
            matrix[row_index][col_index] = num

        return matrix


if __name__ == '__main__':
    A = 1
    # A = 2
    # A = 5

    print(Solution().generateMatrix(A))

