from data_c4_stark import lista_personajes
from Funciones_genericas02 import *
from collections import Counter
"""
Alumno: Nicolás Gabriel Hruszczak - Desafío-01
"""



#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def imprimir_nombres_por_genero(lista:list, clave:str, criterio:chr) -> list:
    criterio_normalizado = criterio.upper().strip()
    listado_heroes_obtenidos = []
    #normalizar_datos(lista)
    
    for heroe in lista:
        if heroe[clave] == criterio_normalizado: #Si la clave es igual a la que viene por párametro, lo sumo al listado de héroes
            listado_heroes_obtenidos.append(heroe)
            #print(heroe["nombre"]) #Punto A y B
    return listado_heroes_obtenidos
#Fin función imprimir_nombres_por_genero




#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def buscar_mas_menos_alto_por_genero(lista:list, clave:str, genero:chr, min_max:str) -> list:
    
    ejecucion_func_por_genero = imprimir_nombres_por_genero(lista,"genero",genero)#La clave género es fija y el genero por párametro podrá ser M o F a elección del usuario.
    heroe_buscado = []

    if min_max == "max":
        heroe_buscado = calcular_max(ejecucion_func_por_genero,clave) #Si el criterio fue máximo, llamo a la función calcular max y le paso la lista que guardé en la ejecución de la función "imprimir nombres por género" y la clave será la que entre por párametro para poder ser génerica
    elif min_max == "min":
        heroe_buscado = calcular_min(ejecucion_func_por_genero,clave)
    else:
        return print(mensaje_error_dos_valores("min","max")) 
    
    return heroe_buscado
#Fin función buscar_mas_menos_alto_por_genero




#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def altura_promedio_por_genero(lista:list, clave:str, criterio:chr):
    resultado = 0

    if criterio == "F":
        listado_femeninos = imprimir_nombres_por_genero(lista, "genero", "F") #Me daba error cuando pasaba el criterio en lugar del hardcodeo de "F" o "M", por eso lo hice con dos IF. No encontré el error :S
        resultado = promedio_por_clave(listado_femeninos,clave)
    elif criterio == "M":
        listado_masculinos = imprimir_nombres_por_genero(lista, "genero", "M")
        resultado = promedio_por_clave(listado_masculinos,clave)
    else:
        mensaje_error_un_valor("F o M para el genero.")
    return resultado
#Fin función altura_promedio_por_genero



#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def informar_nombre_heroes_mas_menos_alto_por_genero(listado:list, clave:str, genero:chr, criterio:str) -> str:
    listado_resultante = buscar_mas_menos_alto_por_genero(listado,clave,genero,criterio)
    nombre_heroe = "El héroe buscado se llama: {0}"

    for heroe in listado_resultante:
        nombre_heroe = nombre_heroe.format(heroe["nombre"])
    return nombre_heroe
#Fin función informar_nombre_heroes_mas_menos_alto_por_genero


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def calcular_cantidad_heroes_por_tipo(lista,clave):

    listado_tipos = []
    mensaje = ""
    resultado = []

    for tipo in lista:
        if tipo[clave] == "":
            listado_tipos.append("no tiene dato de inteligencia cargado")
        else:
            listado_tipos.append(tipo[clave]) #Guardo todos los valores de la clave informada por párametro
    
    contador = Counter(listado_tipos) #Este método cuenta las ocurrencias identicas de un listado.
    
    for elemento, cantidad in contador.items(): #Con el método items, obtengo la clave y su valor asociado.
        mensaje = "Del tipo buscado, {0} hay: {1} ocurrencias".format(elemento,cantidad)
        print(mensaje)
        resultado.append(mensaje)

    return resultado
#Fin función calcular_cantidad_heroes_por_tipo



#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def ejecutar_menu_desafio_01():
    print("Bienvenido Mr.Stark, a continuación indique con opción con su letra correspondiente, para obtener la información buscada: \n")

    opcion_a = "\nA. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M\n"
    opcion_b = "B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F\n"
    opcion_c = "C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M \n"
    opcion_d = "D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F \n"
    opcion_e = "E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M \n"
    opcion_f = "F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F\n"
    opcion_g = "G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M\n"
    opcion_h = "H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F\n"
    opcion_i = "I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)\n"
    opcion_j = "J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n"
    opcion_k = "K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n"
    opcion_l = "L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con No Tiene).\n"
    opcion_m = "M. Listar todos los superhéroes agrupados por color de ojos.\n"
    opcion_n = "N. Listar todos los superhéroes agrupados por color de pelo.\n"
    opcion_o = "O. Listar todos los superhéroes agrupados por tipo de inteligencia\n"
    opcion_p = "\nP. Salir del programa \n"
    opciones = ("{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}{15}").format(opcion_a,opcion_b,opcion_c,opcion_d,opcion_e,opcion_f,opcion_g,opcion_h,opcion_i,opcion_j,opcion_k,opcion_l,opcion_m,opcion_n,opcion_o,opcion_p)
    print(opciones)

    while True:
        opc_usr = input("Indique una opción (a-q):")
        opc_usr = opc_usr.lower().strip()

        match opc_usr:
            case "a": print(imprimir_nombres_por_genero(lista_personajes,"genero","M"))
            case "b": print(imprimir_nombres_por_genero(lista_personajes,"genero","F"))
            case "c": print(buscar_mas_menos_alto_por_genero(lista_personajes,"altura","M","max"))
            case "d": print(buscar_mas_menos_alto_por_genero(lista_personajes,"altura","F","max"))
            case "e": print(buscar_mas_menos_alto_por_genero(lista_personajes,"altura","M","min"))
            case "f": print(buscar_mas_menos_alto_por_genero(lista_personajes,"altura","F","min"))
            case "g": print(altura_promedio_por_genero(lista_personajes,"altura","M"))
            case "h": print(altura_promedio_por_genero(lista_personajes,"altura","F"))
            case "i": print(informar_nombre_heroes_mas_menos_alto_por_genero(lista_personajes,"altura","F","max"))
            case "j": print(calcular_cantidad_heroes_por_tipo(lista_personajes,"color_ojos"))
            case "k": print(calcular_cantidad_heroes_por_tipo(lista_personajes,"color_pelo"))
            case "l": print(calcular_cantidad_heroes_por_tipo(lista_personajes,"inteligencia"))
            case "m": print(calcular_cantidad_heroes_por_tipo(lista_personajes,"color_ojos"))
            case "n": print(calcular_cantidad_heroes_por_tipo(lista_personajes,"color_pelo"))
            case "o": print(calcular_cantidad_heroes_por_tipo(lista_personajes,"inteligencia"))
            case "p": break
        print(opciones)

ejecutar_menu_desafio_01()
