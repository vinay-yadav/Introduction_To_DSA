"""
    Find the first missing natural number
        - natural number => [1, 2, 3,........, n]
"""

# arr = [4, 2, 7, 6, 9, 1, 8, 3]
arr = [4, 1, 3, 3, 2, 5]
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)

for i in range(n):
    ele = arr[i]

    if ele == i + 1:
        continue

    while ele != i + 1 and 1 <= ele <= n:
        if ele == arr[ele - 1]:
            break

        arr[i], arr[ele - 1] = arr[ele - 1], arr[i]
        ele = arr[i]

print(arr)

for i in range(n):
    if arr[i] != i + 1:
        print("Missing number", i + 1)
        break
else:
    print("Missing number", n + 1)
