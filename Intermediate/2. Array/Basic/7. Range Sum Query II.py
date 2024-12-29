class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        result = []

        for j in B:
            result.append(sum([A[i] for i in range(j[0], j[1] + 1)]))

        return result


if __name__ == '__main__':
    A = [6, 3, 3, 6]
    B = [[0, 3], [0, 2]]

    t = Solution()
    print(t.solve(A=A, B=B))
