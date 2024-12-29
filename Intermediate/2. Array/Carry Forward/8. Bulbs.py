class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        count = 0

        for i in A:
            if count % 2 == 0:
                state = i
            else:
                state = 1 - i

            if state == 0:
                count += 1

        return count


if __name__ == '__main__':
    # A = [0, 1, 0, 1]
    A = [1, 1, 1, 1]

    print(Solution().bulbs(A=A))
