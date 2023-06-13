class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A[0])

        diagonal = list()

        for j in range(n):
            i = 0
            m = n

            temp = list()
            while m > 0:
                if j < 0:
                    temp.append(0)
                else:
                    temp.append(A[i][j])

                i += 1
                j -= 1
                m -= 1

            diagonal.append(temp)

        for i in range(1, n):
            j = n - 1
            m = n

            temp = list()
            while m > 0:
                if i > n - 1:
                    temp.append(0)
                else:
                    temp.append(A[i][j])

                i += 1
                j -= 1
                m -= 1

            diagonal.append(temp)

        return diagonal


if __name__ == '__main__':
    # A = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9],
    # ]

    A = [
        [1, 2],
        [3, 4],
    ]

    print(Solution().diagonal(A=A))
