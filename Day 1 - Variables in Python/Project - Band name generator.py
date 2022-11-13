
# Day 1 Project - Band name generator
# Date: 10/11/2022

'''

1. Create a greeting for your program.
2. Ask the user for the city that they grew up in.
3. Ask the user for the name of a pet.
4. Combine the name of their city and pet and show them their band name.
5. Make sure the input cursor shows on a new line:


'''

print("Generador de nombres de Equipos de la NBA:\n")

ciudad = input("Escribe el nombre de una ciudad: \n")
animales = input("Escribe un nombre de animales que te gusten: \n")

nombre_candidato = ciudad + " " + animales
print("El equipo de baloncesto de " + ciudad + " podría llamarse: " + nombre_candidato + "\n")