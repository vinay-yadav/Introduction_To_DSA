import sys


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        ans = -sys.maxsize - 1
        carry = 0

        for i in A:
            summ = carry + i

            if summ > ans:
                ans = summ

            if summ < 0:
                carry = 0
            else:
                carry = summ

        return ans

if __name__ == '__main__':
    # Input 1
    A = [1, 2, 3, 4, -10]
    print(f"Input {A} =>", Solution().maxSubArray(A))

    # Input 2
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Input {A} =>", Solution().maxSubArray(A))