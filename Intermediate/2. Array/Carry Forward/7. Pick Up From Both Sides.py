import copy
import sys


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        answer = current = sum(A[:B])

        back = B - 1
        end = len(A) - 1

        while back >= 0:
            current = current - A[back] + A[end]
            answer = max(answer, current)
            back -= 1
            end -= 1

        return answer


if __name__ == '__main__':
    # A = [5, -2, 3, 1, 2]
    # B = 3

    A = [2, 3, -1, 4, 2, 1]
    B = 4

    # A = [5, -2, 3, 1, 2]
    # B = 4

    print(Solution().solve(A=A, B=B))
