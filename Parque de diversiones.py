print("Bienvenidos al parque de diversiones")
altura = int(input("Cuánto mides?"))
total = 0
if altura > 120:
    print("Puedes subir al juego")
    edad = int(input("Cuántos años tienes?"))
    if edad < 12:
        total = 5
        print("El costo del ticket es $5")
    elif edad <= 18:
        total = 7
        print("El costo del ticket es $7")
    else:
        total = 12
        print("El costo del ticket es $12")  

    fotos = input("Quieres tomarte fotos? escribe S para SI y N para NO")
    if fotos == "S":
        total += 3
    print (f"El monto total a pagar es: {total} doláres.")

else:
    print("No tienes la altura suficiente para subir a este juego")

