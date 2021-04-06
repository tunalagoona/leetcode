"""
https://leetcode.com/problems/3sum/
"""


def get_pairs(nums, sum_of_2, first_num):
    result = []
    s = set()
    for i in range(len(nums)):
        if nums[i] == nums[i - 1]:
            if nums[i] + nums[i - 1] != sum_of_2:
                continue
        if sum_of_2 - nums[i] in s:
            result.append([first_num, nums[i], sum_of_2 - nums[i]])
        s.add(nums[i])
    return result


def get_triplets(nums):
    result = []
    if len(nums) < 3:
        return result
    for i in range(len(nums)):
        res = get_pairs(nums[i + 1 :], -nums[i], nums[i])
        if len(res) != 0:
            result += res

    dedupl_set = set()
    for item in result:
        item.sort()
        dedupl_set.add(tuple(item))
    result = []
    for item in dedupl_set:
        result.append(list(item))

    return result
