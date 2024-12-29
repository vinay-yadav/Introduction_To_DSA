import sys


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return sum(self.find_min_max(A))

    def find_min_max(self, A):
        max_number = -sys.maxsize - 1
        min_number = sys.maxsize

        for i in A:
            if i > max_number:
                max_number = i

            if i < min_number:
                min_number = i

        return min_number, max_number


if __name__ == '__main__':
    A = [3, -3, 6, 8, 4, 7, 8, -2, 0]

    t = Solution()
    print(t.solve(A=A))
