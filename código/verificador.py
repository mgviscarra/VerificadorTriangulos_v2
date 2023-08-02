#local imports
from funciones import *

lados = []
print("INGRESE EL LADO A DEL TRIÁNGULO")
lado_a = input()
while(verificar_lado_válido(lado_a) == False):
    print("--ERROR--\nINGRESE UN NÚMERO VÁLIDO PARA EL LADO A DEL TRIÁNGULO")
    lado_a = input()
lado_a = int(lado_a)

print("INGRESE EL LADO B DEL TRIANGULO")
lado_b = input()
while(verificar_lado_válido(lado_b) == False):
    print("--ERROR--\nINGRESE UN NÚMERO VÁLIDO PARA EL LADO B DEL TRIÁNGULO")
    lado_b = input()
print("INGRESE EL LADO C DEL TRIANGULO")
lado_b = int(lado_b)

lado_c = input()
while(verificar_lado_válido(lado_c) == False):
    print("--ERROR--\nINGRESE UN NÚMERO VÁLIDO PARA EL LADO C DEL TRIÁNGULO")
    lado_c = input()
lado_c = int(lado_c)

if(verificar_triángulo_válido(lado_a, lado_b, lado_c) == False):
    print("EL TRIÁNGULO NO ES VÁLIDO")
else: 
    if(lado_a == lado_b and lado_b == lado_c):
        print("EL TRIANGULO ES EQUILATERO")
    else:
        if(lado_a == lado_b or lado_b == lado_c or lado_a == lado_c):
            print("EL TRIANGULO ES ISOSCELES")
        else:
            print("EL TRIANGULO ES ESCALENO")