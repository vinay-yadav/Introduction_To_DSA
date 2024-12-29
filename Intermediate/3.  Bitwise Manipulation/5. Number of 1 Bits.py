class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0

        while A > 0:
            if A & 1:
                count += 1

            A = A >> 1

        return count


if __name__ == '__main__':
    A = 11
    # A = 6

    print(Solution().numSetBits(A))
