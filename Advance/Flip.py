""" Flip """


class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        A = list(A)
        l = r = current = maxx = 0
        ans = [0] * 2

        for i in range(len(A)):
            char = A[i]
            if char == "1":
                current -= 1
            else:
                current += 1

            if current > maxx:
                maxx = current
                ans[0] = l + 1
                ans[1] = r + 1

            if current < 0:
                current = 0
                l = r = i + 1
            else:
                r += 1

        if not maxx:
            return list()

        return ans

if __name__ == "__main__":
    # A = "010"
    # A = "111"
    A = "110000111001"
    print(Solution().flip(A))
