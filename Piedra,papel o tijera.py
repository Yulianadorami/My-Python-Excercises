piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
opciones = [piedra,papel,tijera]

#Eleccion de usuario
eleccion_usuario = int(input("Elije una de las 3 opciones, 0 para piedra, 1 para papel y 2 para tijera\n"))
if eleccion_usuario>=0 and eleccion_usuario<=2:
    print(opciones[eleccion_usuario])

#Eleccio de la computadora
eleccion_computadora = random.randint(0,2)
print("Eleccion de la computadora es:")
print(opciones[eleccion_computadora])

#Resultados
if eleccion_usuario >=3 or eleccion_usuario<0:
    print("Esta opción es inválida. Tú pierdes")
elif  eleccion_usuario == 0 and eleccion_computadora ==2:
    print("Tú ganas")
elif eleccion_usuario == 2 and eleccion_computadora ==0:
    print("Tú pierdes")
elif eleccion_usuario>eleccion_computadora:
    print("Tú ganas")
elif eleccion_usuario<eleccion_computadora:
    print("Tú pierdes")
elif eleccion_usuario == eleccion_computadora:
    print("Es un empate")