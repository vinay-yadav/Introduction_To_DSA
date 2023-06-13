class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        sub_array_count = 0

        n = len(A)

        for s in range(n):
            sub_array_sum = 0
            for e in range(s, n):
                sub_array_sum += A[e]

                if sub_array_sum < B:
                    sub_array_count += 1
        return sub_array_count


if __name__ == '__main__':
    # A = [2, 5, 6]
    # B = 10

    A = [1, 11, 2, 3, 15]
    B = 10

    print(Solution().solve(A=A, B=B))
