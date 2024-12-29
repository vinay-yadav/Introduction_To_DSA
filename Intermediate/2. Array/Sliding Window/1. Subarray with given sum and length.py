class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        answer = 0

        current_sum = 0
        for i in range(B):
            current_sum += A[i]

        if current_sum == C:
            return 1

        s = 1
        e = B
        while e < len(A):
            current_sum = current_sum - A[s - 1] + A[e]
            if current_sum == C:
                return 1

            e += 1
            s += 1

        return answer


if __name__ == '__main__':
    # A = [4, 3, 2, 6, 1]
    # B = 3
    # C = 11

    A = [4, 2, 2, 5, 1]
    B = 4
    C = 6

    print(Solution().solve(A, B, C))
