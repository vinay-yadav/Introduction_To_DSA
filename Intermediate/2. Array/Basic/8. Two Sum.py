from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()

        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in num_dict:
                return [num_dict[compliment], i]

            num_dict[num] = i

        return []


if __name__ == '__main__':
    # nums = [2, 7, 11, 15]
    # target = 9

    nums = [3, 2, 4]
    target = 6

    print(Solution().twoSum(nums=nums, target=target))
