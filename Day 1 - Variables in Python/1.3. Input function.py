
# Day 1.3 - Input function
# Date: 10/11/2022

'''

Write a program that prints the number of characters in a user's name. 
You might need to Google for a function that calculates the length of a string.

Warning. Your program should work for different inputs. e.g. any name that you input.

'''

print("Tu nombre tiene " + str(len(input("¿Cuál es tu nombre? "))) + " caracteres.")

# Queda más legible así:

nombre = input("¿Cuál es tu nombre? ")
longitud = len(nombre)
print("Tu nombre tiene " + str(longitud) + " caracteres.")


