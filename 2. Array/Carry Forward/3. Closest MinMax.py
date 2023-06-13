import sys


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        min_a = min(A)
        max_a = max(A)

        min_index = -1
        max_index = -1
        answer = sys.maxsize

        for i in range(len(A) - 1, -1, -1):
            current = A[i]

            if current == min_a:
                min_index = i
            elif current == max_a:
                max_index = i

            if max_index > min_index:
                diff = max_index - min_index + 1
            else:
                diff = min_index - max_index + 1

            if min_index > -1 and max_index > -1 and diff < answer:
                answer = diff

        return answer


if __name__ == "__main__":
    # A = [1, 3, 2]
    # A = [2, 6, 1, 6, 9]
    A = [343, 291, 963, 165, 152]

    result = Solution().solve(A=A)
    print(result)
