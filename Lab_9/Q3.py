class Polygon:
    def __init__(self, n=0):
        if n == 0:
            self.no_of_sides = int(input("Input No of sides:"))
        else:
            self.no_of_sides = n
        self.edges()

    def edges(self):
        k = input("Enter the edge lengths: ")
        self.lengths = [float(x) for x in k.split(',')]
        assert (len(self.lengths) == self.no_of_sides)


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
        print("Area: ", self.area())

    def area(self):
        perimeter = 0
        for i in self.lengths:
            perimeter += i
        s = perimeter / 2
        a = 1
        for i in self.lengths:
            a = a * (s - i) ** 0.5
        a = (s ** 0.5) * a
        return a


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)
        print("Diagonal Length: ", self.diagonal())

    def edges(self):
        k = input("Enter the length of perpendicular sides: ")
        self.lengths = [float(x) for x in k.split(',')]

    def diagonal(self):
        d = 0
        for x in self.lengths:
            d += (x * x)
        return d**0.5


a = Rectangle()
b = Triangle()
c = Polygon()
