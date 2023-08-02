#AUTOR: MELISA ROJAS SORIA
def verificarTipoTriangulo(a, b, c):
    if a == b == c :
        return "El triangulo es EQUILATERO"
    
    elif a == b or a == c or b == c :
        return "El triangulo es ISOSELES"
    
    else:
        return "El triangulo es ESCALENO"
    
def main():
    try:
        #seccion para ingresar los lados A, B y C de los triangulos
        lA = float(input("Ingrese el Lado A del Triangulo "))
        lB = float(input("Ingrese el Lado B del Triangulo "))
        lC = float(input("Ingrese el Lado C del Triangulo 5"))

        #verificacion del ingreso de numeros positivos
        if lA <= 0 or lB <= 0 or lC <= 0 :
            print("Usted debe ingresar valores numericos y positivos")

        #Realizacion de la verificacion del tipo de triangulo
        else:
            tipoTriangulo = verificarTipoTriangulo(lA, lB, lC)
            print(tipoTriangulo)

    except ValueError:
        print("Error: Ingrese valores numericos validos para los tres lados del triangulo")

if __name__ == "__main__":
    main()