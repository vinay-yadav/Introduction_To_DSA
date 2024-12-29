class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return an list of long
    def rangeSum(self, A, B):
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
        for i in range(1, len(array)):
            array[i] = array[i] + array[i - 1]


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = [[0, 3], [1, 2]]

    # A = [2, 2, 2]
    # B = [[0, 0], [1, 2]]

    a = Solution()
    print(a.rangeSum(A=A, B=B))
