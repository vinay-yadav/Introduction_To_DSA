class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        value = 0
        exp_contribution = 1

        B = 3

        for i in range(len(A) - 1, -1, -1):
            value = (value + exp_contribution * A[i]) % B
            exp_contribution = (exp_contribution * 10) % B

        return 1 if value == 0 else 0


if __name__ == '__main__':
    A = [1, 2, 3]

    # A = [1, 0, 0, 1, 2]

    print((Solution().solve(A)))
