from math import sqrt

class classifyTriangles:
    def main():
        print('Introduce las coordenadas del punto 1:')
        p1 = input()
        print('Introduce las coordenadas del punto 2:')
        p2 = input()
        print('Introduce las coordenadas del punto 3:')
        p3 = input()

        dist1 = sqrt(pow((x1-x0),2)+pow((y1-y0),2))
        dist2 = sqrt(pow((x2-x1),2)+pow((y2-y1),2))
        dist3 = sqrt(pow((x2-x0),2)+pow((y2-y0),2))

        if (isEquilateral(dist1, dist2, dist3) == True):
            print('El triangulo es equilatero')
        elif(isEscalene(dist1, dist2, dist3) == True):
            print('El trinagulo es escaleno')
        else:
            print('El triangulo es isosceles')

    def isEquilateral(dist1, dist2, dist3):
        if (dist1 == dist2 and dist2 == dist3 and dist3 == dist1):
            return True
        else: 
            return False
    def isEscalene(dist1, dist2, dist3):
        if (dist1 != dist2 and dist2 != dist3 and dist3 != dist1):
            return True
        else:
            return False