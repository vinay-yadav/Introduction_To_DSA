class Solution:
    # @param A : list of integers
    # @return an long
    def subarraySum(self, A):
        total_sum = 0

        n = len(A)
        for i in range(n):
            contribution = (i + 1) * (n - i)
            total_sum += A[i] * contribution

        return total_sum


if __name__ == '__main__':
    # A = [1, 2, 3]
    A = [2, 1, 3]
    print(Solution().subarraySum(A))
