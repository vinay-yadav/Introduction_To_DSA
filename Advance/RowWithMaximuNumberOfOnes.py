""" Row with maximum number of ones """


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)

        i, j = 0, n - 1

        maxx, current, row = 0, 0, -1
        while i < n and j >= 0:
            if A[i][j] == 1:
                current += 1
                j -= 1
            else:
                if current > maxx:
                    maxx = current
                    row = i
                # current = 0
                i += 1

        if current > maxx:
            maxx = current
            row = i

        return row

if __name__ == '__main__':
    A = [
        [0, 1, 1],
        [0, 0, 1],
        [0, 1, 1],
    ]

    # A = [
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 1],
    #     [0, 0, 1, 1],
    #     [0, 1, 1, 1],
    # ]

    # A = [
    #     [0, 0, 1, 1],
    #     [0, 0, 1, 1],
    #     [0, 0, 1, 1],
    #     [1, 1, 1, 1]
    # ]

    print(Solution().solve(A))

