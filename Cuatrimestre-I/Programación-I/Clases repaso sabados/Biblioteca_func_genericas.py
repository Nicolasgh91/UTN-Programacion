def buscador_mayor_valor_dicc(diccionario:dict):
    mayor = None

    for valor in diccionario.values():
        if mayor is None or valor > mayor:
            mayor = valor
    return mayor
#Fin función génerica que busca el mayor valor númerico en un diccionario.

def buscador_menor_valor_dicc(diccionario:dict):
    menor = None

    for valor in diccionario.values():
        if menor is None or valor < menor:
            menor = valor
    return menor
#Fin función génerica que busca el menor valor númerico en un diccionario.
