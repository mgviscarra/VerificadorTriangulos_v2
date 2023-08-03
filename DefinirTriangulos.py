def triangulo():
    lado1 = int(input("Ingrese el tamaño del primer lado del triángulo: "))
    lado2 = int(input("Ingrese el tamaño del segundo lado del triángulo: "))
    lado3 = int(input("Ingrese el tamaño del tercer lado del triángulo: "))
    
    if lado1 == lado2 == lado3:
        print("Es un triángulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Es un triángulo isósceles.")
    else:
        print("Es un triángulo escaleno.")

triangulo()