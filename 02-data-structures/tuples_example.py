"""Examples of working with Python tuples."""

from collections import namedtuple


coordinates = (10, 20)
print("Tuple:", coordinates)
print("First value:", coordinates[0])
print("Second value:", coordinates[1])

# Tuple unpacking
x, y = coordinates
print("\nUnpacked values:", x, y)

# Tuples are immutable
colors = ("red", "green", "blue")
print("Colors tuple:", colors)
print("Number of colors:", len(colors))

# Named tuple
Point = namedtuple("Point", ["x", "y"])
home = Point(5, 9)
print("\nNamed tuple:", home)
print("home.x =", home.x)
print("home.y =", home.y)
