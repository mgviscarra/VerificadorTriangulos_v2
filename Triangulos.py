def classifyTriangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilátero"
    elif side1 == side2 or side2 == side3 or side3 == side1:
        return "Isósceles"
    else:
        return "Escaleno"
    
def getSide(message):
    while True:
        try:
            side = int(input(message))
            if side < 1:
                raise ValueError
            return side
        except ValueError:
            print("Ingrese un valor válido (valor entero > 0): ")

def execute():
    control = True
    while control:
        print("Ingrese la longitud de los lados del triángulo:")
        side1 = getSide("Lado 1: ")
        side2 = getSide("Lado 2: ")
        side3 = getSide("Lado 3: ")
        print("El triángulo es: " + classifyTriangle(side1,side2,side3))
        print("¿Desea ingresar los datos de otro triángulo? (1 -> Si, Cualquier tecla -> No)")
        option = input()
        if option != "1":
            control = False
    
if __name__ == "__main__":
    execute()