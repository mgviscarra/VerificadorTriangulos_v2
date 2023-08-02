def verificar_lado_válido(lado):
    lado_válido = True 
    try:
        lado = int(lado)
        if(lado <= 0):
            lado_válido = False
    except ValueError:
        lado_válido = False
    return lado_válido

def verificar_triángulo_válido(lado_a, lado_b, lado_c):
    válido = False
    if((lado_a+lado_b) > lado_c and (lado_a+lado_c)>lado_b and (lado_b+lado_c)>lado_a):
        válido = True  
        #and ((lado_b+lado_c)>lado_a)
        #
    return válido 