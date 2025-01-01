""" Sub-matrix Sum Queries """


class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        q = len(B)

        pf = self.cal_prefix_sum(A)

        ans = list()

        for i in range(q):
            a1, b1 = B[i] - 1, C[i] - 1
            a2, b2 = D[i] - 1, E[i] - 1

            pre = pf[a2][b2]

            if b1 > 0:
                pre -= pf[a2][b1 - 1]

            if a1 > 0:
                pre -= pf[a1 - 1][b2]

            if a1 > 0 and b1 > 0:
                pre += pf[a1 - 1][b1 - 1]

            pre %= 10 ** 9 + 7
            ans.append(pre)

        return ans

    def cal_prefix_sum(self, mat):
        n, m = len(mat), len(mat[0])

        prefix = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                temp = mat[i][j]

                if i > 0:
                    temp += prefix[i - 1][j]

                if j > 0:
                    temp += prefix[i][j - 1]

                if i > 0 and j > 0:
                    temp -= prefix[i - 1][j - 1]

                prefix[i][j] = temp

        return prefix

if __name__ == '__main__':
    # A = [
    #      [1, 2, 3],
    #      [4, 5, 6],
    #      [7, 8, 9]
    # ]
    # B = [1, 2]
    # C = [1, 2]
    # D = [2, 3]
    # E = [2, 3]

    A = [
        [5, 17, 100, 11],
        [0, 0, 2, 8]
    ]
    B = [1, 1]
    C = [1, 4]
    D = [2, 2]
    E = [2, 4]

    print(Solution().solve(A, B, C, D, E))

