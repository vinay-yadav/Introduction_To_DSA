class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return an list of long
    def solve(self, A, B):
        self.create_prefix_sum_array(array=A)

        answer = []

        for i in B:
            lower = i[0]
            upper = i[1]

            if lower == 0:
                answer.append(A[upper])
            else:
                answer.append(A[upper] - A[lower - 1])

        return answer

    @staticmethod
    def create_prefix_sum_array(array):
        for i in range(0, len(array)):
            if array[i] % 2 == 0:
                num = 1
            else:
                num = 0

            if i == 0:
                array[i] = num
            else:
                array[i] = num + array[i - 1]


if __name__ == "__main__":
    # A = [1, 2, 3, 4, 5]
    # B = [[0, 2], [2, 4], [1, 4]]

    A = [2, 1, 8, 3, 9, 6]
    B = [[0, 3], [3, 5], [1, 3], [2, 4]]

    a = Solution()
    print(a.solve(A=A, B=B))
