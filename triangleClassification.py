from trianglesCoordinates import classifyTriangles

class tringleType:
    def main():
        print('Introduce la distancia 1:')
        dist1 = input()
        print('Introduce la distancia 2:')
        dist2 = input()
        print('Introduce la distancia 3:')
        dist3 = input()

        if (tringleType.classifyTriangles.isEquilateral(dist1, dist2, dist3)):
            print('El triangulo es equilatero')
        elif(tringleType.classifyTriangles.isEscalene(dist1, dist2, dist3)):
            print('El triangulo es escaleno')
        else:
            print('El triangulo es isosceles')

tringleType.main()
