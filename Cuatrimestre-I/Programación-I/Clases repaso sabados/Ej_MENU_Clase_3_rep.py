from Biblioteca_func_genericas import *

"""
Alumno: Nicolás Gabriel Hruszczak

Ejercicio con Menú de Opciones
Realizar un programa utilizando los conceptos de la clase:
Opciones del menú:
# 1 Cargar una lista con 10 nombres de animales (perro, gato, león, etc,) y de que tipo son
(terrestre, anfibio, volador).
# 2 Imprimir la lista completa de animales con su tipo.
# 3 Mostrar el porcentaje de animales por tipo.
# 4 Mayor cantidad de animales por tipo.
# 5 Menor cantidad de animales por tipo.
# 6 Pedir un animal e informar si está en la lista y sus datos correspondientes si
efectivamente está en la lista.
# 7 Pedir un animal e informar la primer ocurrencia de ese animal en la lista si es que existe.
# 8 Informar la cantidad de animales por cada tipo de animal.
# 9 Vaciar la lista.
#10 Salir.
"""

"""
# 1 Cargar una lista con 10 nombres de animales (perro, gato, león, etc,) y de que tipo son
(terrestre, anfibio, volador).
"""
listado_animales = [ #Listado de diccionarios
    {"Nombre": "Oso Yogi",# clave, valor
     "Tipo": "Terrestre"
    },
    {"Nombre": "Sapo Pepe",
     "Tipo": "Anfibio"
    },
    {"Nombre": "El pipi",
     "Tipo": "Volador"
    },
    {"Nombre": "Gloria",
     "Tipo": "Terrestre"
    },
    {"Nombre": "Diego",
     "Tipo": "Terrestre"
    },
    {"Nombre": "Melman",
     "Tipo": "Terrestre"
    },
    {"Nombre": "Rico",
     "Tipo": "Ave marina"
    },
    {"Nombre": "Cabo",
     "Tipo": "Ave marina"
    },
    {"Nombre": "Marty",
     "Tipo": "Terrestre"
    },
    {"Nombre": "Rana cuak",
     "Tipo": "Anfibio"
    }
]

"""
# 2 Imprimir la lista completa de animales con su tipo.
"""
def imprimir_listado(listado:list) -> list:
    for elemento in listado:
        animal = "Animal de nombre: {0} es de tipo {1}.".format(elemento["Nombre"],elemento["Tipo"])
        print(animal)

# imprimir_listado(listado_animales)

"""
# 3 Mostrar el porcentaje de animales por tipo.
"""

def calcular_porcentaje_por_tipo_animal(listado:list) -> float:
    
    listado_contadores = {
        "Aves Marinas": 0,
        "Animales terrestres": 0,
        "Animales anfibios": 0,
        "Animales voladores": 0
    }
    
    for animal in listado:
        if animal["Tipo"] == "Ave marina":
            listado_contadores["Aves Marinas"] += 1
        if animal["Tipo"] == "Terrestre":
            listado_contadores["Animales terrestres"] += 1
        if animal["Tipo"] == "Anfibio":
            listado_contadores["Animales anfibios"] += 1
        if animal["Tipo"] == "Volador":
            listado_contadores["Animales voladores"] += 1
    
    for tipo_animal, valor in listado_contadores.items():
        porcentaje = (100 / len(listado)) * valor
        mensaje = "El porcentaje de los {0} es {1}".format(tipo_animal,porcentaje)
        print(mensaje)

# calcular_porcentaje_por_tipo_animal(listado_animales)

"""
# 4 Mayor cantidad de animales por tipo.
# 5 Menor cantidad de animales por tipo.
"""
def tipo_mas_repetido(listado:list, clave:str):
    el_mas_repetido = {} # Voy a acumular la cantidad de apariciones de cada valor.

    for diccionario in listado:   
        tipo = diccionario.get(clave) #El método get() me trae el valor de la clave pasada por párametro.
        if tipo in el_mas_repetido: # Si esa clave ya está en el dicc del mas repetido, entonces le sumo 1.
            el_mas_repetido[tipo] += 1
        else:
            el_mas_repetido[tipo] = 1 #Pero si esa clave que encontró, no estaba, entonces la agrego con valor 1.
    
    print(el_mas_repetido)
    print(buscador_mayor_valor_dicc(el_mas_repetido))
    print(buscador_menor_valor_dicc(el_mas_repetido))

tipo_mas_repetido(listado_animales,"Tipo")

"""
# 6 Pedir un animal e informar si está en la lista y sus datos correspondientes si
efectivamente está en la lista.
"""

def buscar_tipo(lista,tipo):
    

















def ejecutar_menu_animales():
    opcion_usr = int (input("Por favor indique una opción: "))

    listado_opciones = [
        { 2: "#2 Imprimir listado de animales."
        },
        { 3: "#3 Mostrar el porcentaje de animales por tipo."
        },
        { 4: "#4 Mayor cantidad de animales por tipo."
        },
        { 5: "#5 Menor cantidad de animales por tipo."
        },
        { 6: "#6 Pedir un animal e informar si está en la lista y sus datos correspondientes si efectivamente está en la lista."
        },
        { 7: "#7 Pedir un animal e informar la primer ocurrencia de ese animal en la lista si es que existe."
        },
        { 8: "#8 Informar la cantidad de animales por cada tipo de animal."
        },
        { 9: "#9 Vaciar la lista."
        },
        { 10: "#10 Salir."
        },
    ]

    match opcion_usr:
        case 2: print("Op2")
        case 3: print("Op3")
        case 4: print("Op4")
        case 5: print("Op5")
        case 6: print("Op6")
        case 7: print("Op7")
        case 8: print("Op8")
        case 9: print("Op9")
        case 10: print("Op10")

# ejecutar_menu_animales()