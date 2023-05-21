from data_c4_stark import lista_personajes
"""
Alumno: Nicolás Gabriel Hruszczak

1-Alta
2-Baja
3-Salir
"""

#//////////////////////////////////////////////////////////////////////////////////////////////////
def stark_industries():
    
    while True:
        print("\n 1-Alta \n 2-Baja \n 3-Salir \n ")
        opcion_usr = int (input("Indique una opción: "))

        match opcion_usr:
            case 1: print("op 1")
            case 2: print("op 1")
            case 3: break

# stark_industries()#Fin función

#//////////////////////////////////////////////////////////////////////////////////////////////////
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def nombres_heroes():
    for i in lista_personajes:
        print("El nombre del súperheroe es: ", i["nombre"])

#//////////////////////////////////////////////////////////////////////////////////////////////////
# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def nombres_y_altura_heroes():
    for i in lista_personajes:
        print("El nombre del súperheroe es: ", i["nombre"], " y su altura es: ", round( float (i["altura"]),2 ))

#//////////////////////////////////////////////////////////////////////////////////////////////////
# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def heroe_mas_alto():
    mas_alto = lista_personajes[0]
    for personaje in lista_personajes:
        if float(personaje["altura"]) > float(mas_alto["altura"]):
            mas_alto = personaje
    print("El heroe más alto tiene: ", round(float( mas_alto["altura"]),2) ," altura")

#//////////////////////////////////////////////////////////////////////////////////////////////////
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def heroe_mas_bajo():
    mas_bajo = lista_personajes[0]
    
    for personaje in lista_personajes:
        if float(personaje["altura"]) < float(mas_bajo["altura"]):
            mas_bajo = personaje
    print("El heroe más alto tiene: ", round(float(mas_bajo["altura"]),2) ," altura")

#//////////////////////////////////////////////////////////////////////////////////////////////////
# F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
def altura_promedio():
    acumulador = 0
    promedio = 0
    contador = 0
    for heroe in lista_personajes:
        acumulador += float(heroe["altura"])
        contador += 1
    promedio = round(acumulador / contador, 2)
    print("El promedio de altura entre todos los súper heroes es de: ", promedio)

#//////////////////////////////////////////////////////////////////////////////////////////////////
#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
def nombre_heroes_mas_alto_y_bajo():
    menor = lista_personajes[0]
    mayor = lista_personajes[0]

    for heroe in lista_personajes:
        if float(heroe["altura"]) > float(mayor["altura"]):
            mayor = heroe
        if float(heroe["altura"]) < float(menor["altura"]):
            menor = heroe
            
    print("El heroe más bajo es: ", menor["nombre"], "\n y el más alto es: ", mayor["nombre"])

#//////////////////////////////////////////////////////////////////////////////////////////////////
# H. Calcular e informar cual es el superhéroe más y menos pesado.
def heroes_mas_ligero_y_pesado():
    ligero = lista_personajes[0]
    pesado = lista_personajes[0]

    for heroe in lista_personajes:
        if float(heroe["peso"]) > float(pesado["peso"]):
            pesado = heroe
        if float(heroe["peso"]) < float(ligero["peso"]):
            ligero = heroe
    print("El héroe más pesado es: ", pesado["nombre"], " y el más ligero es: ", ligero["nombre"])


#//////////////////////////////////////////////////////////////////////////////////////////////////
# I. Ordenar el código implementando una función para cada uno de los valores informados.
def menu_ejecutable_stark_industries():
    print("Bienvenido Mr.Stark, a continuación indique con opción númerica que información desea obtener: \n")
    
    opciones = "Opción 1: Ver el nombre de cada superhéroe. \nOpción 2: Ver el nombre y altura de cada superhéroe. \nOpción 3: Ver quien es el más alto. \nOpción 4: Ver quien es el más bajo. \nOpción 5: Ver el promedio de altura. \nOpción 6: Ver el nombre del más alto y del más bajo. \nOpción 7: Ver el nombre del más pesado y del más liviano.\nOpción 8: Ver opciones\nOpción 9: Finalizar la aplicación."
    print(opciones)

    while True:
        opc_usr = int (input("Indique una opción: "))
        
        match opc_usr:
            case 1: nombres_heroes()
            case 2: nombres_y_altura_heroes()
            case 3: heroe_mas_alto()
            case 4: heroe_mas_bajo()
            case 5: altura_promedio()
            case 6: nombre_heroes_mas_alto_y_bajo()
            case 7: heroes_mas_ligero_y_pesado()
            case 8: print(opciones)
            case 9: break
        print(opciones)

menu_ejecutable_stark_industries()

#//////////////////////////////////////////////////////////////////////////////////////////////////
def calcular_maximo(listado:list, variante:str) -> dict:
    """
        Calcula un máximo en base a una clave/variante recibida. 
        Recibe: una lista de diccionarios y un string que representará la clave del diccionario.
        Retorna: El máximo diccionario que corresponda a la clave recibida.
        Y retornará -1 en caso de surgir algún error.
    """
    if type(listado) == type(list()) and type(variante) == type(str()) and len(listado) > 0:
        max = listado[0]
        min = listado[0]
        retorno = -1
        for e_lista in listado:
            if e_lista[variante] > max[variante]:
                max = e_lista
                retorno = max
            if e_lista[variante] < min[variante]:
                min = e_lista[variante]
                retorno = min
            return retorno

#//////////////////////////////////////////////////////////////////////////////////////////////////