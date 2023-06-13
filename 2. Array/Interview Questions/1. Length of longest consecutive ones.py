class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        max_ones = 0
        for i in range(len(A)):
            if A[i] == "1":
                max_ones += 1

        if max_ones == len(A):
            return max_ones

        max_sequence = 0

        for j in range(len(A)):
            if not A[j] == "0":
                continue

            l = 0
            for i in range(j-1, -1, -1):
                if A[i] == "0":
                    break
                l += 1

            r = 0
            for i in range(j+1, len(A)):
                if A[i] == "0":
                    break
                r += 1

            if l + r < max_ones:
                sequence = l + r + 1
            else:
                sequence = l + r

            max_sequence = max(max_sequence, sequence)

        return max_sequence


if __name__ == '__main__':
    # A = "111000"
    # A = "111011101"
    # A = "11010110000000000"
    A = "1111111111"
    print(Solution().solve(A))
