def calculate_love_score(name1,name2):
    combined_names = name1 + name2
    lower_names = combined_names.upper()
    palabras_de_amor_1 =["T","R","U","E"]
    palabras_de_amor_2 =["L","O","V","E"]
    puntuacion_1= 0
    puntuacion_2= 0

    for nombre_dos in lower_names:
        if nombre_dos in palabras_de_amor_1:
            puntuacion_1 += 1

    for nombre_dos in lower_names:
        if nombre_dos in palabras_de_amor_2:
            puntuacion_2 += 1

    total= str(puntuacion_1)+str(puntuacion_2)
    print(total)

calculate_love_score("KANYE WEST","KIM KARDASHIAN")
