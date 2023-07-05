class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        i = 1
        answer = 0

        while A > 0:
            if A & 1 != 0:
                answer += 5 ** i

            A = A >> 1

            i += 1

        return answer


if __name__ == '__main__':
    A = 10

    print(Solution().solve(A))
