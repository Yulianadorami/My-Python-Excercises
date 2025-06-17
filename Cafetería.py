print("Bienvenidos a: \n")
print(r'''
   ( (
    ) )
  ........
  |      |]
  \      /    Python Cafe
   `----'
''')
choose_1 = input("Elige tu bebida preferida:\n☕cafe\n🍵te\n🥤chocolate\n").lower()
size_choose = input("Elige el tamaño de tu bebida S, M o L\n").upper()
precio = 0

#Tu bebida favorita
if choose_1 == "cafe":
    precio = 3
    cafe_choose = input("Elige si deseas el café descafeinado, S para SI y N para NO\n").upper()
    if cafe_choose == "S":
        precio += 0.5
        milk_choose = input("Elige si deseas la leche deslactosada, S para SI y N para NO\n").upper()
        if milk_choose == "S":
            precio += 0.3
elif choose_1 == "te":
    precio = 2.5
elif choose_1 == "chocolate":
    precio = 4.0
else:
    print("Lo siento, no tenemos esa bebida, ingresa nuevamente una de las 3 opciones disponibles")

#Tamaño de la bebida

if size_choose == "S":
    precio += 0
elif size_choose == "M":
    precio += 2
elif size_choose == "L":
    precio += 4
else:
    print("El tamaño elegido es inválido, vuelve a elegir")

#Cantidad de bebidas
cantidad = float(input("Cuántas bebidas deseas? Máximo de bebidas por persona es 5\n"))
precio *= cantidad

#Total a pagar
print(f"Total a pagar :${precio} dólares")