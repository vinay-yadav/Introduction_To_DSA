class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort(reverse=True)
        total = sum(A)

        cost = 0

        for i in A:
            cost += total
            total -= i

        return cost


if __name__ == '__main__':
    # A = [2, 1]
    # A = [5]
    A = [8, 0, 10]
    print(Solution().solve(A))
