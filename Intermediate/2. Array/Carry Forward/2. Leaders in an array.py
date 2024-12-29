class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        current_max = A[-1]
        no_of_leaders = [current_max]

        for i in range(len(A) - 2, -1, -1):
            current = A[i]

            if current > current_max:
                current_max = current
                no_of_leaders.append(current)

        return no_of_leaders


if __name__ == "__main__":
    A = [16, 17, 4, 3, 5, 2]

    result = Solution().solve(A=A)
    print(result)
