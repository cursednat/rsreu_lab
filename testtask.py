class Vector:
    def __init__(self, l):
        self.i = l[0]
        self.j = l[1]
        self.k = l[2]

    def __add__(self, other):
        return Vector([self.i + other.i, self.j + other.j, self.k + other.k])

    def __sub__(self, other):
        return Vector([self.i - other.i, self.j - other.j, self.k - other.k])

    def __mul__(self, other):
        return Vector([
            self.j * other.k - self.k * other.j,
            self.k * other.i - self.i * other.k,
            self.i * other.j - self.j * other.i])
    def __eq__(self, other):
        return self.i == other.i and self.j == other.j and self.k == other.k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"


a = Vector([1, 0, 0])
b = Vector([0, 1, 0])
print(a)
print(b)
print(a + b)
print(a - b)
print(a * b)
print(a==b)