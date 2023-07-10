class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        value = 0
        exp_contribution = 1

        for i in range(len(A) - 1, -1, -1):
            value = (value + exp_contribution * A[i]) % B
            exp_contribution = (exp_contribution * 10) % B

        return value


if __name__ == '__main__':
    A = [1, 4, 3]
    B = 2

    # A = [4, 3, 5, 3, 5, 3, 2, 1]
    # B = 47

    print(Solution().solve(A, B))
