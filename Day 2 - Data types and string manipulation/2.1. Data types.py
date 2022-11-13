
# Day 2.1 - Data types
# Date: 11/11/2022

'''

Write a program that adds the digits in a 2 digit number. 
E.g. if the input was 35, then the output should be 3 + 5 = 8

'''

user_input = input("Teclee un número de dos dígitos")

primero = int(user_input[0])
segundo = int(user_input[1])
resultado = primero + segundo

print(f"{primero} + {segundo} = {resultado}")