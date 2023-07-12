class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        print(A)

        count = 0
        n = len(A)
        for i in range(n):
            if A[i] == n - i - 1:
                count += 1

        return count if count else -1

        # A.sort()
        #
        # current = counter = 0
        #
        # if A[0] == 0:
        #     counter += 1
        #
        # for i in range(1, len(A)):
        #     if A[i] != A[i - 1]:
        #         current += 1
        #
        #     if current == A[i]:
        #         counter += 1
        #
        # return counter if counter else -1


if __name__ == '__main__':
    # A = [3, 2, 1, 3]
    # A = [1, 1, 3, 3]
    # A = [2, 4, 5, 6, 7, 8]
    A = [9, 8, 4, 5, 7, 4]

    print(Solution().solve(A))
