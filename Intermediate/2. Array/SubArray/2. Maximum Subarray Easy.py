class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):
        max_sum = 0

        for s in range(A):
            sub_array_sum = 0
            for e in range(s, A):
                sub_array_sum += C[e]
                if sub_array_sum <= B:
                    max_sum = max(max_sum, sub_array_sum)

        return max_sum


if __name__ == '__main__':
    # A = 5
    # B = 12
    # C = [2, 1, 3, 4, 5]

    A = 3
    B = 1
    C = [2, 2, 2]

    print(Solution().maxSubarray(A, B, C))
