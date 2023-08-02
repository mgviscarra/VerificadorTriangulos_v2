class Triangle:
    def __init__(self):
        self.sideA = 0
        self.sideB = 0
        self.sideC = 0

    def insert_sides(self):
        self.sideA = input("INGRESE EL LADO A DEL TRIANGULO:")
        self.sideB = input("INGRESE EL LADO B DEL TRIANGULO:")
        self.sideC = input("INGRESE EL LADO C DEL TRIANGULO:")

    def get_tiangle_type(self):
        if self.sideA == self.sideB == self.sideC:
            print("EL TRIANGULO ES EQUILATERO")
        elif self.sideA == self.sideB or self.sideB == self.sideC or self.sideA == self.sideC:
            print("EL TRIANGULO ES ISOSCELES")
        else:
            print("EL TRIANGULO ES ESCALENO")

T = Triangle()
T.insert_sides()
T.get_tiangle_type()