class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def DecimalToAnyBase(self, A, B):
        if A == 0:
            return 0

        any_base = ""
        while A > 0:
            any_base += str(A % B)
            A = A // B

        return any_base[::-1]


if __name__ == '__main__':
    # A = 4
    # B = 3

    # A = 4
    # B = 2

    A = 0
    B = 7

    print(Solution().DecimalToAnyBase(A, B))
