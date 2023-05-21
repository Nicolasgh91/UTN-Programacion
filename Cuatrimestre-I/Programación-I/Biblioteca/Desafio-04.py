import re
from data_c4_stark import lista_personajes
# Alumno Nicolás Gabriel Hruszczak 

"""1.1.""" # Recibe un string, busca las iniciales de cada palabra y las retorna en un String con todas las iniciales seguidas por un punto.
def extraer_iniciales(nombre_heroe:str) -> str:
    mensaje = "N/A"
    if len(nombre_heroe) == 0:
        return mensaje
    else:
        resultado = re.sub("[-]"," ", nombre_heroe) #Remuevo "-" y reemplazo por espacios.
        resultado = re.sub("[\bthe\b]+","", resultado) #Remuevo todas las ocurrencias de "the"
        resultado = ".".join(re.findall(r"\b[A-Z]", resultado)) + "." #Busco todas las mayúsculas al comienzo de cada palabra.
    return resultado


"""1.2"""
#Recibe un diccionario con los datos de un héroe y le agrega una nueva clave-valor con las iniciales del mismo héroe. Retorna booleano indicando si tuvo éxito.
def definir_iniciales_nombre(heroe:dict) -> bool:
    if type(heroe) == dict and "nombre" in heroe:
        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
        return True
    else:
        return False
#Fin función


#Recibe un listado, verifica haya al menos un elemento e itera la lista verificando si tiene clave nombre y retorna False en caso suceda un error.
def agregar_iniciales_nombre(lista:list) -> bool:
    mensaje = "El origen de datos no contiene el formato correcto"

    if type(lista) == list and len(lista) > 0:
        for heroe in lista:
            resultado = definir_iniciales_nombre(heroe)
            if resultado == False:
                return mensaje
        return True
    else:
        print("Hubo algún otro error")
        return False
#Fin función


"""1.3 bis?"""
def stark_imprimir_nombres_con_iniciales(lista:list):
    if type(lista) == list and len(lista) > 0:
        agregar_iniciales_nombre(lista)
        for heroe in lista:
            heroe["iniciales"] = "(" + heroe["iniciales"] + ")"
            heroe["nombre"] = "* " + heroe["nombre"]
    else:
        return -1
#Fin función


"""2.1""" # Recibe un ID (entero) y el género del héroe, concatena ambos en un string. Y completa de ser necesario para que el string tenga una longitud de 8 caracteres totoal.
def generar_codigo_heroe(id_heroe:int,genero_heroe:str) -> str:
    mensaje = "El ID no es un entero"
    
    if type(id_heroe) == int:
        if genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB":
            str_id_heroe = str(id_heroe)
            mensaje = genero_heroe + "-" + str_id_heroe
            
            if len(mensaje) < 10:
                str_id_heroe = str_id_heroe.rjust(10 - len(mensaje) + len(str_id_heroe), "0") 
                mensaje = genero_heroe + "-" + str_id_heroe
                return mensaje #Devuelve el mensaje con una longitud de 10 caracteres.
        else:
            mensaje = "N/A"
            return mensaje #Devuelve N/A si no es el genero indicado
    else:
        return mensaje # Devuelve el ID no es un entero
#Fin función 
# print(generar_codigo_heroe(2,"NB"))


"""2.2"""
def agregar_codigo_heroe(heroe_dict:dict,id_heroe:int):
    
    if len(heroe_dict) > 0: 
        for heroe in heroe_dict:
            heroe["codigo_heroe"] = generar_codigo_heroe(id_heroe,heroe["genero"])
            print(heroe["codigo_heroe"])

#Fin función
# agregar_codigo_heroe(lista_personajes,2)

