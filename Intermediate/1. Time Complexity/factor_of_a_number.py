import math

"""
    Any no. which divides 'n' completely.
    
    i * j = N
    j = N / i
    
    
    e.g = 24
    
    i   N/i
    1   24
    2   12
    3   8
    4   6
    6   4
    8   3
    12  2
    24  1
    
    Conclusion: i <= N/i => i * i <= N
"""


class Factor:
    # @param A : integer
    # @return an integer
    def solve(self, n):
        answer = 0

        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if i == n / i:
                    answer = answer + 1
                else:
                    answer = answer + 2

        return answer


if __name__ == '__main__':
    print(Factor().solve(n=100))
