import random

def dibujar_dado(numero):
    if numero == 1:
        print(" -------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print(" -------")
    elif numero == 2:
        print(" -------")
        print("| O     |")
        print("|       |")
        print("|     O |")
        print(" -------")
    elif numero == 3:
        print(" -------")
        print("| O     |")
        print("|   O   |")
        print("|     O |")
        print(" -------")
    elif numero == 4:
        print(" -------")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print(" -------")
    elif numero == 5:
        print(" -------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print(" -------")
    elif numero == 6:
        print(" -------")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print(" -------")

print("¡Bienvenido al simulador de dados!")

respuesta = "y"
while respuesta.lower() == "y":
    print("Tirando el dado...")
    numero = random.randint(1, 6)
    dibujar_dado(numero)

    respuesta = input("¿Quieres tirar el dado de nuevo? (y/n): ")

print("¡Gracias por jugar!")
