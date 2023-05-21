#//////////////////////////////////////////////////////////////////////////////////////////////////
def imprimir_por_consola(funcion): 
    print(funcion)

#//////////////////////////////////////////////////////////////////////////////////////////////////
def normalizar_datos(listado:list):
    mensaje = "Datos normalizados"
    if len(listado) == 0:
        mensaje = "Error: El listado está vacío." 
    else:
        for heroe in listado:
            if type(heroe["altura"]) == str or type(heroe["peso"]) == str or type(heroe["fuerza"]) == str:
                heroe["altura"] = float(heroe["altura"])
                heroe["peso"] = float(heroe["peso"])
                heroe["fuerza"] = int(heroe["fuerza"])
    print(mensaje)

lista_Prueba = [] #lista vacia para 
#Esta función convierte aquellos datos númericos que estaban como tipo de dato de string/texto
# Normaliza los str a int/float donde corresponde

#//////////////////////////////////////////////////////////////////////////////////////////////////
def calcular_max(lista:list,clave:str):
    normalizar_datos(lista)#Primero verifico que los datos estén en el formato correcto.
    max = lista[0]

    for heroe in lista:
        if heroe[clave] > max[clave]:
            max = heroe
    print(max)

# calcular_max(lista_personajes,"fuerza")

#//////////////////////////////////////////////////////////////////////////////////////////////////
def calcular_min(lista,clave:str):
    normalizar_datos(lista)
    min = lista[0]

    for heroe in lista:
        if heroe[clave] < min[clave]:
            min = heroe
    print(min)

