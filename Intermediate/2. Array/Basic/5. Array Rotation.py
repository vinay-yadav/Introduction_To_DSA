class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        A = list(A)
        n = len(A)
        B = B % n

        self.reverse(A, 0, n - B - 1)
        self.reverse(A, n - B, n - 1)
        self.reverse(A, 0, n - 1)

        return A

    def reverse(self, array, i, j):
        while i < j:
            array[i], array[j] = array[j], array[i]
            i = i + 1
            j = j - 1


if __name__ == '__main__':
    A = [7, 4, 2, 10, 5]
    B = 10

    t = Solution()
    print(t.solve(A=A, B=B))

"""
Problem Description
    - Given an integer array A of size N and an integer B, you have to return the same array after rotating it B times
      towards the right.

Problem Constraints
    1 <= N <= 105
    1 <= A[i] <=109
    1 <= B <= 109


Input Format
    The first argument given is the integer array A.
    The second argument given is the integer B.


Output Format
    Return the array A after rotating it B times to the right


Example Input
    Input 1:
    A = [1, 2, 3, 4]
    B = 2

    Input 2:
    A = [2, 5, 6]
    B = 1

Example Output
    Output 1:
    [3, 4, 1, 2]

    Output 2:
    [6, 2, 5]

Example Explanation
    Explanation 1:
    Rotate towards the right 2 times - [1, 2, 3, 4] => [4, 1, 2, 3] => [3, 4, 1, 2]

    Explanation 2:
    Rotate towards the right 1 time - [2, 5, 6] => [6, 2, 5]
"""
