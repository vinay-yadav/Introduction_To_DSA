class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        no_of_triplets = 0
        for j in range(1, len(A) - 1):
            l = sum(1 for i in range(j) if A[i] < A[j])
            r = sum(1 for i in range(j + 1, len(A)) if A[i] > A[j])

            no_of_triplets += l * r

        return no_of_triplets


if __name__ == '__main__':
    # A = [1, 2, 4, 3]
    A = [2, 1, 2, 3]
    print(Solution().solve(A))
