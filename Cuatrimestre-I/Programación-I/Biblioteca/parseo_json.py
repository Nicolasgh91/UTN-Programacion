import json
import re

"""def parse_json(nombre_archivo:str) -> list:
    with open(nombre_archivo, "r") as archivo:
        tema_json = json.load(archivo)
    return tema_json["bzrp"]
"""

"""Esta función extrae la información del JSON"""
def parse_json(nombre_archivo:str) -> list:
    
    with open(nombre_archivo, "r") as archivo:
        lista_final = []
        todo_texto = archivo.read()
        print(todo_texto)
        titulo = re.findall(r' "title": "([\(\)a-zA-Z0-9\| #-\\]+) ', todo_texto) #Los parentesis es para excluir info #La r del principio es necesaria!
        vistas = re.findall(r'"views:" ([0-9]+)', todo_texto)
        
        
        i = 0
        for i in range(len(titulo)):
            tema = {}
            tema["title"] = titulo[i]
            tema["views"] = vistas[i]
            
            
            lista_final.append(tema)
            i+=1

        #print(titulo, vistas)
    return lista_final

lista = parse_json("Biblioteca\JSON-Stark_simulacro.json")
print(lista)

