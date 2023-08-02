class VerificadorTriangulos:
    def triangleType(self, a, b, c):
        if a == b and b == c:
            return "Equilatero"
        elif a == b or b == c or a == c:
            return "Isosceles"
        else:
            return "Escaleno"
        
    def checkTriangle(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            print("\nError: Los lados del triangulo deben ser numeros positivos.\n")
            return False
        elif a + b <= c or a + c <= b or b + c <= a:
            print("\nError: La suma de dos lados del triangulo debe ser mayor al tercer lado.\n")
            return False
        else:
            return True
        
    def main(self):
        a = float(input("Ingrese el lado A del triangulo: "))
        b = float(input("Ingrese el lado B del triangulo: "))
        c = float(input("Ingrese el lado C del triangulo: "))
        
        if self.checkTriangle(a, b, c):
            triangle_type = self.triangleType(a, b, c)
            print("El triangulo es " + triangle_type + "\n")

if __name__ == "__main__":
    verificadorTriangulos = VerificadorTriangulos()
    verificadorTriangulos.main()