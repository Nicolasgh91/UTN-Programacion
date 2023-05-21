import re, json
from Funciones_genericas02 import *
from Funciones_reutilizables_examen import *

# lista = parseo_json("Biblioteca\data_C9.json")
lista_json = leer_json("Biblioteca/data_C9.json")
lista_heroes = lista_json["heroes"] 

#Menu ejecutable
def menu_app(listado:list) -> list:
    normalizar_datos(listado)
    copia_listado = copiar_lista(listado)
    imprimir_menu()
    num_opc_usr = opcion_usr()
    lista_final_app = []
    otra_consulta = ""

    while otra_consulta == "s":

        if num_opc_usr == 1:
            cantidad = ""
            while validar_entero(cantidad) == False:
                cantidad = input("Indique la cantidad de elementos que desea obtener: ")
            cantidad = int(cantidad)
            lista_final_app = listar_n_elementos_dicc(copia_listado,cantidad)
        elif num_opc_usr == 2:
            lista_final_app = ordenar_heroe_por_criterio_y_clave(copia_listado,"altura")
        elif num_opc_usr == 3:
            lista_final_app = ordenar_heroe_por_criterio_y_clave(copia_listado,"fuerza")
        elif num_opc_usr == 4:
            clave_opc_usr = ""
            while clave_opc_usr != "altura" and clave_opc_usr != "fuerza" and clave_opc_usr != "peso":
                clave_opc_usr = input("Indique de cual caracteristica del héroe quiere obtener el promedio: ")
            lista_final_app = ordenar_heroe_por_criterio_y_clave(copia_listado,clave_opc_usr)
        elif num_opc_usr == 5:
            eleccion_usr = input("Qué heroes quiere listar? Filtro por inteligencia 'good', 'average' o 'high' :")
            lista_final_app = listar_valores_x_clave(copia_listado,eleccion_usr)
        elif num_opc_usr == 6:
            nombre_archivo = input("Indique el nombre del archivo a guardar: ")
            exportar_lista_csv(lista_final_app,nombre_archivo)
        else:
            print("Por favor indique una opción válida.")

    otra_consulta = input("Quiere realizar otra consulta? s/n")

    #print(lista_final_app)
    return lista_final_app
#Fin función

menu_app(lista_heroes)
