from math import sqrt

class classifyTriangles:
    @staticmethod
    def main():
        print('Introduce las coordenadas del punto 1:')
        p1 = input()
        x0, y0 = map(float, p1.split())
        print('Introduce las coordenadas del punto 2:')
        p2 = input()
        x1, y1 = map(float, p2.split())
        print('Introduce las coordenadas del punto 3:')
        p3 = input()
        x2, y2 = map(float, p3.split())

        dist1 = abs(sqrt(pow((x1-x0),2)+pow((y1-y0),2)))
        dist2 = abs(sqrt(pow((x2-x1),2)+pow((y2-y1),2)))
        dist3 = abs(sqrt(pow((x2-x0),2)+pow((y2-y0),2)))

        if (classifyTriangles.isEquilateral(dist1, dist2, dist3)):
            print('El triangulo es equilatero')
        elif(classifyTriangles.isEscalene(dist1, dist2, dist3)):
            print('El trinagulo es escaleno')
        else:
            print('El triangulo es isosceles')

    @staticmethod
    def isEquilateral(dist1, dist2, dist3):
        return dist1 == dist2 == dist3

    @staticmethod
    def isEscalene(dist1, dist2, dist3):
        return dist1 != dist2 != dist3 != dist1

classifyTriangles.main()
