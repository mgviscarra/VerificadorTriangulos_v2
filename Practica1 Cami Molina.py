def determinar_tipo_triangulo(a, b, c):
    if a == b == c:
        return "EL TRIANGULO ES EQUILATERO"
    elif a == b or a == c or b == c:
        return "EL TRIANGULO ES ISOSCELES"
    else:
        return "EL TRIANGULO ES ESCALENO"

def main():
    try:
        lado_a = float(input("INGRESE EL LADO A DEL TRIANGULO: "))
        lado_b = float(input("INGRESE EL LADO B DEL TRIANGULO: "))
        lado_c = float(input("INGRESE EL LADO C DEL TRIANGULO: "))

        if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
            print("Error: Los lados del triángulo deben ser mayores que cero.")
        else:
            tipo_triangulo = determinar_tipo_triangulo(lado_a, lado_b, lado_c)
            print(tipo_triangulo)

    except ValueError:
        print("Error: Ingrese valores numéricos válidos para los lados del triángulo.")

if __name__ == "__main__":
    main()
