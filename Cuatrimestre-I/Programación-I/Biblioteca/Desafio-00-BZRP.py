from data_bzrp import lista_bzrp

#//////////////////////////////////////////////////////////////////////////////////////////////////
# b) Recorrer la lista imprimiendo por consola el título de cada video
def listado_titulos_videos():
    for e in lista_bzrp:
        print(e["title"])

#//////////////////////////////////////////////////////////////////////////////////////////////////
# c) Recorrer la lista imprimiendo por consola el título de cada video junto a la cantidad de reproducciones del mismo
def cant_reproducciones_x_titl():
    for e in lista_bzrp:
        print(e["title"], e["views"])

#//////////////////////////////////////////////////////////////////////////////////////////////////
# d) Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones (MÁXIMO)
def video_mas_visto():
    maximo = lista_bzrp[0]["views"]
    
    for e in lista_bzrp:
        if maximo < e["views"]:
            maximo = e["views"]    
    print(maximo)

#//////////////////////////////////////////////////////////////////////////////////////////////////
# e) Recorrer la lista y determinar cuál es la cantidad mínima de reproducciones (MÍNIMO)
def video_menos_visto():
    minimo = lista_bzrp[0]["views"]
    for e in lista_bzrp:
        if e["views"] < minimo:
            minimo = e["views"]
    print(minimo)

#//////////////////////////////////////////////////////////////////////////////////////////////////
# f) Recorrer la lista y determinar la cantidad total de reproducciones del canal (ACUMULADOR)
def cant_reproduc_canal():
    acumulador = 0
    for e in lista_bzrp:
        acumulador += e["views"]
    print(acumulador)

#//////////////////////////////////////////////////////////////////////////////////////////////////
# g) Recorrer la lista y determinar la cantidad promedio de reproducciones que tiene un video (PROMEDIO)
def prome_rep_x_cant_videos():
    promedio = 0
    acumulador = 0
    contador = 0
    for e in lista_bzrp:
        acumulador += e["views"]
        contador += 1  

    promedio = acumulador / contador
    print( int (promedio))

#//////////////////////////////////////////////////////////////////////////////////////////////////
# h) Informar cual es el Título del vídeo asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
def ver_titl_videos_mas_y_men_vistos():
    maximo = lista_bzrp[0]["views"]
    minimo = lista_bzrp[0]["views"]
    nombre_minimo = None
    nombre_maximo = None
    for e in lista_bzrp:
        if e["views"] > maximo:
            maximo = e["views"]
            nombre_maximo = e["title"]
            
        if e["views"] < minimo:
            minimo = e["views"]
            nombre_minimo = e["title"]       
    print(nombre_maximo, " es el máximo")
    print(nombre_minimo, " es el mínimo")

#//////////////////////////////////////////////////////////////////////////////////////////////////
# i) Calcular e informar cual es el video que más y el que menos dura.
def vid_menor_y_mayor_durac():
    maximo = lista_bzrp[0]["length"]
    minimo = lista_bzrp[0]["length"]
    titulo_maximo = None
    titulo_minimo = None
    
    for e in lista_bzrp:
        if maximo < e["length"]:
            maximo = e["length"]
            titulo_maximo = e["title"]
        if e["length"] < minimo:
            minimo = e["length"]
            titulo_minimo = e["title"]
    
    print(titulo_maximo, "Es el máximo")
    print(titulo_minimo, "Es el mínimo")

#//////////////////////////////////////////////////////////////////////////////////////////////////
# k) Construir un menú que permita elegir qué dato obtener
def menu_ejecutable_info_bzrp():
    print("Biza, bienvenido! Acá tengo la información que pediste. Fijate a continuación cual queres ver e introducí solo el número de referencia para que te devuelva los datos:\n")
    print(
        "Opción #1: Ver un listado con los títulos de cada video.\n" +
        "Opción #2: Ver la cantidad de reproducciones de cada video.\n" +
        "Opción #3: Ver qué video fue el más visto.\n" +
        "Opción #4: Ver qué video fue el menos visto.\n" +
        "Opción #5: Ver la cantidad de reproducciones total del canal.\n" +
        "Opción #6: Ver el promedio de reproducciones en base a la cantidad de videos total.\n" +
        "Opción #7: Ver el título de los videos más y menos vistos. \n" + 
        "Opción #8: Ver el título de los videos con menor y mayor duración. \n")
    
    opcion_usuario = int (input("\n Indica una opción mediante el número que corresponda: "))

    match opcion_usuario:
        case 1: listado_titulos_videos()
        case 2: cant_reproducciones_x_titl()
        case 3: video_mas_visto()
        case 4: video_menos_visto()
        case 5: cant_reproduc_canal()
        case 6: prome_rep_x_cant_videos()
        case 7: ver_titl_videos_mas_y_men_vistos()
        case 8: vid_menor_y_mayor_durac()
    
    otra_consulta = input("Queres hacer otra consulta? s/n")

    if otra_consulta == "s":
        menu_ejecutable_info_bzrp()
    else:
        print("Gracias por confiar en nosotros Biza! Saludos..")

menu_ejecutable_info_bzrp() #Fin función k)

