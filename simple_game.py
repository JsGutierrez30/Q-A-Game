print("¡Bienvenido a este cuestionario!")
res = input("Estas listo para comenzar? (si/no): ")
puntaje = 0
total_preguntas = 5
if res.lower() == "si":
    res = input("1. ¿En que pais se encuentra el edificio mas alto del mundo? ")
    if res.lower() == "Emiratos Arabes Unidos" or res.lower() == "emiratos arabes unidos":
        puntaje += 1
        print("¡Correcto!")
    else:
        print("Incorrecto")    
    res = input("2. ¿Cual es el animal que provoca mas muertes al año? ")
    if res.lower() == "zancudo" or res.lower() == "mosquito":
        puntaje += 1
        print("¡Correcto!")
    else:
        print("Incorrecto")   
    res = input("3. ¿Cuantos planetas hay en el sistema solar? ")
    if res == "8":
        puntaje += 1
        print("¡Correcto!")
    else:
        print("Incorrecto")   
    res = input("4. ¿Cuál es la película más taquillera de la historia? ")
    if res.lower() == "avengers endgame" or res.lower() == "endgame":
        puntaje += 1
        print("¡Correcto!")
    else:
        print("Incorrecto")  
    res = input("5. ¿Cual es el material mas duro del planeta? ")
    if res.lower() == "el diamante" or res.lower() == "diamante":
        puntaje += 1
        print("¡Correcto!")
    else:
        print("Incorrecto")  
    print("¡Muchas gracias por jugar! Obtuviste" , puntaje , "respuestas correctas")
    marca = (puntaje/total_preguntas) * 100
    print("Tu marca es:" , str(marca) + '%')
    print("Gracias por jugar!!")