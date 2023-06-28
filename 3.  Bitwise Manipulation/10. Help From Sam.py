class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        count = 0
        while A > 0:
            if A & 1:
                count += 1
            A = A >> 1

        return count


if __name__ == '__main__':
    # A = 5
    # A = 3
    A = 17
    print(Solution().solve(A))