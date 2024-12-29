class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        obj = {}
        for i in range(0, len(A)):
            diff = B - A[i]

            if obj.get(A[i]):
                return 1

            obj[diff] = A[i]

        return 0

        # for i in range(0, len(A)):
        #     for j in range(i + 1, len(A)):
        #         if i != j and A[i] + A[j] == B:
        #             return 1
        #
        # return 0


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    B = 7

    t = Solution()
    print(t.solve(A=A, B=B))

"""
Problem Description
    - Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B).
      Check if any good pair exist or not.

Problem Constraints
    1 <= A.size() <= 104
    1 <= A[i] <= 109
    1 <= B <= 109

Input Format
    - First argument is an integer array A.
    - Second argument is an integer B.

Example Input:
Input 1:
    A = [1,2,3,4]
    B = 7

Input 2:
    A = [1,2,4]
    B = 4

Input 3:
    A = [1,2,2]
    B = 4

Example Output:
    Output 1:
    1

    Output 2:
    0

    Output 3:
    1
"""
