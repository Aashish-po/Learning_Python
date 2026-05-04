"""Two-sum example used in the exercises section."""


def two_sum(nums, target):
    """Return indices of two numbers that add up to target."""
    seen = {}
    for index, number in enumerate(nums):
        difference = target - number
        if difference in seen:
            return [seen[difference], index]
        seen[number] = index


def main():
    """Demonstrate the two-sum solution with a simple example."""
    example = [2, 7, 11, 15]
    print(two_sum(example, 9))


if __name__ == "__main__":
    main()
