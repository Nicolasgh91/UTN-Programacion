from Funciones_genericas02 import *

#Recibe una lista con diccionarios, toma por páramentro un entero y retorna un listado con n cantidad de dicc solicitados.
def listar_n_elementos_dicc(lista:list,cantidad:int) -> list:
    listado_resultante = []
    contador = 0

    if cantidad > len(lista):
        print("La cantidad de héroes indicada excede a la cantidad de héroes del listado.")
        return -1
    else:
            for dicc in lista:
                if contador < cantidad:
                    listado_resultante.append(dicc)
                    contador += 1
    
    return listado_resultante
#Fin función

# La función toma un listada y una clave. Si esa clave tiene valores númericos, los ordena de manera ascendente o descendente según opción del usuario.
def ordenar_heroe_por_criterio_y_clave(lista:list, clave:str) -> list:
    listado_a_ordenar = []
    opc_usr = input("Queres ordenar de manera ascendente o descendente la lista? 'asc' o 'desc'")
    
    if opc_usr == "asc" or opc_usr == "desc":
        for heroe in lista:
                if type(heroe[clave]) == int or type(heroe[clave]) == float:
                    listado_a_ordenar.append(heroe)
                else:
                    print("Sólo calcula claves con valores númericos.")
                    return -1
    else:
        print("Debe indicar 'desc' o 'asc'.")
        return -1 
    
    listado_resultante = orden_desc_asc(listado_a_ordenar,opc_usr,clave)
    return listado_resultante
#Fin función



# Recibe una lista, una clave númerica de la cual busca un promedio y un condición mayor o menor y retorna una lista de aquellos mayores o menores al promedio obtenido.   
def calcular_promedio_por_clave(lista:list,clave:str,condicion:str) -> list:
    acumulador = 0
    contador = 0
    lista_buscada = []

    if condicion == "mayor" or condicion == "menor":
        for heroe in lista:
            if type(heroe[clave]) == int or type(heroe[clave]) == float:
                acumulador += heroe[clave]
                contador = contador + 1
            else:
                print("La clave deberá ser númerica para poder sacar el promedio.")
                return -1
    else:
        print("La condición debe ser mayor o menor.")
        return -1
    
    if acumulador > 0 and contador > 0:
        promedio =  round((acumulador / contador),2)
    else:
        promedio = 0
    
    for heroe in lista:
        if (heroe[clave] < promedio and condicion =="menor") or (heroe[clave] > promedio and condicion == "mayor"):
            lista_buscada.append(heroe[clave])
        else:
            print("La clave indicada no tiene valor númerico")
            return -1
    
    mensaje = "El promedio de la clave {0} es de: {1}. Y el listado de los heroes con su {2} {3} son: {4}".format(clave,promedio,clave,condicion, lista_buscada)
    # print(mensaje)
    return lista_buscada
#Fin función


#Recibbe una lista y un valor (sólo validos good,average,high) y devuelve un listado de las coincidencias
def listar_valores_x_clave(lista:list,valor:str): 
    patron_regex = r"^(good|average|high| )$"
    listado_resultante = []

    if bool(re.match(patron_regex,valor)) == True:
        for heroe in lista:
            if heroe["inteligencia"] == valor:
                    listado_resultante.append(heroe)
    else:
        print("Las opciones válidas son: 'good', 'average' o 'high'.")
        return -1  
    return listado_resultante
#Fin función

#La función toma una lista y un nombre de archivo por párametro. Genera un archivo con ese nombre y parsea los datos de la lista recibida a formato CSV.
def exportar_lista_csv(lista_a_parsear:list, nombre_archivo_final:str):
    contador = 0
    with open(nombre_archivo_final,"w") as archivo:
        
        for heroe in lista_a_parsear:
            contador = contador + 1
            datos_heroe = "{6}. {0},{1},{2},{3},{4},{5},\n"
            datos_heroe = datos_heroe.format(
                heroe["nombre"],
                heroe["identidad"],
                heroe["altura"],
                heroe["peso"],
                heroe["fuerza"],
                heroe["inteligencia"],
                contador
            )
            archivo.write(datos_heroe)
#Fin función