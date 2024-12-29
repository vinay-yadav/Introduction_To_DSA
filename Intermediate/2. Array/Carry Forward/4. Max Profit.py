import sys


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        length = len(A)

        if length < 2:
            return 0

        current_max = A[-1]
        answer = 0

        for i in range(length - 2, -1, -1):
            if A[i] > current_max:
                current_max = A[i]
            else:
                answer = max(answer, current_max - A[i])

        return answer


if __name__ == '__main__':
    # A = [1, 2]
    A = [1, 4, 5, 2, 4]
    # A = [2, 1]

    print(Solution().maxProfit(A=A))
