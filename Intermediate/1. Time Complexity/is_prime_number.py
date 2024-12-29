from factor_of_a_number import Factor


"""
    Count of factors == 2
"""


class IsPrime:
    def solve(self, n):
        factor = Factor().solve(n=n)
        if factor == 2:
            return 1
        else:
            return 0


print(IsPrime().solve(n=15))
