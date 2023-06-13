class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for i in A:
            result ^= i

        return result


if __name__ == '__main__':
    # A = [1, 2, 2, 3, 1]

    A = [1, 2, 2]
    print(Solution().singleNumber(A))