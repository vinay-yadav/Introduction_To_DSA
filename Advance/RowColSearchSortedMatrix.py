""" Search in a row wise and column wise sorted matrix """


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n, m = len(A), len(A[0])

        i, j = 0, m - 1

        ans = float("inf")
        while 0 <= i < n and 0 <= j < m:
            ele = A[i][j]

            if ele == B:
                cal = (i + 1) * 1009 + (j + 1)
                if ans > cal:
                    p, k = i, j
                    ans = cal
                j -= 1
            elif ele < B:
                i += 1
            else:
                j -= 1

        if ans == float("inf"):
            return -1
        return ans

if __name__ == '__main__':
    # A = [[1, 2, 3],
    #      [4, 5, 6],
    #      [7, 8, 9]]
    # B = 2

    A = [[1, 2],
         [3, 3]]
    B = 3

    print(Solution().solve(A, B))

