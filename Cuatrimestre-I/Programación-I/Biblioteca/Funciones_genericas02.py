


#//////////////////////////////////////////////////////////////////////////////////
#Pide una opción númerica al usuario, la valida, castea a int y retorna el número.
def opcion_usr() -> int:
    opcion_usuario = ""
    while validar_entero(opcion_usuario) == False:
        opcion_usuario = input("Indique una opción mediante el número correspondiente: ")
    opcion_usuario = int(opcion_usuario)
    return opcion_usuario
#Fin función



#//////////////////////////////////////////////////////////////////////////////////
def imprimir_menu():
    print("Bienvenid@ profe! Qué información de los héroes deseas obtener?")
    op_1 = "Opción 1: Listar n cantidad de héroes.\n"
    op_2 = "Opción 2: Obtener los héroes listados por altura, puede ser de manera ascendente o descendente.\n"
    op_3 = "Opción 3: Obtener los héroes listados por fuerza, puede ser de manera ascendente o descendente.\n"
    op_4 = "Opción 4: Obtener promedio de caracteristica héroe, opciones: 'peso', 'altura' o 'fuerza'. Deberá indicar si quiere listar aquellos héroes que superen el promedio o estén por debajo \n"
    op_5 = "Opción 5: Listar héroes según su inteligencia.\n"
    op_6 = "Opción 6: Exportar a CSV la lista buscada.\n"

    opciones = "{0}{1}{2}{3}{4}{5}".format(op_1,op_2,op_3,op_4,op_5,op_6)
    print(opciones)
#Fin función


import json, re
#//////////////////////////////////////////////////////////////////////////////////
def leer_json(ruta:str) ->list:
    with open(ruta, "r") as archivo:
        lista_resultante = json.load(archivo)
    return lista_resultante
#Fin función


#//////////////////////////////////////////////////////////////////////////////////
def guardar_json(ruta:str, lista_usuarios:list) -> None:
    with open(ruta, "w") as archivo:
        json.dump(lista_usuarios, archivo, indent=4)
#Fin función


#//////////////////////////////////////////////////////////////////////////////////
def guardar_csv(ruta:str, lista:list):
    with open(ruta,"w") as archivo:
        for usuario in lista:
            archivo.write(",".join(usuario)+ "\n")
#Fin función


#//////////////////////////////////////////////////////////////////////////////////
def leer_csv(ruta:str):
    lista_retorno = []

    with open(ruta, "r") as archivo:
        for usuario in archivo:
            lista_aux = usuario.split(",")
            lista_retorno.append(lista_aux)
        return lista_retorno
#Fin función

#//////////////////////////////////////////////////////////////////////////////////
def parseo_json(archivo_a_parsear:str) -> list:
    with open(archivo_a_parsear, "r") as archivo:
        lista_final = []
        todo_el_texto = archivo.read()
        nombre_heroe = re.findall(r' "nombre:" "([\(\)a-zA-Z0-9\| #-\\]+) ',todo_el_texto)
        identidad_heroe = re.findall(r' "identidad:" ',todo_el_texto)
        altura_heroe = re.findall(r' "altura:" ([0-9]+)',todo_el_texto)
        peso_heroe = re.findall(r' "peso:" ([0-9]+)',todo_el_texto)
        fuerza_heroe = re.findall(r' "fuerza:" ([0-9]+)',todo_el_texto)
        inteligencia_heroe = re.findall(r' "inteligencia:" ',todo_el_texto)

        for i in range(len(nombre_heroe)):
            dic_heroe = {}
            dic_heroe["nombre"] = nombre_heroe[i]
            dic_heroe["identidad"] = identidad_heroe[i]
            dic_heroe["altura"] = altura_heroe[i]
            dic_heroe["peso"] = peso_heroe[i]
            dic_heroe["fuerza"] = fuerza_heroe[i]
            dic_heroe["inteligencia"] = inteligencia_heroe[i]
            lista_final.append(dic_heroe)
    return lista_final
#Fin función



#//////////////////////////////////////////////////////////////////////////////////
#Ordenamiento ascendente o descendente, según elección por párametro.
def orden_desc_asc(lista:list, criterio:str, clave:str) ->list:  
    if criterio == "desc" or criterio == "asc":  
        for i in range(len(lista)-1):
            for j in range(i+1, len(lista)):
                if (criterio == "desc" and lista[i][clave] < lista[j][clave]) or (criterio == "asc" and lista[i][clave] > lista[j][clave]):
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux
    else:
         print("El criterio debe ser 'asc' o 'desc'")
         return -1
    return lista
#Fin función


#//////////////////////////////////////////////////////////////////////////////////
#Recibe un diccionario de héroe y parsea sus datos a string para imprimir por consola.
def imprimir_heroe(heroe:dict) -> str:
    parseo_heroe = " Nombre: {0}\n Identidad: {1}\n Altura: {2}\n Peso: {3}\n Fuerza: {4}\n Inteligencia: {5}\n"
    resultado = parseo_heroe.format(heroe["nombre"],heroe["identidad"],heroe["altura"],heroe["peso"], heroe["fuerza"], heroe["inteligencia"])
    return resultado
#Fin función

#//////////////////////////////////////////////////////////////////////////////////
def validar_entero(cadena_numerica:str) ->bool:
    patron = r"[0-9]+"
    if bool(re.fullmatch(patron,cadena_numerica)) == True:
        return True
    else:
        return False
#Fin función


#//////////////////////////////////////////////////////////////////////////////////
#Recibe una lista y copia la misma.
def copiar_lista(lista:list) -> list:
    lista_copiada = lista.copy()
    return lista_copiada
#Fin función.

#//////////////////////////////////////////////////////////////////////////////////
def imprimir_por_consola(funcion): 
    print(funcion)

#//////////////////////////////////////////////////////////////////////////////////
def normalizar_datos(listado:list) -> list:
    mensaje = "Datos normalizados"

    if len(listado) == 0: 
        mensaje = "Error: El listado está vacío."
        return imprimir_por_consola(mensaje)
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


#//////////////////////////////////////////////////////////////////////////////////
def calcular_max(lista:list,clave:str) -> list:
    normalizar_datos(lista)#Primero verifico que los datos estén en el formato correcto.
    max = lista[0]
    elemento_maximo = []

    for heroe in lista:
        if heroe[clave] > max[clave]:
            max = heroe
    elemento_maximo.append(max)
    return elemento_maximo

# calcular_max(lista_personajes,"fuerza")

#//////////////////////////////////////////////////////////////////////////////////
def calcular_min(lista,clave:str) -> list:
    normalizar_datos(lista)
    min = lista[0]
    elemento_minimo = []

    for heroe in lista:
        if heroe[clave] < min[clave]:
            min = heroe
    elemento_minimo.append(min)
    return elemento_minimo

#//////////////////////////////////////////////////////////////////////////////////
def mensaje_error_dos_valores(valor_uno:str, valor_dos:str) -> str:
    mensaje = "Hubo un error, por favor introduzca {0} o {1}".format(valor_uno,valor_dos)
    return mensaje

#//////////////////////////////////////////////////////////////////////////////////
def mensaje_error_un_valor(valor_uno:str) -> str:
    mensaje = "Hubo un error, por favor introduzca {0} ".format(valor_uno)
    return mensaje

#//////////////////////////////////////////////////////////////////////////////////
def promedio_por_clave(lista:list,clave:str) -> float:
    acumulador = 0
    contador = 0
    
    for heroe in lista:
        acumulador += heroe[clave]
        contador += 1

    if contador and acumulador > 0.01:
        promedio = round( (acumulador / contador), 2)
    else:
        return "Hubo un error en el promedio."
    return promedio
#Fin función promedio

#//////////////////////////////////////////////////////////////////////////////////
def buscador_mayor_valor_dicc(diccionario:dict):
    mayor = None

    for valor in diccionario.values():
        if mayor is None or valor > mayor:
            mayor = valor
    return mayor
#Fin función génerica que busca el mayor valor númerico en un diccionario.

#//////////////////////////////////////////////////////////////////////////////////
def buscador_menor_valor_dicc(diccionario:dict):
    menor = None

    for valor in diccionario.values():
        if menor is None or valor < menor:
            menor = valor
    return menor
#Fin función génerica que busca el menor valor númerico en un diccionario.

#//////////////////////////////////////////////////////////////////////////////////