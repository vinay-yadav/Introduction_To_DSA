class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A):
        sub_arrays = []

        n = len(A)

        for s in range(n):
            for e in range(s, n):
                sub_arrays.append([A[i] for i in range(s, e + 1)])

        return sub_arrays


if __name__ == '__main__':
    A = [1, 2, 3]
    # A = [5, 2, 1, 4]

    print(Solution().solve(A=A))

