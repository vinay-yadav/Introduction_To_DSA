import sys


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        k = 0
        for i in A:
            if i <= B:
                k += 1

        window_size = k

        count = 0
        for i in range(k):
            if A[i] <= B:
                count += 1

        min_swaps = window_size - count

        s = 1
        while k < len(A):
            if A[s - 1] <= B:
                count -= 1

            if A[k] <= B:
                count += 1

            min_swaps = min(min_swaps, window_size - count)
            k += 1
            s += 1

        return min_swaps


if __name__ == '__main__':
    A = [1, 12, 10, 3, 14, 10, 5]
    B = 8

    # A = [5, 17, 100, 11]
    # B = 20

    # A = [0]
    # B = 0

    print(Solution().solve(A, B))
