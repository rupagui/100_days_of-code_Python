
# Day 1.4 - Variables
# Date: 10/11/2022

'''

Write a program that switches the values stored in the variables a and b.

'''

a = input("Introduce un valor para 'a': ")
b = input("Introduce un valor para 'b': ")

print("a = " + str(a))
print("b = " + str(b))

temp = a

a = b
b = temp

print("Ahora hemos intercambiado los valores.\na = " + str(a) + "\nb = " + str(b) + ".")

