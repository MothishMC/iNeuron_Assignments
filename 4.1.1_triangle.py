class Triangle():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def setLength(self):
        self.a = int(input("Enter value for a:"))
        self.b = int(input("Enter value for b:"))
        self.c = int(input("Enter value for c:"))


class Tri_area(Triangle):
    def area(self):
        self.setLength()
        s = (self.a + self.b + self.c) / 2
        result = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return result


if __name__ == '__main__':
    triangle = Tri_area()
    result = triangle.area()
    print(f"Area of the triangle is {result}")
