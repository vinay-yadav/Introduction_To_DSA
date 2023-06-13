class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        result = list()

        for row in range(len(A)):
            temp = 0
            for col in range(len(A[0])):
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
