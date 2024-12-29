""" Add One To Number """


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 1

        self.reverse(A)

        for i in range(0, len(A)):
            temp = A[i] + carry
            if temp >= 10:
                A[i] = 0
                carry = temp // 10
            else:
                A[i] = temp
                carry = 0

        if carry:
            A.append(carry)

        while A[-1] == 0:
            A.pop()

        self.reverse(A)

        return A

    def reverse(self, arr):
        i, j = 0, len(arr) - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1


if __name__ == "__main__":
    # A = [0,8,9,9]
    # A = [0,3,7,6,4,0,5,5,5]
    A = [0, 0, 4, 4, 6, 0, 9, 6, 5, 1]
    print(Solution().plusOne(A))
