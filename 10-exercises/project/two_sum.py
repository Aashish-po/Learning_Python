# Two-sum example placeholder
def two_sum(nums, target):
    """Return indices of two numbers that add up to target (simple example)."""
    seen = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i


if __name__ == "__main__":
    example = [2, 7, 11, 15]
    print(two_sum(example, 9))
