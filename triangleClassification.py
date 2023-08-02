class tringleType:
    def main():
        print('Introduce la distancia 1:')
        dist1 = input()
        print('Introduce la distancia 2:')
        dist2 = input()
        print('Introduce la distancia 3:')
        dist3 = input()

        if tringleType.isEquilateral(dist1, dist2, dist3):
            print('El triangulo es equilatero')
        elif tringleType.isEscalene(dist1, dist2, dist3):
            print('El triangulo es escaleno')
        else:
            print('El triangulo es isosceles')
    @staticmethod
    def isEquilateral(d1, d2, d3):
        return d1 == d2 == d3
    
    @staticmethod
    def isEscalene(d1, d2, d3):
        return d1 != d2 != d3

tringleType.main()
