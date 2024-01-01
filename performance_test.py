from timeit import timeit
def tmit(stmt, setup="", number=10**6):
    print(timeit(stmt=stmt, setup=setup, number=number))
# Data type performance
'''
# tuple
# List 
# dict
# class
# array.array & collections.deque

print("Slots",
# Creat New
timeit(
stmt = """
A = Coor2d(1, 2)
""",
setup = """
class Coor2d:
    __slots__ = ("x", "y")
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
""",
number = 10**8),
# Access created instance
timeit(
stmt = """
A.x == A.y
A.x + A.y
A.x * A.y
""",
setup = """
class Coor2d:
    __slots__ = ("x", "y")
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
A = Coor2d(1, 2)
""",
number = 10**8)
)

print("Without slots",
# Creat New
timeit(
stmt = """
B = Coornd(1, 2)
""",
setup = """
class Coornd:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
""",
number = 10**8),
# Access created instance
timeit(
stmt = """
B.x == B.y
B.x + B.y
B.x * B.y
""",
setup = """
class Coornd:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
B = Coornd(1, 2)
""",
number = 10**8)
)

print("List",
# Creat New
timeit(
stmt = """
C = [1.0, 2.0]
""",
setup = """
""",
number = 10**8),
# Access created instance
timeit(
stmt = """
C[0] == C[1]
C[0] + C[1]
C[0] * C[1]
""",
setup = """
C = [1.0, 2.0]
""",
number = 10**8)
)

print("Array",
# Creat New
timeit(
stmt = """
D = array("f", (1.0, 2.0))
""",
setup = """
from array import array
""",
number = 10**8),
# Access created instance
timeit(
stmt = """
D[0] == D[1]
D[0] + D[1]
D[0] * D[1]
""",
setup = """
from array import array
D = array("f", (1.0, 2.0))
""",
number = 10**8)
)

print("Deque",
# Creat New
timeit(
stmt = """
E = deque([1.0, 2.0], 2)
""",
setup = """
from collections import deque
""",
number = 10**8),
# Access created instance
timeit(
stmt = """
E[0] == E[1]
E[0] + E[1]
E[0] * E[1]
""",
setup = """
from collections import deque
E = deque([1.0, 2.0], 2)
""",
number = 10**8)
)

print("Dictionary",
# Creat New
timeit(
stmt = """
F = {0:1.0, 1:2.0}
""",
setup = """
""",
number = 10**8),
# Access created instance
timeit(
stmt = """
F[0] == F[1]
F[0] + F[1]
F[0] * F[1]
""",
setup = """
F = {0:1.0, 1:2.0}
""",
number = 10**8)
)

print("Tuple",
# Creat New
timeit(
stmt = """
G = (1.0, 2.0)
""",
setup = """
""",
number = 10**8),
# Access created instance
timeit(
stmt = """
D[0] == D[1]
D[0] + D[1]
D[0] * D[1]
""",
setup = """
D = (1.0, 2.0)
""",
number = 10**8)
)


# if A[1] == C[1]:
#     g = lambda y: A[1]
# else:
#     g = lambda y: int((A[0] - C[0]) / (A[1] - C[1]) * y + A[0] - A[1] * (A[0] - C[0]) / (A[1] - C[1]))


# if A[1] == C[1]:
#     g = lambda y: A[1]
# else:
#     t = (A[0] - C[0]) / (A[1] - C[1])
#     g = lambda y: int(t * y + A[0] - A[1] * t)

# exit()

faces = [[0, 1, 2, 3, 4] for _ in range(1000)]
facesMap = list(map(lambda face: face[0] + 10, faces))
for face in faces:
    face[0] += 10
print(facesMap == faces)
print(timeit(
"""
faces = list(map(lambda face: face[0] + 10, faces))
""",
"""
faces = [[0, 1, 2, 3, 4] for _ in range(1000)]
""",
number = 10**3) 
)
print(timeit(
"""
for face in faces:
    face[0] += 10
""",
"""
faces = [[0, 1, 2, 3, 4] for _ in range(1000)]
""",
number = 10**3)
)

l = [([0, 1, 2], 91, 81), ([3, 4, 5,], 92, 82), ([6, 7, 8], 93, 83), ([9, 10, 11], 94, 85)]
print(tuple(map(lambda item: item[0], l)))
print(tuple(zip(*tuple(zip(*l))[0])))
# exit()
# 1.2452824999927543
print(timeit(
"""
tuple(map(lambda item: item[0], l))
""",
"""
l = [([0, 1, 2], 91, 81), ([3, 4, 5,], 92, 82), ([6, 7, 8], 93, 83), ([9, 10, 11], 94, 85)]
""",
number=10**6
))

# 1.1478829000261612
print(timeit(
"""
tuple(zip(*l))[0]
""",
"""
l = [([0, 1, 2], 91, 81), ([3, 4, 5,], 92, 82), ([6, 7, 8], 93, 83), ([9, 10, 11], 94, 85)]
""",
number=10**6
))

# 2.3158868000027724
print(timeit(
"""
tuple(zip(*tuple(zip(*l))[0]))
""",
"""
l = [([0, 1, 2], 91, 81), ([3, 4, 5,], 92, 82), ([6, 7, 8], 93, 83), ([9, 10, 11], 94, 85)]
""",
number=10**6
))
'''
import Readability.png as png
from copy import deepcopy
texture0 = png.Png("texture", "", from_pickle=False, to_pickle=False).pixels
print(png.Png("texture", "").pixels == deepcopy(texture0))

# 0.9501629999722354
print(timeit(
"""
texture = png.Png("texture", "", from_pickle=False, to_pickle=False).pixels
""",
"""
import Readability.png as png
texture0 = png.Png("texture", "", from_pickle=False, to_pickle=False).pixels
""",
number = 10
))

# 3.509561200044118
print(timeit(
"""
texture = deepcopy(texture0)
""",
"""
import Readability.png as png
from copy import deepcopy
texture0 = png.Png("texture", "", from_pickle=False, to_pickle=False).pixels
""",
number = 10
))

