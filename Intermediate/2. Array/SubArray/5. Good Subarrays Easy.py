class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        good_array_count = 0

        n = len(A)

        for s in range(n):
            sub_array_sum = 0
            for e in range(s, n):
                no_of_elements = e - s + 1
                sub_array_sum += A[e]

                if no_of_elements % 2 == 0:
                    if sub_array_sum < B:
                        good_array_count += 1
                else:
                    if sub_array_sum > B:
                        good_array_count += 1

        return good_array_count


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = 4

    # A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
    # B = 65

    print(Solution().solve(A=A, B=B))
