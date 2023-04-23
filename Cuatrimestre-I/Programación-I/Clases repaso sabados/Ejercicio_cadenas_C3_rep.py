
# Alumno: Nicolás Gabriel Hruszczak
# Ejercicio cadenas

"""
1.Contar letras: Crea una función que tome una cadena
de texto como argumento y
cuente el número de letras que contiene.
"""
ejercicio_uno_string = "Hoy termino los desafios"

def contador_letras_string(cadena:str) -> int:
    cadena_sin_espacios_extremos = cadena.strip()
    contador = 0
    
    for caracter in cadena_sin_espacios_extremos:
        contador += 1
    print("La cantidad de caracteres que tiene el string es: ",contador)
    print("Usando el método len, la cadena tiene ", len(cadena), " caracteres")
#Fin función contador de letras por string.
# contador_letras_string(ejercicio_uno_string)

"""
2.Eliminar caracteres: Crea una función que tome una
cadena de texto y un carácter como argumentos, y
elimine todas las ocurrencias de ese carácter en la
cadena.
"""
ejercicio_dos_string = "Hoy termino los desafios"
def eliminar_caracter_indicado(cadena:str, caracter_a_eliminar:chr) -> str:
    for caracter in cadena:
        if caracter == caracter_a_eliminar:
            cadena = cadena.replace(caracter_a_eliminar,"")
            
    return print(cadena)

# eliminar_caracter_indicado(ejercicio_uno_string,"o")

"""
3.Contar palabras: Crea una función que tome una
cadena de texto como argumento y
cuente el número de palabras que contiene.
Suponga que las palabras están separadas por un
espacio.
"""
cadena_prueba_ej_3 = "Hola Hola Hola Hola Hola Hola Hola Hola 9"
def contador_palabras_por_cadena(cadena:str) -> str:
    contador = 0
    mensaje = "La cantidad de palabras es: "
    for caracter in cadena:
        if caracter == " ":
            contador += 1
    
    if cadena.endswith(" "):
        return print(mensaje,contador) #Si termina con un espacio, quiere decir que no hay mas palabras
    else:
        contador = contador + 1 #Si no termina con un espacio, es por que termina con un caracter, por ende hay una palabra más
        return print(mensaje,contador)

# contador_palabras_por_cadena(cadena_prueba_ej_3)

"""
4.Reemplazar palabras: Crea una función que tome una
cadena de texto, una palabra y otra palabra como
argumentos, y reemplace todas las ocurrencias de la
primera palabra por la segunda en la cadena.
"""
cadena_prueba_ej_4 = "Sábado Sábado Sábado Sábado Sábado Sábado "
def reemplazar_palabras(cadena:str, primer_palabra:str, segunda_palabra:str) -> str:
  cadena_modificada = cadena.replace(primer_palabra, segunda_palabra)
  return print(cadena_modificada)

# reemplazar_palabras(cadena_prueba_ej_4,"Sábado", "Domingo")

"""
5.Buscar patrón: Crea una función que tome dos cadenas
de texto como argumentos: una cadena principal y un
patrón. La función debe encontrar todas las ocurrencias
del patrón en la cadena principal y devolver una lista con
las posiciones donde se encontró el patrón.
"""
string_ej_5 = "Juan tiene 5 perros, 2 gatos, 5 perros y 2 jirafas."

def buscar_ocurrencias(cadena:str, patron:str) -> list:
    listado = []
    posicion = 0
   
    while True:
        indice = cadena.find(patron, posicion) #Arranca en la posición 0 y va iterando caracter por caracter.
        if indice == -1:# Cuando llega al final, retorna -1 y finaliza el ciclo.
            break
        else:
            listado.append(indice)
            posicion = indice + 1 #Cambia a la siguiente posición para iterar.
    return listado

buscar_ocurrencias(string_ej_5, "perros")




