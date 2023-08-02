#Andrés Santiago Mena Angulo
#67020

print("###########################################")
print("  ESTE ES UN CLASIFICADOR DE TRIANGULOS")
print("###########################################\n\n")

Salir = True
while(Salir):
    LadoA = input("Ingresa el lado \"A\" del triangulo:\n")
    LadoB = input("Ingresa el lado \"B\" del triangulo:\n")
    LadoC = input("Ingresa el lado \"C\" del triangulo:\n")
    Tipo = ""
    if(LadoA == LadoB and LadoB == LadoC):
        Tipo = "Equilatero"
    elif(LadoA != LadoB and LadoB != LadoC and LadoA != LadoC):
        Tipo = "Escaleno"
    else:
        Tipo = "Isósceles"
    print("\nEl tringulo introducido es del tipo " + Tipo + "\n")
    SalirAux=input("[S]alir o [N]uevo triangulo\n")
    if(SalirAux == "S"):
        Salir = False
    elif(SalirAux=="N"):
        Salir = True
