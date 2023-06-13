class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        n = len(A)

        for i in range(n):
            for j in range(i, n):
                A[i][j], A[j][i] = A[j][i], A[i][j]

        for sub_array in A:
            self.reverse_array(array=sub_array)

        return A

    def reverse_array(self, array):
        i = 0
        j = len(array) - 1

        while i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    # A = [
    #     [1, 2],
    #     [3, 4]
    # ]

    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(Solution().solve(A=A))
