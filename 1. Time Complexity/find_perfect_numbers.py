import math


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        sum_of_factors = self.get_sum_of_proper_divisor(n=A)

        if sum_of_factors == A:
            return 1
        return 0

    @staticmethod
    def get_sum_of_proper_divisor(n):
        proper_divisors = []

        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0 and i < n:
                proper_divisors.append(i)

                ratio = n / i
                if ratio < n and ratio not in proper_divisors:
                    proper_divisors.append(int(ratio))

        print("proper_divisors", proper_divisors)
        return sum(proper_divisors)


print(Solution().solve(A=6))
