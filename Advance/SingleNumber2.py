""" Single Number II """

"""
Problem Description
    Given an array of integers, every element appears thrice except for one, which occurs once.
    Find that element that does not appear thrice.
    NOTE: Your algorithm should have a linear runtime complexity.
    Could you implement it without using extra memory?
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans = 0
        for i in range(32):
            ones = 0
            for j in A:
                if self.checkbit(j, i):
                    ones += 1

            if ones % 3 != 0:
                ans += 1 << i

        return ans

    def checkbit(self, num, i):
        if (num >> i) & 1 == 1:
            return True

if __name__ == '__main__':
    A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]  # 4
    # A = [0, 0, 0, 1]  # 1

    print(Solution().singleNumber(A))