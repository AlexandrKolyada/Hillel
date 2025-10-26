from math import sqrt, isclose


class Rectangle:

    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return isclose(self.get_square(), other.get_square())

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        total_area = self.get_square() + other.get_square()

        if total_area == 0:
            return Rectangle(0, 0)
        ratio = self.width / self.height if self.height != 0 else 1.0
        new_w = sqrt(total_area * ratio)
        new_h = total_area / new_w
        return Rectangle(new_w, new_h)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        if n < 0:
            raise ValueError("Множник має бути невід’ємним")
        if n == 0 or self.get_square() == 0:
            return Rectangle(0, 0)
        scale = sqrt(n)
        return Rectangle(self.width * scale, self.height * scale)

    def __rmul__(self, n):
        return self.__mul__(n)

    def __str__(self):
        return f"Rectangle({self.width:g}, {self.height:g})"

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert isclose(r3.get_square(), 26), 'Test3'

r4 = r1 * 4
assert isclose(r4.get_square(), 32), 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print(r3.get_square())
print(r4.get_square())