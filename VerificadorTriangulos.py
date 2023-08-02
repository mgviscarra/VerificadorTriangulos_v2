class VerificadorTriangulos:
    def triangleType(self, a, b, c):
        if a == b and b == c:
            return "Equilatero"
        elif a == b or b == c or a == c:
            return "Isosceles"
        else:
            return "Escaleno"
        
    def main(self):
        triangle = self.triangleType(7, 8, 9)
        print("El triangulo es " + triangle + "\n")

if __name__ == "__main__":
    verificadorTriangulos = VerificadorTriangulos()
    verificadorTriangulos.main()