class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

        character_count = 0
        amazing_strings = 0

        for i in range(len(A) - 1, -1, -1):
            character_count += 1
            if A[i] in vowels:
                amazing_strings += character_count

        return amazing_strings % (10 ** 4 + 3)


if __name__ == '__main__':
    A = "ABEC"

    print(Solution().solve(A=A))
