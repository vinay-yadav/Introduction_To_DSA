class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        answer = ""

        i = n-1
        while i > -1:
            if A[i] != " ":
                current = ""

                while A[i] != " " and i > -1:
                    current += A[i]
                    i -= 1

                current = self.reverse(current)

                if answer:
                    answer += " "
                answer += current

            i -= 1

        return answer

    def reverse(self, string):
        a = ""
        for i in range(len(string)-1, -1, -1):
            a += string[i]
        return a


if __name__ == '__main__':
    # A = "  blue is the sky  "
    # A = "ib is this"
    # A = 'crulgzfkif gg  ombt vemmoxrgf qoddptokkz op xdq hv'
    A = ' bwroafq rfmy eimspekey w wnzjh qisjiabv ya hncn mazvb pfwlcsnkqz muiapt nnvwwx rp bsypbqu ymg bjwapykfil'
    a = Solution().solve(A)
    print(f'"{a}"')
    # print(f'"{A}"')
