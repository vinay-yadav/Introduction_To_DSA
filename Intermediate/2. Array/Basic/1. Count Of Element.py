import sys


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_number = -sys.maxsize - 1
        max_number_count = 0

        for i in A:
            if i > max_number:
                max_number = i

        for i in A:
            if i == max_number:
                max_number_count = max_number_count + 1

        return len(A) - max_number_count


if __name__ == '__main__':
    A = [5, 5, 3]

    t = Solution()
    print(t.solve(A=A))


"""
Problem Description
    - Given an array A of N integers. Count the number of elements that have at least 1 elements greater than itself.

Problem Constraints
    - 1 <= N <= 105
    - 1 <= A[i] <= 109

Example Input
    Input 1:
    A = [3, 1, 2]

    Input 2:
    A = [5, 5, 3]

Example Output
    Output 1:
    2

    Output 2:
    1
"""