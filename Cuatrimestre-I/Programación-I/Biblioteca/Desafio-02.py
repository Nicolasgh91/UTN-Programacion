from data_c4_stark import lista_personajes
import re

"""Alumno: Nicolás Gabriel Hruszczak - Desafío-02"""

"""0)"""
#/////////////////////////////////////////////////////////////////////////////////////////////////////
def stark_normalizar_datos(listado:list) -> str: #Recibe un listado y verifica los datos que deben ser númericos, no sean String. Retorna mensaje.
    mensaje = "Datos normalizados"
    
    if len(listado) == 0:
        mensaje = "Error: El listado está vacío."
        return -1
    else:
        for heroe in listado:
            if type(heroe["altura"]) == str or type(heroe["peso"]) == str or type(heroe["fuerza"]) == str:
                heroe["altura"] = float(heroe["altura"])
                heroe["peso"] = float(heroe["peso"])
                heroe["fuerza"] = int(heroe["fuerza"])
    
    return mensaje
#Fin función

"""1.1"""
#/////////////////////////////////////////////////////////////////////////////////////////////////////
def obtener_nombre(diccionario_heroe:dict) -> list:
    listado = []
    for heroe in diccionario_heroe:
        heroe_buscado = "Nombre: "+ heroe["nombre"]
        #print(heroe_buscado) Acá imprime todos los nombres por consola.
        listado.append(heroe_buscado)
    return listado  
# Fin función

#/////////////////////////////////////////////////////////////////////////////////////////////////////
"""1.2"""
def imprimir_dato(dato_a_imprimir:str):
    print(dato_a_imprimir)
# Fin función

#/////////////////////////////////////////////////////////////////////////////////////////////////////
"""1.3"""
def stark_imprimir_nombres_heroes(listado:list):
    if len(listado) == 0:
        return -1
    else:
        imprimir_dato(obtener_nombre(listado))
# Fin función

#/////////////////////////////////////////////////////////////////////////////////////////////////////
"""2)"""
def obtener_nombre_y_dato(lista:dict, clave:str) -> str:
    mensaje = ""
    if stark_imprimir_nombres_heroes(lista) == -1:
        print("El listado está vacío.")
    else:
        for heroe in lista:
            mensaje = "Nombre: " + heroe["nombre"] + " | {0}: {1}".format(clave, heroe[clave])
            imprimir_dato(mensaje)
# Fin función

"""3"""
#/////////////////////////////////////////////////////////////////////////////////////////////////////
def stark_imprimir_nombres_alturas(listado_heroes:list):
    obtener_nombre_y_dato(listado_heroes, "altura")
# Fin función

"""4.1."""
#/////////////////////////////////////////////////////////////////////////////////////////////////////
def calcular_max(lista:list,clave:str) -> dict:#Recibe una lista, una clave a buscar y retorna una lista con el diccionario del héroe encontrado.
    stark_normalizar_datos(lista)#Primero verifico que los datos estén en el formato correcto.
    max = lista[0]
    lista_resultado = {}

    for heroe in lista:
        if heroe[clave] > max[clave]:
            max = heroe
            
        lista_resultado = max
    return lista_resultado
# Fin función


"""4.2."""
#/////////////////////////////////////////////////////////////////////////////////////////////////////
def calcular_min(lista:list,clave:str) -> dict: #Recibe una lista, una clave a buscar y retorna una lista con el diccionario del héroe encontrado.
    stark_normalizar_datos(lista_personajes)
    min = lista[0]
    lista_resultado = {}
    
    for heroe in lista:
        if heroe[clave] < min[clave]:
            min = heroe

        lista_resultado = min
    return lista_resultado
# Fin función

#/////////////////////////////////////////////////////////////////////////////////////////////////////
"""4.3"""
def calcular_max_min_dato(lista:list,clave:str,criterio:str) -> dict: #Recibe una lista, una clave a buscar y retorna una lista con el diccionario del héroe encontrado.
    resultado = None
    mensaje_error = "El criterio debe ser 'min' o 'max'."
    if criterio == "min":
        resultado = calcular_min(lista,clave)
    elif criterio == "max":
        resultado = calcular_max(lista,clave)
    else:
        return print(mensaje_error)
    return print(resultado)
# Fin función

#/////////////////////////////////////////////////////////////////////////////////////////////////////
"""4.4"""
def stark_calcular_imprimir_heroe(lista:list,clave:str,criterio:str):
    #Función 4.3
    heroe_resultante = calcular_max_min_dato(lista,clave,criterio)
    #Función 1.2
    imprimir_dato(heroe_resultante) 
    #Función punto 2
# Fin función

#/////////////////////////////////////////////////////////////////////////////////////////////////////
#5.1
def sumar_dato_heroe(lista:list,clave:str) -> float:
    acumulador_clave_heroes = 0.0
    listado = []

    if stark_normalizar_datos(lista) == -1:
        return "El listado está vacío."
    else:
        for heroe in lista:
            if type(heroe[clave]) == str:
                listado.append(heroe[clave]) 
            else:
                acumulador_clave_heroes += heroe[clave]
        #print(listado)
        return acumulador_clave_heroes
#Fin función

#/////////////////////////////////////////////////////////////////////////////////////////////////////
#5.2
def dividir(dividiendo:float, divisor:float) -> float:
    resultado = 0.0
    if divisor == 0:
        return 0
    else:
       resultado = dividiendo / divisor
    return resultado
#Fin función

#/////////////////////////////////////////////////////////////////////////////////////////////////////
#5.3
def calcular_promedio(lista:list,clave:str) -> float:
    contador = 0
    for heroe in lista:
        if type(heroe[clave]) == int or type(heroe[clave]) == float:
            contador = contador + 1
        else:
            return print("Hubo algún dato que no era de tipo númerico, intente nuevamente.")
    promedio = dividir(sumar_dato_heroe(lista,clave),contador) 
    return promedio
#Fin función

#/////////////////////////////////////////////////////////////////////////////////////////////////////
#5.4
def stark_calcular_imprimir_promedio_altura(lista:list) -> float:
    if stark_normalizar_datos(lista) == -1:
        return -1
    promedio_altura = calcular_promedio(lista, "altura")
    imprimir_dato(promedio_altura)
    return promedio_altura
#Fin función

#/////////////////////////////////////////////////////////////////////////////////////////////////////
#6.1
def imprimir_menu():
    #dato_clave_heroe = ""
    
    print("Bienvenido villano! Qué información de los héroes deseas obtener?")
    op_1 = "Opción 1: Obtener nombre de los héroes.\n"
    op_2 = "Opción 2: Obtener nombre y altura de los héroes.\n"
    op_3 = "Opción 3: Obtener dato máximo númerico de  héroe, opciones: 'peso', 'altura' o 'fuerza'.\n"
    op_4 = "Opción 4: Obtener dato mínimo númerico de  héroe, opciones: 'peso', 'altura' o 'fuerza'.\n"
    op_5 = "Opción 5: Sumar dato númerico de los héroes, opciones: 'peso', 'altura' o 'fuerza'.\n"
    op_6 = "Opción 6: Calcular promedio de dato númerido de los héroes, opciones: 'peso', 'altura' o 'fuerza'.\n"
    op_7 = "Opción 7: Obtener el promedio de altura de los héroes.\n"

    opciones = "{0}{1}{2}{3}{4}{5}{6}".format(op_1,op_2,op_3,op_4,op_5,op_6,op_7)
    print(opciones)

    """opcion_usr =  int(input("Indica una opción mediante el número que corresponda: "))

    if opcion_usr >= 3 and opcion_usr <= 6:
        dato_clave_heroe = str(input("Que dato del héroe te gustaria calcular? Las opciones son: 'peso','altura' o 'fuerza'.  "))

    dato_clave_heroe = dato_clave_heroe.strip().lower()

    match opcion_usr:
        case 1: stark_imprimir_nombres_heroes(lista_personajes)
        case 2: stark_imprimir_nombres_alturas(lista_personajes)
        case 3: imprimir_dato(calcular_max(lista_personajes,dato_clave_heroe))
        case 4: imprimir_dato(calcular_min(lista_personajes,dato_clave_heroe))
        case 5: imprimir_dato(sumar_dato_heroe(lista_personajes,dato_clave_heroe))
        case 6: imprimir_dato(calcular_promedio(lista_personajes,dato_clave_heroe))
        case 7: stark_calcular_imprimir_promedio_altura(lista_personajes)

    otra_consulta = input("Queres hacer otra consulta? s/n")

    if otra_consulta == "s":
        imprimir_menu()
    else:
        print("Vuelva prontos! Saludos..")"""
#Fin función

#/////////////////////////////////////////////////////////////////////////////////////////////////////
#6.2
def validar_entero(cadena_numerica:str) ->bool:
    patron = r"[0-9]+"
    if bool(re.fullmatch(patron,cadena_numerica)) == True:
        return True
    else:
        return False
#Fin función


"""6.3.Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú de
opciones y le pedirá al usuario que ingrese el número de una de las opciones elegidas y
deberá validarlo. En caso de ser correcto dicho número, lo retornara casteado a entero,
caso contrario retorna -1. Reutilizar las funciones del ejercicio 6.1 y 6.2"""
"""
7. Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes y
se encargará de la ejecución principal de nuestro programa.
Utilizar if/elif o match según prefiera (match solo para los que cuentan con python
3.10+). Debe informar por consola en caso de seleccionar una opción incorrecta y
volver a pedir el dato al usuario. Reutilizar las funciones con prefijo 'stark_' donde crea
correspondiente.
"""
#/////////////////////////////////////////////////////////////////////////////////////////////////////
def stark_menu_principal():
    dato_clave_heroe = ""
    imprimir_menu()
    
    opcion_usr =  input("Indica una opción mediante el número que corresponda: ")
    if validar_entero(opcion_usr) == True:
        opcion_usr = int(opcion_usr)
    else:
        return -1
    
    if opcion_usr >= 3 and opcion_usr <= 6:
        dato_clave_heroe = str(input("Que dato del héroe te gustaria calcular? Las opciones son: 'peso','altura' o 'fuerza'.  "))

    dato_clave_heroe = dato_clave_heroe.strip().lower()

    match opcion_usr:
        case 1: stark_imprimir_nombres_heroes(lista_personajes)
        case 2: stark_imprimir_nombres_alturas(lista_personajes)
        case 3: imprimir_dato(calcular_max(lista_personajes,dato_clave_heroe))
        case 4: imprimir_dato(calcular_min(lista_personajes,dato_clave_heroe))
        case 5: imprimir_dato(sumar_dato_heroe(lista_personajes,dato_clave_heroe))
        case 6: imprimir_dato(calcular_promedio(lista_personajes,dato_clave_heroe))
        case 7: stark_calcular_imprimir_promedio_altura(lista_personajes)

    otra_consulta = input("Queres hacer otra consulta? s/n")

    if otra_consulta == "s":
        stark_menu_principal()
    else:
        print("Vuelva prontos! Saludos..")
#Fin función
# stark_menu_principal()

