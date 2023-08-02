def verificar_tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def obtener_valor_numerico(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingresa un valor numérico válido.")

def main():
    print("Verificación de tipo de triángulo")
    
    lado_a = obtener_valor_numerico("Ingresa el valor del lado A: ")
    lado_b = obtener_valor_numerico("Ingresa el valor del lado B: ")
    lado_c = obtener_valor_numerico("Ingresa el valor del lado C: ")
    
    if lado_a > 0 and lado_b > 0 and lado_c > 0:
        tipo = verificar_tipo_triangulo(lado_a, lado_b, lado_c)
        print(f"El triángulo es de tipo: {tipo}")
    else:
        print("Los valores de los lados deben ser positivos.")

if __name__ == "__main__":
    main()