def classifyTriangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilátero"
    elif side1 == side2 or side2 == side3 or side3 == side1:
        return "Isósceles"
    else:
        return "Escaleno"
    

