class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        count = 0
        while A > 0:
            count += 1
            A = A & A - 1
        return count


if __name__ == '__main__':
    # A = 5
    A = 8

    print(Solution().solve(A))
