import copy


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        prefix_sum = self.create_prefix_sum_array(array=A)

        for i in range(0, len(A)):
            if i == 0:
                left = 0
            else:
                left = prefix_sum[i - 1]

            right = prefix_sum[len(A) - 1] - prefix_sum[i]

            if left == right:
                return i

        return -1

    @staticmethod
    def create_prefix_sum_array(array):
        new_array = copy.deepcopy(array)
        for i in range(1, len(new_array)):
            new_array[i] = new_array[i] + new_array[i - 1]

        return new_array


if __name__ == "__main__":
    A = [-7, 1, 5, 2, -4, 3, 0]

    # A = [1, 2, 3]

    a = Solution()
    print(a.solve(A=A))
