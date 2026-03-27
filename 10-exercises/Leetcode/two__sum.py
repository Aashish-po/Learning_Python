"""
LeetCode #1: Two Sum
Difficulty: Easy

Given array of integers, return indices of two numbers that add up to target.
"""


def two_sum(nums, target):
    """
    Time: O(n), Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Tests
assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
print("✓ Tests passed!")
