class Solution:
    # @param A : list of integers
    # @return a list of integers
    # def solve(self, A):
    #     product = 1
    #     for i in A:
    #         product = product * i
    #
    #     new_array = []
    #     for i in A:
    #         new_array.append(product//i)
    #
    #     return new_array

    def solve(self, A):
        pf = []
        sf = []
        multi = 1
        m = 1
        # loop for calculating prefix array
        for i in A:
            multi *= i
            pf.append(multi)
        # loop for calculating sufix array
        for i in reversed(A):
            m *= i
            sf.append(m)
        sf.reverse()  # reversing sf because we cannot calculate and store the value backward

        print(pf, sf)

        # Calculating product array
        product_array = []
        for i in range(len(A)):
            k = len(A)
            left = 1  # handling edge case of index 0
            right = 1  # handling edge case of last index
            if i - 1 >= 0:
                left = pf[i - 1]
            if i + 1 < k:
                right = sf[i + 1]
            n = left * right
            product_array.append(n)
        return product_array


if __name__ == "__main__":
    A = [5, 1, 10, 1]

    # A = [1, 2, 3, 4, 5]

    a = Solution()
    print(a.solve(A=A))
