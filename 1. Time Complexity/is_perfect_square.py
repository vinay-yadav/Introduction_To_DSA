class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, n):
        answer = None

        for i in range(1, n + 1):
            square = i * i

            if not square <= n:
                break

            else:
                answer = i

        if answer * answer == n:
            return answer
        return -1


print(Solution().solve(n=1001))
