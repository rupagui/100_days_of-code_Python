
# Day 2.2 - BMI calculator
# Date: 11/11/2022

'''

Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of someone's weight taking into account their height. 
(More details at: https://en.wikipedia.org/wiki/Body_mass_index)

E.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)

Give the result as a whole number (integer)

'''

peso = float(input("Teclee su peso en Kg.: "))
altura = float(input("Teclee su altura en m.: "))

imc = int(peso/altura**2)

print(f"Tiene un IMC de {imc}")