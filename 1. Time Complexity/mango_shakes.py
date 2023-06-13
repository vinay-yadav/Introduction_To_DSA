"""
    Given two integers A and B. A represents the count of mangoes and B represent the count of slices of mangoes.
    Mango can be cut into three slices of mangoes. A glass of mango shake can be formed by two slices of mangoes.

    Find the maximum number of glasses of mango shakes you can make with A mangoes and B slices of mangoes initially.
"""
from math import floor


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        slices = (A * 3) + B
        return floor(slices/2)


print(Solution().solve(A=7, B=1))
