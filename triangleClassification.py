from trianglesCoornidates import classifyTriangles

def main():
    print('Introduce la distancia 1:')
    dist1 = input()
    print('Introduce la distancia 2:')
    dist2 = input()
    print('Introduce la distancia 3:')
    dist3 = input()

    if (classifyTriangles.isEquilateral(dist1, dist2, dist3)):
        print('El triangulo es equilatero')
    elif(classifyTriangles.isEscalene(dist1, dist2, dist3)):
        print('El triangulo es escaleno')
    else:
        print('El triangulo es isosceles')

classifyClassification.main()
