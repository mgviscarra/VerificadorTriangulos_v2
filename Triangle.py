class Triangle:
    def __init__(self):
        self.sideA = 0
        self.sideB = 0
        self.sideC = 0

    def insert_sides(self):
        self.sideA = self.get_float_value("INGRESE EL LADO A DEL TRIANGULO:")
        self.sideB = self.get_float_value("INGRESE EL LADO B DEL TRIANGULO:")
        self.sideC = self.get_float_value("INGRESE EL LADO C DEL TRIANGULO:")

    def get_tiangle_type(self):
        if self.sideA == self.sideB == self.sideC:
            print("EL TRIANGULO ES EQUILATERO")
        elif self.sideA == self.sideB or self.sideB == self.sideC or self.sideA == self.sideC:
            print("EL TRIANGULO ES ISOSCELES")
        else:
            print("EL TRIANGULO ES ESCALENO")

    def get_float_value(self, message):
        while True:
            try:
                side = float(input(message))
                return side
            except ValueError:
                print("ERROR: Por favor ingrese un número.")

while True:

    T = Triangle()

    check = input("¿Desea ingresar un triangulo? (s/n): ")

    if check.lower() == "s":
        T.insert_sides()
        T.get_tiangle_type()
    elif check.lower() == "n":
        break
    else:
        print("Error: Ingrese 's' para continuar o 'n' para salir.")