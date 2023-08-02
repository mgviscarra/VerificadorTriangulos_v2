def determinar_tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

try:
    lado_a = float(input("Ingresa el tamaño del lado A: "))
    lado_b = float(input("Ingresa el tamaño del lado B: "))
    lado_c = float(input("Ingresa el tamaño del lado C: "))

    if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
        print("Error: Los lados deben tener tamaños positivos.")
    else:
        tipo_triangulo = determinar_tipo_triangulo(lado_a, lado_b, lado_c)
        print("El triángulo es de tipo:", tipo_triangulo)
except ValueError:
    print("Error: Ingresa valores numéricos válidos para los lados del triángulo.")
