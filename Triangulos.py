def verificarTriangulo(a,b,c):
    if a == b == c:
        return "Equilatero"
    elif(a == b or b == c or c == a):
        return "Isosceles"
    else:
        return "Escaleno"
    
def verificarLado(msg):
    while True:
        try:
            lado = int(input(msg))
            if lado < 0:
                raise ValueError
            return lado
        except ValueError:
            print("Ingrese un valor positivo")
        
def ejecutar():
    
    print("\n\nIngrese los lados a, b, c de su triangulo para clasificarlo:")
        
    a = verificarLado("Ingrese el lado a: ")
    b = verificarLado("Ingrese el lado b: ")
    c = verificarLado("Ingrese el lado c: ")

    print("Su triangulo es: " + verificarTriangulo(a,b,c))    
    
    while True:
        res = input("¿Desea intentar de nuevo? y/n\n")
    
        if res.lower() == "y":
            ejecutar()
        elif res.lower() == "n":
            break
        else:
            print("Opcion no valida: "+res)

            
if __name__ == "__main__":
    ejecutar()
            