print("Bienveidos a pizzas Yuliana")
tamaño = input("Qué tamaño de pizza deseas? S para small, M para medium y L para large\n")
pepperoni = input("Deseas agregar pepperoni? S para SI y N para NO\n")
extra_cheese = input("Deseas agregar queso extra? S para SI y N para No\n")
cuenta = 0

#Tamaño de pizza
if tamaño == "S":
    cuenta += 15
elif tamaño == "M":
    cuenta += 20
elif tamaño == "L":
    cuenta += 25
else:
    print("Tu elección de tamaño de pizza es inválida")

#Agregar pepperoni
if pepperoni == "S":
    cuenta += 2
else:
    cuenta += 3

#Agregar queso extra
if extra_cheese == "S":
    cuenta +=1
print(f"El total a pagar es  de ${cuenta} dólares")

