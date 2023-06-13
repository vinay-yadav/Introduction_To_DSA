import math


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        primes = []

        for i in range(1, A + 1):
            if self.is_prime_number(n=i):
                primes.append(i)

        print("primes", primes)

        return len(primes)

    def is_prime_number(self, n):
        answer = 0

        for i in range(1, int(math.sqrt(n)) + 1):
            if answer > 2:
                break

            if n % i == 0:
                if i == n / i:
                    answer = answer + 1
                else:
                    answer = answer + 2

        return answer == 2


print(Solution().solve(A=19))
